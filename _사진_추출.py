"""
🖼️ 토요일 시험 HTML에서 혜원이 정답/오답 사진을 추출해서
hyewon/correct/, hyewon/wrong/ 폴더에 저장
→ 모든 퀴즈에서 공유 사용 가능
"""
import re
import base64
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).parent.resolve()
HYEWON_DIR = ROOT / "hyewon"
CORRECT_DIR = HYEWON_DIR / "correct"
WRONG_DIR = HYEWON_DIR / "wrong"
CORRECT_DIR.mkdir(parents=True, exist_ok=True)
WRONG_DIR.mkdir(parents=True, exist_ok=True)

# 추출 대상 (한 파일만 있어도 됨 - 같은 사진 데이터)
SOURCE = ROOT / "20260502" / "혜원이_영단어_토요일_종합시험.html"

if not SOURCE.exists():
    print(f"❌ 소스 파일 없음: {SOURCE}")
    sys.exit(1)

print(f"📂 추출 중: {SOURCE.name}")
content = SOURCE.read_text(encoding='utf-8')


def extract_photos(content, var_name):
    """const VAR = ["data:image/...", "data:image/...", ...] 추출"""
    pattern = rf'const\s+{var_name}\s*=\s*\[(.+?)\];'
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return []
    inside = m.group(1)
    # 각 따옴표로 둘러싸인 base64 데이터 추출
    photos = re.findall(r'"(data:image/[^"]+)"', inside)
    return photos


correct_photos = extract_photos(content, 'CORRECT_PHOTOS')
wrong_photos = extract_photos(content, 'WRONG_PHOTOS')

print(f"\n✅ 정답 사진: {len(correct_photos)}개 발견")
print(f"❌ 오답 사진: {len(wrong_photos)}개 발견")


def save_data_url(data_url, dest):
    """data:image/jpeg;base64,XXXX → 파일로 저장"""
    m = re.match(r'data:image/(\w+);base64,(.+)', data_url)
    if not m:
        return False
    ext = m.group(1).lower()
    if ext == 'jpeg':
        ext = 'jpg'
    img_bytes = base64.b64decode(m.group(2))
    final_path = dest.with_suffix('.' + ext)
    final_path.write_bytes(img_bytes)
    return final_path


saved_correct = []
for i, photo in enumerate(correct_photos, 1):
    dest = CORRECT_DIR / f"photo_{i:02d}"
    saved = save_data_url(photo, dest)
    if saved:
        saved_correct.append(saved.name)
        print(f"  ✓ correct/{saved.name} ({saved.stat().st_size//1024} KB)")

saved_wrong = []
for i, photo in enumerate(wrong_photos, 1):
    dest = WRONG_DIR / f"photo_{i:02d}"
    saved = save_data_url(photo, dest)
    if saved:
        saved_wrong.append(saved.name)
        print(f"  ✓ wrong/{saved.name} ({saved.stat().st_size//1024} KB)")

print(f"\n📊 결과:")
print(f"  hyewon/correct/: {len(saved_correct)}개 저장")
print(f"  hyewon/wrong/: {len(saved_wrong)}개 저장")
print(f"\n→ 영어 퀴즈에서 이제 이 폴더의 사진을 참조하세요!")
