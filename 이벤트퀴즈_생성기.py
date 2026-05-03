"""
🎯 이벤트 퀴즈 자동 생성기
─────────────────────────
기존 이벤트 퀴즈 HTML을 템플릿으로 사용해서
새 문제 + 새 표지로 새 퀴즈 HTML 생성

사용 (스크립트 직접 호출 X, 다른 코드에서 함수 사용):
  from 이벤트퀴즈_생성기 import build_quiz
  build_quiz(template_path, dest_path, config)
"""
import re
import json
import sys
from pathlib import Path


def build_quiz_html(template_html, config):
    """
    template_html: 기존 퀴즈 HTML 문자열
    config: dict with keys:
        title          : 표지 큰 제목 (예: "약수와 배수 수학 퀴즈")
        sub            : 표지 부제목 (예: "공약수·공배수 · 총 20문제")
        badge          : 표지 뱃지 (예: "✨ 초등 5학년")
        icon           : 표지 이모지 (예: "🔢")
        cover_card     : 표지 카드 본문 (3-4줄)
        page_title     : <title> 태그 내용
        questions      : list of dicts [{tc, tag, q, choices, ans, explain}]
    """
    html = template_html

    # 1. <title> 교체
    html = re.sub(
        r'<title>[^<]*</title>',
        f"<title>{config['page_title']}</title>",
        html, count=1
    )

    # 2. 표지 아이콘 교체 (cover-icon 안의 이모지)
    html = re.sub(
        r'(<div class="cover-icon">)[^<]*(</div>)',
        rf"\g<1>{config['icon']}\g<2>",
        html, count=1
    )

    # 3. 표지 뱃지
    html = re.sub(
        r'(<div class="cover-badge">)[^<]*(</div>)',
        rf"\g<1>{config['badge']}\g<2>",
        html, count=1
    )

    # 4. 표지 제목
    html = re.sub(
        r'(<div class="cover-title">)[^<]*(</div>)',
        rf"\g<1>{config['title']}\g<2>",
        html, count=1
    )

    # 5. 표지 부제목
    html = re.sub(
        r'(<div class="cover-sub">).*?(</div>)',
        rf"\g<1>{config['sub']}\g<2>",
        html, count=1, flags=re.DOTALL
    )

    # 6. 표지 카드 (cover-card 내부 <p>)
    html = re.sub(
        r'(<div class="cover-card"><p>).*?(</p></div>)',
        rf"\g<1>{config['cover_card']}\g<2>",
        html, count=1, flags=re.DOTALL
    )

    # 7. QUESTIONS 배열 교체 (가장 중요!)
    questions_js = "var QUESTIONS=[\n"
    for q in config['questions']:
        choices_str = '[' + ','.join(f'"{c}"' for c in q['choices']) + ']'
        # JS 문자열 안전 escape
        q_text = q['q'].replace('"', '\\"').replace('\n', ' ')
        explain_text = q['explain'].replace('"', '\\"').replace('\n', ' ')
        questions_js += f'  {{tc:"{q["tc"]}",tag:"{q["tag"]}",q:"{q_text}",choices:{choices_str},ans:{q["ans"]},explain:"{explain_text}"}},\n'
    questions_js = questions_js.rstrip(',\n') + '\n];'

    html = re.sub(
        r'var QUESTIONS\s*=\s*\[.*?\];',
        questions_js,
        html, count=1, flags=re.DOTALL
    )

    return html


def build_from_files(template_path, dest_path, config):
    """파일 경로로 작업"""
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    new_html = build_quiz_html(template, config)
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    return dest_path


if __name__ == '__main__':
    print("이 스크립트는 다른 스크립트에서 import해서 사용하세요.")
    print("사용 예:")
    print("  from 이벤트퀴즈_생성기 import build_from_files")
    print("  build_from_files('템플릿.html', '저장경로.html', config)")
