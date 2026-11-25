#!/usr/bin/env python3
"""Render a point-in-time PE(TTM) valuation band as an SVG.

The script takes a CSV of daily PE observations (or market cap and TTM net
profit), computes a rolling lower/middle/upper band at every date using only
the observations available up to that date, and writes a self-contained SVG.
It is a reference implementation for the lens `Historical Valuation
Band` method; it is deliberately dependency-free.

Examples:
    python3 scripts/pe_band_chart.py --input pe.csv --output pe-band.svg
    python3 scripts/pe_band_chart.py --input pe.csv --method percentile \
        --lower 20 --upper 80 --window 750 --min-obs 250
    python3 scripts/pe_band_chart.py --input pe.csv --method mean --k 1

Input columns:
    date,pe
    date,market_cap,ttm_net_profit

Dates are ISO `YYYY-MM-DD` (or `YYYY/MM/DD`). PE values must be positive;
non-positive observations are skipped and reported on stderr.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import math
import statistics
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


PARCHMENT = "#F6F0EA"
INK = "#2E2622"
MUTED = "#7A6E66"
GRID = "#DED3C8"
PE_COLOR = "#2F5D8A"
BAND_COLOR = "#B83D2E"
TTM_FORMULA = "PE(TTM) = total market cap / TTM net profit attributable to parent"


@dataclass(frozen=True)
class Point:
    day: date
    pe: float


@dataclass
class BandPoint:
    day: date
    pe: float
    lower: float | None
    middle: float | None
    upper: float | None
    percentile: float | None


def parse_day(raw: str) -> date:
    value = raw.strip().replace("/", "-")
    if len(value) == 8 and value.isdigit():
        value = f"{value[:4]}-{value[4:6]}-{value[6:]}"
    return date.fromisoformat(value)


def read_rows(path: Path, date_col: str, pe_col: str, cap_col: str, profit_col: str) -> list[Point]:
    points: list[Point] = []
    skipped = 0
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit("input CSV has no header row")
        fields = set(reader.fieldnames)
        use_pe = pe_col in fields
        use_ratio = cap_col in fields and profit_col in fields
        if not use_pe and not use_ratio:
            raise SystemExit(
                f"input CSV needs either {pe_col!r} or both {cap_col!r} and {profit_col!r}; "
                f"found {sorted(fields)}"
            )
        for row in reader:
            try:
                day = parse_day(row[date_col])
                if use_pe:
                    pe = float(row[pe_col])
                else:
                    cap = float(row[cap_col])
                    profit = float(row[profit_col])
                    pe = cap / profit if profit else float("nan")
            except (KeyError, TypeError, ValueError):
                skipped += 1
                continue
            if not math.isfinite(pe) or pe <= 0:
                skipped += 1
                continue
            points.append(Point(day, pe))
    if not points:
        raise SystemExit("no positive PE observations found")
    points.sort(key=lambda p: p.day)
    if skipped:
        print(f"skipped {skipped} row(s) with missing, non-numeric, or non-positive values", file=sys.stderr)
    return points


def percentile(sorted_values: list[float], pct: float) -> float:
    if not sorted_values:
        raise ValueError("percentile of empty list")
    if len(sorted_values) == 1:
        return sorted_values[0]
    position = (len(sorted_values) - 1) * pct / 100.0
    low = math.floor(position)
    high = math.ceil(position)
    if low == high:
        return sorted_values[low]
    return sorted_values[low] * (high - position) + sorted_values[high] * (position - low)


def build_band(points: list[Point], window: int, min_obs: int, method: str, lower_pct: float, upper_pct: float, k: float) -> list[BandPoint]:
    values = [p.pe for p in points]
    band: list[BandPoint] = []
    for index, point in enumerate(points):
        start = max(0, index - window + 1)
        sample = values[start : index + 1]
        if len(sample) < min_obs:
            band.append(BandPoint(point.day, point.pe, None, None, None, None))
            continue
        ordered = sorted(sample)
        current_pct = 100.0 * sum(1 for value in sample if value <= point.pe) / len(sample)
        if method == "percentile":
            middle = percentile(ordered, 50)
            lower = percentile(ordered, lower_pct)
            upper = percentile(ordered, upper_pct)
        else:
            middle = statistics.fmean(sample)
            spread = statistics.stdev(sample) if len(sample) > 1 else 0.0
            lower = max(0.0, middle - k * spread)
            upper = middle + k * spread
        band.append(BandPoint(point.day, point.pe, lower, middle, upper, current_pct))
    return band


def slope_label(values: list[float], lookback: int) -> str:
    if len(values) < lookback * 2:
        return "n/a"
    recent = percentile(sorted(values[-lookback:]), 50)
    prior = percentile(sorted(values[-2 * lookback : -lookback]), 50)
    if prior <= 0:
        return "n/a"
    change = (recent - prior) / prior
    if change > 0.02:
        return "rising"
    if change < -0.02:
        return "falling"
    return "flat"


def nice_max(value: float) -> float:
    if value <= 0:
        return 10.0
    magnitude = 10 ** math.floor(math.log10(value))
    for step in (1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10):
        candidate = step * magnitude
        if value <= candidate * 1.02:
            return candidate
    return 10 * magnitude


def fmt_tick(value: float, ymax: float) -> str:
    return f"{value:.1f}" if ymax < 10 else f"{value:.0f}"


def text(x: float, y: float, value: str, size: int, fill: str, *, anchor: str = "start", family: str = "Charter, Georgia, serif", weight: str = "400", extra: str = "") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>'
        f"{html.escape(value)}</text>"
    )


def path_for(points: list[BandPoint], key: str, x_of, y_of, n: int) -> str:
    parts: list[str] = []
    for index, point in enumerate(points):
        value = getattr(point, key)
        if value is None:
            continue
        command = "M" if not parts else "L"
        parts.append(f"{command}{x_of(index):.1f},{y_of(value):.1f}")
    return " ".join(parts)


def render_svg(band: list[BandPoint], args: argparse.Namespace) -> str:
    width, height = args.width, args.height
    left, right, top, bottom = 64, 112, 82, 78
    plot_w = width - left - right
    plot_h = height - top - bottom
    n = len(band)
    values = [p.pe for p in band]
    valid_upper = [p.upper for p in band if p.upper is not None]
    raw_max = max(max(values), max(valid_upper) if valid_upper else 0)
    ymax = nice_max(raw_max * 1.08)
    last = band[-1]
    last_band = next((p for p in reversed(band) if p.middle is not None), None)
    slope = slope_label(values, args.slope_window)

    def x_of(index: int) -> float:
        return left if n == 1 else left + (index / (n - 1)) * plot_w

    def y_of(value: float) -> float:
        return top + (1 - value / ymax) * plot_h

    pieces: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">{html.escape(args.title)}</title>",
        f"<desc id=\"desc\">{html.escape(args.title)}: point-in-time PE(TTM) line with a rolling lower, middle, and upper valuation band. Descriptive, not a forecast or a trading signal.</desc>",
        f'<rect width="{width}" height="{height}" fill="{PARCHMENT}"/>',
        text(left, 34, args.title, 22, INK, weight="500"),
    ]
    if args.subtitle:
        pieces.append(text(left, 55, args.subtitle, 12, MUTED, family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))
    pieces.append(f'<line x1="{left}" y1="70" x2="{left + 22}" y2="70" stroke="{PE_COLOR}" stroke-width="2"/>')
    pieces.append(text(left + 28, 74, "PE(TTM) line", 10, MUTED, family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))
    pieces.append(f'<line x1="{left + 112}" y1="70" x2="{left + 134}" y2="70" stroke="{BAND_COLOR}" stroke-width="1.2" stroke-dasharray="5 4"/>')
    pieces.append(text(left + 140, 74, "rolling band", 10, MUTED, family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))

    for tick in range(5):
        value = ymax * tick / 4
        y = y_of(value)
        pieces.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" stroke="{GRID}" stroke-width="0.6" stroke-dasharray="2 4"/>')
        pieces.append(text(left - 10, y + 4, fmt_tick(value, ymax), 10, MUTED, anchor="end", family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))

    tick_count = min(6, n)
    tick_indices = sorted({round(i * (n - 1) / max(1, tick_count - 1)) for i in range(tick_count)}) if n > 1 else [0]
    for index in tick_indices:
        x = x_of(index)
        pieces.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top + plot_h}" stroke="{GRID}" stroke-width="0.4" opacity="0.6"/>')
        pieces.append(text(x, top + plot_h + 18, band[index].day.strftime("%Y-%m"), 10, MUTED, anchor="middle", family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))

    valid_indices = [i for i, p in enumerate(band) if p.upper is not None]
    if len(valid_indices) >= 2:
        upper_points = " ".join(f"{x_of(i):.1f},{y_of(band[i].upper):.1f}" for i in valid_indices)
        lower_points = " ".join(f"{x_of(i):.1f},{y_of(band[i].lower):.1f}" for i in reversed(valid_indices))
        pieces.append(f'<polygon points="{upper_points} {lower_points}" fill="{BAND_COLOR}" fill-opacity="0.10" stroke="none"/>')

    pieces.append(f'<path d="{path_for(band, "upper", x_of, y_of, n)}" fill="none" stroke="{BAND_COLOR}" stroke-width="1.2" stroke-dasharray="5 4" opacity="0.75"/>')
    pieces.append(f'<path d="{path_for(band, "middle", x_of, y_of, n)}" fill="none" stroke="{BAND_COLOR}" stroke-width="1.2" stroke-dasharray="2 4" opacity="0.55"/>')
    pieces.append(f'<path d="{path_for(band, "lower", x_of, y_of, n)}" fill="none" stroke="{BAND_COLOR}" stroke-width="1.2" stroke-dasharray="5 4" opacity="0.75"/>')
    pieces.append(f'<path d="{path_for(band, "pe", x_of, y_of, n)}" fill="none" stroke="{PE_COLOR}" stroke-width="1.8"/>')

    if last_band is not None:
        x = left + plot_w + 10
        for key, label in (("upper", "Upper"), ("middle", "Mid"), ("lower", "Lower")):
            value = getattr(last_band, key)
            pieces.append(text(x, y_of(value) + 4, f"{label} {value:.1f}", 10, BAND_COLOR, family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))

    last_x, last_y = x_of(n - 1), y_of(last.pe)
    pieces.append(f'<circle cx="{last_x:.1f}" cy="{last_y:.1f}" r="4.5" fill="{PE_COLOR}" stroke="{PARCHMENT}" stroke-width="1.5"/>')
    current_label = f"PE {last.pe:.2f}"
    if last.percentile is not None:
        current_label += f" · P{last.percentile:.0f}"
    pieces.append(text(min(last_x + 8, left + plot_w - 4), max(last_y - 10, top + 12), current_label, 11, PE_COLOR, weight="500", family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))

    source = args.source or "Source: user-supplied CSV"
    method = f"{args.method} band"
    if args.method == "percentile":
        method += f" P{args.lower:g}/P{args.upper:g} ({args.upper - args.lower:g}% central)"
    else:
        method += f" μ ± {args.k:g}σ"
    pieces.append(text(left, height - 46, f"{source} · {TTM_FORMULA}", 9, MUTED, family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))
    pieces.append(text(left, height - 30, f"{method} · window ≤ {args.window} obs · min {args.min_obs} obs · slope {slope}", 9, MUTED, family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))
    pieces.append(text(left, height - 14, args.note, 9, MUTED, family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"))
    pieces.append("</svg>")
    return "\n".join(pieces)


def write_table(path: Path, band: list[BandPoint]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["date", "pe", "lower", "middle", "upper", "percentile"])
        for point in band:
            writer.writerow([
                point.day.isoformat(),
                f"{point.pe:.4f}",
                "" if point.lower is None else f"{point.lower:.4f}",
                "" if point.middle is None else f"{point.middle:.4f}",
                "" if point.upper is None else f"{point.upper:.4f}",
                "" if point.percentile is None else f"{point.percentile:.2f}",
            ])


def summary(band: list[BandPoint], args: argparse.Namespace) -> dict:
    last = band[-1]
    slope = slope_label([p.pe for p in band], args.slope_window)
    return {
        "date": last.day.isoformat(),
        "pe": round(last.pe, 4),
        "lower": None if last.lower is None else round(last.lower, 4),
        "middle": None if last.middle is None else round(last.middle, 4),
        "upper": None if last.upper is None else round(last.upper, 4),
        "percentile": None if last.percentile is None else round(last.percentile, 2),
        "slope": slope,
        "window": args.window,
        "min_obs": args.min_obs,
        "method": args.method,
        "observations": len(band),
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render a point-in-time PE(TTM) valuation band as SVG.")
    parser.add_argument("--input", required=True, type=Path, help="CSV with date,pe or date,market_cap,ttm_net_profit")
    parser.add_argument("--output", type=Path, default=Path("pe-band.svg"), help="SVG output path")
    parser.add_argument("--table-output", type=Path, help="optional CSV with date,pe,lower,middle,upper,percentile")
    parser.add_argument("--summary-json", type=Path, help="optional JSON summary of the latest observation")
    parser.add_argument("--date-col", default="date")
    parser.add_argument("--pe-col", default="pe")
    parser.add_argument("--market-cap-col", default="market_cap")
    parser.add_argument("--profit-col", default="ttm_net_profit")
    parser.add_argument("--window", type=int, default=750, help="trailing observations in the rolling band")
    parser.add_argument("--min-obs", type=int, default=250, help="minimum observations before drawing a band")
    parser.add_argument("--method", choices=("percentile", "mean"), default="percentile")
    parser.add_argument("--lower", type=float, default=20.0, help="lower percentile for --method percentile")
    parser.add_argument("--upper", type=float, default=80.0, help="upper percentile for --method percentile")
    parser.add_argument("--k", type=float, default=1.0, help="standard-deviation multiplier for --method mean")
    parser.add_argument("--slope-window", type=int, default=250, help="observations in each half of the slope comparison")
    parser.add_argument("--width", type=int, default=960, help="SVG viewBox width")
    parser.add_argument("--height", type=int, default=520, help="SVG viewBox height")
    parser.add_argument("--title", default="PE(TTM) Band")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--source", default="")
    parser.add_argument("--note", default="Point-in-time rolling band. Descriptive, not a signal.")
    args = parser.parse_args(argv)

    if args.window < 2:
        parser.error("--window must be at least 2")
    if args.min_obs < 2 or args.min_obs > args.window:
        parser.error("--min-obs must be at least 2 and no larger than --window")
    if args.method == "percentile" and not (0 < args.lower < args.upper < 100):
        parser.error("--lower and --upper must satisfy 0 < lower < upper < 100")
    if args.method == "mean" and args.k <= 0:
        parser.error("--k must be positive")
    if args.width < 640 or args.height < 360:
        parser.error("--width must be at least 640 and --height at least 360")

    points = read_rows(args.input, args.date_col, args.pe_col, args.market_cap_col, args.profit_col)
    band = build_band(points, args.window, args.min_obs, args.method, args.lower, args.upper, args.k)
    args.output.write_text(render_svg(band, args), encoding="utf-8")
    if args.table_output:
        write_table(args.table_output, band)
    result = summary(band, args)
    if args.summary_json:
        args.summary_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        f"Latest: {result['date']} PE {result['pe']:.2f} | "
        f"lower {result['lower']} | mid {result['middle']} | upper {result['upper']} | "
        f"percentile {result['percentile']} | slope {result['slope']} | "
        f"window {result['window']} | observations {result['observations']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
