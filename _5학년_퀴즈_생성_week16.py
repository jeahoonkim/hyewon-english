"""5학년 8/17~8/23 이벤트 퀴즈 7개"""
import sys
from pathlib import Path
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).parent.resolve()
SOURCE_ROOT = Path("/sessions/nifty-keen-dirac/mnt/03. 꾸준한 문제")
if not SOURCE_ROOT.exists():
    SOURCE_ROOT = Path("D:/Claude/03. 꾸준한 문제")

sys.path.insert(0, str(ROOT))
from 이벤트퀴즈_생성기 import build_from_files

def make(title, icon, badge, cover, qs):
    return {'page_title':f'혜원이 {icon} {title}','icon':icon,'badge':badge,
            'title':title,'sub':f'{title} 총 20문제','cover_card':cover,'questions':qs}

MATH_8_17 = make('5학년 수학 (분수의 나눗셈)','➗','✨ 초등 5학년','➗ 분수의 나눗셈!\n🧮 응용 문제!\n⭐ 차근차근!', [
    {'tc':'수학','tag':'분수','q':'1/2 ÷ 2 = ?','choices':['1/4','1','2','1/2'],'ans':0,'explain':'1/2 × 1/2 = 1/4'},
    {'tc':'수학','tag':'분수','q':'2/3 ÷ 2 = ?','choices':['1/3','2/3','1/6','2'],'ans':0,'explain':'2/3 × 1/2 = 1/3'},
    {'tc':'수학','tag':'분수','q':'3/4 ÷ 3 = ?','choices':['1/4','3/4','1/12','3'],'ans':0,'explain':'1/4'},
    {'tc':'수학','tag':'분수','q':'역수: 2/3의 역수?','choices':['3/2','2/3','1/2','1/3'],'ans':0,'explain':'분자/분모 뒤집기'},
    {'tc':'수학','tag':'분수','q':'역수: 4의 역수?','choices':['1/4','4','1','40'],'ans':0,'explain':'1/4'},
    {'tc':'수학','tag':'분수','q':'1/2 ÷ 1/4 = ?','choices':['1','2','1/8','4'],'ans':1,'explain':'1/2 × 4 = 2'},
    {'tc':'수학','tag':'분수','q':'1/3 ÷ 1/6 = ?','choices':['1','2','3','1/2'],'ans':1,'explain':'1/3 × 6 = 2'},
    {'tc':'수학','tag':'분수','q':'2/5 ÷ 1/5 = ?','choices':['1','2','2/25','5'],'ans':1,'explain':'2/5 × 5 = 2'},
    {'tc':'수학','tag':'활용','q':'피자 1/2을 4명 똑같이?','choices':['1/8씩','1/4씩','1/2씩','1씩'],'ans':0,'explain':'1/2 ÷ 4 = 1/8'},
    {'tc':'수학','tag':'활용','q':'리본 3/4m를 3등분?','choices':['1/4m','3/4m','1/12m','3m'],'ans':0,'explain':'1/4m'},
    {'tc':'수학','tag':'분수','q':'1/2 × 2 = ?','choices':['1','1/4','2','4'],'ans':0,'explain':'1'},
    {'tc':'수학','tag':'분수','q':'2/3 × 6 = ?','choices':['4','6','12','1/4'],'ans':0,'explain':'2/3 × 6 = 12/3 = 4'},
    {'tc':'수학','tag':'분수','q':'1/4 × 8 = ?','choices':['2','4','8','1/2'],'ans':0,'explain':'8/4 = 2'},
    {'tc':'수학','tag':'단위분수','q':'1/2 + 1/4 = ?','choices':['2/6','3/4','1/8','1'],'ans':1,'explain':'2/4 + 1/4 = 3/4'},
    {'tc':'수학','tag':'단위분수','q':'1/2 - 1/4 = ?','choices':['1/2','1/4','2/4','1/8'],'ans':1,'explain':'2/4 - 1/4 = 1/4'},
    {'tc':'수학','tag':'대분수','q':'2 1/2를 가분수로?','choices':['5/2','3/2','4/2','2/2'],'ans':0,'explain':'2×2+1=5, 5/2'},
    {'tc':'수학','tag':'대분수','q':'7/3을 대분수?','choices':['2 1/3','3 1/3','1 1/3','7 1/3'],'ans':0,'explain':'7÷3=2 나머지 1'},
    {'tc':'수학','tag':'활용','q':'케이크 1/2 × 2명 + 1/4 × 2명?','choices':['1.5조각','2조각','3조각','1조각'],'ans':0,'explain':'1+0.5=1.5'},
    {'tc':'수학','tag':'활용','q':'우유 1/2L를 5컵 나누면?','choices':['1/10L','1/5L','5/2L','없음'],'ans':0,'explain':'1/2 ÷ 5 = 1/10'},
    {'tc':'수학','tag':'활용','q':'리본 8m를 1/2m씩?','choices':['4개','8개','16개','2개'],'ans':2,'explain':'8 ÷ 1/2 = 16!'},
])

SCIENCE_8_18 = make('5학년 과학 (지층과 화석)','🪨','✨ 초등 5학년','🪨 지층과 화석!\n🦴 옛 생물의 흔적!\n⭐ 지구의 역사!', [
    {'tc':'과학','tag':'지층','q':'지층이란?','choices':['땅의 층','산','바다','없음'],'ans':0,'explain':'땅이 쌓인 층'},
    {'tc':'과학','tag':'지층','q':'지층 만들어지는 시간?','choices':['오래','순간','하루','없음'],'ans':0,'explain':'오랜 시간!'},
    {'tc':'과학','tag':'화석','q':'화석은?','choices':['옛 생물 흔적','새 동물','새 식물','없음'],'ans':0,'explain':'옛 흔적!'},
    {'tc':'과학','tag':'화석','q':'화석으로 알 수 있는 것?','choices':['옛 환경·생물','새 학교','새 친구','없음'],'ans':0,'explain':'옛 정보!'},
    {'tc':'과학','tag':'지층','q':'아래 층 vs 위 층 시대?','choices':['아래가 오래됨','위가 오래됨','같음','모름'],'ans':0,'explain':'아래 먼저 쌓임'},
    {'tc':'과학','tag':'지층','q':'지층 모양?','choices':['줄무늬·층층','없음','다 같음','꼬불꼬불'],'ans':0,'explain':'층층!'},
    {'tc':'과학','tag':'암석','q':'암석 = ?','choices':['바위','강','산','달'],'ans':0,'explain':'바위 = 암석'},
    {'tc':'과학','tag':'암석','q':'화성암 예?','choices':['현무암','진흙','모래','없음'],'ans':0,'explain':'화산에서!'},
    {'tc':'과학','tag':'암석','q':'퇴적암 예?','choices':['사암·셰일','현무암','없음','다 같음'],'ans':0,'explain':'쌓여 만들어짐'},
    {'tc':'과학','tag':'화석','q':'공룡 화석은 어디?','choices':['암석 속','강 속','집 속','학교 속'],'ans':0,'explain':'땅 속!'},
    {'tc':'과학','tag':'화석','q':'고생물학자가 하는 일?','choices':['화석 연구','요리','옷','자기'],'ans':0,'explain':'옛 생물 연구'},
    {'tc':'과학','tag':'화산','q':'화산이 폭발하면?','choices':['용암 분출','꽃 핌','자','없음'],'ans':0,'explain':'마그마!'},
    {'tc':'과학','tag':'지진','q':'지진은 왜?','choices':['지각 흔들림','없음','자','놀'],'ans':0,'explain':'땅 흔들림'},
    {'tc':'과학','tag':'지구','q':'지구 표면은?','choices':['지각','맨틀','외핵','내핵'],'ans':0,'explain':'지각!'},
    {'tc':'과학','tag':'지구','q':'지구 내부 가장 안쪽?','choices':['내핵','지각','맨틀','외핵'],'ans':0,'explain':'내핵 = 중심'},
    {'tc':'과학','tag':'활용','q':'바다 속에서 발견된 화석은?','choices':['옛 바다 생물','새 생물','없음','다 같음'],'ans':0,'explain':'그 자리 옛 바다!'},
    {'tc':'과학','tag':'활용','q':'산에서 조개 화석이?','choices':['옛날 바다','없음','다 같음','산에 조개'],'ans':0,'explain':'땅 융기!'},
    {'tc':'과학','tag':'활용','q':'지층 두께가 두꺼우면?','choices':['오래 쌓임','짧은 시간','없음','다 같음'],'ans':0,'explain':'시간 김!'},
    {'tc':'과학','tag':'화석','q':'호박 속 곤충은?','choices':['화석','옷','책','음식'],'ans':0,'explain':'송진에 갇힘!'},
    {'tc':'과학','tag':'활용','q':'지구의 나이?','choices':['약 46억 년','100년','1000년','없음'],'ans':0,'explain':'엄청 오래!'},
])

KOREAN_8_19 = make('5학년 국어 (논설문)','📝','✨ 초등 5학년','📝 논설문 마스터!\n💪 의견 잘 말하기!\n⭐ 설득력!', [
    {'tc':'국어','tag':'논설문','q':'논설문 = ?','choices':['주장하는 글','이야기','시','일기'],'ans':0,'explain':'설득 글!'},
    {'tc':'국어','tag':'논설문','q':'논설문에 필요?','choices':['주장+근거','이야기','노래','그림'],'ans':0,'explain':'근거가 중요!'},
    {'tc':'국어','tag':'논설문','q':'주장이란?','choices':['내 생각','사실만','이야기','없음'],'ans':0,'explain':'내 의견'},
    {'tc':'국어','tag':'논설문','q':'근거란?','choices':['주장 뒷받침','이야기','색','없음'],'ans':0,'explain':'증명!'},
    {'tc':'국어','tag':'논설문','q':'좋은 근거?','choices':['믿을 만한 사실','상상','거짓','없음'],'ans':0,'explain':'사실 위주!'},
    {'tc':'국어','tag':'논설문','q':'논설문 짜임?','choices':['서론-본론-결론','없음','자유','한 가지'],'ans':0,'explain':'3 부분!'},
    {'tc':'국어','tag':'서론','q':'서론에는?','choices':['주제 소개','결말','이야기','없음'],'ans':0,'explain':'문제 제기!'},
    {'tc':'국어','tag':'본론','q':'본론에는?','choices':['주장+근거 자세히','시작','끝','없음'],'ans':0,'explain':'논거 펼침!'},
    {'tc':'국어','tag':'결론','q':'결론에는?','choices':['주장 다시 강조','시작','자','없음'],'ans':0,'explain':'마무리!'},
    {'tc':'국어','tag':'설득','q':'설득력 있는 표현?','choices':['정확한 사실','거짓','이야기','없음'],'ans':0,'explain':'근거 중요'},
    {'tc':'국어','tag':'토론','q':'토론 시 중요?','choices':['예의·근거·경청','싸움','우김','없음'],'ans':0,'explain':'존중!'},
    {'tc':'국어','tag':'토론','q':'반대 의견 들으면?','choices':['경청·존중','무시','자','없음'],'ans':0,'explain':'잘 듣기!'},
    {'tc':'국어','tag':'단어','q':'\"왜냐하면\"의 역할?','choices':['이유 설명','반박','시작','끝'],'ans':0,'explain':'근거 시작'},
    {'tc':'국어','tag':'단어','q':'\"그러므로\"의 역할?','choices':['결론 도출','시작','이야기','없음'],'ans':0,'explain':'결과 표시'},
    {'tc':'국어','tag':'단어','q':'\"예를 들어\"의 역할?','choices':['예시 제시','시작','결론','없음'],'ans':0,'explain':'구체 예!'},
    {'tc':'국어','tag':'활용','q':'주장: 잠은 중요. 근거?','choices':['건강·집중','없음','다 같음','자기'],'ans':0,'explain':'좋은 근거!'},
    {'tc':'국어','tag':'활용','q':'주장: 운동 필요. 근거?','choices':['건강·기분 좋아짐','없음','자','놀'],'ans':0,'explain':'근거!'},
    {'tc':'국어','tag':'활용','q':'주장: 친환경 중요. 근거?','choices':['지구 보호','없음','자','놀'],'ans':0,'explain':'환경!'},
    {'tc':'국어','tag':'주의','q':'논설문에서 조심?','choices':['감정만 안 됨','이야기 안 됨','다 가능','없음'],'ans':0,'explain':'근거 필수!'},
    {'tc':'국어','tag':'주의','q':'논설문 vs 시?','choices':['논설=주장, 시=감정','같음','없음','다 같음'],'ans':0,'explain':'목적 다름!'},
])

SOCIAL_8_20 = make('5학년 사회 (한국 지방)','🗺️','✨ 초등 5학년','🗺️ 한국 지방!\n🏞️ 우리 지역 알기!\n📍 자랑스러운 우리 땅!', [
    {'tc':'사회','tag':'지방','q':'한국 행정 구역 8도?','choices':['있었음 (지금 9도)','없음','다 같음','한 가지'],'ans':0,'explain':'옛 8도!'},
    {'tc':'사회','tag':'지방','q':'서울의 위치?','choices':['중부 한강 근처','남쪽','북쪽','동쪽'],'ans':0,'explain':'중부!'},
    {'tc':'사회','tag':'지방','q':'경기도의 특징?','choices':['서울 둘러쌈','동쪽 끝','없음','다 같음'],'ans':0,'explain':'수도권!'},
    {'tc':'사회','tag':'지방','q':'강원도의 명물?','choices':['설악산·동해','한라산','지리산','없음'],'ans':0,'explain':'설악산!'},
    {'tc':'사회','tag':'지방','q':'충청도의 도시?','choices':['대전·청주','부산·울산','광주·전주','서울·경기'],'ans':0,'explain':'대전!'},
    {'tc':'사회','tag':'지방','q':'전라도의 도시?','choices':['광주·전주','대전·청주','부산·울산','서울·경기'],'ans':0,'explain':'광주!'},
    {'tc':'사회','tag':'지방','q':'경상도의 도시?','choices':['부산·대구·울산','대전·청주','광주·전주','서울'],'ans':0,'explain':'부산!'},
    {'tc':'사회','tag':'지방','q':'제주도의 특징?','choices':['섬·한라산·관광','산이 없음','강이 많음','없음'],'ans':0,'explain':'유명 관광지!'},
    {'tc':'사회','tag':'지방','q':'한국 가장 큰 섬?','choices':['제주도','독도','울릉도','거제도'],'ans':0,'explain':'제주도!'},
    {'tc':'사회','tag':'지방','q':'서울의 강?','choices':['한강','낙동강','금강','영산강'],'ans':0,'explain':'한강!'},
    {'tc':'사회','tag':'지방','q':'부산의 특징?','choices':['남쪽 항구도시','북쪽 산','동쪽 사막','없음'],'ans':0,'explain':'바다!'},
    {'tc':'사회','tag':'지방','q':'대구의 특징?','choices':['더운 분지','시원','북쪽','없음'],'ans':0,'explain':'분지!'},
    {'tc':'사회','tag':'지방','q':'한국 가장 높은 산?','choices':['한라산','지리산','설악산','북한산'],'ans':0,'explain':'한라산 1950m!'},
    {'tc':'사회','tag':'지방','q':'한국 가장 긴 강?','choices':['낙동강','한강','금강','영산강'],'ans':0,'explain':'낙동강 510km!'},
    {'tc':'사회','tag':'지방','q':'대한민국 수도?','choices':['서울','부산','대구','광주'],'ans':0,'explain':'서울!'},
    {'tc':'사회','tag':'지방','q':'동해와 가까운 도?','choices':['강원·경북','전라','충청','경기'],'ans':0,'explain':'동해!'},
    {'tc':'사회','tag':'지방','q':'서해와 가까운 도?','choices':['충청·전라','강원','경북','경남'],'ans':0,'explain':'서해!'},
    {'tc':'사회','tag':'지방','q':'독도는 어디?','choices':['동해 (경상북도)','서해','남해','북해'],'ans':0,'explain':'경북 울릉도 옆!'},
    {'tc':'사회','tag':'지방','q':'한국 지방 음식?','choices':['지역마다 다름','다 같음','한 가지','없음'],'ans':0,'explain':'8도 음식!'},
    {'tc':'사회','tag':'지방','q':'경복궁은 어디?','choices':['서울','부산','대구','광주'],'ans':0,'explain':'서울!'},
])

ENGLISH_8_21 = make('5학년 영어 (비교·최상급)','📈','✨ 초등 5학년','📈 비교급·최상급!\n⭐ 더 크다·가장 크다!\n💪 영어 실력 UP!', [
    {'tc':'영어','tag':'비교급','q':'비교급 만드는 법?','choices':['-er 또는 more','-est','-ed','-ing'],'ans':0,'explain':'-er!'},
    {'tc':'영어','tag':'비교급','q':'\"big\"의 비교급?','choices':['bigger','biggest','more big','big'],'ans':0,'explain':'bigger!'},
    {'tc':'영어','tag':'비교급','q':'\"tall\"의 비교급?','choices':['taller','tallest','more tall','tall'],'ans':0,'explain':'taller'},
    {'tc':'영어','tag':'비교급','q':'\"happy\"의 비교급?','choices':['happier','happiest','more happy','happy'],'ans':0,'explain':'-y → -ier'},
    {'tc':'영어','tag':'비교급','q':'\"beautiful\" 비교급?','choices':['beautifuler','more beautiful','beautifulest','beautiful'],'ans':1,'explain':'긴 단어 = more!'},
    {'tc':'영어','tag':'비교급','q':'\"good\"의 비교급?','choices':['gooder','better','best','more good'],'ans':1,'explain':'불규칙 better'},
    {'tc':'영어','tag':'비교급','q':'\"bad\"의 비교급?','choices':['badder','worse','worst','more bad'],'ans':1,'explain':'불규칙 worse'},
    {'tc':'영어','tag':'최상급','q':'최상급 만드는 법?','choices':['-est 또는 most','-er','-ed','-ing'],'ans':0,'explain':'-est!'},
    {'tc':'영어','tag':'최상급','q':'\"big\"의 최상급?','choices':['biggest','bigger','more big','big'],'ans':0,'explain':'biggest'},
    {'tc':'영어','tag':'최상급','q':'\"good\"의 최상급?','choices':['best','better','goodest','more good'],'ans':0,'explain':'불규칙 best'},
    {'tc':'영어','tag':'최상급','q':'\"bad\"의 최상급?','choices':['worst','worse','badest','most bad'],'ans':0,'explain':'불규칙 worst'},
    {'tc':'영어','tag':'최상급','q':'\"interesting\" 최상급?','choices':['interestingest','most interesting','more interesting','interesting'],'ans':1,'explain':'most!'},
    {'tc':'영어','tag':'활용','q':'\"I am ___ than you.\" 키 큼','choices':['taller','tallest','more tall','tall'],'ans':0,'explain':'비교!'},
    {'tc':'영어','tag':'활용','q':'\"This is the ___ book.\" 최고','choices':['better','best','good','well'],'ans':1,'explain':'최상급!'},
    {'tc':'영어','tag':'활용','q':'\"She is ___ me.\" 더 똑똑','choices':['smarter than','smartest','smart','more smart'],'ans':0,'explain':'-er than'},
    {'tc':'영어','tag':'활용','q':'\"He is the ___ in class.\"','choices':['fast','faster','fastest','more fast'],'ans':2,'explain':'반에서 가장!'},
    {'tc':'영어','tag':'활용','q':'\"This is ___ that.\"','choices':['better than','best','good','more good'],'ans':0,'explain':'비교'},
    {'tc':'영어','tag':'활용','q':'\"more\" 사용 시?','choices':['긴 형용사','짧은 형용사','없음','다 같음'],'ans':0,'explain':'2음절 이상'},
    {'tc':'영어','tag':'활용','q':'\"-est\" 사용 시?','choices':['짧은 형용사','긴 형용사','없음','다 같음'],'ans':0,'explain':'1음절!'},
    {'tc':'영어','tag':'활용','q':'\"as ___ as\" 뜻?','choices':['~만큼 ~한','~보다','~만큼 안','없음'],'ans':0,'explain':'동등 비교'},
])

NONSENSE_8_22 = make('넌센스 퀴즈 20탄','🤪','🎉 재미','🤪 20탄!\n🎉 머리 식히기!\n💡 창의력!', [
    {'tc':'넌센스','tag':'재치','q':'세상에서 가장 큰 박?','choices':['수박','대박','호박','말박'],'ans':1,'explain':'대박!'},
    {'tc':'넌센스','tag':'언어','q':'세상에서 가장 늦게 자는 동물?','choices':['올빼미','부엉이','늦자는 동물','다 가능'],'ans':2,'explain':'늦자!'},
    {'tc':'넌센스','tag':'재치','q':'사람이 가장 좋아하는 색?','choices':['빨강','파랑','내 색','무지개색'],'ans':2,'explain':'내가 좋아하는!'},
    {'tc':'넌센스','tag':'재치','q':'사람이 못 보는 자기 얼굴은?','choices':['거울 안','옆 얼굴','자기 얼굴','자기 얼굴은 안 보임'],'ans':3,'explain':'자기 안 보임!'},
    {'tc':'넌센스','tag':'언어','q':'먹어도 안 줄어드는 약은?','choices':['사약','약속','거짓약','말약'],'ans':1,'explain':'약속!'},
    {'tc':'넌센스','tag':'재치','q':'가장 더운 책은?','choices':['뜨거운 책','자기책 (잠 책)','뜨거운 사람의 책','없음'],'ans':2,'explain':'장난!'},
    {'tc':'넌센스','tag':'재치','q':'사람이 가장 무거운 시간?','choices':['아침','잘 때','시험 보기 전','다 같음'],'ans':1,'explain':'잘 때 무거움'},
    {'tc':'넌센스','tag':'언어','q':'\"감\"이 들어간 과일?','choices':['감 (그냥)','단감','홍시','다 가능'],'ans':3,'explain':'다 감!'},
    {'tc':'넌센스','tag':'재치','q':'사람의 가장 큰 그릇?','choices':['밥그릇','국그릇','마음 그릇','다 같음'],'ans':2,'explain':'마음!'},
    {'tc':'넌센스','tag':'재치','q':'엄마가 가장 좋아하는 글자?','choices':['ㄱ','ㄴ','내 이름','자식 이름'],'ans':3,'explain':'자식!'},
    {'tc':'넌센스','tag':'언어','q':'\"바\"가 5번 나오는 곳?','choices':['바닷가','바위','바바바바바','없음'],'ans':2,'explain':'바바바바바!'},
    {'tc':'넌센스','tag':'재치','q':'세상에서 가장 무서운 운동은?','choices':['축구','농구','시험 운동','달리기'],'ans':2,'explain':'시험!'},
    {'tc':'넌센스','tag':'재치','q':'먹어도 살 안 찌는 약?','choices':['감약','마약','약속','다 같음'],'ans':2,'explain':'약속!'},
    {'tc':'넌센스','tag':'언어','q':'세상에서 가장 좋은 새는?','choices':['앵무새','참새','반가운 새','좋은 새'],'ans':2,'explain':'반가운!'},
    {'tc':'넌센스','tag':'재치','q':'가장 작은 콩은?','choices':['콩알','꼬마 콩','콩 한 알','내 콩'],'ans':2,'explain':'한 알!'},
    {'tc':'넌센스','tag':'재치','q':'가장 안 흔들리는 의자?','choices':['단단한 의자','새 의자','없음 (안 흔들리는 의자)','내 의자'],'ans':2,'explain':'안 흔들!'},
    {'tc':'넌센스','tag':'언어','q':'\"엄\"이 두 번 나오는 사람?','choices':['엄마','엄청 큰 사람','엄엄 (장난)','다 가능'],'ans':2,'explain':'엄엄!'},
    {'tc':'넌센스','tag':'재치','q':'세상에서 가장 작은 곰?','choices':['아기곰','꼬마곰','말곰 (말 곰)','잠곰'],'ans':2,'explain':'말 곰!'},
    {'tc':'넌센스','tag':'재치','q':'사람이 가장 자주 만지는 거?','choices':['전화','책','얼굴','다 가능'],'ans':2,'explain':'얼굴 만짐!'},
    {'tc':'넌센스','tag':'언어','q':'세상에서 가장 흰 색?','choices':['흰색','민트','진흰색','매우 흰'],'ans':2,'explain':'진흰색!'},
])

MIXED_8_23 = make('8월 셋째 주 종합','📚','✨ 초등 5학년','📚 8월 셋째주!\n💪 종합 도전!\n⭐ 화이팅!', [
    {'tc':'종합','tag':'수학','q':'1/2 ÷ 2 = ?','choices':['1/4','1','2','1/2'],'ans':0,'explain':'1/4'},
    {'tc':'종합','tag':'수학','q':'2/3의 역수?','choices':['3/2','2/3','1/2','1/3'],'ans':0,'explain':'3/2'},
    {'tc':'종합','tag':'과학','q':'화석은?','choices':['옛 생물 흔적','새 생물','새 식물','없음'],'ans':0,'explain':'옛 흔적'},
    {'tc':'종합','tag':'과학','q':'지층은 어떻게 만들어져?','choices':['오랜 시간 쌓임','순간에','하루','없음'],'ans':0,'explain':'오래!'},
    {'tc':'종합','tag':'국어','q':'논설문 필요?','choices':['주장+근거','이야기','시','노래'],'ans':0,'explain':'근거!'},
    {'tc':'종합','tag':'국어','q':'\"왜냐하면\" 역할?','choices':['이유 설명','반박','결론','없음'],'ans':0,'explain':'이유!'},
    {'tc':'종합','tag':'사회','q':'한국 가장 큰 섬?','choices':['제주도','독도','울릉도','거제도'],'ans':0,'explain':'제주도'},
    {'tc':'종합','tag':'사회','q':'한국 수도?','choices':['서울','부산','대구','광주'],'ans':0,'explain':'서울'},
    {'tc':'종합','tag':'영어','q':'\"big\" 비교급?','choices':['bigger','biggest','more big','big'],'ans':0,'explain':'bigger'},
    {'tc':'종합','tag':'영어','q':'\"good\" 비교급?','choices':['better','best','gooder','good'],'ans':0,'explain':'better'},
    {'tc':'종합','tag':'수학','q':'1/3 ÷ 1/6 = ?','choices':['1','2','3','1/2'],'ans':1,'explain':'2'},
    {'tc':'종합','tag':'수학','q':'2 1/2 가분수?','choices':['5/2','3/2','4/2','2/2'],'ans':0,'explain':'5/2'},
    {'tc':'종합','tag':'과학','q':'한국 가장 높은 산?','choices':['한라산','지리산','설악산','북한산'],'ans':0,'explain':'한라산'},
    {'tc':'종합','tag':'과학','q':'지구 표면은?','choices':['지각','맨틀','외핵','내핵'],'ans':0,'explain':'지각'},
    {'tc':'종합','tag':'사회','q':'경복궁은 어디?','choices':['서울','부산','대구','광주'],'ans':0,'explain':'서울'},
    {'tc':'종합','tag':'사회','q':'독도는 어디?','choices':['동해','서해','남해','북해'],'ans':0,'explain':'동해'},
    {'tc':'종합','tag':'영어','q':'\"good\" 최상급?','choices':['best','better','goodest','more good'],'ans':0,'explain':'best'},
    {'tc':'종합','tag':'영어','q':'\"bad\" 비교급?','choices':['worse','worst','badder','more bad'],'ans':0,'explain':'worse'},
    {'tc':'종합','tag':'국어','q':'논설문 짜임?','choices':['서론-본론-결론','없음','자유','한 가지'],'ans':0,'explain':'3 부분'},
    {'tc':'종합','tag':'잡학','q':'한국 가장 긴 강?','choices':['낙동강','한강','금강','영산강'],'ans':0,'explain':'낙동강'},
])


def main():
    print("\n=== 8/17~8/23 이벤트 퀴즈 7개 ===")
    if not SOURCE_ROOT.exists(): print("❌ 폴더 없음"); return
    templates = {
        'math': '20260507/혜원이_수학도형측정_퀴즈_20260507.html',
        'science': '20260509/혜원이_과학지구우주_퀴즈_20260509.html',
        'korean': '20260429/혜원이_국어퀴즈_20260429.html',
        'social': '20260506/혜원이_사회세계지리_퀴즈_20260506.html',
        'english': '20260508/혜원이_영어회화문장_퀴즈_20260508.html',
        'nonsense': '20260510/혜원이_넌센스퀴즈_4탄_20260510.html',
    }
    tasks = [
        ('20260817', templates['math'],     '혜원이_수학분수나눗셈_퀴즈_20260817.html', MATH_8_17),
        ('20260818', templates['science'],  '혜원이_과학지층화석_퀴즈_20260818.html', SCIENCE_8_18),
        ('20260819', templates['korean'],   '혜원이_국어논설문_퀴즈_20260819.html', KOREAN_8_19),
        ('20260820', templates['social'],   '혜원이_사회한국지방_퀴즈_20260820.html', SOCIAL_8_20),
        ('20260821', templates['english'],  '혜원이_영어비교최상_퀴즈_20260821.html', ENGLISH_8_21),
        ('20260822', templates['nonsense'], '혜원이_넌센스퀴즈_20탄_20260822.html', NONSENSE_8_22),
        ('20260823', templates['math'],     '혜원이_8월셋째주_퀴즈_20260823.html', MIXED_8_23),
    ]
    success = 0
    for date_folder, template_rel, new_filename, config in tasks:
        template_path = SOURCE_ROOT / template_rel
        if not template_path.exists():
            template_path = SOURCE_ROOT / templates['math']
        dest = SOURCE_ROOT / date_folder / new_filename
        try:
            build_from_files(str(template_path), str(dest), config)
            print(f"✅ {date_folder}: {config['title']}")
            success += 1
        except Exception as e:
            print(f"❌ {date_folder}: {e}")
    print(f"\n✅ {success}/{len(tasks)}개 완료!")

if __name__ == '__main__':
    main()
