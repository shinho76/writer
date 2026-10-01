# 블로그 글 작성 자동화

주제를 받으면 리서치 → 글쓰기 → 이미지 → 조립까지 서브 에이전트에게 맡겨 네이버 블로그 글 한 편을 만든다.

## 폴더 구조

- `agents/` 서브 에이전트 지침 (researcher, writer, image-maker, assembler)
- `guides/` 말투(`style-guide.md`), SEO(`seo-guide.md`), 이미지(`image-guide.md`) 가이드
- `output/[주제]/` 결과물 (research.md, draft.md, images/, final.md, final.html)
- `user-images/` (옵션) 사용자가 직접 찍은 이미지. image-maker가 활용한다
- `scripts/build_index.py` `output/*/final.html`을 모아 루트 `index.html`을 만든다
- `index.html` 모든 글을 모은 한 페이지 (사이드바 제목 목록)

## 나의 역할: 오케스트레이터

**메인(나)은 직접 리서치하거나 글을 쓰지 않는다.** 모든 작업은 서브 에이전트에게 위임하고, 나는 순서와 진행을 관리한다.

- 위임 방법: Agent 도구로 서브 에이전트를 띄우고, 프롬프트에 "`agents/<이름>.md`를 끝까지 읽고 그대로 따라라. 주제는 `<주제>`"라고 지시한다. (`agents/`는 `.claude/agents/`가 아니라서 자동 인식되지 않는다.)
- 이미지 생성, HTML 조립 같은 파일 작업도 직접 하지 않고 해당 에이전트에게 맡긴다.
- `[주제]` 폴더명은 Step 1에서 정해진 것을 끝까지 같게 쓴다.

## 주제가 들어오면 (순서대로)

1. **리서치**: `agents/researcher.md` → `output/[주제]/research.md`
2. **글쓰기**: `agents/writer.md` → `output/[주제]/draft.md`
3. **이미지**: `agents/image-maker.md` → `output/[주제]/images/`, draft.md의 `[IMAGE:]` 마커를 이미지 경로로 치환
4. **조립**: `agents/assembler.md` → `output/[주제]/final.html`, `final.md`
5. **인덱스 갱신 + 자동 커밋·푸시** (메인이 직접 실행. 서브 에이전트에 맡기지 않는다)
   1. `python scripts/build_index.py` → 루트 `index.html` 재생성 (왼쪽 사이드바에 글 제목, 클릭하면 해당 글). 출력의 글 편수에 이번 글이 포함됐는지 확인
   2. `git add index.html scripts output` (**`git add -A` 금지.** `sample/` 등 다른 폴더는 올리지 않는다)
   3. `git commit -m "Add post: [글 제목]"` (메시지 끝에 평소의 Co-Authored-By 줄을 붙인다)
   4. `git push` (force push 금지)
   - Step 1~4 중 하나라도 실패했거나 `final.html`이 없으면 5단계를 하지 않는다.
   - 커밋·푸시가 거부되거나 실패하면 우회하지 말고 사용자에게 사유를 알린다.
   - 사용자가 이 5단계를 명시적으로 요청해 둔 것이다. 이 자동 푸시는 글 작성 파이프라인에 한정한다.

각 단계가 끝나면 **다음 단계로 넘어가기 전에 산출물 파일이 실제로 생겼는지 확인**한다. 없으면 다음으로 가지 않고 사용자에게 알린다.

## 진행 보고

단계 사이마다 사용자에게 한두 줄로 알린다. (예: "1/4 리서치 완료, 소스 6개. 글쓰기를 시작합니다.") 서브 에이전트가 남긴 보고(`[TODO]`, 정보 충돌, 확인 못 한 부분)는 요약해서 그대로 전달한다.

마지막에는 커밋·푸시 결과(커밋 해시)를 알리고, `final.html`과 `index.html`을 브라우저로 열어 보라고 안내한다.

## 하지 말 것

- 메인이 직접 웹 검색, 초안 작성, 글 수정을 하지 않는다. 고칠 곳이 있으면 해당 에이전트에게 다시 시킨다.
- 서브 에이전트의 보고를 부풀리거나 숨기지 않는다.
