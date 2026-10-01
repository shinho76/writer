"""HTML 생성 스크립트. 문구를 고친 뒤 `python build.py && python capture.py` 로 다시 만든다."""
from pathlib import Path

HERE = Path(__file__).parent

FONT = '"Pretendard", "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", sans-serif'
MONO = '"JetBrains Mono", "D2Coding", Consolas, Menlo, monospace'
IMPORT = '@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css");'

BODY_CSS = f"""
{IMPORT}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; }}
body {{
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  font-family: {FONT}; color:#fff;
  padding: 72px 72px; word-break: keep-all; overflow-wrap: break-word;
}}
.heading {{ font-size:40px; font-weight:800; margin-bottom:36px; }}
.heading small {{ display:block; margin-top:10px; font-size:28px; font-weight:500; color:#b8bcc8; }}
.card {{ background:#0f1626; border:1px solid rgba(255,255,255,0.12); border-radius:20px; }}
.mono {{ font-family:{MONO}; }}
.note {{ margin-top:28px; font-size:28px; color:#b8bcc8; }}
table {{ width:100%; border-collapse:collapse; font-size:30px; color:#fff; }}
th {{ color:#4f8cff; font-weight:700; text-align:left; padding:18px 20px; border-bottom:2px solid #4f8cff; font-size:28px; vertical-align:bottom; }}
td {{ padding:20px 20px; border-bottom:1px solid rgba(255,255,255,0.12); vertical-align:top; line-height:1.4; }}
tr:last-child td {{ border-bottom:none; }}
td:first-child {{ color:#b8bcc8; font-weight:600; }}
.ref {{ display:block; font-family:{MONO}; font-size:26px; color:#b8bcc8; font-weight:500; margin-bottom:4px; }}
.dim {{ color:#b8bcc8; }}
"""


def page(css, body, extra_head=""):
    return f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<style>{css}</style></head>
<body>
{body}
</body></html>
"""


# ---------------- thumbnail ----------------
thumb_css = f"""
{IMPORT}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; height:1080px; }}
body {{
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  font-family:{FONT};
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:0 90px; position:relative; overflow:hidden;
}}
.sub {{ color:#b8bcc8; font-weight:500; font-size:36px; margin-bottom:36px; }}
.title {{ color:#fff; font-weight:800; font-size:78px; line-height:1.3; word-break:keep-all; overflow-wrap:break-word; }}
.grid {{ margin-top:56px; display:grid; grid-template-columns:1fr 1fr; gap:20px; width:100%; }}
.c {{ background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.12); border-radius:20px;
      padding:22px 24px; text-align:center; }}
.c .idx {{ font-family:{MONO}; color:#4f8cff; font-weight:700; font-size:26px; }}
.c b {{ display:block; font-size:34px; font-weight:800; color:#fff; margin-top:4px; }}
.c span {{ display:block; margin-top:6px; font-size:26px; color:#b8bcc8; line-height:1.35; }}
.accent {{ position:absolute; left:70px; top:60px; font-family:{MONO}; font-weight:700; font-size:120px;
          color:#4f8cff; opacity:0.75; line-height:1; }}
"""
thumb_body = """
<div class="accent">&lt;/&gt;</div>
<div class="sub">에베소서 5:21~6:4</div>
<div class="title">성경이 말하는 남편과 아내,<br>자녀의 도리</div>
<div class="grid">
  <div class="c"><div class="idx">01</div><b>아내</b><span>주께 하듯</span></div>
  <div class="c"><div class="idx">02</div><b>남편</b><span>그리스도가 교회를<br>사랑하심 같이</span></div>
  <div class="c"><div class="idx">03</div><b>자녀</b><span>주 안에서 옳으니라,<br>약속 있는 계명</span></div>
  <div class="c"><div class="idx">04</div><b>아버지</b><span>노엽게 하지 말고 양육</span></div>
</div>
"""
(HERE / "thumbnail.html").write_text(page(thumb_css, thumb_body), encoding="utf-8")

# ---------------- body-1 : 비교 표 ----------------
b1 = """
<div class="heading">세 본문의 대응 관계</div>
<div class="card" style="padding:12px 20px">
<table>
<thead><tr><th style="width:120px"></th><th>에베소서</th><th>골로새서</th><th>베드로전서</th></tr></thead>
<tbody>
<tr><td>아내</td><td><span class="ref">5:22~24, 33</span>복종·존경</td><td><span class="ref">3:18</span>복종</td><td><span class="ref">3:1~6</span>순종(개역개정)</td></tr>
<tr><td>남편</td><td><span class="ref">5:25~33</span>사랑</td><td><span class="ref">3:19</span>사랑,<br>모질게 대하지 말라</td><td><span class="ref">3:7</span>지식을 따라 동거, 귀히 여김</td></tr>
<tr><td>자녀</td><td><span class="ref">6:1~3</span>순종·공경</td><td><span class="ref">3:20</span>모든 일에 순종</td><td class="dim">확인하지 못함</td></tr>
<tr><td>아버지</td><td><span class="ref">6:4</span>노엽게 하지 말고 양육</td><td><span class="ref">3:21</span>낙심하지 않게</td><td class="dim">확인하지 못함</td></tr>
</tbody></table></div>
<div class="note">베드로전서는 3:1~7 범위에서 확인한 내용이다.</div>
"""
(HERE / "body-1.html").write_text(page(BODY_CSS, b1), encoding="utf-8")

# ---------------- body-2 : 남편 명령 인용 카드 ----------------
b2_css = BODY_CSS + f"""
.q {{ padding:34px 40px; border-left:8px solid #4f8cff; border-radius:8px 20px 20px 8px;
      background:rgba(255,255,255,0.05); margin-bottom:24px; }}
.q:last-child {{ margin-bottom:0; }}
.q .src {{ font-size:28px; color:#4f8cff; font-weight:700; margin-bottom:12px; }}
.q .src span {{ color:#b8bcc8; font-weight:500; margin-left:10px; }}
.q p {{ font-size:36px; font-weight:700; line-height:1.45; }}
.q p.en {{ font-size:34px; }}
"""
b2 = """
<div class="heading">남편에게 주어진 명령</div>
<div class="q"><div class="src">에베소서 5:28<span>개역개정</span></div>
  <p>“자기 아내 사랑하기를 자기 자신과 같이 할지니”</p></div>
<div class="q"><div class="src">골로새서 3:19<span>ESV</span></div>
  <p class="en">“Husbands, love your wives, and do not be harsh with them.”</p></div>
<div class="q"><div class="src">베드로전서 3:7<span>개역개정</span></div>
  <p>“지식을 따라” 동거,<br>“생명의 은혜를 함께 이어받을 자”로 귀히 여김</p></div>
"""
(HERE / "body-2.html").write_text(page(b2_css, b2), encoding="utf-8")

# ---------------- body-3 : 번역어 비교 표 ----------------
b3_css = BODY_CSS + """
td.en { font-weight:600; }
.extra { margin-top:24px; padding:26px 28px; border-radius:16px; background:rgba(79,140,255,0.10);
         border:1px solid rgba(79,140,255,0.5); font-size:30px; }
.extra .ref { display:inline; margin:0 12px 0 0; }
"""
b3 = """
<div class="heading">‘복종’의 번역어</div>
<div class="card" style="padding:12px 20px">
<table>
<thead><tr><th>본문</th><th>개역개정</th><th>ESV</th></tr></thead>
<tbody>
<tr><td>에베소서 5:22</td><td>복종</td><td class="en">submit</td></tr>
<tr><td>골로새서 3:18</td><td>복종</td><td class="en">submit</td></tr>
<tr><td>베드로전서 3:1</td><td>순종</td><td class="en">be subject to</td></tr>
</tbody></table></div>
<div class="extra"><span class="ref">에베소서 5:33 · ESV</span>respect (존경)</div>
<div class="note">확인된 구절 기준이다.</div>
"""
(HERE / "body-3.html").write_text(page(b3_css, b3), encoding="utf-8")

# ---------------- body-4 : 자녀·아버지 두 칸 카드 ----------------
b4_css = BODY_CSS + f"""
.pill {{ display:block; width:max-content; margin:0 auto 32px; padding:14px 36px; border-radius:999px;
        background:rgba(79,140,255,0.15); border:1px solid #4f8cff; color:#fff; font-size:32px; font-weight:800; }}
.two {{ display:grid; grid-template-columns:1fr 1fr; gap:24px; align-items:stretch; }}
.col {{ padding:32px 30px; border-radius:20px; background:rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.12); }}
.col h3 {{ font-size:40px; font-weight:800; margin-bottom:22px; padding-bottom:16px; border-bottom:2px solid #4f8cff; }}
.it {{ margin-bottom:22px; }}
.it:last-child {{ margin-bottom:0; }}
.it .ref {{ margin-bottom:6px; color:#4f8cff; }}
.it p {{ font-size:30px; font-weight:600; line-height:1.4; }}
"""
b4 = """
<div class="pill">약속 있는 계명</div>
<div class="two">
  <div class="col"><h3>자녀</h3>
    <div class="it"><span class="ref">출애굽기 20:12</span><p>“Honor your father and your mother”</p></div>
    <div class="it"><span class="ref">에베소서 6:1~3</span><p>주 안에서 순종</p></div>
    <div class="it"><span class="ref">골로새서 3:20</span><p>모든 일에 순종</p></div>
  </div>
  <div class="col"><h3>아버지</h3>
    <div class="it"><span class="ref">에베소서 6:4</span><p>노엽게 하지 말고 주의 훈계와 교훈으로 양육</p></div>
    <div class="it"><span class="ref">골로새서 3:21</span><p>낙심하지 않게</p></div>
  </div>
</div>
"""
(HERE / "body-4.html").write_text(page(b4_css, b4), encoding="utf-8")

# ---------------- body-5 : 에베소서 5:21~22 두 입장 비교 표 ----------------
b5_css = BODY_CSS + """
table { table-layout:fixed; }
th { font-size:30px; }
td:first-child { color:#fff; font-weight:400; }
td .who { display:block; font-size:28px; font-weight:700; color:#fff; }
td .meta { display:block; font-size:26px; color:#b8bcc8; margin-bottom:10px; }
td p { font-size:28px; line-height:1.45; }
td.common { color:#c8d3f5; font-size:28px; }
td.common b { color:#4f8cff; }
"""
b5 = """
<div class="heading">에베소서 5:21과 5:22의 관계<small>같은 본문을 함께 읽지만 결론이 다르다</small></div>
<div class="card" style="padding:12px 20px">
<table>
<thead><tr><th>상호복종을 강조하는 입장</th><th>질서·역할상 복종을 유지하는 입장</th></tr></thead>
<tbody>
<tr>
 <td><span class="who">키너</span><span class="meta">CBE 블로그, 2016-06-01</span>
   <p>5:21과 6:9가 틀을 이룸. 5:22에 동사가 없어 5:21의 동사가 이어짐. 아내의 복종은 상호복종의 한 예</p></td>
 <td><span class="who">보이스 해설</span><span class="meta">기독일보, 2020-01-23</span>
   <p>5:21에 근거하되 아내의 복종은 자발적 수용</p></td>
</tr>
<tr>
 <td><span class="who">코람데오닷컴 김민호</span><span class="meta">2021-05-26</span>
   <p>일방적 가부장적 순종이 아님</p></td>
 <td><span class="who">단버스 선언</span><span class="meta">CBMW, 1988</span>
   <p>남편의 리더십은 창조 질서의 일부</p></td>
</tr>
<tr><td colspan="2" class="common"><b>공통점</b> 남편의 사랑 강조, 죄로 이끄는 권위를 따를 의무는 없음</td></tr>
</tbody></table></div>
"""
(HERE / "body-5.html").write_text(page(b5_css, b5), encoding="utf-8")

# ---------------- body-6 : ‘머리’ 세 갈래 ----------------
b6_css = BODY_CSS + f"""
.root {{ display:block; width:max-content; margin:0 auto; padding:16px 44px; border-radius:16px;
        background:#0b0f1a; border:1px solid rgba(255,255,255,0.12);
        font-size:34px; font-weight:800; }}
.root .mono {{ color:#4f8cff; margin-left:10px; font-size:30px; }}
.stem {{ width:4px; height:32px; background:rgba(79,140,255,0.5); margin:0 auto; }}
.bar {{ height:4px; background:rgba(79,140,255,0.5); margin:0 0 0 149px; width:638px; }}
.three {{ display:grid; grid-template-columns:repeat(3,1fr); gap:20px; }}
.br {{ position:relative; padding:30px 22px 26px; margin-top:32px; border-radius:20px; text-align:center;
       background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.12); }}
.br::before {{ content:""; position:absolute; left:50%; top:-32px; width:4px; height:32px;
              margin-left:-2px; background:rgba(79,140,255,0.5); }}
.br h3 {{ font-size:38px; font-weight:800; color:#4f8cff; }}
.br .en {{ font-size:26px; color:#b8bcc8; margin:2px 0 18px; font-family:{MONO}; }}
.br .n {{ font-size:30px; font-weight:700; margin-top:14px; line-height:1.3; }}
.br .n small {{ display:block; font-size:26px; font-weight:500; color:#b8bcc8; }}
.warn {{ margin-top:36px; padding:22px 28px; border-radius:16px; border:1px solid rgba(255,255,255,0.12);
        font-size:28px; color:#b8bcc8; text-align:center; line-height:1.45; }}
"""
b6 = """
<div class="root">머리<span class="mono">kephalē</span></div>
<div class="stem"></div>
<div class="bar"></div>
<div class="three">
  <div class="br"><h3>권위</h3><div class="en">&nbsp;</div>
    <div class="n">그루뎀<small>1985·1990·2001</small></div></div>
  <div class="br"><h3>탁월함</h3><div class="en">preeminent</div>
    <div class="n">티슬턴<small>2000<br>증거가 shrinking이라고 정리</small></div></div>
  <div class="br"><h3>근원</h3><div class="en">생명의 근원</div>
    <div class="n">스크록스<small>1972</small></div>
    <div class="n">빌레지키언<small>1985·1986</small></div>
    <div class="n">Groothuis</div></div>
</div>
<div class="warn">이 정리는 평등주의 단체 CBE가 낸 메타연구에 근거한다.</div>
"""
(HERE / "body-6.html").write_text(page(b6_css, b6), encoding="utf-8")
print("built")
