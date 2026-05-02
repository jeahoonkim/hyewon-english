"""
╔══════════════════════════════════════════════════╗
║   🎯 이벤트 자동 등록 스크립트                     ║
║   ─────────────────────────────────────────      ║
║   사용법: python 이벤트_등록.py                    ║
║                                                  ║
║   기능:                                          ║
║   1. D:\\Claude\\03. 꾸준한 문제\\ 폴더 자동 스캔   ║
║   2. events/ 폴더에 새 파일 자동 복사              ║
║   3. localStorage 자동 저장 코드 자동 패치        ║
║   4. events/manifest.json 자동 생성/업데이트       ║
║                                                  ║
║   → 이거 한 번만 실행하면 모든 이벤트 자동 등록!   ║
╚══════════════════════════════════════════════════╝
"""
import os
import re
import json
import sys
import shutil
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# ──────────────────────────────────────────────
# 경로 설정
# ──────────────────────────────────────────────
ROOT = Path(__file__).parent.resolve()
EVENTS_DIR = ROOT / "events"
MANIFEST = EVENTS_DIR / "manifest.json"

# 03. 꾸준한 문제 폴더 (Windows 또는 Linux/Mac mount)
SOURCE_DIRS = [
    Path("D:/Claude/03. 꾸준한 문제"),
    Path("/sessions/nifty-keen-dirac/mnt/03. 꾸준한 문제"),
]

SOURCE = None
for d in SOURCE_DIRS:
    if d.exists():
        SOURCE = d
        break


# ──────────────────────────────────────────────
# 테마/아이콘 자동 추정 (파일명 키워드 매칭)
# ──────────────────────────────────────────────
THEME_RULES = [
    ('어린이날', '🎈 어린이날 특집'),
    ('국어',     '📖 국어 퀴즈'),
    ('수학',     '🔢 수학 퀴즈'),
    ('과학',     '🔬 과학 퀴즈'),
    ('영어',     '🇺🇸 영어 퀴즈'),
    ('사회',     '🏛️ 사회 퀴즈'),
    ('역사',     '🏛️ 역사 퀴즈'),
    ('지리',     '🌍 지리 퀴즈'),
    ('넌센스',   '🤔 넌센스 퀴즈'),
    ('도형',     '📐 도형 퀴즈'),
    ('회화',     '💬 회화 퀴즈'),
    ('동물',     '🐾 동물 퀴즈'),
    ('식물',     '🌱 식물 퀴즈'),
    ('우주',     '🚀 우주 퀴즈'),
    ('지구',     '🌍 지구 퀴즈'),
]

def guess_theme(filename):
    """파일명에서 테마와 아이콘 추정"""
    name = filename.replace('혜원이_', '').replace('_퀴즈', '').replace('.html', '')
    name = re.sub(r'_\d{8}', '', name)  # 날짜 제거
    name = re.sub(r'_\d+탄', '', name)  # X탄 제거

    for keyword, label in THEME_RULES:
        if keyword in filename:
            # 라벨에서 아이콘과 테마 분리
            parts = label.split(' ', 1)
            return {
                'icon': parts[0],
                'theme': parts[1] if len(parts) > 1 else label
            }

    # 매칭 안 되면 기본값
    return {'icon': '📚', 'theme': name + ' 퀴즈'}


# ──────────────────────────────────────────────
# localStorage 저장 코드 (이벤트 HTML에 삽입)
# ──────────────────────────────────────────────
INSERT_CODE = '''
  // 🎯 이벤트 점수 자동 저장 (홈페이지가 읽어서 자동 적립)
  try {
    var eventKey = 'hyewon_event_pending_' + ds;
    localStorage.setItem(eventKey, JSON.stringify({
      score: score,
      total: n,
      percent: pct,
      subject: SUBJECT,
      date: ds,
      time: ts,
      timestamp: Date.now()
    }));
  } catch(e) { console.warn('이벤트 점수 저장 실패:', e); }
'''


def patch_file(filepath):
    """파일에 localStorage 저장 코드 삽입 (이미 패치된 거면 스킵)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'hyewon_event_pending_' in html:
        return False  # 이미 패치됨

    # fetch(APPS_URL+"?... 패턴 찾기
    pattern = r"(try\{fetch\(APPS_URL.*?\}catch\(e\)\{\})"
    match = re.search(pattern, html)

    if not match:
        return False  # 패턴 못 찾음

    new_html = html[:match.end()] + INSERT_CODE + html[match.end():]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    return True


# ──────────────────────────────────────────────
# 메인
# ──────────────────────────────────────────────
def main():
    print("\n" + "=" * 56)
    print("  🎯 이벤트 자동 등록 시작")
    print("=" * 56)

    if not SOURCE:
        print("\n❌ '03. 꾸준한 문제' 폴더를 못 찾아요!")
        print("   확인 경로:")
        for d in SOURCE_DIRS:
            print(f"   - {d}")
        input("\n엔터로 종료...")
        sys.exit(1)

    print(f"\n📁 원본 폴더: {SOURCE}")
    EVENTS_DIR.mkdir(exist_ok=True)
    print(f"📁 대상 폴더: {EVENTS_DIR}")

    # 03. 꾸준한 문제 폴더 스캔 (날짜 폴더만)
    date_folders = sorted([d for d in SOURCE.iterdir()
                          if d.is_dir() and re.match(r'^\d{8}$', d.name)])
    print(f"\n📊 날짜 폴더 발견: {len(date_folders)}개")

    manifest = {'events': {}}
    new_count = 0
    patched_count = 0
    total_events = 0

    updated_count = 0
    for folder in date_folders:
        date_key = folder.name  # "20260504"
        # YYYY-MM-DD 형식으로 변환
        date_iso = f"{date_key[:4]}-{date_key[4:6]}-{date_key[6:8]}"

        # 폴더 안의 HTML 파일 찾기 (가장 최근 수정된 파일 우선)
        html_files = sorted(folder.glob("*.html"),
                           key=lambda f: f.stat().st_mtime,
                           reverse=True)
        if not html_files:
            continue

        src_file = html_files[0]
        dst_file = EVENTS_DIR / src_file.name

        # 🔄 복사 결정 (없거나 / 원본이 더 최신이면 덮어쓰기)
        should_copy = False
        copy_reason = ''
        if not dst_file.exists():
            should_copy = True
            copy_reason = '새로 복사'
            new_count += 1
        else:
            src_mtime = src_file.stat().st_mtime
            dst_mtime = dst_file.stat().st_mtime
            # 원본이 1초 이상 더 최신이면 갱신
            if src_mtime > dst_mtime + 1:
                should_copy = True
                copy_reason = '갱신 (원본 더 최신)'
                updated_count += 1

        if should_copy:
            shutil.copy2(src_file, dst_file)
            print(f"  📄 {copy_reason}: {src_file.name}")

        # 패치 (자동 저장 코드 삽입 - 갱신된 파일은 다시 패치 필요)
        if patch_file(dst_file):
            patched_count += 1
            print(f"  🔧 패치: {dst_file.name}")

        # 테마/아이콘 추정
        info = guess_theme(src_file.name)
        manifest['events'][date_iso] = {
            'theme': info['theme'],
            'file': src_file.name,
            'icon': info['icon']
        }
        total_events += 1

    # manifest.json 저장
    with open(MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 56)
    print("  🎉 완료!")
    print("=" * 56)
    print(f"  📊 총 이벤트: {total_events}개")
    print(f"  📄 새로 복사: {new_count}개")
    print(f"  🔄 갱신됨: {updated_count}개")
    print(f"  🔧 새로 패치: {patched_count}개")
    print(f"  📋 manifest.json: {MANIFEST.name}")
    print()
    print("  ▶️ 다음: python 업로드.py")
    print()
    input("엔터로 종료...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n취소됨")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        input("\n엔터로 종료...")
