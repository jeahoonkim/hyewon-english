"""
╔══════════════════════════════════════════════╗
║   🐱 혜원이 영단어 자동 업로드 스크립트 🌸     ║
║   ─────────────────────────────────────      ║
║   사용법: python 업로드.py                    ║
║   기능: git add + commit + push 자동 실행    ║
╚══════════════════════════════════════════════╝
"""
import subprocess
import os
import sys
from datetime import datetime

# Windows CMD에서 한글 깨짐 방지
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def header(msg):
    print()
    print("=" * 50)
    print(f"  {msg}")
    print("=" * 50)


def ok(msg):
    print(f"  [OK] {msg}")


def fail(msg):
    print(f"  [FAIL] {msg}")


def run(cmd):
    """명령어를 실행하고 결과를 반환해요."""
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    return result


def main():
    header("🐱 혜원이 영단어 업로드 시작! 🌸")

    # ──────────────────────────────────────
    # 1. 현재 위치가 Git 폴더인지 확인
    # ──────────────────────────────────────
    cwd = os.getcwd()
    print(f"\n📍 현재 폴더: {cwd}")

    if not os.path.isdir('.git'):
        fail("여긴 Git 저장소가 아니에요!")
        print("   → D:\\Claude\\05.혜원 영어 폴더에서 실행해주세요.")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)
    ok("Git 저장소 확인")

    # ──────────────────────────────────────
    # 2. 변경 사항 확인
    # ──────────────────────────────────────
    print("\n🔍 변경된 파일 확인 중...")
    status = run("git status --short")

    if not status.stdout.strip():
        print("\n✨ 업로드할 변경사항이 없어요!")
        print("   모든 파일이 이미 최신 상태입니다 😺")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(0)

    print("\n📝 변경된 파일들:")
    print("─" * 50)
    for line in status.stdout.strip().split('\n'):
        print(f"  {line}")
    print("─" * 50)

    # ──────────────────────────────────────
    # 3. 커밋 메시지 입력
    # ──────────────────────────────────────
    now = datetime.now()
    default_msg = f"업데이트 {now.strftime('%Y-%m-%d')}"

    print(f"\n💬 커밋 메시지를 입력해주세요")
    print(f"   (그냥 엔터 누르면 '{default_msg}' 사용)")
    msg = input("   > ").strip()
    if not msg:
        msg = default_msg

    # 메시지에 따옴표 있으면 제거 (오류 방지)
    msg = msg.replace('"', '').replace("'", '')

    # ──────────────────────────────────────
    # 4. Git 명령어 순서대로 실행
    # ──────────────────────────────────────
    print(f"\n⏳ '{msg}' 메시지로 업로드를 시작할게요...")

    # git add
    print("\n  1/3) 파일 담기 (git add)...")
    add_result = run("git add .")
    if add_result.returncode != 0:
        fail(f"git add 실패")
        print(add_result.stderr)
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)
    ok("파일 담기 완료")

    # git commit
    print("\n  2/3) 기록 남기기 (git commit)...")
    commit_result = run(f'git commit -m "{msg}"')
    if commit_result.returncode != 0:
        fail(f"git commit 실패")
        print(commit_result.stderr or commit_result.stdout)
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)
    ok("기록 남기기 완료")

    # git push
    print("\n  3/3) GitHub에 업로드 (git push)...")
    print("       (인증 창이 뜨면 로그인해주세요)")
    push_result = subprocess.run("git push", shell=True)
    if push_result.returncode != 0:
        fail("git push 실패")
        print("   혹시 인터넷 연결이 안 되어 있거나 로그인이 필요할 수 있어요.")
        input("\n엔터를 누르면 종료합니다...")
        sys.exit(1)
    ok("GitHub 업로드 완료!")

    # ──────────────────────────────────────
    # 5. 완료 메시지
    # ──────────────────────────────────────
    header("🎉 업로드 성공! 🎉")
    print("\n📱 1~2분 뒤 아래 링크에서 확인해보세요:")
    print("\n   👉 https://hyewon-english.pages.dev/")
    print("\n🐱 혜원이한테 이 링크만 보내면 끝이에요! 💕")
    input("\n엔터를 누르면 종료합니다...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 업로드를 취소했어요.")
    except Exception as e:
        print(f"\n[ERROR] 예상치 못한 오류: {e}")
        input("\n엔터를 누르면 종료합니다...")
