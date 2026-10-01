#!/usr/bin/env python3
"""output/*/final.html 들을 모아 프로젝트 루트의 index.html 하나로 만든다.

- 왼쪽 사이드바에는 글 제목만 나열하고, 제목을 누르면 오른쪽에 그 글이 열린다.
- 각 final.html의 <article ...> 안쪽을 그대로 가져오고, 이미지 경로만
  ./images/ -> output/<폴더>/images/ 로 바꾼다. (글 내용은 고치지 않는다.)
- 최신 글(final.html 수정 시각)이 맨 위에 온다.
- 표준 라이브러리만 사용한다. 실행: python scripts/build_index.py
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"
TARGET = ROOT / "index.html"

ARTICLE_RE = re.compile(r"<article(?:\s[^>]*)?>(.*)</article>", re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")


def collect_posts():
    posts = []
    for final in OUTPUT.glob("*/final.html"):
        folder = final.parent.name
        text = final.read_text(encoding="utf-8")
        m = ARTICLE_RE.search(text)
        if not m:
            print(f"[건너뜀] {final}: <article> 를 찾지 못함", file=sys.stderr)
            continue
        body = m.group(1)
        h1 = H1_RE.search(body)
        title = html.unescape(TAG_RE.sub("", h1.group(1))).strip() if h1 else folder
        body = body.replace('src="./images/', f'src="output/{folder}/images/')
        posts.append({"folder": folder, "title": title, "body": body,
                      "mtime": final.stat().st_mtime})
    posts.sort(key=lambda p: p["mtime"], reverse=True)
    return posts


CSS = """
*{box-sizing:border-box}
html,body{margin:0;height:100%}
body{background:#f5f6f7;color:#333;font-family:"Nanum Gothic","NanumGothic","Pretendard","Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;font-size:16px;line-height:1.85;word-break:keep-all;overflow-wrap:break-word}
.layout{display:flex;min-height:100%}
.sidebar{position:fixed;top:0;left:0;bottom:0;width:300px;background:#fff;border-right:1px solid #e5e5e5;overflow-y:auto;padding:24px 0;z-index:20}
.sidebar .brand{margin:0 24px 16px;font-size:13px;font-weight:700;color:#03c75a;letter-spacing:.04em}
.sidebar ul{list-style:none;margin:0;padding:0}
.sidebar li a{display:block;padding:12px 24px;font-size:15px;line-height:1.5;color:#444;text-decoration:none;border-left:4px solid transparent}
.sidebar li a:hover{background:#f5f6f7}
.sidebar li a.active{color:#111;font-weight:700;background:#f0faf4;border-left-color:#03c75a}
.menu-btn{display:none;position:fixed;top:12px;left:12px;z-index:30;border:1px solid #ddd;background:#fff;border-radius:8px;padding:8px 12px;font-size:14px;font-family:inherit;color:#333;cursor:pointer}
.backdrop{display:none;position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:15}
main{margin-left:300px;flex:1;min-width:0}
.post{display:none;max-width:700px;margin:32px auto;background:#fff;padding:48px 28px}
.post.active{display:block}
.post h1{font-size:30px;font-weight:800;color:#111;line-height:1.4;margin:0 0 20px}
.post p.lead{font-size:15px;color:#777;margin:0 0 32px;padding-bottom:20px;border-bottom:1px solid #e5e5e5}
.post h2{font-size:22px;font-weight:700;color:#111;line-height:1.5;margin:56px 0 16px;padding-left:14px;border-left:4px solid #03c75a}
.post h3{font-size:18px;font-weight:700;color:#111;margin:36px 0 12px}
.post p{font-size:16px;font-weight:400;margin:0 0 1.3em}
.post strong{font-weight:700}
.post figure{margin:0}
.post img{max-width:100%;height:auto;display:block;margin:32px auto;border:1px solid #ececec;border-radius:8px}
.post hr{border:0;border-top:1px solid #e5e5e5;margin:44px 0}
.post a,.post a:visited{color:#1a6ed8;text-decoration:underline}
.post ul,.post ol{margin:0 0 1.3em;padding-left:22px}
.post ul.refs{font-size:14px;color:#666;line-height:1.7}
.post ul.refs li{font-size:14px;margin-bottom:4px}
.post p.tags{margin:0;padding-top:24px;border-top:1px solid #e5e5e5}
.post hr + p.tags{border-top:0;padding-top:0;margin-top:-20px}
.post p.tags span{display:inline-block;background:#eef1f4;color:#555;font-size:14px;line-height:1.4;padding:6px 12px;border-radius:999px;margin:0 6px 8px 0}
.post .todo{background:#fff3bf;color:#8a6d00;border-radius:6px;font-weight:700;padding:2px 8px}
.post .missing{background:#ffe3e3;border:1px dashed #e03131;color:#c92a2a;padding:12px 16px;margin:16px 0;border-radius:6px}
.post blockquote{margin:0 0 1.3em;padding:16px 20px;border-left:4px solid #d0d5da;background:#f8f9fa}
.post blockquote p{margin:0}
.post code{background:#f1f3f5;border-radius:4px;font-family:Consolas,"Courier New",monospace;font-size:.9em;padding:1px 5px}
.post pre{background:#1e1e2e;color:#e6e6f0;padding:20px;border-radius:8px;overflow-x:auto}
.post pre code{background:none;padding:0;color:inherit}
.post .table-wrap{overflow-x:auto}
.post table{width:100%;border-collapse:collapse}
.post th,.post td{padding:12px 14px;border:1px solid #e3e6e9}
.post th{background:#f3f5f7}
.empty{max-width:700px;margin:80px auto;padding:0 24px;color:#777;text-align:center}
@media (max-width:860px){
  .sidebar{transform:translateX(-100%);transition:transform .2s;box-shadow:none}
  body.nav-open .sidebar{transform:none;box-shadow:2px 0 12px rgba(0,0,0,.15)}
  body.nav-open .backdrop{display:block}
  .menu-btn{display:block}
  main{margin-left:0}
  .post{margin:0;padding:64px 16px 32px}
}
"""

JS = """
(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.sidebar a[data-slug]'));
  var posts = Array.prototype.slice.call(document.querySelectorAll('.post[data-slug]'));
  function slugFromHash() {
    try { return decodeURIComponent(location.hash.replace(/^#/, '')); } catch (e) { return ''; }
  }
  function show(slug) {
    var found = posts.some(function (p) { return p.dataset.slug === slug; });
    if (!found && posts.length) slug = posts[0].dataset.slug;
    posts.forEach(function (p) { p.classList.toggle('active', p.dataset.slug === slug); });
    links.forEach(function (a) { a.classList.toggle('active', a.dataset.slug === slug); });
    var active = posts.filter(function (p) { return p.dataset.slug === slug; })[0];
    if (active) {
      var h1 = active.querySelector('h1');
      if (h1) document.title = h1.textContent;
    }
    document.body.classList.remove('nav-open');
    window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', function () { show(slugFromHash()); });
  document.querySelector('.menu-btn').addEventListener('click', function () {
    document.body.classList.toggle('nav-open');
  });
  document.querySelector('.backdrop').addEventListener('click', function () {
    document.body.classList.remove('nav-open');
  });
  show(slugFromHash());
})();
"""


def render(posts):
    if posts:
        items = "\n".join(
            f'      <li><a href="#{html.escape(p["folder"], quote=True)}" '
            f'data-slug="{html.escape(p["folder"], quote=True)}">{html.escape(p["title"])}</a></li>'
            for p in posts
        )
        articles = "\n".join(
            f'    <article class="post" data-slug="{html.escape(p["folder"], quote=True)}">{p["body"]}</article>'
            for p in posts
        )
    else:
        items = ""
        articles = '    <p class="empty">아직 만들어진 글이 없습니다.</p>'

    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>블로그 글 목록</title>
<style>{CSS}</style>
</head>
<body>
<button class="menu-btn" type="button" aria-label="글 목록 열기">글 목록</button>
<div class="backdrop"></div>
<div class="layout">
  <nav class="sidebar" aria-label="글 목록">
    <div class="brand">POSTS</div>
    <ul>
{items}
    </ul>
  </nav>
  <main>
{articles}
  </main>
</div>
<script>{JS}</script>
</body>
</html>
"""


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            pass
    posts = collect_posts()
    TARGET.write_text(render(posts), encoding="utf-8", newline="\n")
    print(f"index.html 생성: 글 {len(posts)}편")
    for p in posts:
        print(f"  - {p['title']}  ({p['folder']})")


if __name__ == "__main__":
    main()
