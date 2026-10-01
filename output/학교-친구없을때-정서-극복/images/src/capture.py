import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

SRC = Path(__file__).resolve().parent
OUT = SRC.parent

def capture(html_path, png_path, width=1080, height=1080, full_page=False):
    html = Path(html_path).resolve()
    Path(png_path).parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        page.goto(html.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        # element-level clipping check
        clipped = page.evaluate("""() => [...document.querySelectorAll('body *')].filter(e => e.scrollWidth > e.clientWidth + 1 && getComputedStyle(e).display !== 'inline' && e.clientWidth>0).map(e => e.className + ':' + e.textContent.slice(0,20))""")
        font = page.evaluate("getComputedStyle(document.body).fontFamily")
        page.screenshot(path=str(png_path), full_page=full_page)
        size = page.evaluate("[document.documentElement.scrollWidth, document.documentElement.scrollHeight]")
        browser.close()
    return {"overflow": overflow, "clipped": clipped, "width": size[0], "height": size[1]}

if __name__ == "__main__":
    names = sys.argv[1:] or ["thumbnail"] + [f"body-{i}" for i in range(1, 8)]
    for n in names:
        if n == "thumbnail":
            r = capture(SRC / "thumbnail.html", OUT / "thumbnail.png", 1080, 1080, False)
        else:
            r = capture(SRC / f"{n}.html", OUT / f"{n}.png", 1080, 600, True)
        print(n, r)
