"""
╔══════════════════════════════════════════════════════════╗
║   🚀 혜원이 영어 전체 자동 빌드 + 업로드 마스터 스크립트   ║
║   ───────────────────────────────────────────────────    ║
║   사용법: python 전체_빌드.py                              ║
║   (또는 🚀_전체_업로드.bat 더블클릭)                       ║
║                                                          ║
║   기능:                                                  ║
║   1. data/YYYYMMDD.json (평일 단어) → HTML 자동 생성     ║
║   2. data/종합시험_*.json (토요일) → HTML 자동 생성       ║
║   3. data/복습_*.json (일요일) → HTML 자동 생성          ║
║   4. events/ 폴더 → manifest.json 자동 갱신             ║
║   5. Git add + commit + push 자동 실행                  ║
║                                                          ║
║   [똑똑한 점]                                            ║
║   - JSON이 HTML보다 새로우면 ONLY 그것만 다시 빌드        ║
║   - 변경 없으면 빠르게 스킵                               ║
╚══════════════════════════════════════════════════════════╝
"""
import os
import sys
import re
import subprocess
from pathlib import Path
from datetime import datetime

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).parent.resolve()
DATA_DIR = ROOT / "data"
EVENTS_DIR = ROOT / "events"


# ── 출력 헬퍼
def header(msg):
    print()
    print("=" * 60)
    print(f"  {msg}")
    print("=" * 60)

def section(msg):
    print()
    print(f"━━━ {msg} ━━━")

def ok(msg):    print(f"  [OK] {msg}")
def skip(msg):  print(f"  [SKIP] {msg}")
def fail(msg):  print(f"  [FAIL] {msg}")
def info(msg):  print(f"  [INFO] {msg}")


def run_python(script_name, arg=None):
    """Python 스크립트 실행 (출력 그대로 보여줌)"""
    cmd = [sys.executable, str(ROOT / script_name)]
    if arg:
        cmd.append(str(arg))
    result = subprocess.run(cmd, cwd=str(ROOT), capture_output=False)
    return result.returncode == 0


def run_shell(cmd):
    """쉘 명령 실행 (캡처)"""
    return subprocess.run(
        cmd, shell=True, capture_output=True, text=True,
        encoding='utf-8', errors='replace', cwd=str(ROOT)
    )


def needs_rebuild(json_path, html_paths):
    """JSON이 HTML보다 새로우면 True (다시 빌드 필요)"""
    if not json_path.exists():
        return False
    json_mtime = json_path.stat().st_mtime
    for html_path in html_paths:
        if not html_path.exists():
            return True  # HTML 자체가 없음
        if json_mtime > html_path.stat().st_mtime:
            return True
    return False


# ════════════════════════════════════════════════════
# 1단계: 평일 단어 (월~금) 빌드
# ════════════════════════════════════════════════════
def build_weekday_vocab():
    section("📚 평일 단어 빌드 (월~금)")

    if not DATA_DIR.exists():
        skip(f"data/ 폴더 없음")
        return 0

    built = 0
    weekday_jsons = sorted([
        p for p in DATA_DIR.glob("*.json")
        if not p.name.startswith("종합시험_")
        and not p.name.startswith("복습_")
        and re.match(r'^\d{8}\.json$', p.name)
    ])

    for json_path in weekday_jsons:
        date_str = json_path.stem  # "20260504"

        # JSON 읽어서 파일명 알아내기
        try:
            import json as _json
            with open(json_path, 'r', encoding='utf-8') as f:
                config = _json.load(f)
            folder = ROOT / config['folderName']
            vocab_html = folder / config['vocabFileName']
            quiz_html = folder / config['quizFileName']
        except Exception as e:
            fail(f"{date_str}: JSON 읽기 실패 - {e}")
            continue

        if not needs_rebuild(json_path, [vocab_html, quiz_html]):
            skip(f"{date_str} ({config.get('theme','')}) - 최신")
            continue

        info(f"{date_str} ({config.get('theme','')}) 빌드 중...")
        if run_python("새단어_만들기.py", date_str):
            ok(f"{date_str} 완료")
            built += 1
        else:
            fail(f"{date_str} 빌드 실패")

    if built == 0:
        info("새로 빌드할 평일 단어 없음 (모두 최신)")
    return built


# ════════════════════════════════════════════════════
# 2단계: 토요일 종합시험 빌드
# ════════════════════════════════════════════════════
def build_saturday_exams():
    section("🏆 토요일 종합시험 빌드")
    if not DATA_DIR.exists():
        return 0

    built = 0
    for json_path in sorted(DATA_DIR.glob("종합시험_*.json")):
        # 종합시험_20260509.json → 20260509
        m = re.match(r'종합시험_(\d{8})\.json', json_path.name)
        if not m:
            continue
        date_str = m.group(1)
        folder = ROOT / date_str
        # 종합시험 파일명은 generated 후 알 수 있어서 단순화: 폴더 안에 토요일 파일이 있는지로 판단
        sat_html = folder / "혜원이_영단어_토요일_종합시험.html"

        if not needs_rebuild(json_path, [sat_html]):
            skip(f"{date_str} - 최신")
            continue

        info(f"{date_str} 종합시험 빌드 중...")
        if run_python("종합시험_만들기.py", date_str):
            ok(f"{date_str} 완료")
            built += 1
        else:
            fail(f"{date_str} 빌드 실패")

    if built == 0:
        info("새로 빌드할 종합시험 없음")
    return built


# ════════════════════════════════════════════════════
# 3단계: 일요일 복습 빌드
# ════════════════════════════════════════════════════
def build_sunday_reviews():
    section("🌻 일요일 복습 퀴즈 빌드")
    if not DATA_DIR.exists():
        return 0

    built = 0
    for json_path in sorted(DATA_DIR.glob("복습_*.json")):
        m = re.match(r'복습_(\d{8})\.json', json_path.name)
        if not m:
            continue
        date_str = m.group(1)
        folder = ROOT / date_str
        sun_html = folder / "혜원이_영단어_일요일_복습.html"

        if not needs_rebuild(json_path, [sun_html]):
            skip(f"{date_str} - 최신")
            continue

        info(f"{date_str} 일요일 복습 빌드 중...")
        if run_python("일요일_복습_만들기.py", date_str):
            ok(f"{date_str} 완료")
            built += 1
        else:
            fail(f"{date_str} 빌드 실패")

    if built == 0:
        info("새로 빌드할 일요일 복습 없음")
    return built


# ════════════════════════════════════════════════════
# 4단계: 이벤트 매니페스트 갱신
# ════════════════════════════════════════════════════
def update_events():
    section("🎉 이벤트 매니페스트 갱신")
    if not (ROOT / "이벤트_등록.py").exists():
        skip("이벤트_등록.py 없음")
        return False
    return run_python("이벤트_등록.py")


# ════════════════════════════════════════════════════
# 5단계: GitHub 업로드 (Git add + commit + push)
# ════════════════════════════════════════════════════
def git_upload():
    section("🚀 GitHub 자동 업로드")

    if not (ROOT / ".git").exists():
        fail(".git 폴더 없음 - GitHub 연결이 안 되어 있어요")
        return False

    # 변경 사항 확인
    status = run_shell("git status --short")
    if not status.stdout.strip():
        info("✨ 업로드할 변경 사항이 없어요 (모두 최신)")
        return True

    print()
    print("  📝 변경된 파일들:")
    print("  " + "─" * 50)
    status_lines = status.stdout.strip().split('\n')
    for line in status_lines[:20]:
        print(f"    {line}")
    if len(status_lines) > 20:
        extra_count = len(status_lines) - 20
        print(f"    ... 외 {extra_count}개")
    print("  " + "─" * 50)

    # 커밋 메시지 자동
    now = datetime.now()
    commit_msg = f"자동 빌드 업로드 {now.strftime('%Y-%m-%d %H:%M')}"
    print(f"\n  💬 커밋 메시지: {commit_msg}")
    print(f"     (다른 메시지로 바꾸려면 입력, 그냥 엔터 = 위 메시지 사용)")
    user_input = input("  > ").strip()
    if user_input:
        commit_msg = user_input.replace('"', '').replace("'", '')

    # git add
    print("\n  1/4) git add ...")
    r = run_shell("git add .")
    if r.returncode != 0:
        fail(f"git add 실패\n{r.stderr}")
        return False
    ok("스테이징 완료")

    # git commit
    print("  2/4) git commit ...")
    r = run_shell(f'git commit -m "{commit_msg}"')
    if r.returncode != 0:
        fail(f"git commit 실패\n{r.stderr or r.stdout}")
        return False
    ok("커밋 완료")

    # git pull --rebase (먼저 GitHub 최신 받기 - 충돌 자동 방지)
    print("  3/4) GitHub 최신 받기 (rebase)...")
    pull_result = run_shell("git pull --rebase -X ours")
    if pull_result.returncode != 0:
        # 자동 해결 실패 시 abort 후 안내
        run_shell("git rebase --abort")
        fail("⚠️  GitHub와 충돌이 발생했어요!")
        print()
        print("  [해결 방법]")
        print("  1) '🆘_충돌해결_업로드.bat' 더블클릭")
        print("  2) 또는 cmd에서 차례로:")
        print("     git pull --rebase")
        print("     (충돌 시) git checkout --ours <파일>")
        print("     git rebase --continue")
        print("     git push")
        return False
    ok("머지 완료")

    # git push
    print("  4/4) git push ...")
    push_result = subprocess.run("git push", shell=True, cwd=str(ROOT))
    if push_result.returncode != 0:
        fail("git push 실패 - 인터넷 / 로그인 / 권한 확인하세요")
        print()
        print("  💡 'rejected' 에러면 '🆘_충돌해결_업로드.bat' 사용하세요!")
        return False
    ok("GitHub 푸시 완료!")
    return True


# ════════════════════════════════════════════════════
# 메인
# ════════════════════════════════════════════════════
def main():
    header("🚀 혜원이 영어 전체 자동 빌드 + 업로드")

    started = datetime.now()

    weekday_built = build_weekday_vocab()
    sat_built = build_saturday_exams()
    sun_built = build_sunday_reviews()
    events_ok = update_events()
    git_ok = git_upload()

    elapsed = (datetime.now() - started).total_seconds()

    header("✅ 자동 빌드 완료!")
    print(f"\n  📚 평일 단어:   {weekday_built}개 새로 빌드")
    print(f"  🏆 토요시험:    {sat_built}개 새로 빌드")
    print(f"  🌻 일요복습:    {sun_built}개 새로 빌드")
    print(f"  🎉 이벤트:      {'갱신 OK' if events_ok else '실패'}")
    print(f"  🚀 GitHub:     {'업로드 OK' if git_ok else '실패/스킵'}")
    print(f"\n  ⏱️  소요 시간:  {elapsed:.1f}초")
    print(f"\n  🌐 1~2분 후 사이트 확인:")
    print(f"     👉 https://hyewon-english.pages.dev/")

    print()
    input("엔터를 누르면 종료합니다...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 작업을 취소했어요.")
    except Exception as e:
        print(f"\n[ERROR] 예상치 못한 오류: {e}")
        import traceback
        traceback.print_exc()
        input("\n엔터를 누르면 종료합니다...")
   