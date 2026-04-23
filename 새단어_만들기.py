"""
╔══════════════════════════════════════════════════╗
║   🐱 혜원이 영단어 새 날짜 자동 생성 스크립트 🌸   ║
║   ─────────────────────────────────────────      ║
║   사용법: python 새단어_만들기.py 20260423         ║
║   (또는 python 새단어_만들기.py → 안내 대화형)     ║
║                                                  ║
║   기능:                                          ║
║   1. data/YYYYMMDD.json 읽기                     ║
║   2. 단어장 HTML + 퀴즈 HTML 자동 생성            ║
║   3. index.html의 SCHEDULE 배열 자동 추가         ║
╚══════════════════════════════════════════════════╝
"""
import json
import re
import os
import sys
from pathlib import Path

# Windows CMD 한글 깨짐 방지
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# 루트 폴더 (이 스크립트가 있는 위치)
ROOT = Path(__file__).parent.resolve()
TEMPLATE_DIR = ROOT / "20260427"  # 월요일 파일이 기준 템플릿
VOCAB_TEMPLATE = TEMPLATE_DIR / "혜원이_영단어_월요일_동물과자연.html"
QUIZ_TEMPLATE = TEMPLATE_DIR / "혜원이_영단어_월요일_퀴즈.html"
INDEX_HTML = ROOT / "index.html"
DATA_DIR = ROOT / "data"


# ───────────────────────────────────────────
# 유틸
# ───────────────────────────────────────────
def header(msg):
    print()
    print("=" * 56)
    print(f"  {msg}")
    print("=" * 56)


def ok(msg):
    print(f"  [OK] {msg}")


def fail(msg):
    print(f"  [FAIL] {msg}")


# ───────────────────────────────────────────
# WORDS 배열 생성 (JSON → JS 객체 문자열)
# ───────────────────────────────────────────
def build_words_array(words):
    """JSON의 단어 배열을 JS const WORDS = [...] 문자열로 변환"""
    lines = ["const WORDS = ["]
    for w in words:
        lines.append(f'  {{ word: "{w["word"]}", ipa: "{w["ipa"]}", meaning: "{w["meaning"]}", emoji: "{w["emoji"]}",')
        lines.append(f'    example: "{w["example"]}",')
        lines.append(f'    exampleKo: "{w["exampleKo"]}",')
        lines.append(f'    fact: "{w["fact"]}" }},')
    # 마지막 쉼표 제거
    if lines[-1].endswith('},'):
        lines[-1] = lines[-1][:-1]  # 쉼표 제거
    lines.append("];")
    return "\n".join(lines)


# ───────────────────────────────────────────
# 단어장 HTML 생성
# ───────────────────────────────────────────
def generate_vocab_html(data):
    """월요일 단어장 템플릿을 기반으로 새 날짜 단어장 생성"""
    print(f"\n📚 단어장 HTML 생성: {data['vocabFileName']}")

    with open(VOCAB_TEMPLATE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. WORDS 배열 교체
    new_words = build_words_array(data['words'])
    html = re.sub(
        r'const WORDS = \[.*?\];',
        new_words,
        html,
        count=1,
        flags=re.DOTALL
    )

    # 2. 제목/요일/테마 교체
    html = re.sub(
        r'<title>.*?</title>',
        f'<title>🌸 {data["dayKoFull"]} - {data["theme"]}</title>',
        html,
        count=1
    )
    html = re.sub(
        r'월요일 · Day 1 · 동물과 자연</div>',
        f'{data["dayKoFull"]} · Day {data["dayIdx"]} · {data["theme"]}</div>',
        html
    )
    html = html.replace('재미있는 <b>동물과 자연</b>', f'재미있는 <b>{data["theme"]}</b>')
    html = html.replace(
        '"혜원이_영단어_월요일_퀴즈.html"',
        f'"{data["quizFileName"]}"'
    )
    html = html.replace("day: 'Monday',", f"day: '{data['dayEn']}',")
    html = html.replace('dayIdx: 1,', f'dayIdx: {data["dayIdx"]},')
    html = html.replace("theme: '동물과 자연',", f"theme: '{data['theme']}',")

    # 3. 배경 그라데이션 교체
    html = re.sub(
        r'background:\s*linear-gradient\(180deg,\s*#87ceeb\s*0%,\s*#b5e48c\s*50%,\s*#76c893\s*100%\);',
        f'background: {data["bgGradient"]}',
        html
    )

    # 4. 헤더 제목 교체
    html = re.sub(
        r'<h1>🌳 영단어 모험 🌳</h1>',
        f'<h1>{data["headerTitle"]}</h1>',
        html
    )

    # 5. 저장 (폴더 생성 포함)
    dest_folder = ROOT / data['folderName']
    dest_folder.mkdir(exist_ok=True)
    dest = dest_folder / data['vocabFileName']
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(html)

    size = os.path.getsize(dest) / 1024
    ok(f"저장 완료 ({size:.1f} KB) → {dest.relative_to(ROOT)}")
    return dest


# ───────────────────────────────────────────
# 퀴즈 HTML 생성
# ───────────────────────────────────────────
def generate_quiz_html(data):
    """월요일 퀴즈 템플릿을 기반으로 새 날짜 퀴즈 생성 (사진 10장 그대로 유지)"""
    print(f"\n📝 퀴즈 HTML 생성: {data['quizFileName']}")

    with open(QUIZ_TEMPLATE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. WORDS 배열 교체 (Base64 사진들 그대로 보존됨)
    new_words = build_words_array(data['words'])
    html = re.sub(
        r'const WORDS = \[.*?\];',
        new_words,
        html,
        count=1,
        flags=re.DOTALL
    )

    # 2. 제목/요일 교체
    html = html.replace('🎯 월요일 퀴즈 🎯', f'🎯 {data["dayKoFull"]} 퀴즈 🎯')
    html = re.sub(
        r'<title>.*?</title>',
        f'<title>혜원이의 영단어 퀴즈 📝 {data["dayKoFull"]}</title>',
        html,
        count=1
    )
    html = html.replace(
        'Day 1 · 동물과 자연',
        f'Day {data["dayIdx"]} · {data["theme"]}'
    )

    # 3. 기록용 변수 교체
    html = html.replace("day: 'Monday',", f"day: '{data['dayEn']}',")
    html = html.replace('dayIdx: 1,', f'dayIdx: {data["dayIdx"]},')
    html = html.replace("quizRec.day || 'Monday'", f"quizRec.day || '{data['dayEn']}'")

    # 4. 배경 그라데이션 교체 (단어장과 맞춤)
    html = re.sub(
        r'background:\s*linear-gradient\(180deg,\s*#87ceeb\s*0%,\s*#b5e48c\s*50%,\s*#76c893\s*100%\);',
        f'background: {data["bgGradient"]}',
        html
    )

    # 5. 저장
    dest_folder = ROOT / data['folderName']
    dest_folder.mkdir(exist_ok=True)
    dest = dest_folder / data['quizFileName']
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(html)

    size = os.path.getsize(dest) / 1024
    ok(f"저장 완료 ({size:.1f} KB, 사진 포함) → {dest.relative_to(ROOT)}")

    # GAS_URL 확인
    if 'AKfycbyg0RNvnjzeUpWBu3KDrwre' in html:
        ok("Google Sheets URL 자동 반영됨")
    else:
        fail("Google Sheets URL 누락! (템플릿 확인 필요)")

    return dest


# ───────────────────────────────────────────
# index.html의 SCHEDULE 배열에 새 항목 추가
# ───────────────────────────────────────────
def update_index_schedule(data):
    """index.html의 SCHEDULE 배열에 새 항목 추가 (중복이면 교체)"""
    print(f"\n🏠 홈페이지 index.html 업데이트 중...")

    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        html = f.read()

    # 새 항목 JS 객체 문자열
    new_entry = f'''  {{
    date: "{data['date']}", dayKo: "{data['dayKo']}", dayEn: "{data['dayEn'][:3]}",
    theme: "{data['theme']}", emoji: "{data['themeEmoji']}",
    folder: "{data['folderName']}",
    vocab: "{data['vocabFileName']}",
    quiz: "{data['quizFileName']}"
  }}'''

    # 기존 항목에 같은 date가 있으면 제거
    pattern_existing = re.compile(
        r'\s*\{\s*\n\s*date:\s*"' + re.escape(data['date']) + r'".*?\}\s*,?',
        re.DOTALL
    )
    if pattern_existing.search(html):
        html = pattern_existing.sub('', html)
        print(f"  (기존 {data['date']} 항목 삭제 후 재추가)")

    # SCHEDULE 배열 찾아서 새 항목 추가
    match = re.search(r'(const SCHEDULE = \[)(.*?)(\];)', html, re.DOTALL)
    if not match:
        fail("index.html에서 SCHEDULE 배열을 찾을 수 없어요!")
        return False

    head = match.group(1)
    body = match.group(2)
    tail = match.group(3)

    # 기존 내용에 새 항목 추가
    body = body.rstrip()
    if body.rstrip().endswith('}'):
        body = body + ','
    new_body = body + '\n' + new_entry + '\n'

    new_schedule = head + new_body + tail
    html = html[:match.start()] + new_schedule + html[match.end():]

    with open(INDEX_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    ok(f"index.html SCHEDULE 배열에 {data['date']} 추가 완료")
    return True


# ───────────────────────────────────────────
# 메인
# ───────────────────────────────────────────
def main():
    header("🐱 혜원이 영단어 자동 생성기 🌸")

    # 1. 입력 받기 (인자 또는 대화형)
    if len(sys.argv) > 1:
        target = sys.argv[1].strip()
    else:
        print("\n📅 어떤 날짜를 만들까요? (예: 20260423)")
        target = input("   > ").strip()

    # JSON 파일 경로
    json_path = DATA_DIR / f"{target}.json"

    if not json_path.exists():
        fail(f"data/{target}.json 파일이 없어요!")
        print(f"   먼저 {json_path} 파일을 만들어주세요.")
        print(f"   (예시 참고: data/20260423.json)")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)

    # 2. JSON 읽기
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\n📋 설정 정보:")
    print(f"   • 날짜: {data['date']} ({data['dayKoFull']})")
    print(f"   • 테마: {data['theme']} {data['themeEmoji']}")
    print(f"   • 단어 개수: {len(data['words'])}개")
    print(f"   • 폴더: {data['folderName']}/")

    if len(data['words']) != 20:
        print(f"\n⚠️ 경고: 단어가 {len(data['words'])}개네요. 20개가 표준이에요!")
        answer = input("그래도 진행할까요? (y/N): ")
        if answer.lower() != 'y':
            print("취소했어요.")
            sys.exit(0)

    # 3. 템플릿 존재 확인
    if not VOCAB_TEMPLATE.exists() or not QUIZ_TEMPLATE.exists():
        fail("월요일 템플릿 파일이 없어요!")
        print(f"   필요: {VOCAB_TEMPLATE}")
        print(f"   필요: {QUIZ_TEMPLATE}")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)

    # 4. 단어장/퀴즈 생성
    generate_vocab_html(data)
    generate_quiz_html(data)

    # 5. index.html 업데이트
    update_index_schedule(data)

    # 6. 완료
    header("🎉 생성 완료! 🎉")
    print(f"\n📦 만들어진 파일:")
    print(f"   📚 {data['folderName']}/{data['vocabFileName']}")
    print(f"   📝 {data['folderName']}/{data['quizFileName']}")
    print(f"   🏠 index.html (SCHEDULE 업데이트)")

    print(f"\n▶️  다음 단계: GitHub에 업로드하세요!")
    print(f"   → python 업로드.py")
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
