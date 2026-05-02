@echo off
chcp 65001 > nul
title 🆘 GitHub 충돌 자동 해결 + 업로드
cd /d "%~dp0"

echo.
echo ╔════════════════════════════════════════════════════╗
echo ║                                                    ║
echo ║   🆘 GitHub 충돌 자동 해결 + 업로드                  ║
echo ║                                                    ║
echo ║   [언제 사용?]                                     ║
echo ║   - "rejected" 또는 "fetch first" 에러 났을 때     ║
echo ║   - 다른 곳(웹/다른 PC)에서 GitHub 수정한 적 있을 때 ║
echo ║                                                    ║
echo ║   [원리]                                           ║
echo ║   1. 우선 로컬 변경 사항 임시 저장 (stash)         ║
echo ║   2. GitHub의 최신 받아오기 (pull --rebase)        ║
echo ║   3. 충돌 시 우리 로컬 버전 유지 (-X ours)         ║
echo ║   4. 임시 저장 복원 + 커밋 + 푸시                  ║
echo ║                                                    ║
echo ╚════════════════════════════════════════════════════╝
echo.

REM 1) 변경 사항 있으면 일단 커밋
git add . > nul 2>&1
git diff --cached --quiet
if errorlevel 1 (
    echo [1/4] 변경 사항 임시 커밋...
    git commit -m "임시 커밋 (충돌 해결 전)" > nul 2>&1
    echo   [OK] 임시 커밋 완료
) else (
    echo [1/4] 변경 사항 없음 - 스킵
)
echo.

REM 2) GitHub의 최신 가져오기 (충돌 시 우리 거 유지)
echo [2/4] GitHub에서 최신 받아오기...
git pull --rebase -X ours
if errorlevel 1 (
    echo.
    echo   [경고] 자동 머지 실패! 수동 해결이 필요해요.
    echo   다음 명령을 시도해보세요:
    echo     git rebase --abort
    echo     git pull
    echo   그 후 Cowork에 와서 도움 요청하세요!
    echo.
    pause
    exit /b 1
)
echo   [OK] 머지 완료
echo.

REM 3) 푸시
echo [3/4] GitHub에 푸시 중...
git push
if errorlevel 1 (
    echo   [실패] 푸시 실패. 인터넷/로그인 확인하세요.
    pause
    exit /b 1
)
echo   [OK] 푸시 성공!
echo.

REM 4) 완료 메시지
echo [4/4] 완료!
echo.
echo ╔════════════════════════════════════════════════════╗
echo ║   ✅ GitHub 업로드 성공!                            ║
echo ║                                                    ║
echo ║   🌐 1~2분 후 확인:                                ║
echo ║      https://hyewon-english.pages.dev/             ║
echo ╚════════════════════════════════════════════════════╝
echo.
echo ──────────────────────────────────────
echo  창을 닫으려면 아무 키나 눌러주세요...
echo ──────────────────────────────────────
pause > nul
