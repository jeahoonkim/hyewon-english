"""
╔══════════════════════════════════════════════════╗
║   🌻 혜원이 일요일 복습 퀴즈 자동 생성 📚          ║
║   ─────────────────────────────────────────      ║
║   사용법: python 일요일_복습_만들기.py 20260426    ║
║                                                  ║
║   기능:                                          ║
║   1. 이번 주 모든 단어를 WORDS에 포함             ║
║   2. localStorage에서 어제(토요일) 틀린 단어만 필터 ║
║   3. 틀린 단어만 골라서 복습 퀴즈                  ║
║   4. 100점이면 '쉬는 날' 메시지                   ║
╚══════════════════════════════════════════════════╝
"""
import json
import re
import os
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).parent.resolve()
TEMPLATE_DIR = ROOT / "20260427"
QUIZ_TEMPLATE = TEMPLATE_DIR / "혜원이_영단어_월요일_퀴즈.html"
INDEX_HTML = ROOT / "index.html"
DATA_DIR = ROOT / "data"


def header(msg):
    print()
    print("=" * 56)
    print(f"  {msg}")
    print("=" * 56)


def ok(msg): print(f"  [OK] {msg}")
def fail(msg): print(f"  [FAIL] {msg}")


def build_words_array(words):
    lines = ["const WORDS = ["]
    for w in words:
        lines.append(f'  {{ word: "{w["word"]}", ipa: "{w["ipa"]}", meaning: "{w["meaning"]}", emoji: "{w["emoji"]}",')
        lines.append(f'    example: "{w["example"]}",')
        lines.append(f'    exampleKo: "{w["exampleKo"]}",')
        lines.append(f'    fact: "{w["fact"]}" }},')
    if lines[-1].endswith('},'):
        lines[-1] = lines[-1][:-1]
    lines.append("];")
    return "\n".join(lines)


# ──────────────────────────────────────────────────
# 복습 모드: WORDS 배열을 localStorage 기반으로 필터링
# ──────────────────────────────────────────────────
REVIEW_FILTER_SCRIPT = """
// ═══════════════════════════════════════════════
// 🌻 복습 모드: 어제 토요일에 틀린 단어만 남김
// ═══════════════════════════════════════════════
const REVIEW_MODE = true;
const ORIGINAL_WORDS_COUNT = WORDS.length;

(function initReview() {
  try {
    const history = JSON.parse(localStorage.getItem('hyewon_quiz_history') || '[]');
    // 가장 최근 '종합시험' 또는 'Saturday' 퀴즈 찾기
    const saturdays = history.filter(q =>
      q.day === 'Saturday' || (q.day && q.day.indexOf('Sat') !== -1)
    );

    if (saturdays.length === 0) {
      // 토요일 퀴즈를 아직 안 풀었어요
      WORDS.length = 0;
      window.__REVIEW_STATE__ = 'no_saturday';
      return;
    }

    const mostRecent = saturdays[saturdays.length - 1];
    const wrongList = mostRecent.wrongWords || [];

    if (wrongList.length === 0) {
      // 토요일에 100점! 복습할 필요 없음
      WORDS.length = 0;
      window.__REVIEW_STATE__ = 'perfect';
      return;
    }

    // 틀린 단어만 남기기
    const filtered = WORDS.filter(w => wrongList.includes(w.word));
    WORDS.length = 0;
    filtered.forEach(w => WORDS.push(w));
    window.__REVIEW_STATE__ = 'ready';
    window.__WRONG_COUNT__ = wrongList.length;
  } catch (e) {
    console.error('복습 초기화 실패:', e);
    WORDS.length = 0;
    window.__REVIEW_STATE__ = 'error';
  }
})();

// 상태별 안내 메시지 표시
window.addEventListener('DOMContentLoaded', function() {
  const state = window.__REVIEW_STATE__;
  if (state === 'ready') return; // 정상 진행

  // 시작 화면 가리고 메시지 표시
  setTimeout(function() {
    const container = document.querySelector('.container') || document.body;
    let html = '';

    if (state === 'no_saturday') {
      html = `
        <div style="text-align:center; padding:60px 20px; font-family:'Jua',sans-serif;">
          <div style="font-size:5em; margin-bottom:20px;">🤔</div>
          <h2 style="color:#d63384; font-size:1.8em; margin-bottom:15px;">
            토요일 시험을 먼저 풀어주세요!
          </h2>
          <p style="color:#666; font-size:1.1em; margin-bottom:30px; line-height:1.7;">
            일요일 복습은 토요일에 틀린 단어로 만들어요 📝<br>
            먼저 토요일 종합시험을 풀고 와주세요!
          </p>
          <a href="../" style="display:inline-block; background:#ff8fb5; color:white;
             padding:14px 28px; border-radius:30px; text-decoration:none;
             font-size:1.1em; font-family:'Jua',sans-serif;">
             🏠 홈으로 가기
          </a>
        </div>
      `;
    } else if (state === 'perfect') {
      html = `
        <div style="text-align:center; padding:60px 20px; font-family:'Jua',sans-serif;">
          <div style="font-size:6em; margin-bottom:20px;">🏆</div>
          <h2 style="color:#d63384; font-size:2em; margin-bottom:15px;">
            완벽했어요!!! 🎉
          </h2>
          <p style="color:#555; font-size:1.15em; margin-bottom:20px; line-height:1.7;">
            토요일 종합시험에서 <b style="color:#ff8fb5;">100점</b>을 받았어요!<br>
            복습할 단어가 하나도 없네요 👏
          </p>
          <div style="background:#fff3bf; padding:20px; border-radius:20px;
               margin:30px auto; max-width:400px; font-family:'Gaegu',sans-serif;
               font-size:1.1em; line-height:1.6;">
            😸 오늘은 편하게 쉬어요!<br>
            혜원이 정말 대단해~ 💕
          </div>
          <a href="../" style="display:inline-block; background:#ff8fb5; color:white;
             padding:14px 28px; border-radius:30px; text-decoration:none;
             font-size:1.1em; font-family:'Jua',sans-serif;">
             🏠 홈으로 가기
          </a>
        </div>
      `;
    } else if (state === 'error') {
      html = `
        <div style="text-align:center; padding:60px 20px;">
          <h2>🙀 오류가 발생했어요</h2>
          <p>다시 시도해주세요.</p>
        </div>
      `;
    }

    if (html) {
      container.innerHTML = html;
    }
  }, 100);
});
"""


def main():
    header("🌻 혜원이 일요일 복습 생성기 📚")

    if len(sys.argv) > 1:
        target = sys.argv[1].strip()
    else:
        print("\n📅 복습 날짜? (예: 20260426)")
        target = input("   > ").strip()

    config_path = DATA_DIR / f"복습_{target}.json"
    if not config_path.exists():
        fail(f"data/복습_{target}.json 파일이 없어요!")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    print(f"\n📋 복습 설정:")
    print(f"   • 날짜: {config['date']} ({config['dayKoFull']})")
    print(f"   • 참조 날짜: {', '.join(config['includeDates'])}")

    # 단어 수집
    all_words = []
    for ds in config['includeDates']:
        day_json = DATA_DIR / f"{ds}.json"
        if not day_json.exists():
            fail(f"data/{ds}.json 없음! 건너뜀")
            continue
        with open(day_json, 'r', encoding='utf-8') as f:
            day_data = json.load(f)
        all_words.extend(day_data['words'])

    print(f"\n📚 전체 단어 풀: {len(all_words)}개")
    print(f"   (실제 퀴즈는 혜원이가 어제 틀린 단어만)")

    if not all_words:
        fail("단어 풀이 비어있어요!")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)

    # HTML 생성
    print(f"\n📝 복습 HTML 생성 중...")
    with open(QUIZ_TEMPLATE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. WORDS 배열 교체 + 필터링 스크립트 주입
    new_words = build_words_array(all_words)
    injected = new_words + "\n" + REVIEW_FILTER_SCRIPT
    html = re.sub(
        r'const WORDS = \[.*?\];',
        injected,
        html,
        count=1,
        flags=re.DOTALL
    )

    # 2. 제목/헤더 교체
    html = html.replace('🎯 월요일 퀴즈 🎯', '🌻 일요일 복습 📚')
    html = re.sub(
        r'<title>.*?</title>',
        '<title>혜원이 일요일 복습 🌻</title>',
        html, count=1
    )
    html = html.replace(
        'Day 1 · 동물과 자연',
        '어제 틀린 단어만 다시!'
    )

    # 3. 기록용 변수
    html = html.replace("day: 'Monday',", f"day: '{config['dayEn']}',")
    html = html.replace('dayIdx: 1,', f'dayIdx: {config["dayIdx"]},')
    html = html.replace("quizRec.day || 'Monday'", f"quizRec.day || '{config['dayEn']}'")
    html = html.replace("const QUIZ_SCHEDULED_DATE = '2026-04-27';", f"const QUIZ_SCHEDULED_DATE = '{config['date']}';")

    # 4. 배경색
    html = re.sub(
        r'background:\s*linear-gradient\(180deg,\s*#87ceeb\s*0%,\s*#b5e48c\s*50%,\s*#76c893\s*100%\);',
        f'background: {config["bgGradient"]}',
        html
    )

    # 저장
    dest_folder = ROOT / config['folderName']
    dest_folder.mkdir(exist_ok=True)
    dest = dest_folder / config['quizFileName']
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(html)

    size = os.path.getsize(dest) / 1024
    ok(f"저장 완료 ({size:.1f} KB)")
    print(f"       → {dest.relative_to(ROOT)}")

    # index.html 업데이트
    print(f"\n🏠 홈페이지 SCHEDULE 업데이트 중...")
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        idx_html = f.read()

    new_entry = f'''  {{
    date: "{config['date']}", dayKo: "{config['dayKo']}", dayEn: "{config['dayEn'][:3]}",
    theme: "일요일 복습 ({config['weekLabel']})", emoji: "🌻",
    folder: "{config['folderName']}",
    vocab: "{config['quizFileName']}",
    quiz: "{config['quizFileName']}"
  }}'''

    pattern_existing = re.compile(
        r'\s*\{\s*\n\s*date:\s*"' + re.escape(config['date']) + r'".*?\}\s*,?',
        re.DOTALL
    )
    if pattern_existing.search(idx_html):
        idx_html = pattern_existing.sub('', idx_html)

    match = re.search(r'(const SCHEDULE = \[)(.*?)(\];)', idx_html, re.DOTALL)
    if match:
        head_txt = match.group(1)
        body = match.group(2).rstrip()
        tail = match.group(3)
        if body.endswith('}'):
            body = body + ','
        new_schedule = head_txt + body + '\n' + new_entry + '\n' + tail
        idx_html = idx_html[:match.start()] + new_schedule + idx_html[match.end():]
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(idx_html)
        ok(f"SCHEDULE에 {config['date']} (일요일 복습) 추가됨")

    header("🎉 일요일 복습 생성 완료! 🎉")
    print(f"\n📦 파일: {config['folderName']}/{config['quizFileName']}")
    print(f"\n🔍 작동 방식:")
    print(f"   혜원이가 일요일에 열면:")
    print(f"   ① 브라우저에서 토요일 퀴즈 기록 확인")
    print(f"   ② 틀린 단어만 골라서 퀴즈 구성")
    print(f"   ③ 틀린 거 없으면 '완벽! 쉬는 날' 메시지")
    print(f"\n▶️  다음: python 업로드.py")
    print()
    input("엔터를 누르면 종료합니다...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 취소했어요.")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        input("\n엔터를 누르면 종료합니다...")
