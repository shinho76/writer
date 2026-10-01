# -*- coding: utf-8 -*-
import sys, subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright
SRC = Path(__file__).parent
OUT = SRC.parent

def capture(html_path, png_path, width=1080, height=1080, full_page=False):
    html = Path(html_path).resolve()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        page.goto(html.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        pret = page.evaluate("document.fonts.check('16px Pretendard')")
        page.screenshot(path=str(png_path), full_page=full_page)
        size = page.evaluate("[document.documentElement.scrollWidth, document.documentElement.scrollHeight]")
        title = page.evaluate("(document.getElementById('title')||{}).innerText||''")
        browser.close()
    return {"overflow": overflow, "w": size[0], "h": size[1], "pretendard": pret, "title": title}

if __name__ == "__main__":
    subprocess.run([sys.executable, str(SRC / "build.py")], check=True)
    names = sys.argv[1:] or ["thumbnail"] + [f"body-{i}" for i in range(1, 8)]
    for n in names:
        if n == "thumbnail":
            r = capture(SRC / "thumbnail.html", OUT / "thumbnail.png", 1080, 1080, False)
        else:
            r = capture(SRC / f"{n}.html", OUT / f"{n}.png", 1080, 300, True)
        print(n, r)
