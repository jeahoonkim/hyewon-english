"""
╔══════════════════════════════════════════════════╗
║   🏆 혜원이 주간 종합시험 자동 생성 스크립트 🌈    ║
║   ─────────────────────────────────────────      ║
║   사용법: python 종합시험_만들기.py 20260425       ║
║                                                  ║
║   기능:                                          ║
║   1. data/종합시험_YYYYMMDD.json 읽기            ║
║   2. includeDates의 단어들을 모두 합쳐서 종합 퀴즈 생성  ║
║   3. index.html의 SCHEDULE 배열 자동 추가         ║
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
    """여러 날짜의 단어를 하나의 const WORDS = [...] 문자열로 변환"""
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


def main():
    header("🏆 혜원이 주간 종합시험 생성기 🌈")

    if len(sys.argv) > 1:
        target = sys.argv[1].strip()
    else:
        print("\n📅 종합시험 날짜? (예: 20260425)")
        target = input("   > ").strip()

    # 설정 파일 읽기
    config_path = DATA_DIR / f"종합시험_{target}.json"
    if not config_path.exists():
        fail(f"data/종합시험_{target}.json 파일이 없어요!")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    print(f"\n📋 종합시험 설정:")
    print(f"   • 날짜: {config['date']} ({config['dayKoFull']})")
    print(f"   • 주차: {config['weekLabel']}")
    print(f"   • 포함 날짜: {', '.join(config['includeDates'])}")

    # 각 날짜의 단어들 수집
    all_words = []
    theme_list = []
    for ds in config['includeDates']:
        day_json_path = DATA_DIR / f"{ds}.json"
        if not day_json_path.exists():
            fail(f"data/{ds}.json 없음! 건너뜀")
            continue
        with open(day_json_path, 'r', encoding='utf-8') as f:
            day_data = json.load(f)
        all_words.extend(day_data['words'])
        theme_list.append(f"{day_data['dayKo']}({day_data['theme']})")

    print(f"\n📚 수집된 단어: 총 {len(all_words)}개")
    print(f"   • {' → '.join(theme_list)}")

    if len(all_words) == 0:
        fail("단어가 하나도 없어요!")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)

    # 퀴즈 HTML 생성
    print(f"\n📝 종합시험 HTML 생성 중...")

    with open(QUIZ_TEMPLATE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. WORDS 배열 교체 (80개 단어)
    new_words = build_words_array(all_words)
    html = re.sub(
        r'const WORDS = \[.*?\];',
        new_words,
        html,
        count=1,
        flags=re.DOTALL
    )

    # 2. 제목/헤더 교체
    html = html.replace('🎯 월요일 퀴즈 🎯', f'🎯 주간 종합 시험 🏆 ({config["weekLabel"]})')
    html = re.sub(
        r'<title>.*?</title>',
        f'<title>혜원이 주간 종합시험 🏆 {config["weekLabel"]}</title>',
        html, count=1
    )
    html = html.replace(
        'Day 1 · 동물과 자연',
        f'{config["weekLabel"]} · {config["themeSummary"]} 총정리'
    )

    # 3. 기록용 변수 교체
    html = html.replace("day: 'Monday',", f"day: '{config['dayEn']}',")
    html = html.replace('dayIdx: 1,', f'dayIdx: {config["dayIdx"]},')
    html = html.replace("quizRec.day || 'Monday'", f"quizRec.day || '{config['dayEn']}'")
    html = html.replace("const QUIZ_SCHEDULED_DATE = '2026-04-27';", f"const QUIZ_SCHEDULED_DATE = '{config['date']}';")

    # 4. 배경색 변경 (무지개 느낌)
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

    size_kb = os.path.getsize(dest) / 1024
    ok(f"저장 완료 ({size_kb:.1f} KB, 사진 포함)")
    print(f"       → {dest.relative_to(ROOT)}")

    if 'AKfycbyg0RNvnjzeUpWBu3KDrwre' in html:
        ok("Google Sheets URL 자동 반영됨")

    # index.html 업데이트
    print(f"\n🏠 홈페이지 index.html 업데이트 중...")
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        idx_html = f.read()

    # SCHEDULE 항목 (vocab 없이 quiz만 존재하는 특수 형태 — 여기서는 vocab 필드에도 quiz 넣어두기)
    new_entry = f'''  {{
    date: "{config['date']}", dayKo: "{config['dayKo']}", dayEn: "{config['dayEn'][:3]}",
    theme: "종합시험 ({config['weekLabel']})", emoji: "🏆",
    folder: "{config['folderName']}",
    vocab: "{config['quizFileName']}",
    quiz: "{config['quizFileName']}"
  }}'''

    # 기존 항목 있으면 제거
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
        ok(f"SCHEDULE에 {config['date']} (종합시험) 추가됨")

    header("🎉 종합시험 생성 완료! 🎉")
    print(f"\n📦 만들어진 파일:")
    print(f"   📝 {config['folderName']}/{config['quizFileName']}")
    print(f"\n📊 문제: {len(all_words)}문항 (랜덤 출제)")
    print(f"\n▶️  다음: python 업로드.py")
    print()
    input("엔터를 누르면 종료합니다...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 취소했어요.")
    except Exception as e:
        print(f"\n[ERROR] 예상치 못한 오류: {e}")
        import traceback
        traceback.print_exc()
        input("\n엔터를 누르면 종료합니다...")
