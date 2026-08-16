#!/usr/bin/env python3
"""Stack pdftoppm page PNGs (<base>-page-*.png) into one <base>.png and trim trailing blank space."""
import glob
import sys

from PIL import Image

GAP = 16
BG = (246, 240, 234)
BOTTOM_MARGIN = 40


def trim_bottom(img: Image.Image) -> Image.Image:
    """Drop the empty tail of a continuous render, keeping a small bottom margin."""
    pixels = img.load()
    step = max(1, img.width // 200)
    last = 0
    for y in range(img.height - 1, -1, -1):
        row_has_ink = False
        for x in range(0, img.width, step):
            r, g, b = pixels[x, y]
            if abs(r - BG[0]) > 6 or abs(g - BG[1]) > 6 or abs(b - BG[2]) > 6:
                row_has_ink = True
                break
        if row_has_ink:
            last = y
            break
    bottom = min(img.height, last + BOTTOM_MARGIN)
    return img.crop((0, 0, img.width, bottom))


def main() -> int:
    base = sys.argv[1]
    paths = sorted(glob.glob(base + "-page-*.png"))
    if not paths:
        print("no page images for " + base, file=sys.stderr)
        return 1
    pages = [trim_bottom(Image.open(p).convert("RGB")) for p in paths]
    width = max(p.width for p in pages)
    height = sum(p.height for p in pages) + GAP * (len(pages) - 1)
    canvas = Image.new("RGB", (width, height), BG)
    y = 0
    for page in pages:
        canvas.paste(page, ((width - page.width) // 2, y))
        y += page.height + GAP
    canvas.save(base + ".png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
