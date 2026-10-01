# -*- coding: utf-8 -*-
"""HTML 생성 스크립트. 문구를 고치고 다시 실행한 뒤 capture.py로 캡처한다."""
from pathlib import Path
SRC = Path(__file__).parent

HEAD = '''<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<style>
@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css");
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px}
body{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);
 font-family:"Pretendard","Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;
 color:#fff;word-break:keep-all;overflow-wrap:break-word}
.wrap{padding:64px 72px}
.heading{font-size:40px;font-weight:800;line-height:1.3;margin-bottom:12px}
.tag{display:inline-block;font-size:26px;font-weight:600;color:#4f8cff;border:1px solid #4f8cff;border-radius:999px;padding:4px 18px;margin-bottom:22px}
.foot{margin-top:30px;color:#b8bcc8;font-size:26px;line-height:1.5}
table{width:100%;border-collapse:collapse;color:#fff}
th{color:#4f8cff;font-weight:700;text-align:left;padding:18px 20px;border-bottom:2px solid #4f8cff}
td{padding:20px;border-bottom:1px solid rgba(255,255,255,0.12);line-height:1.4;vertical-align:middle}
td:first-child{color:#b8bcc8;font-weight:600}
.mono{font-family:"JetBrains Mono","D2Coding",Consolas,Menlo,monospace}
.panel{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.12);border-radius:20px}
</style></head><body>
'''
def page(name, body, extra_css=""):
    html = HEAD.replace("</style>", extra_css + "</style>") + body + "\n</body></html>\n"
    (SRC / f"{name}.html").write_text(html, encoding="utf-8")

# ---------- thumbnail ----------
t = '''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><style>
@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css");
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1080px}
body{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);
 font-family:"Pretendard","Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;
 display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
 padding:0 110px;position:relative;overflow:hidden}
.title{color:#fff;font-weight:800;font-size:78px;line-height:1.3;word-break:keep-all;overflow-wrap:break-word}
.sub{margin-top:40px;color:#b8bcc8;font-weight:500;font-size:36px;word-break:keep-all}
.accent{position:absolute;right:80px;bottom:80px;font-family:"JetBrains Mono","D2Coding",Consolas,Menlo,monospace;
 font-weight:700;font-size:120px;color:#4f8cff;opacity:.5;line-height:1}
</style></head><body>
<div class="title" id="title">혼자인 자녀 위로,<br>부모가 곁에 있는 방법</div>
<div class="sub">미국 기관 권고와 한국 공공 도움 창구 정리</div>
<div class="accent">{ }</div>
</body></html>
'''
(SRC/"thumbnail.html").write_text(t, encoding="utf-8")

# ---------- body-1 : 외로움 vs 사회적 고립 (비교 표) ----------
page("body-1", '''<div class="wrap">
<h2 class="heading">외로움과 사회적 고립</h2>
<table><thead><tr><th></th><th>외로움</th><th>사회적 고립</th></tr></thead><tbody>
<tr><td>성격</td><td>감정</td><td>객관적 상태</td></tr>
<tr><td>기준</td><td>원하는·실제 연결의 격차</td><td>관계·역할·상호작용이 적음</td></tr>
<tr><td>확인 방법</td><td>주관적으로 느낌</td><td>쉽게 세고 측정 가능</td></tr>
</tbody></table>
<div class="foot">출처: WHO, 2025-06-30</div></div>''',
 "table{font-size:32px}th{font-size:32px}td{padding:28px 20px}td:first-child{width:200px}.wrap{padding:76px 72px}")

# ---------- body-2 : 수치 카드 2x2 ----------
page("body-2", '''<div class="wrap">
<h2 class="heading">한국 아동청소년 외로움·고립 수치</h2>
<div class="grid">
<div class="panel c"><span class="n">거의 3명 중 1명</span><span class="d">이유 없이 외로웠던 경험</span></div>
<div class="panel c"><span class="n">9.5%</span><span class="d">외부적 고립</span></div>
<div class="panel c"><span class="n">13.9%</span><span class="d">스스로 고립 인지</span></div>
<div class="panel c"><span class="n">1.4%</span><span class="d">항상 고립</span></div>
</div>
<div class="foot">아동청소년 인권실태조사(통계청 승인통계), KEDI 웹진 2024-02-21 서술. 표본 수 미확인, 원 보고서 미열람</div></div>''',
 ".grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:28px}"
 ".c{padding:40px 36px;display:flex;flex-direction:column;gap:14px}"
 ".n{font-size:50px;font-weight:800;color:#4f8cff;line-height:1.2}.d{font-size:32px;font-weight:600}")

# ---------- body-3 : 부모의 반응 방법 5개 ----------
rows = [("먼저 들을 공간 주기","Child Mind"),("관심사에 호기심 갖기","Seattle Children's"),
        ("밀지 않고 다시 시도","Child Mind"),("가족 루틴 만들기","Seattle Children's"),
        ("친구 관계 대화 잇기","AAP")]
items = "".join(f'<div class="panel r"><span class="idx mono">0{i+1}</span><b>{a}</b><small>{b}</small></div>'
                for i,(a,b) in enumerate(rows))
page("body-3", f'''<div class="wrap">
<h2 class="heading">부모의 반응 방법 5가지</h2>
<span class="tag">모두 미국 기관 권고</span>
<div class="list">{items}</div>
<div class="foot">한국 기관의 권고가 아님</div></div>''',
 ".list{display:flex;flex-direction:column;gap:16px}"
 ".r{display:flex;align-items:center;gap:24px;padding:26px 32px}"
 ".idx{color:#4f8cff;font-weight:700;font-size:28px;flex:none}"
 ".r b{font-size:36px;font-weight:700;flex:1}"
 ".r small{color:#b8bcc8;font-size:28px;flex:none}")

# ---------- body-4 : 피해야 할 반응 3열 표 ----------
rows = [("바로 해결하려 함","Child Mind","외로운 아이"),("과한 동정·감정 표현","Child Mind","외로운 아이"),
        ("실망을 축소함","Child Mind","거절 경험"),("파국화·즉각 반응","AAP","청소년"),("훈계","AAP","청소년")]
tr = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in rows)
page("body-4", f'''<div class="wrap">
<h2 class="heading">부담을 줄 수 있는 반응</h2>
<span class="tag">소스는 모두 미국 기관</span>
<table><thead><tr><th>반응</th><th>소스</th><th>대상</th></tr></thead><tbody>{tr}</tbody></table>
<div class="foot">대상 연령이 다르니 한 가지 기준처럼 읽지 않는 편이 좋다</div></div>''',
 "table{font-size:32px}th{font-size:30px}td:first-child{color:#fff;font-weight:600}td:nth-child(n+2){color:#b8bcc8}")

# ---------- body-5 : 두 상자 비교 ----------
page("body-5", '''<div class="wrap">
<h2 class="heading">서로 다른 결로 읽히는 권고</h2>
<span class="tag">모두 미국 기관·전문가</span>
<div class="two">
<div class="panel box"><div class="bt">감정 인정을 강조</div><div class="bs">Child Mind<br>Seattle Children's</div></div>
<div class="panel box"><div class="bt">과한 공감을 경계</div><div class="bs">AAP(청소년 대상)<br>Child Mind</div></div>
</div>
<div class="mid">소스는 직접 모순이라고 말하지 않음</div>
<div class="foot" style="text-align:center">이 글은 어느 쪽도 판정하지 않는다</div></div>''',
 ".two{display:grid;grid-template-columns:1fr 1fr;gap:24px}"
 ".box{padding:48px 36px;text-align:center}"
 ".bt{font-size:40px;font-weight:800;line-height:1.3;margin-bottom:28px}"
 ".bs{font-size:30px;font-weight:600;color:#b8bcc8;line-height:1.6}"
 ".mid{margin-top:36px;padding:26px 24px;text-align:center;font-size:32px;font-weight:700;"
 "border-top:2px solid #4f8cff;border-bottom:2px solid #4f8cff}")

# ---------- body-6 : 징후 체크리스트 ----------
its = ["표정이 어둡고 기운이 없음","학교 가기를 싫어하거나 두려워함","이유 없는 결석·전학 요청",
       "모둠 활동에서 소외·배제","소지품 분실·의류 손상 증가"]
li = "".join(f'<div class="it"><span class="bx"></span><span>{s}</span></div>' for s in its)
page("body-6", f'''<div class="wrap">
<h2 class="heading">피해학생 징후 안내 목록</h2>
<div class="panel chk">{li}</div>
<div class="foot">출처: 찾기쉬운 생활법령정보. 법적 해석 근거 아님<br>하나로 단정하지 않고 여러 모습을 함께 본다</div></div>''',
 ".chk{padding:20px 40px;margin-top:24px}"
 ".it{display:flex;align-items:center;gap:26px;padding:26px 0;font-size:34px;font-weight:600;border-bottom:1px solid rgba(255,255,255,0.12)}"
 ".it:last-child{border-bottom:none}"
 ".bx{flex:none;width:34px;height:34px;border:3px solid #4f8cff;border-radius:8px}")

# ---------- body-7 : 공공 도움 창구 표 ----------
rows = [("117","경찰청","학생·학부모 등 누구나","24시간 전화·문자"),
        ("청소년상담 1388","여성가족부","청소년과 학부모","365일 24시간"),
        ("위(Wee) 클래스","교육부","학교 학생","학교 상담 담당자에게 신청"),
        ("함께학교<br>전문가 상담","교육부","학생·학부모·교원","가입 후 무료 1:1")]
tr = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a,b,c,d in rows)
page("body-7", f'''<div class="wrap">
<h2 class="heading">한국 공공 도움 창구</h2>
<table><thead><tr><th>창구</th><th>운영</th><th>대상</th><th>이용</th></tr></thead><tbody>{tr}</tbody></table>
<div class="foot">모두 공공기관 소스 기준. 함께학교는 2024년 3월 기능 확대 시점의 언론 보도에 근거</div></div>''',
 "table{font-size:28px;table-layout:fixed}th{font-size:28px;padding:18px 14px}td{padding:22px 14px;text-wrap:balance}th:nth-child(1){width:262px}th:nth-child(2){width:160px}th:nth-child(3){width:224px}"
 "td:first-child{color:#fff;font-weight:700}td:nth-child(2),td:nth-child(3),td:nth-child(4){color:#e6e8ef}")
print("built")
