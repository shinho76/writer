# 이미지 제작 가이드 (Image Guide)

> **읽는 이**: image-maker 에이전트
> **역할**: 블로그 글(draft.md)의 `[IMAGE: 설명]` 자리에 들어갈 이미지를 **HTML + CSS로 만들고, Python + Playwright로 PNG로 캡처**한다.
> **분위기**: AI·테크. 어두운 배경, 흰 글씨, 코드 블록 스타일.
> **원칙**: 이미지는 **보조 수단**이다. 텍스트는 최대한 짧게 쓴다.

표기: **[지정]** = 사용자가 정한 값이라 바꾸지 않는다. **[제안]** = 지정되지 않아 이 가이드가 정한 기본값이다. 글 분위기에 맞게 조정할 수 있다.

---

## 0. 작업 순서 요약

1. `output/[주제]/draft.md`에서 `[IMAGE: ...]` 표시를 **위에서부터 모두** 찾는다.
2. 첫 번째(대표 이미지)는 **1장의 규격**대로 만든다.
3. 나머지는 설명 내용에 맞춰 **2장의 네 가지 종류 중 하나**를 고른다.
4. 각 이미지를 `.html`로 만들고, Playwright로 `.png`로 캡처한다. (**4장**)
5. 캡처한 PNG를 **직접 열어 눈으로 확인**한다. (**5장 점검표**)
6. 결과를 `output/[주제]/images/`에 저장하고, 어떤 `[IMAGE]`에 어떤 파일이 대응하는지 사용자에게 보고한다.

---

## 1. 대표 이미지 규격

### 1-1. 크기와 배경 **[지정]**

| 항목 | 값 |
|---|---|
| 크기 | **1080 × 1080px** (1:1 정사각형) |
| 배경 | 어두운 블루-퍼플 그라데이션 **`#1a1a2e` → `#16213e`** |
| 그라데이션 방향 | 대각선 `135deg` **[제안]** |

```css
background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
```

### 1-2. 텍스트 **[지정]**

| 항목 | 값 |
|---|---|
| **메인 텍스트** | **글 제목.** 큰 글씨, **흰색 `#ffffff`** |
| **보조 텍스트** | 카테고리 또는 부제. 작은 글씨, **연한 회색** |
| 정렬 | **모든 텍스트를 가로·세로 중앙 정렬** |
| 폰트 | **Pretendard** 또는 시스템 기본 한글 폰트 |

**[제안] 세부 값**

| 항목 | 값 |
|---|---|
| 보조 텍스트 색 | `#b8bcc8` |
| 메인 글자 굵기 | 800 (ExtraBold) |
| 메인 줄간격 | 1.3 |
| 보조 글자 크기 | 36px, 굵기 500 |
| 메인과 보조 사이 간격 | 40px |
| 좌우 안쪽 여백 | 110px 이상 |
| 줄바꿈 | `word-break: keep-all; overflow-wrap: break-word;` (단어 중간에서 끊기지 않게) |

**제목 길이에 따른 메인 글자 크기 [제안]**

| 제목 글자 수(공백 포함) | 글자 크기 |
|---|---|
| 12자 이하 | 104px |
| 13~20자 | 90px |
| 21~28자 | 78px |
| 29자 이상 | 68px |

- 제목은 **3줄을 넘기지 않는다.** 넘기면 글자 크기를 한 단계 줄인다.
- 제목이 길어서 어색하게 끊기면, 의미 단위에서 `<br>`로 직접 줄을 나눈다. (예: `클로드 코드 핵심 기능 5가지,<br>써보고 정리`)
- **제목 문구는 바꾸지 않는다.** 요약하거나 고치지 않고 draft.md의 제목 그대로 쓴다.
- 보조 텍스트는 **한 줄, 30자 이내**. draft.md에 카테고리·부제가 없으면 글의 핵심 키워드나 분야명을 쓴다. (예: `AI 코딩 도구`)

### 1-3. 액센트 **[지정]**

- **우측 하단 또는 좌상단**에 작은 액센트를 **하나만** 둔다. 도형, 코드 심볼(`</>`, `{ }`, `>_`), 단순한 아이콘 중 글 분위기에 맞는 것을 고른다.
- 텍스트와 겹치지 않고, 눈에 띄되 **시선을 빼앗지 않는** 크기로 둔다. **[제안]** 액센트 크기는 한 변 120~180px, 투명도 0.5~0.9.
- **[제안]** 액센트 색: 블루 `#4f8cff` 또는 퍼플 `#8b7cf6`. 두 색을 섞어 쓰지 않는다.
- 아이콘 이미지 파일을 외부에서 받지 않는다. **CSS 도형이나 텍스트 기호로 만든다.** (외부 파일 의존과 저작권 문제를 피한다.)

### 1-4. 대표 이미지 HTML 뼈대

```html
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<style>
  @import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css");
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 1080px; height: 1080px; }
  body {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    font-family: "Pretendard", "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", sans-serif;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center;
    padding: 0 110px;
    position: relative; overflow: hidden;
  }
  .title {
    color: #ffffff; font-weight: 800; font-size: 90px; line-height: 1.3;
    word-break: keep-all; overflow-wrap: break-word;
  }
  .sub {
    margin-top: 40px; color: #b8bcc8; font-weight: 500; font-size: 36px;
  }
  .accent {
    position: absolute; right: 80px; bottom: 80px;
    font-family: "JetBrains Mono", "D2Coding", Consolas, Menlo, monospace;
    font-weight: 700; font-size: 150px; color: #4f8cff; opacity: 0.75;
    line-height: 1;
  }
</style>
</head>
<body>
  <div class="title">제목이 들어간다</div>
  <div class="sub">보조 텍스트</div>
  <div class="accent">&lt;/&gt;</div>
</body>
</html>
```

---

## 2. 본문 삽입 이미지 (네 가지 중 선택)

### 2-1. 공통 규격

| 항목 | 값 |
|---|---|
| 가로 | **1080px** **[제안]** (블로그 본문 폭에 맞춰 줄어들어도 글씨가 읽히도록) |
| 세로 | **내용에 맞춰 자동** **[제안]** (600~1080px 안에서 끝나도록 텍스트를 줄인다) |
| 배경 | 대표 이미지와 **같은 그라데이션**(`#1a1a2e` → `#16213e`)을 기본으로 한다. 글 분위기에 따라 단색 `#16213e`도 가능 |
| 폰트 | 대표 이미지와 같다. 코드 느낌이 필요한 요소에만 모노스페이스 |
| 바깥 여백 | 좌우 72px, 상하 64px 이상 |

**색 팔레트 [제안]**

| 용도 | 값 |
|---|---|
| 배경 | `#1a1a2e` → `#16213e` |
| 카드·표 바탕 | `#0f1626` (더 어두운 남색) 또는 `rgba(255,255,255,0.05)` |
| 카드 테두리 | `rgba(255,255,255,0.12)` |
| 주 텍스트 | `#ffffff` |
| 보조 텍스트 | `#b8bcc8` |
| 강조색(블루) | `#4f8cff` |
| 강조색(퍼플) | `#8b7cf6` |
| 코드 블록 바탕 | `#0b0f1a` |
| 코드 텍스트 | `#c8d3f5` |

- 강조색은 **한 이미지에서 블루 또는 퍼플 하나만** 쓴다. (한 글의 이미지 전체에서도 같은 색으로 통일하면 좋다.)
- 흰 배경은 쓰지 않는다. 밝은 색이 들어가는 요소는 작은 포인트에만 쓴다.

**코드 블록 스타일을 디자인 요소로 활용할 수 있다.** 모노스페이스, 어두운 바탕, 둥근 모서리, 왼쪽 위의 세 점(창 버튼 모양)이 어울린다.

```css
.code {
  background: #0b0f1a; border: 1px solid rgba(255,255,255,0.12);
  border-radius: 16px; padding: 28px 32px;
  font-family: "JetBrains Mono", "D2Coding", Consolas, Menlo, monospace;
  font-size: 30px; color: #c8d3f5; line-height: 1.6;
}
```

### 2-2. 종류 선택 기준

`[IMAGE: 설명]`의 설명과, 그 이미지가 들어갈 **문단의 내용**을 보고 고른다.

| 종류 | 언제 고르나 | 설명에 자주 나오는 말 |
|---|---|---|
| **① 비교 표** | 제품·방법·옵션을 **나란히 비교**할 때 | 비교, 표, 차이, vs, 장단점 |
| **② 단계별 다이어그램** | **절차나 순서**를 보여줄 때 | 워크플로우, 단계, 순서, 흐름, 과정 |
| **③ 핵심 포인트 카드** | **3~5개 요점**을 정리할 때 | 요약, 핵심, 포인트, 정리, N가지 |
| **④ 인용/강조 박스** | **중요한 한 마디**를 강조할 때 | 인용, 강조, 한 줄, 원칙, 결론 |

- 애매하면 **문단 내용**으로 고른다. 요점이 여러 개면 ③, 순서가 있으면 ②, 두 가지 이상을 견주면 ①, 한 문장이 핵심이면 ④.
- 한 글 안에서 **같은 종류가 연속 두 번** 나오지 않게 배분한다. (가능하면 네 가지를 섞는다.)
- 위 네 가지로 표현되지 않는 요청이면 **가장 가까운 종류로 만들고**, 사용자에게 보고할 때 그 사실을 적는다.

### 2-3. ① 비교 표

- **열 2~4개, 행 3~6개.** 셀 안 글은 **15자 이내**.
- 첫 열은 항목 이름, 헤더 행은 강조색 밑줄이나 옅은 바탕으로 구분한다.
- 각 행을 옅은 구분선으로 나누고, 줄무늬 배경은 쓰지 않는다.
- **표의 수치·항목은 draft.md와 research.md에 있는 것만** 쓴다.

```html
<div class="card">
  <h2 class="heading">제목 (선택, 20자 이내)</h2>
  <table>
    <thead><tr><th></th><th>A</th><th>B</th></tr></thead>
    <tbody>
      <tr><td>항목1</td><td>값</td><td>값</td></tr>
      <tr><td>항목2</td><td>값</td><td>값</td></tr>
    </tbody>
  </table>
</div>
```
```css
table { width: 100%; border-collapse: collapse; font-size: 32px; color: #fff; }
th { color: #4f8cff; font-weight: 700; text-align: left; padding: 20px 24px;
     border-bottom: 2px solid #4f8cff; }
td { padding: 22px 24px; border-bottom: 1px solid rgba(255,255,255,0.12); }
td:first-child { color: #b8bcc8; font-weight: 600; }
```

### 2-4. ② 단계별 다이어그램

- **단계 3~6개.** 단계마다 **번호 + 제목(10자 이내) + 한 줄 설명(20자 이내, 선택)**.
- 세로 배치를 기본으로 한다. (모바일에서 읽기 쉽다.) 단계가 3~4개이고 짧으면 가로 배치도 가능하다.
- 단계는 **원형 번호 배지**와 **연결선**(또는 화살표 `→`, `↓`)으로 잇는다.
- 단계 안에 명령어·파일명이 나오면 **인라인 코드 스타일**(모노스페이스, 어두운 배경)로 표시한다.

```html
<div class="flow">
  <div class="step"><span class="num">1</span><div><b>단계 제목</b><small>짧은 설명</small></div></div>
  <div class="link"></div>
  <div class="step"><span class="num">2</span><div><b>단계 제목</b><small>짧은 설명</small></div></div>
</div>
```
```css
.step { display: flex; align-items: center; gap: 28px; padding: 26px 32px;
        background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px; color: #fff; font-size: 34px; }
.step b { display: block; font-weight: 700; }
.step small { display: block; margin-top: 6px; color: #b8bcc8; font-size: 26px; }
.num { flex: none; width: 64px; height: 64px; border-radius: 50%;
       background: #4f8cff; color: #0b0f1a; font-weight: 800; font-size: 32px;
       display: flex; align-items: center; justify-content: center; }
.link { width: 4px; height: 28px; margin: 0 0 0 60px; background: rgba(79,140,255,0.5); }
```

### 2-5. ③ 핵심 포인트 카드

- **카드 3~5개.** 카드마다 **제목(12자 이내) + 한 줄 설명(25자 이내)**.
- 3개면 가로 1줄 또는 세로 3줄, 4개는 2×2, 5개는 세로 5줄이 읽기 좋다.
- 카드 왼쪽 위에 **번호 또는 짧은 기호**(`01`, `02`… 모노스페이스, 강조색)를 둔다.
- 이모지는 쓰지 않는다. (환경에 따라 렌더링이 달라진다.)

```html
<div class="cards">
  <div class="pcard"><span class="idx">01</span><b>핵심 제목</b><small>한 줄 설명</small></div>
  <div class="pcard"><span class="idx">02</span><b>핵심 제목</b><small>한 줄 설명</small></div>
</div>
```
```css
.cards { display: grid; gap: 24px; }
.pcard { padding: 32px 36px; background: rgba(255,255,255,0.05);
         border: 1px solid rgba(255,255,255,0.12); border-radius: 20px; color: #fff; }
.idx { display: block; font-family: "JetBrains Mono","D2Coding",Consolas,Menlo,monospace;
       color: #4f8cff; font-weight: 700; font-size: 28px; margin-bottom: 12px; }
.pcard b { display: block; font-size: 38px; font-weight: 700; }
.pcard small { display: block; margin-top: 8px; color: #b8bcc8; font-size: 28px; }
```

### 2-6. ④ 인용/강조 박스

- **한 문장, 40자 이내.** 문장 부호 외에 다른 요소를 최소화한다.
- 큰 따옴표 모양(`“`)이나 왼쪽 굵은 세로줄을 강조색으로 둔다.
- 출처(누구의 말인지)가 있으면 **작은 글씨로 아래에** 쓴다. 출처 없이 글쓴이의 결론이면 생략한다.
- **인용문은 research.md 또는 draft.md에 있는 문장을 그대로** 쓴다. 지어내거나 바꾸지 않는다.

```html
<div class="quote">
  <div class="mark">“</div>
  <p>강조할 한 문장</p>
  <cite>출처 (선택)</cite>
</div>
```
```css
.quote { padding: 64px 72px; background: rgba(255,255,255,0.05);
         border-left: 8px solid #8b7cf6; border-radius: 8px 24px 24px 8px; color: #fff; }
.mark { font-size: 120px; line-height: 0.6; color: #8b7cf6; font-weight: 800; }
.quote p { font-size: 54px; font-weight: 700; line-height: 1.45; word-break: keep-all; }
cite { display: block; margin-top: 28px; font-style: normal; color: #b8bcc8; font-size: 28px; }
```

---

## 3. 공통 규칙

1. **모두 HTML + CSS로 만든다.** 이미지 생성 모델이나 외부 이미지 파일을 쓰지 않는다.
2. **Python + Playwright로 PNG를 캡처한다.** (4장)
3. **배경 톤은 본문과 어울리게, AI·테크 분위기.** 어두운 남색 계열, 코드 블록 느낌, 얇은 테두리, 둥근 모서리.
4. **텍스트는 최대한 짧게.** 이미지는 보조 수단이다. 본문에서 이미 설명한 내용을 이미지에서 다시 길게 쓰지 않는다.
5. **글자 크기는 모바일에서 읽히는 수준으로.** 본문 삽입 이미지는 **최소 26px**(1080px 폭 기준) 이상. 그보다 작은 글씨는 쓰지 않는다.
6. **이미지 안의 사실 정보는 draft.md·research.md에 있는 것만 쓴다.** 수치, 이름, 날짜, 인용을 만들어 넣지 않는다.
7. **대비를 확보한다.** 흰 글씨와 연회색 글씨만 쓰고, 어두운 바탕 위에서 읽기 어려운 색(짙은 회색 등)을 쓰지 않는다.
8. **한 이미지에 요소를 너무 많이 넣지 않는다.** 표는 6행 이하, 카드는 5개 이하, 단계는 6개 이하.
9. **여백을 충분히 둔다.** 요소가 가장자리에 붙지 않게 한다.
10. **장식은 절제한다.** 그림자, 글로우, 그라데이션 글자 같은 효과는 액센트 하나 정도만. 글자 위에 복잡한 패턴을 깔지 않는다.
11. **로고·상표·저작권 있는 이미지를 넣지 않는다.** 특정 제품 로고가 필요해 보여도 텍스트 이름으로 대신한다.
12. **이모지를 쓰지 않는다.** 렌더링 환경에 따라 모양이 달라진다.

---

## 4. Playwright 캡처 방법

### 4-1. 준비

```bash
pip install playwright
playwright install chromium
```

- 이미 설치되어 있으면 건너뛴다. `python -c "import playwright"`로 확인한다.
- 설치가 막히거나 실패하면 **임의로 다른 방법(다른 라이브러리, 스크린샷 도구)으로 바꾸지 말고** 사용자에게 알린다.

### 4-2. 캡처 스크립트

```python
from pathlib import Path
from playwright.sync_api import sync_playwright

def capture(html_path: str, png_path: str, width: int = 1080, height: int = 1080,
            full_page: bool = False) -> dict:
    """HTML 파일을 PNG로 캡처한다. 대표 이미지는 1080x1080 고정,
    본문 이미지는 full_page=True로 높이를 내용에 맞춘다."""
    html = Path(html_path).resolve()
    Path(png_path).parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height},
                                device_scale_factor=1)
        page.goto(html.as_uri())
        page.wait_for_load_state("networkidle")   # 웹폰트 로딩 대기
        page.evaluate("document.fonts.ready")     # 폰트 적용 완료 대기
        # 넘침 검사: 가로 스크롤이 생기면 텍스트가 잘린 것이다
        overflow = page.evaluate(
            "document.documentElement.scrollWidth > document.documentElement.clientWidth")
        page.screenshot(path=png_path, full_page=full_page)
        size = page.evaluate(
            "[document.documentElement.scrollWidth, document.documentElement.scrollHeight]")
        browser.close()
    return {"overflow": overflow, "width": size[0], "height": size[1]}
```

- **대표 이미지**: `capture(html, png, 1080, 1080, full_page=False)` → 결과가 **정확히 1080×1080**이어야 한다.
- **본문 이미지**: `capture(html, png, 1080, 800, full_page=True)` → 높이는 내용에 맞게 정해진다.
- 웹폰트(Pretendard)는 인터넷 연결이 필요하다. **오프라인이거나 폰트가 로딩되지 않으면** 폰트 스택의 다음 폰트(`Apple SD Gothic Neo`, `Malgun Gothic`, `Noto Sans KR`)가 쓰인다. 어느 폰트로 렌더링됐는지 결과를 확인하고, 한글이 깨지거나 네모(□)로 나오면 다른 시스템 한글 폰트로 바꾼다.
- 스크립트나 HTML 파일은 작업이 끝난 뒤 `output/[주제]/images/src/`에 두어 **나중에 문구를 고쳐 다시 캡처할 수 있게** 한다.

### 4-3. 저장 위치와 파일 이름

```
output/[주제]/images/
  thumbnail.png           ← 대표 이미지
  body-1.png              ← 본문 이미지 (draft.md에서 [IMAGE]가 나오는 순서대로)
  body-2.png
  body-3.png
  …
  src/
    thumbnail.html
    body-1.html
    body-2.html
    capture.py
    …
```

- 본문 이미지 번호는 draft.md에서 `[IMAGE]`가 **나오는 순서**와 같다. (`대표 이미지 -`로 시작하는 마커는 `thumbnail.png` 자리이고 번호에 넣지 않는다.)
- 이미지의 종류(비교 표, 다이어그램 등)는 파일 이름에 넣지 않는다. 대응 관계는 작업 보고에 적는다.
- 형식은 **PNG**. 용량이 크면(수 MB 이상) 해상도를 유지한 채 PNG 최적화만 한다. 크기를 줄이지 않는다.

---

## 5. 완료 전 점검표

**캡처된 PNG를 직접 열어서 눈으로 확인한다.** 코드가 돌아갔다는 것만으로 완료로 치지 않는다.

**대표 이미지**
- [ ] 크기가 **정확히 1080×1080**인가?
- [ ] 배경이 `#1a1a2e → #16213e` 그라데이션인가?
- [ ] 제목이 **흰색, 큰 글씨, 가로·세로 중앙**인가? 보조 텍스트는 연한 회색 작은 글씨인가?
- [ ] 제목이 draft.md의 제목과 **글자 그대로 같은가?**
- [ ] 제목이 3줄 이내이고, 단어 중간에서 끊기지 않았는가?
- [ ] 액센트가 **우측 하단 또는 좌상단에 하나만** 있고, 텍스트와 겹치지 않는가?

**본문 이미지**
- [ ] `[IMAGE]` 설명에 맞는 **종류**를 골랐는가?
- [ ] 글자 수 제한(셀 15자, 카드 제목 12자 등)을 지켰는가?
- [ ] 글자 크기가 26px 이상인가?
- [ ] 이미지 안의 수치·이름·인용이 **draft.md·research.md와 일치**하는가?
- [ ] 같은 종류가 연속되지 않게 배분되었는가?

**공통**
- [ ] 텍스트가 잘리거나 겹치지 않았는가? (`overflow`가 `False`인가?)
- [ ] 한글이 깨지거나 네모(□)로 나오지 않는가?
- [ ] 흰색·연회색 글씨가 배경 위에서 또렷이 읽히는가?
- [ ] 이모지, 외부 이미지, 로고를 쓰지 않았는가?
- [ ] 파일 이름·위치가 4-3의 규칙과 같은가?

문제가 있으면 HTML을 고쳐 **다시 캡처**한다. 고칠 수 없는 문제(폰트 없음, 설치 실패 등)는 숨기지 말고 사용자에게 알린다.

---

## 6. 작업이 끝나면 사용자에게 보고할 것

짧게 다음만 알린다.

1. 저장 위치 (`output/[주제]/images/`)와 만든 이미지 수
2. **`[IMAGE]` 표시와 파일의 대응표** (draft.md의 몇 번째 `[IMAGE]` → 어떤 파일, 어떤 종류)
3. 대표 이미지에서 제목을 줄바꿈하거나 글자 크기를 줄인 곳
4. 네 가지 종류로 딱 맞지 않아서 **가까운 종류로 만든 이미지**
5. 렌더링에 쓰인 폰트, 확인하지 못했거나 실패한 부분

---

## 7. 한 줄 원칙

> **"어두운 남색 바탕에, 흰 글씨를 짧게, 중앙에. 이미지는 글을 돕는 것이지 글을 대신하지 않는다."**
