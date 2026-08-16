#!/usr/bin/env bash
# Render examples/*.html to a paginated A4 .pdf and a single continuous .png.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/examples"
PY="${FOLIO_WEASY_PYTHON:-$HOME/.codex/skills/folio/.venv-weasy/bin/python}"
PNG_WIDTH="${PNG_WIDTH:-1400}"
PNG_PAGE_HEIGHT="${PNG_PAGE_HEIGHT:-1600mm}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:-${TMPDIR:-/tmp}/marketlens-cache}"
mkdir -p "$XDG_CACHE_HOME"

if [ ! -x "$PY" ]; then echo "weasyprint python not found: $PY" >&2; exit 1; fi
command -v pdftoppm >/dev/null || { echo "pdftoppm not found" >&2; exit 1; }

TARGETS=("$@")
if [ ${#TARGETS[@]} -eq 0 ]; then TARGETS=("$OUT"/*.html); fi

for html in "${TARGETS[@]}"; do
  base="${html%.html}"
  "$PY" -c 'import sys; from weasyprint import HTML; HTML(sys.argv[1]).write_pdf(sys.argv[2])' \
    "$html" "$base.pdf" 2>/dev/null
  rm -f "$base"-page-*.png "$base.png"
  tall="$XDG_CACHE_HOME/$(basename "$base")-tall.pdf"
  # The document's own @page rule wins over an appended stylesheet, so swap the
  # page size in the source text to get one continuous page instead of A4 pages.
  "$PY" -c 'import pathlib, sys; from weasyprint import HTML; src = pathlib.Path(sys.argv[1]); HTML(string=src.read_text(encoding="utf-8").replace("size: A4;", "size: 210mm %s;" % sys.argv[3]), base_url=str(src)).write_pdf(sys.argv[2])' \
    "$html" "$tall" "$PNG_PAGE_HEIGHT" 2>/dev/null
  pdftoppm -png -scale-to-x "$PNG_WIDTH" -scale-to-y -1 "$tall" "$base-page" >/dev/null 2>&1
  "$PY" "$ROOT/scripts/stack_pages.py" "$base"
  rm -f "$base"-page-*.png "$tall"
  pages=$("$PY" -c 'import sys,pypdf; print(len(pypdf.PdfReader(sys.argv[1]).pages))' "$base.pdf")
  echo "Rendered $(basename "$base").pdf ($pages A4 page(s)) and continuous .png"
done

echo "Rendered ${#TARGETS[@]} example(s)"
