import sys, json
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
OUT = HERE.parent


def capture(html_path, png_path, width=1080, height=1080, full_page=False):
    html = Path(html_path).resolve()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        page.goto(html.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        fonts = page.evaluate("[...document.fonts].filter(f=>f.status=='loaded').map(f=>f.family)")
        page.screenshot(path=str(png_path), full_page=full_page)
        size = page.evaluate("[document.documentElement.scrollWidth, document.documentElement.scrollHeight]")
        browser.close()
    return {"overflow": overflow, "width": size[0], "height": size[1], "fonts": sorted(set(fonts))}


if __name__ == "__main__":
    names = sys.argv[1:] or ["thumbnail"] + [f"body-{i}" for i in range(1, 7)]
    for n in names:
        if n == "thumbnail":
            r = capture(HERE / "thumbnail.html", OUT / "thumbnail.png", 1080, 1080, False)
        else:
            r = capture(HERE / f"{n}.html", OUT / f"{n}.png", 1080, 100, True)
        print(n, json.dumps(r, ensure_ascii=False))
