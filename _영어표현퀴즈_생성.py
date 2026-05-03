"""
🇺🇸 매일 영어 표현 퀴즈 자동 생성기
─────────────────────────────────────
- 일주일치 영어 표현 퀴즈 HTML 생성 (5/11~5/17)
- 발음 듣기 (🔊) + 힌트 (💡) + 정답 시 +10P
- 5학년 1학기 일상 영어 표현 수준
- index.html과 자동 연동 (포인트 시스템 공유)

폴더: english_quiz/영어퀴즈_YYYYMMDD.html
"""
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).parent.resolve()
OUT_DIR = ROOT / "english_quiz"
OUT_DIR.mkdir(exist_ok=True)


# ═══════════════════════════════════════════════
# 7일치 퀴즈 데이터 (각 20문항)
# ═══════════════════════════════════════════════
# 각 문항: { en, ko_choices[4], ans, hint_word, hint_meaning, explain }
# en: 영어 문장 (발음 대상)
# ko_choices: 4지선다 (한글 보기)
# ans: 정답 인덱스 (0~3)
# hint_word: 어려운 단어
# hint_meaning: 그 단어의 한글 뜻
# explain: 해설

QUIZZES = {
    # ═════════════════════════════════════════════
    # 5/4 (월) - 인사 · 자기소개
    # ═════════════════════════════════════════════
    '20260504': {
        'date': '2026-05-04',
        'day_ko': '월',
        'theme': '인사 · 자기소개',
        'theme_emoji': '👋',
        'description': '안녕! 만나서 반가워! 자기소개해봐요!',
        'questions': [
            {'en':'Hello!','choices':['안녕하세요!','잘 가세요!','고마워요!','죄송해요!'],'ans':0,'hint':('hello','안녕'),'explain':'Hello = 안녕(하세요)'},
            {'en':'Good morning!','choices':['잘 자요!','좋은 아침!','잘 가요!','반가워요!'],'ans':1,'hint':('morning','아침'),'explain':'Good morning = 좋은 아침(인사)'},
            {'en':'Good afternoon.','choices':['좋은 아침','좋은 오후 (인사)','좋은 밤','잘 가'],'ans':1,'hint':('afternoon','오후'),'explain':'Good afternoon = 좋은 오후 인사'},
            {'en':'Good night!','choices':['좋은 아침!','좋은 오후!','잘 자요!','반가워요!'],'ans':2,'hint':('night','밤'),'explain':'Good night = 잘 자요 (잠자기 전)'},
            {'en':'How are you?','choices':['이름이 뭐야?','잘 지내?','어디야?','뭐 해?'],'ans':1,'hint':('how','어떻게'),'explain':'How are you? = 잘 지내?'},
            {'en':"I'm fine, thank you.",'choices':['좋아, 고마워','싫어, 미안해','몰라, 미안해','괜찮아, 좋아'],'ans':0,'hint':('fine','괜찮은'),'explain':"I'm fine = 좋아요/괜찮아요"},
            {'en':"What's your name?",'choices':['몇 살이야?','이름이 뭐야?','어디 살아?','뭐 좋아해?'],'ans':1,'hint':('name','이름'),'explain':'What\\\'s your name? = 이름이 뭐야?'},
            {'en':'My name is Hyewon.','choices':['집은 혜원이야','이름은 혜원이야','학교는 혜원이야','친구는 혜원이야'],'ans':1,'hint':('name','이름'),'explain':'My name is ~ = 내 이름은 ~'},
            {'en':'Nice to meet you.','choices':['만나서 반가워','잘 가요','죄송해요','고마워요'],'ans':0,'hint':('meet','만나다'),'explain':'Nice to meet you = 만나서 반가워'},
            {'en':'Nice to meet you, too.','choices':['고마워요','너도 반가워','싫어요','잘 가요'],'ans':1,'hint':('too','~도'),'explain':'too = ~도, 역시'},
            {'en':'How old are you?','choices':['어디서 왔어?','몇 살이야?','뭐 해?','어디 살아?'],'ans':1,'hint':('old','나이가 든'),'explain':'How old? = 몇 살?'},
            {'en':"I'm eleven years old.",'choices':['10살이야','11살이야','12살이야','13살이야'],'ans':1,'hint':('eleven','11'),'explain':'eleven = 11'},
            {'en':'Where are you from?','choices':['어디 가?','어디서 왔어?','어디 살아?','어디 있어?'],'ans':1,'hint':('from','~에서, ~로부터'),'explain':'Where are you from? = 어디 출신?'},
            {'en':"I'm from Korea.",'choices':['한국에 가요','한국에서 왔어요','한국에 살아요','한국이 좋아요'],'ans':1,'hint':('Korea','한국'),'explain':"I'm from ~ = ~에서 왔어요"},
            {'en':'See you later!','choices':['처음 봐요','이따 봐요','벌써 가요?','지금 봐요'],'ans':1,'hint':('later','나중에'),'explain':'See you later = 이따 봐'},
            {'en':'Goodbye!','choices':['안녕(만남)','안녕히 가세요!','반가워요!','고마워요!'],'ans':1,'hint':('goodbye','잘 가/안녕(헤어질 때)'),'explain':'Goodbye = 헤어질 때 인사'},
            {'en':'See you tomorrow!','choices':['내일 봐!','어제 봤어!','오늘 봐!','다음 주 봐!'],'ans':0,'hint':('tomorrow','내일'),'explain':'See you tomorrow = 내일 보자'},
            {'en':'Thank you very much.','choices':['죄송해요','정말 고마워요','잘 모르겠어요','반가워요'],'ans':1,'hint':('thank','감사하다'),'explain':'Thank you very much = 정말 감사합니다'},
            {'en':"You're welcome.",'choices':['천만에요','죄송해요','반가워요','잘 가요'],'ans':0,'hint':('welcome','환영하는'),'explain':"You're welcome = 천만에요 (감사 인사 답)"},
            {'en':'Have a nice day!',
             'choices':['좋은 하루 보내!','좋은 밤 보내!','수고했어!','잘 가!'],'ans':0,'hint':('nice','좋은'),'explain':'Have a nice day = 좋은 하루 되세요'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/5 (화) - 어린이날 특집! 🎉
    # ═════════════════════════════════════════════
    '20260505': {
        'date': '2026-05-05',
        'day_ko': '화',
        'theme': '어린이날 특집 🎉',
        'theme_emoji': '🎈',
        'description': '신나는 어린이날! 축하·선물·놀이 표현!',
        'questions': [
            {'en':"Happy Children's Day!",'choices':['새해 복 많이!','어린이날 축하해!','크리스마스 즐겁게!','생일 축하해!'],'ans':1,'hint':("children's day",'어린이날'),'explain':'Happy Children\\\'s Day = 어린이날 축하해!'},
            {'en':"It's a special day.",'choices':['특별한 날이야','평범한 날이야','슬픈 날이야','지루한 날이야'],'ans':0,'hint':('special','특별한'),'explain':'special = 특별한'},
            {'en':"Let's have fun!",'choices':['공부하자!','자자!','신나게 놀자!','조용히 하자!'],'ans':2,'hint':('fun','재미'),'explain':"Let's have fun = 신나게 놀자!"},
            {'en':"This is a present for you.",'choices':['이건 너의 선물이야','이건 책이야','이건 음식이야','이건 옷이야'],'ans':0,'hint':('present','선물'),'explain':'present = 선물'},
            {'en':'Wow, thank you so much!','choices':['우와, 정말 고마워!','우와, 미안해!','우와, 모르겠어!','우와, 잘 가!'],'ans':0,'hint':('so much','정말 많이'),'explain':'so much = 정말 많이'},
            {'en':'I love it!','choices':['싫어!','정말 마음에 들어!','괜찮아!','몰라!'],'ans':1,'hint':('love','정말 좋아하다'),'explain':'I love it! = 정말 마음에 들어!'},
            {'en':"Let's go to the park.",'choices':['공원에 가자','학교에 가자','집에 가자','도서관에 가자'],'ans':0,'hint':('park','공원'),'explain':'park = 공원'},
            {'en':'Can we ride the roller coaster?','choices':['놀이공원 가자','롤러코스터 타도 돼?','자전거 사자','집에 가자'],'ans':1,'hint':('roller coaster','롤러코스터'),'explain':'Can we ~? = 우리 ~해도 돼?'},
            {'en':"It's so exciting!",'choices':['너무 무서워!','너무 신나!','너무 졸려!','너무 따분해!'],'ans':1,'hint':('exciting','신나는'),'explain':'exciting = 신나는'},
            {'en':"Let's eat ice cream!",'choices':['아이스크림 만들자!','아이스크림 먹자!','아이스크림 사자!','아이스크림 보자!'],'ans':1,'hint':('eat','먹다'),'explain':"Let's eat ~ = ~ 먹자!"},
            {'en':'I want a chocolate cake.','choices':['초코 케이크 좋아해','초코 케이크 줄게','초코 케이크 만들었어','초코 케이크 원해'],'ans':3,'hint':('want','원하다'),'explain':'I want ~ = ~을 원해'},
            {'en':'Today is so much fun!','choices':['오늘 너무 재밌어!','오늘 너무 졸려!','오늘 너무 더워!','오늘 너무 추워!'],'ans':0,'hint':('fun','재미'),'explain':'so much fun = 정말 재미있는'},
            {'en':"Let's play hide and seek.",'choices':['축구하자','숨바꼭질하자','농구하자','달리기하자'],'ans':1,'hint':('hide and seek','숨바꼭질'),'explain':'hide and seek = 숨바꼭질'},
            {'en':"You're it!",'choices':['네가 술래야!','네가 우승!','네가 졌어!','네가 이겼어!'],'ans':0,'hint':('it','술래 (놀이에서)'),'explain':"You're it! = 술래는 너야!"},
            {'en':"Let's take a picture!",'choices':['책 읽자!','사진 찍자!','공부하자!','자자!'],'ans':1,'hint':('picture','사진'),'explain':'take a picture = 사진을 찍다'},
            {'en':'Smile, please!','choices':['웃어 주세요!','자 주세요!','일어나 주세요!','앉아 주세요!'],'ans':0,'hint':('smile','미소짓다'),'explain':'smile = 웃다, 미소짓다'},
            {'en':'You look so happy!','choices':['너 슬퍼 보여!','너 졸려 보여!','너 정말 행복해 보여!','너 화나 보여!'],'ans':2,'hint':('look','~처럼 보이다'),'explain':'look ~ = ~처럼 보인다'},
            {'en':"It's the best day ever!",'choices':['최악의 날이야','평범한 날이야','지금까지 최고의 날이야!','마지막 날이야'],'ans':2,'hint':('ever','지금까지'),'explain':'best ~ ever = 지금까지 최고의 ~'},
            {'en':'I had so much fun today.','choices':['오늘 너무 졸렸어','오늘 너무 재밌었어','오늘 너무 슬펐어','오늘 너무 바빴어'],'ans':1,'hint':('had','have의 과거형'),'explain':'had fun = 재밌게 보냈다'},
            {'en':"Let's do this again!",'choices':['다시는 안 해!','다시 하자!','이제 그만!','집에 가자!'],'ans':1,'hint':('again','다시'),'explain':"Let's do this again! = 또 하자!"},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/6 (수) - 학교 생활
    # ═════════════════════════════════════════════
    '20260506': {
        'date': '2026-05-06',
        'day_ko': '수',
        'theme': '학교 생활',
        'theme_emoji': '🏫',
        'description': '학교에서 자주 쓰는 표현!',
        'questions': [
            {'en':'I go to school.','choices':['학교에 가요','학교에서 와요','학교가 좋아요','학교를 봐요'],'ans':0,'hint':('go to','~에 가다'),'explain':'go to school = 학교에 가다'},
            {'en':"I'm a fifth grader.",'choices':['4학년이에요','5학년이에요','6학년이에요','중학생이에요'],'ans':1,'hint':('fifth','다섯 번째'),'explain':'fifth grader = 5학년 학생'},
            {'en':"What's your favorite subject?",'choices':['좋아하는 음식이 뭐야?','가장 좋아하는 과목이 뭐야?','어떤 책 좋아해?','뭐 그릴래?'],'ans':1,'hint':('subject','과목'),'explain':'subject = 과목'},
            {'en':'I like math.','choices':['수학이 싫어','수학을 좋아해','수학 잘 못해','수학 책 줘'],'ans':1,'hint':('math','수학'),'explain':'math = 수학'},
            {'en':'My teacher is kind.','choices':['우리 선생님은 무서워','우리 선생님은 친절해','우리 선생님은 키 커','우리 선생님은 어려'],'ans':1,'hint':('kind','친절한'),'explain':'kind = 친절한'},
            {'en':'Open your book, please.','choices':['책을 펴 주세요','책을 덮어주세요','책을 사 주세요','책을 읽어주세요'],'ans':0,'hint':('open','열다, 펴다'),'explain':'open = 열다 / 펴다'},
            {'en':'Close your book.','choices':['책을 펴','책을 덮어','책을 줘','책을 봐'],'ans':1,'hint':('close','닫다'),'explain':'close = 닫다, 덮다'},
            {'en':"Let's read together.",'choices':['같이 자자','같이 먹자','같이 읽자','같이 가자'],'ans':2,'hint':('read','읽다'),'explain':'read together = 함께 읽다'},
            {'en':'Raise your hand.','choices':['손을 들어','일어나','앉아','조용히 해'],'ans':0,'hint':('raise','들다, 올리다'),'explain':'raise your hand = 손을 들다'},
            {'en':"That's correct!",'choices':['틀렸어!','맞았어!','다시 해!','조용히!'],'ans':1,'hint':('correct','맞은, 정확한'),'explain':'correct = 맞은, 정답'},
            {'en':"Good job!",'choices':['잘했어!','못했어!','다시!','쉬자!'],'ans':0,'hint':('job','일'),'explain':'Good job! = 잘했어!'},
            {'en':"Let's take a break.",'choices':['공부 시작하자','잠시 쉬자','숙제하자','집에 가자'],'ans':1,'hint':('break','쉬는 시간'),'explain':'take a break = 쉬다'},
            {'en':"Where is your pencil?",'choices':['연필 사줘','연필 어디 있어?','연필 좋아해?','연필 만들었어?'],'ans':1,'hint':('pencil','연필'),'explain':'pencil = 연필'},
            {'en':"It's in my pencil case.",'choices':['책가방 안에 있어','필통 안에 있어','책상 위에 있어','집에 두고 왔어'],'ans':1,'hint':('pencil case','필통'),'explain':'pencil case = 필통'},
            {'en':'I forgot my homework.','choices':['숙제 안 했어','숙제 두고 왔어 (잊었어)','숙제 다 했어','숙제 좋아해'],'ans':1,'hint':('forgot','잊었다'),'explain':'forgot = 잊었다 (forget의 과거형)'},
            {'en':'May I go to the bathroom?','choices':['화장실 가도 돼요?','화장실이 어디예요?','집에 가도 돼요?','일어나도 돼요?'],'ans':0,'hint':('bathroom','화장실'),'explain':'May I ~? = ~해도 돼요? (정중)'},
            {'en':'Yes, you may.','choices':['아니, 안 돼','응, 돼','잘 모르겠어','싫어'],'ans':1,'hint':('may','~해도 좋다'),'explain':'you may = 해도 좋다'},
            {'en':'The class is over.','choices':['수업 시작이야','수업 끝났어','수업 어려워','수업 재밌어'],'ans':1,'hint':('over','끝난'),'explain':'over = 끝난'},
            {'en':"Let's go home.",'choices':['집에 가자','집에서 와','집이 어디야?','집이 멀어'],'ans':0,'hint':('home','집'),'explain':"Let's go home = 집에 가자"},
            {'en':'See you tomorrow at school!','choices':['내일 학교에서 봐!','내일 집에서 봐!','어제 학교에서 봤어!','다음 주에 봐!'],'ans':0,'hint':('at','~에서'),'explain':'at school = 학교에서'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/7 (목) - 색깔 · 모양
    # ═════════════════════════════════════════════
    '20260507': {
        'date': '2026-05-07',
        'day_ko': '목',
        'theme': '색깔 · 모양',
        'theme_emoji': '🎨',
        'description': '무슨 색이야? 어떻게 생겼어?',
        'questions': [
            {'en':'What color is it?','choices':['그게 뭐야?','무슨 색이야?','얼마야?','어디야?'],'ans':1,'hint':('color','색깔'),'explain':'What color = 무슨 색'},
            {'en':"It's red.",'choices':['파란색이야','빨간색이야','노란색이야','초록색이야'],'ans':1,'hint':('red','빨간색'),'explain':'red = 빨간색'},
            {'en':'My favorite color is blue.','choices':['가장 좋아하는 색은 파란색','가장 좋아하는 색은 빨간색','가장 좋아하는 색은 노란색','가장 좋아하는 색은 초록색'],'ans':0,'hint':('blue','파란색'),'explain':'blue = 파란색'},
            {'en':"The sun is yellow.",'choices':['해는 빨간색','해는 노란색','해는 흰색','해는 검은색'],'ans':1,'hint':('yellow','노란색'),'explain':'yellow = 노란색'},
            {'en':"Grass is green.",'choices':['잔디는 갈색','잔디는 초록색','잔디는 노란색','잔디는 검은색'],'ans':1,'hint':('grass','잔디, 풀'),'explain':'green = 초록색'},
            {'en':'I have a black cat.','choices':['하얀 고양이 있어','검은 고양이 있어','노란 고양이 있어','회색 고양이 있어'],'ans':1,'hint':('black','검은색'),'explain':'black = 검은색'},
            {'en':"Snow is white.",'choices':['눈은 흰색','눈은 회색','눈은 검은색','눈은 파란색'],'ans':0,'hint':('snow','눈'),'explain':'white = 흰색'},
            {'en':'I like pink and purple.','choices':['빨강과 노랑','분홍과 보라','검정과 흰색','파랑과 초록'],'ans':1,'hint':('purple','보라색'),'explain':'pink = 분홍, purple = 보라'},
            {'en':'Oranges are orange.','choices':['오렌지는 빨간색','오렌지는 주황색','오렌지는 노란색','오렌지는 갈색'],'ans':1,'hint':('orange','주황색 (또는 오렌지)'),'explain':'orange = 주황색'},
            {'en':"What shape is it?",'choices':['무슨 모양이야?','무슨 색이야?','얼마야?','어디 있어?'],'ans':0,'hint':('shape','모양'),'explain':'shape = 모양'},
            {'en':"It's a circle.",'choices':['삼각형','원(동그라미)','사각형','별'],'ans':1,'hint':('circle','원, 동그라미'),'explain':'circle = 원'},
            {'en':"It's a triangle.",'choices':['원','삼각형','사각형','오각형'],'ans':1,'hint':('triangle','삼각형'),'explain':'triangle = 삼각형'},
            {'en':"It's a square.",'choices':['원','정사각형','삼각형','별'],'ans':1,'hint':('square','정사각형'),'explain':'square = 정사각형'},
            {'en':'A star has five points.','choices':['별은 점이 4개','별은 점이 5개','별은 점이 3개','별은 점이 6개'],'ans':1,'hint':('star','별'),'explain':'star = 별, point = 끝점'},
            {'en':'The ball is round.','choices':['공은 둥글어','공은 네모야','공은 길어','공은 작아'],'ans':0,'hint':('round','둥근'),'explain':'round = 둥근'},
            {'en':'My pencil is long.','choices':['연필이 짧아','연필이 길어','연필이 작아','연필이 커'],'ans':1,'hint':('long','긴'),'explain':'long = 긴'},
            {'en':'My eraser is short.','choices':['지우개가 길어','지우개가 짧아','지우개가 커','지우개가 작아'],'ans':1,'hint':('short','짧은'),'explain':'short = 짧은'},
            {'en':'The elephant is big.','choices':['코끼리는 작아','코끼리는 커','코끼리는 빨라','코끼리는 느려'],'ans':1,'hint':('big','큰'),'explain':'big = 큰'},
            {'en':'The mouse is small.','choices':['쥐는 커','쥐는 작아','쥐는 빨라','쥐는 느려'],'ans':1,'hint':('small','작은'),'explain':'small = 작은'},
            {'en':'My dress is colorful.','choices':['내 드레스는 까매','내 드레스는 화려해 (색이 많아)','내 드레스는 길어','내 드레스는 작아'],'ans':1,'hint':('colorful','색이 많은, 화려한'),'explain':'colorful = 색깔이 많은, 화려한'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/8 (금) - 동물
    # ═════════════════════════════════════════════
    '20260508': {
        'date': '2026-05-08',
        'day_ko': '금',
        'theme': '동물 친구들',
        'theme_emoji': '🐶',
        'description': '동물원에 가요! 동물 영어 이름!',
        'questions': [
            {'en':'I have a dog.','choices':['고양이 있어요','강아지 있어요','새 있어요','토끼 있어요'],'ans':1,'hint':('dog','강아지, 개'),'explain':'dog = 개, 강아지'},
            {'en':'My cat is cute.','choices':['우리 강아지 귀여워','우리 고양이 귀여워','우리 토끼 귀여워','우리 햄스터 귀여워'],'ans':1,'hint':('cat','고양이'),'explain':'cat = 고양이'},
            {'en':'Birds can fly.','choices':['새는 헤엄칠 수 있어','새는 날 수 있어','새는 달릴 수 있어','새는 점프할 수 있어'],'ans':1,'hint':('fly','날다'),'explain':'fly = 날다'},
            {'en':'Fish live in water.','choices':['물고기는 산에 살아','물고기는 물에 살아','물고기는 하늘에 살아','물고기는 땅에 살아'],'ans':1,'hint':('fish','물고기'),'explain':'fish = 물고기'},
            {'en':'I love my puppy.','choices':['우리 새끼 강아지 사랑해','우리 새끼 고양이 사랑해','우리 토끼 사랑해','우리 새 사랑해'],'ans':0,'hint':('puppy','강아지(새끼)'),'explain':'puppy = 강아지(새끼 강아지)'},
            {'en':"The lion is strong.",'choices':['사자는 약해','사자는 강해','사자는 작아','사자는 빨라'],'ans':1,'hint':('lion','사자'),'explain':'lion = 사자, strong = 강한'},
            {'en':"Tigers are big cats.",'choices':['호랑이는 작은 고양이야','호랑이는 큰 고양잇과(같은 종류)야','호랑이는 개야','호랑이는 사자야'],'ans':1,'hint':('tiger','호랑이'),'explain':'tiger도 cat과(고양잇과) 동물이에요!'},
            {'en':"Elephants have big ears.",'choices':['코끼리는 작은 귀','코끼리는 큰 귀','코끼리는 긴 코','코끼리는 짧은 다리'],'ans':1,'hint':('ear','귀'),'explain':'ear = 귀'},
            {'en':"Monkeys love bananas.",'choices':['원숭이는 바나나를 사랑해','원숭이는 사과를 사랑해','원숭이는 사람을 사랑해','원숭이는 비를 사랑해'],'ans':0,'hint':('monkey','원숭이'),'explain':'monkey = 원숭이'},
            {'en':"Rabbits eat carrots.",'choices':['토끼는 풀을 먹어','토끼는 당근을 먹어','토끼는 고기를 먹어','토끼는 물고기를 먹어'],'ans':1,'hint':('rabbit','토끼'),'explain':'rabbit = 토끼, carrot = 당근'},
            {'en':"The owl is awake at night.",'choices':['올빼미는 낮에 깨어있어','올빼미는 밤에 깨어있어','올빼미는 잠만 자','올빼미는 날 수 없어'],'ans':1,'hint':('owl','올빼미'),'explain':'owl = 올빼미, awake = 깨어있는'},
            {'en':"Penguins live in cold places.",'choices':['펭귄은 따뜻한 곳에 살아','펭귄은 추운 곳에 살아','펭귄은 사막에 살아','펭귄은 숲에 살아'],'ans':1,'hint':('penguin','펭귄'),'explain':'penguin = 펭귄'},
            {'en':"Cows give us milk.",'choices':['소는 우리에게 우유를 줘','소는 우리에게 고기를 줘','소는 우리에게 물을 줘','소는 우리에게 집을 줘'],'ans':0,'hint':('cow','소'),'explain':'cow = 소'},
            {'en':"Sheep have white wool.",'choices':['양은 검은 털이 있어','양은 하얀 털이 있어','양은 갈색 털이 있어','양은 색깔이 많아'],'ans':1,'hint':('sheep','양'),'explain':'sheep = 양, wool = 양털'},
            {'en':"The dog is barking.",'choices':['강아지가 자고 있어','강아지가 짖고 있어','강아지가 먹고 있어','강아지가 달리고 있어'],'ans':1,'hint':('bark','(개가) 짖다'),'explain':'bark = 짖다'},
            {'en':"The cat is sleeping.",'choices':['고양이가 자고 있어','고양이가 놀고 있어','고양이가 먹고 있어','고양이가 우는 중이야'],'ans':0,'hint':('sleep','자다'),'explain':'sleeping = 자고 있는'},
            {'en':"Cows say moo.",'choices':['소는 멍멍','소는 음매','소는 야옹','소는 꼬꼬'],'ans':1,'hint':('say','말하다'),'explain':'영어로 소는 \\"moo\\"라고 표현해요'},
            {'en':"Dogs say woof.",'choices':['개는 음매','개는 야옹','개는 멍멍','개는 꽥꽥'],'ans':2,'hint':('say','말하다'),'explain':'영어로 개는 \\"woof\\"라고 표현해요'},
            {'en':"I want to be a vet.",'choices':['선생님이 되고 싶어','수의사가 되고 싶어','요리사가 되고 싶어','경찰이 되고 싶어'],'ans':1,'hint':('vet','수의사 (veterinarian의 줄임말)'),'explain':'vet = 수의사 (동물 의사)'},
            {'en':"Animals are our friends.",'choices':['동물은 우리 친구야','동물은 위험해','동물은 무서워','동물은 멀리 있어'],'ans':0,'hint':('animal','동물'),'explain':'animal = 동물'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/9 (토) - 운동 · 놀이
    # ═════════════════════════════════════════════
    '20260509': {
        'date': '2026-05-09',
        'day_ko': '토',
        'theme': '운동 · 놀이',
        'theme_emoji': '⚽',
        'description': '같이 운동하자! 같이 놀자!',
        'questions': [
            {'en':'I like soccer.','choices':['축구 싫어','축구 좋아해','축구 못해','축구 잘해'],'ans':1,'hint':('soccer','축구'),'explain':'soccer = 축구'},
            {'en':"Let's play basketball.",'choices':['농구하자','야구하자','축구하자','배구하자'],'ans':0,'hint':('basketball','농구'),'explain':'basketball = 농구'},
            {'en':'I can swim.','choices':['수영 못해','수영 할 수 있어','수영 좋아해','수영 가르쳐'],'ans':1,'hint':('can','~할 수 있다'),'explain':'I can ~ = ~할 수 있어'},
            {'en':"Let's go swimming!",'choices':['수영하러 가자!','수영장 사자!','수영 보자!','수영 그만!'],'ans':0,'hint':('swimming','수영'),'explain':'go swimming = 수영하러 가다'},
            {'en':'I run every morning.','choices':['매일 밤 달려','매일 아침 달려','매일 점심 달려','매일 저녁 달려'],'ans':1,'hint':('every','매~'),'explain':'every morning = 매일 아침'},
            {'en':"Can you ride a bike?",'choices':['자전거 만들 수 있어?','자전거 탈 수 있어?','자전거 살 수 있어?','자전거 줄 수 있어?'],'ans':1,'hint':('ride','타다'),'explain':'ride = (자전거 등을) 타다'},
            {'en':'Yes, I can.','choices':['응, 할 수 있어','아니, 못해','잘 모르겠어','싫어'],'ans':0,'hint':('yes','네/응'),'explain':'Yes, I can = 응, 할 수 있어'},
            {'en':"No, I can't.",'choices':['응, 할 수 있어','아니, 못해','잘 모르겠어','좋아'],'ans':1,'hint':("can't",'~할 수 없다'),'explain':"I can't = 할 수 없어"},
            {'en':'Tennis is fun!','choices':['테니스 무서워!','테니스 재밌어!','테니스 어려워!','테니스 비싸!'],'ans':1,'hint':('tennis','테니스'),'explain':'tennis = 테니스'},
            {'en':'I jump rope at school.','choices':['학교에서 줄넘기 해','집에서 줄넘기 해','공원에서 줄넘기 해','어디서도 줄넘기 안 해'],'ans':0,'hint':('jump rope','줄넘기'),'explain':'jump rope = 줄넘기'},
            {'en':"Let's play tag!",'choices':['술래잡기 하자!','숨바꼭질 하자!','책 읽자!','조용히 하자!'],'ans':0,'hint':('tag','술래잡기'),'explain':'tag = 술래잡기'},
            {'en':'I scored a goal!','choices':['골을 넣었어!','골을 못 넣었어!','시합 졌어!','시합 끝났어!'],'ans':0,'hint':('score','득점하다'),'explain':'score a goal = 골을 넣다'},
            {'en':'Our team won!','choices':['우리 팀이 졌어!','우리 팀이 이겼어!','우리 팀이 비겼어!','우리 팀이 없어!'],'ans':1,'hint':('won','이겼다'),'explain':'won = win(이기다)의 과거형'},
            {'en':'We lost the game.','choices':['우리가 이겼어','우리가 졌어','우리가 비겼어','우리가 시작해'],'ans':1,'hint':('lost','졌다'),'explain':'lost = lose(지다)의 과거형'},
            {'en':'Good game!','choices':['좋은 경기였어!','나쁜 경기였어!','시간 없어!','경기 끝!'],'ans':0,'hint':('game','경기, 게임'),'explain':'Good game = 경기 잘했어! (스포츠 인사)'},
            {'en':'I love playing chess.','choices':['체스 두는 거 좋아해','체스 만드는 거 좋아해','체스 보는 거 싫어','체스 사는 거 좋아해'],'ans':0,'hint':('chess','체스'),'explain':'chess = 체스'},
            {'en':"Let's play together.",'choices':['혼자 놀자','같이 놀자','집에 가자','공부하자'],'ans':1,'hint':('together','함께'),'explain':'play together = 같이 놀다'},
            {'en':"That's not fair!",'choices':['공평하지 않아!','정말 멋져!','괜찮아!','이상해!'],'ans':0,'hint':('fair','공평한'),'explain':'fair = 공평한'},
            {'en':'You did a great job.','choices':['너 잘 못했어','너 정말 잘했어','너 다시 해','너 그만 해'],'ans':1,'hint':('great','정말 좋은'),'explain':'great job = 정말 잘했어'},
            {'en':"I'm tired now.",'choices':['이제 신나','이제 피곤해','이제 배고파','이제 졸려'],'ans':1,'hint':('tired','피곤한'),'explain':'tired = 피곤한'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/10 (일) - 날씨 · 계절
    # ═════════════════════════════════════════════
    '20260510': {
        'date': '2026-05-10',
        'day_ko': '일',
        'theme': '날씨 · 계절',
        'theme_emoji': '☀️',
        'description': '오늘 날씨 어때? 어떤 계절 좋아해?',
        'questions': [
            {'en':"How's the weather today?",'choices':['오늘 날씨 어때?','오늘 뭐 해?','오늘 며칠이야?','오늘 어디 가?'],'ans':0,'hint':('weather','날씨'),'explain':'weather = 날씨'},
            {'en':"It's sunny.",'choices':['비와','맑아','흐려','눈와'],'ans':1,'hint':('sunny','맑은'),'explain':'sunny = 햇빛 비치는, 맑은'},
            {'en':"It's rainy today.",'choices':['오늘 비 와','오늘 맑아','오늘 추워','오늘 더워'],'ans':0,'hint':('rainy','비 오는'),'explain':'rainy = 비 오는'},
            {'en':"It's cloudy.",'choices':['맑아','흐려 (구름 많아)','눈와','바람불어'],'ans':1,'hint':('cloudy','구름 많은, 흐린'),'explain':'cloudy = 흐린'},
            {'en':"It's snowing!",'choices':['눈이 와!','비가 와!','해가 떠!','바람이 불어!'],'ans':0,'hint':('snow','눈'),'explain':"It's snowing = 눈이 오고 있어"},
            {'en':"It's windy outside.",'choices':['밖에 비와','밖에 바람불어','밖에 해 떴어','밖에 눈와'],'ans':1,'hint':('windy','바람 부는'),'explain':'windy = 바람 부는'},
            {'en':"It's hot today.",'choices':['오늘 추워','오늘 더워','오늘 시원해','오늘 따뜻해'],'ans':1,'hint':('hot','더운'),'explain':'hot = 더운'},
            {'en':"It's cold.",'choices':['더워','추워','시원해','따뜻해'],'ans':1,'hint':('cold','추운'),'explain':'cold = 추운'},
            {'en':"It's warm.",'choices':['더워','추워','시원해','따뜻해'],'ans':3,'hint':('warm','따뜻한'),'explain':'warm = 따뜻한'},
            {'en':"It's cool today.",'choices':['오늘 멋져','오늘 시원해','오늘 더워','오늘 추워'],'ans':1,'hint':('cool','시원한'),'explain':'cool = 시원한 (멋진 의미도 있음)'},
            {'en':"I love spring!",'choices':['봄 사랑해!','여름 사랑해!','가을 사랑해!','겨울 사랑해!'],'ans':0,'hint':('spring','봄'),'explain':'spring = 봄'},
            {'en':"Summer is so hot.",'choices':['여름은 너무 더워','겨울은 너무 더워','봄은 너무 따뜻해','가을은 너무 시원해'],'ans':0,'hint':('summer','여름'),'explain':'summer = 여름'},
            {'en':"Fall is beautiful.",'choices':['봄이 아름다워','여름이 아름다워','가을이 아름다워','겨울이 아름다워'],'ans':2,'hint':('fall','가을'),'explain':'fall = 가을 (autumn도 같은 뜻)'},
            {'en':"Winter is cold and snowy.",'choices':['겨울은 따뜻하고 비와','겨울은 춥고 눈와','겨울은 덥고 맑아','겨울은 시원하고 흐려'],'ans':1,'hint':('winter','겨울'),'explain':'winter = 겨울'},
            {'en':'I like flowers in spring.','choices':['봄에 꽃이 좋아','겨울에 눈이 좋아','여름에 비가 좋아','가을에 단풍이 좋아'],'ans':0,'hint':('flower','꽃'),'explain':'flower = 꽃'},
            {'en':"Don't forget your umbrella.",'choices':['우산 잊지 마','우산 사 와','우산 쓰지 마','우산 줘'],'ans':0,'hint':('umbrella','우산'),'explain':'umbrella = 우산'},
            {'en':"Wear a coat. It's cold.",'choices':['모자를 써 (더우니까)','코트를 입어 (추우니까)','신발을 신어 (운동가니까)','셔츠를 입어 (예쁘게)'],'ans':1,'hint':('wear','입다'),'explain':'wear = 입다, coat = 코트'},
            {'en':"It's a beautiful day.",'choices':['아름다운 날이야','지루한 날이야','슬픈 날이야','피곤한 날이야'],'ans':0,'hint':('beautiful','아름다운'),'explain':'beautiful = 아름다운'},
            {'en':"Let's go outside!",'choices':['집에 있자!','밖에 나가자!','자자!','공부하자!'],'ans':1,'hint':('outside','밖, 바깥'),'explain':'outside = 바깥, 밖'},
            {'en':'Look at the rainbow!','choices':['해를 봐!','비를 봐!','무지개를 봐!','구름을 봐!'],'ans':2,'hint':('rainbow','무지개'),'explain':'rainbow = 무지개'},
        ]
    },

    # ─────────────────────────────────────────────
    # 5/11 (월) - 시간 표현
    # ─────────────────────────────────────────────
    '20260511': {
        'date': '2026-05-11',
        'day_ko': '월',
        'theme': '시간 표현',
        'theme_emoji': '🕐',
        'description': '몇 시예요? 아침인가요? 저녁인가요?',
        'questions': [
            {'en':'What time is it?','choices':['몇 시예요?','며칠이에요?','뭐 해요?','어디예요?'],'ans':0,'hint':('time','시간'),'explain':'"What time is it?" = "몇 시예요?"'},
            {'en':"It's 7 o'clock.",'choices':['7월이에요','7일이에요','7시예요','7명이에요'],'ans':2,'hint':("o'clock",'정시 (시 단위)'),'explain':'"o\\\'clock"은 정확히 그 시간이에요. 7시!'},
            {'en':"It's half past three.",'choices':['3시 반이에요','3시예요','30분이에요','3년이에요'],'ans':0,'hint':('half','반'),'explain':'"half past 3" = 3시 반 = 3시 30분!'},
            {'en':'See you in the morning.','choices':['밤에 만나요','아침에 봐요','오후에 봐요','내일 봐요'],'ans':1,'hint':('morning','아침'),'explain':'"in the morning" = 아침에'},
            {'en':"Let's meet at noon.",'choices':['저녁에 만나자','새벽에 만나자','정오(낮 12시)에 만나자','밤에 만나자'],'ans':2,'hint':('noon','정오, 낮 12시'),'explain':'noon은 낮 12시(정오)예요!'},
            {'en':"It's almost midnight.",'choices':['거의 저녁이에요','거의 자정(밤 12시)이에요','거의 아침이에요','거의 점심이에요'],'ans':1,'hint':('midnight','자정, 밤 12시'),'explain':'midnight = 밤 12시!'},
            {'en':'I wake up at seven.','choices':['7시에 자요','7시에 일어나요','7시에 학교 가요','7시에 먹어요'],'ans':1,'hint':('wake up','일어나다'),'explain':'wake up = 잠에서 깨다, 일어나다'},
            {'en':'I go to bed at ten.','choices':['10시에 일어나요','10시에 먹어요','10시에 자요','10시에 놀아요'],'ans':2,'hint':('go to bed','잠자리에 들다'),'explain':'go to bed = 자러 가다'},
            {'en':'School starts at nine.','choices':['학교는 9시에 끝나요','학교는 9시에 시작해요','학교는 9시간이에요','학교는 9개예요'],'ans':1,'hint':('start','시작하다'),'explain':'start = 시작하다'},
            {'en':'The class is over.','choices':['수업이 시작됐어요','수업이 끝났어요','수업이 어려워요','수업이 재밌어요'],'ans':1,'hint':('over','끝난'),'explain':'be over = 끝나다'},
            {'en':"It's Monday today.",'choices':['오늘은 월요일이에요','오늘은 화요일이에요','오늘은 일요일이에요','오늘은 수요일이에요'],'ans':0,'hint':('Monday','월요일'),'explain':'Monday = 월요일'},
            {'en':'See you on Friday!','choices':['목요일에 봐요','금요일에 봐요','토요일에 봐요','일요일에 봐요'],'ans':1,'hint':('Friday','금요일'),'explain':'Friday = 금요일'},
            {'en':'I have lunch at twelve.','choices':['12시에 점심을 먹어요','12시에 일어나요','12시에 자요','12시에 학교 가요'],'ans':0,'hint':('lunch','점심'),'explain':'lunch = 점심 식사'},
            {'en':"Let's eat dinner together.",'choices':['같이 아침 먹자','같이 점심 먹자','같이 저녁 먹자','같이 간식 먹자'],'ans':2,'hint':('dinner','저녁 식사'),'explain':'dinner = 저녁 식사'},
            {'en':'My birthday is in May.','choices':['내 생일은 3월이에요','내 생일은 5월이에요','내 생일은 7월이에요','내 생일은 10월이에요'],'ans':1,'hint':('May','5월'),'explain':'May = 5월'},
            {'en':'Today is May fourth.','choices':['오늘은 4월 5일','오늘은 5월 4일','오늘은 5월 14일','오늘은 4월 15일'],'ans':1,'hint':('fourth','4번째, 4일'),'explain':'May fourth = 5월 4일'},
            {'en':"It's a sunny afternoon.",'choices':['흐린 아침이에요','맑은 오후예요','비 오는 저녁이에요','추운 밤이에요'],'ans':1,'hint':('afternoon','오후'),'explain':'afternoon = 오후 (정오~저녁 사이)'},
            {'en':'Good night, Mom!','choices':['엄마, 좋은 아침!','엄마, 잘 자요!','엄마, 안녕하세요!','엄마, 고마워요!'],'ans':1,'hint':('night','밤'),'explain':'Good night = 잠자기 전 인사'},
            {'en':'See you tomorrow.','choices':['어제 봤어요','오늘 봐요','내일 봐요','다음 주에 봐요'],'ans':2,'hint':('tomorrow','내일'),'explain':'tomorrow = 내일'},
            {'en':'How long does it take?','choices':['얼마나 커요?','얼마나 비싸요?','얼마나 걸려요?','얼마나 멀어요?'],'ans':2,'hint':('take','시간이 걸리다'),'explain':'How long does it take? = 얼마나 걸려요? (시간)'},
        ]
    },

    # ─────────────────────────────────────────────
    # 5/12 (화) - 장소/길찾기
    # ─────────────────────────────────────────────
    '20260512': {
        'date': '2026-05-12',
        'day_ko': '화',
        'theme': '장소·길찾기',
        'theme_emoji': '📍',
        'description': '어디 있어요? 어떻게 가요?',
        'questions': [
            {'en':'Where is the bookstore?','choices':['언제 가요?','책방이 어디 있어요?','책 빌릴 수 있어요?','책 사주세요'],'ans':1,'hint':('bookstore','서점, 책방'),'explain':'Where is ~? = ~가 어디 있어요?'},
            {'en':"It's next to the bank.",'choices':['은행 위에 있어요','은행 옆에 있어요','은행 안에 있어요','은행 멀리 있어요'],'ans':1,'hint':('next to','~ 옆에'),'explain':'next to = ~ 옆에'},
            {'en':"It's in front of the school.",'choices':['학교 안에 있어요','학교 뒤에 있어요','학교 앞에 있어요','학교 옆에 있어요'],'ans':2,'hint':('in front of','~ 앞에'),'explain':'in front of = ~ 앞에'},
            {'en':"It's behind the park.",'choices':['공원 앞','공원 뒤','공원 안','공원 옆'],'ans':1,'hint':('behind','~ 뒤에'),'explain':'behind = ~ 뒤에'},
            {'en':'Go straight, please.','choices':['오른쪽으로 가세요','왼쪽으로 가세요','똑바로 가세요','뒤로 가세요'],'ans':2,'hint':('straight','똑바로, 직진'),'explain':'straight = 똑바로'},
            {'en':'Turn right at the corner.','choices':['모퉁이에서 좌회전하세요','모퉁이에서 우회전하세요','모퉁이에서 멈추세요','모퉁이에서 돌아가세요'],'ans':1,'hint':('corner','모퉁이'),'explain':'turn right = 우회전, corner = 모퉁이'},
            {'en':'Turn left.','choices':['오른쪽','왼쪽으로 도세요','앞으로','뒤로'],'ans':1,'hint':('left','왼쪽'),'explain':'turn left = 왼쪽으로 돌다'},
            {'en':"It's on your right.",'choices':['오른쪽에 있어요','왼쪽에 있어요','앞에 있어요','뒤에 있어요'],'ans':0,'hint':('right','오른쪽'),'explain':'on your right = 당신의 오른쪽에'},
            {'en':"It's on the second floor.",'choices':['1층에 있어요','2층에 있어요','3층에 있어요','지하에 있어요'],'ans':1,'hint':('floor','층'),'explain':'second floor = 2층'},
            {'en':'How do I get to the library?','choices':['도서관이 어디예요?','도서관 어떻게 가요?','도서관 몇 시예요?','도서관 비싸요?'],'ans':1,'hint':('get to','~에 도착하다'),'explain':'How do I get to ~? = ~에 어떻게 가요?'},
            {'en':'Take the bus number 7.','choices':['7번 버스를 타세요','7시에 버스를 타세요','7개의 버스가 있어요','7번째 정거장이에요'],'ans':0,'hint':('take','타다'),'explain':'take the bus = 버스를 타다'},
            {'en':"It's far from here.",'choices':['여기서 가까워요','여기서 멀어요','여기 있어요','여기서 떠나요'],'ans':1,'hint':('far','먼'),'explain':'far = 멀다'},
            {'en':"It's near my house.",'choices':['우리 집과 멀어요','우리 집 근처예요','우리 집 안이에요','우리 집 위예요'],'ans':1,'hint':('near','가까운'),'explain':'near = 가까이, 근처'},
            {'en':'I live in Seoul.','choices':['서울에 살아요','서울에서 왔어요','서울에 가요','서울을 봐요'],'ans':0,'hint':('live','살다'),'explain':'live in ~ = ~에 살다'},
            {'en':'Where do you live?','choices':['어디서 일해요?','어디 살아요?','어디 가요?','어디 있어요?'],'ans':1,'hint':('live','살다'),'explain':'Where do you live? = 어디 사세요?'},
            {'en':'Excuse me, where is the restroom?','choices':['실례합니다, 화장실 어디 있어요?','실례합니다, 식당 어디 있어요?','감사합니다','죄송합니다'],'ans':0,'hint':('restroom','화장실'),'explain':'restroom = 화장실'},
            {'en':"Let's meet at the playground.",'choices':['운동장에서 만나자','학교에서 만나자','집에서 만나자','공원에서 만나자'],'ans':0,'hint':('playground','운동장, 놀이터'),'explain':'playground = 놀이터/운동장'},
            {'en':"It's a long way.",'choices':['빠른 길이에요','짧은 길이에요','먼 길이에요','넓은 길이에요'],'ans':2,'hint':('long','긴'),'explain':'long way = 먼 길'},
            {'en':"It's just around the corner.",'choices':['멀리 있어요','모퉁이 바로 돌면 있어요','집 안에 있어요','없어요'],'ans':1,'hint':('around','주위에'),'explain':'around the corner = 모퉁이만 돌면!'},
            {'en':"You can't miss it.",'choices':['찾기 쉬워요 (꼭 찾을 수 있어요)','찾을 수 없어요','놓치지 마세요','잃어버렸어요'],'ans':0,'hint':('miss','놓치다'),'explain':'You can\\\'t miss it = (눈에 잘 띄어서) 못 찾을 수가 없어요'},
        ]
    },

    # ─────────────────────────────────────────────
    # 5/13 (수) - 부탁/요청
    # ─────────────────────────────────────────────
    '20260513': {
        'date': '2026-05-13',
        'day_ko': '수',
        'theme': '부탁·요청 표현',
        'theme_emoji': '🙏',
        'description': '도와주세요! 같이 해요!',
        'questions': [
            {'en':'Can you help me?','choices':['도와주실래요?','만나서 반가워요','잘 가요','이게 뭐예요?'],'ans':0,'hint':('help','돕다'),'explain':'Can you ~? = ~해 주실래요?'},
            {'en':'Sure, no problem.','choices':['아니요, 안 돼요','네, 문제없어요','잘 모르겠어요','죄송해요'],'ans':1,'hint':('problem','문제'),'explain':'No problem = 문제없어요, 괜찮아요'},
            {'en':'Could you open the door?','choices':['문을 열어주실래요?','문을 닫아주실래요?','문이 어디예요?','문이 잠겼어요'],'ans':0,'hint':('open','열다'),'explain':'Could you ~? = Can you 보다 더 정중한 부탁'},
            {'en':'Please pass the salt.','choices':['소금 좀 주세요','소금이 어디예요?','소금 사세요','소금 만드세요'],'ans':0,'hint':('pass','건네주다'),'explain':'pass = 건네주다, salt = 소금'},
            {'en':'May I borrow your pen?','choices':['펜 사도 돼요?','펜 빌려도 돼요?','펜 어디 있어요?','펜 줘요'],'ans':1,'hint':('borrow','빌리다'),'explain':'May I ~? = ~해도 돼요? (정중한 허락)'},
            {'en':'Of course, here you go.','choices':['아니요, 안 돼요','당연하죠, 여기 있어요','잠시만요','다음에요'],'ans':1,'hint':('of course','물론'),'explain':'Of course = 물론이죠. Here you go = 여기 있어요'},
            {'en':"Can I have some water?",'choices':['물 마실래요?','물 좀 주실래요?','물이 어디예요?','물 좋아해요'],'ans':1,'hint':('have','가지다 / 받다'),'explain':'Can I have ~? = ~ 좀 주세요'},
            {'en':"Could you say it again?",'choices':['다시 한번 말해주실래요?','조용히 해주실래요?','크게 말해주실래요?','쓰세요'],'ans':0,'hint':('again','다시'),'explain':'say it again = 다시 말하다'},
            {'en':"Speak more slowly, please.",'choices':['더 빨리 말해주세요','더 천천히 말해주세요','크게 말해주세요','조용히 해주세요'],'ans':1,'hint':('slowly','천천히'),'explain':'slowly = 천천히'},
            {'en':"I don't understand.",'choices':['알겠어요','이해 못했어요','좋아요','모르겠어요'],'ans':1,'hint':('understand','이해하다'),'explain':"don't understand = 이해 못해요"},
            {'en':"Let's play together!",'choices':['혼자 놀자!','같이 놀자!','집에 가자!','공부하자!'],'ans':1,'hint':('together','함께'),'explain':"Let's ~! = ~하자!"},
            {'en':"Don't worry.",'choices':['걱정 마세요','일하세요','웃어요','자세요'],'ans':0,'hint':('worry','걱정하다'),'explain':"Don't worry = 걱정하지 마"},
            {'en':"Please be quiet.",'choices':['조용히 해주세요','더 크게 말해주세요','웃어주세요','일어나주세요'],'ans':0,'hint':('quiet','조용한'),'explain':'quiet = 조용한'},
            {'en':"Wait a minute, please.",'choices':['빨리요','잠시만 기다려주세요','지금 가세요','앉으세요'],'ans':1,'hint':('wait','기다리다'),'explain':'Wait a minute = 잠시만 기다려'},
            {'en':"Hold on, please.",'choices':['놓아주세요','잠시만 (전화)','잡아주세요','일어나주세요'],'ans':1,'hint':('hold on','잠시 멈추다 / 기다리다'),'explain':'Hold on = 잠깐 기다려요 (전화에서 자주 씀)'},
            {'en':"Could you repeat that?",'choices':['그거 다시 한번 말해주실래요?','반복하지 마세요','쓰세요','노래하세요'],'ans':0,'hint':('repeat','반복하다'),'explain':'repeat = 반복하다'},
            {'en':"Show me, please.",'choices':['보여주세요','말해주세요','만들어주세요','주세요'],'ans':0,'hint':('show','보여주다'),'explain':'show = 보여주다'},
            {'en':"Listen to me carefully.",'choices':['저를 보세요','조심해서 들어주세요','조용히 해주세요','말씀하세요'],'ans':1,'hint':('carefully','조심해서, 신중히'),'explain':'carefully = 신중히, 잘'},
            {'en':"Try it again.",'choices':['다시 해보세요','그만하세요','시작하세요','보세요'],'ans':0,'hint':('try','시도하다'),'explain':'try again = 다시 시도하다'},
            {'en':"You can do it!",'choices':['넌 할 수 있어!','너는 잘 못해','너 어디 있어?','넌 누구야?'],'ans':0,'hint':('can do','할 수 있다'),'explain':'You can do it! = 응원하는 표현! 넌 할 수 있어!'},
        ]
    },

    # ─────────────────────────────────────────────
    # 5/14 (목) - 감정/상태
    # ─────────────────────────────────────────────
    '20260514': {
        'date': '2026-05-14',
        'day_ko': '목',
        'theme': '감정·기분',
        'theme_emoji': '😊',
        'description': '오늘 기분이 어때요?',
        'questions': [
            {'en':'How are you?','choices':['어디 있어요?','잘 지내요?','뭐 해요?','누구예요?'],'ans':1,'hint':('how','어떻게'),'explain':'How are you? = 잘 지내세요?'},
            {'en':"I'm happy today.",'choices':['오늘 슬퍼요','오늘 화나요','오늘 행복해요','오늘 피곤해요'],'ans':2,'hint':('happy','행복한'),'explain':'happy = 행복한'},
            {'en':"I'm a little sad.",'choices':['조금 슬퍼요','조금 기뻐요','매우 화나요','괜찮아요'],'ans':0,'hint':('sad','슬픈'),'explain':'sad = 슬픈, a little = 조금'},
            {'en':"I'm so tired.",'choices':['배고파요','졸려요','너무 피곤해요','신나요'],'ans':2,'hint':('tired','피곤한'),'explain':'tired = 피곤한'},
            {'en':"I'm hungry.",'choices':['목말라요','배고파요','졸려요','추워요'],'ans':1,'hint':('hungry','배고픈'),'explain':'hungry = 배고픈'},
            {'en':"I'm thirsty.",'choices':['배고파요','목말라요','졸려요','더워요'],'ans':1,'hint':('thirsty','목마른'),'explain':'thirsty = 목마른'},
            {'en':"I'm cold.",'choices':['더워요','추워요','아파요','졸려요'],'ans':1,'hint':('cold','추운'),'explain':'cold = 추운'},
            {'en':"I'm so excited!",'choices':['너무 졸려요','너무 신나요','너무 슬퍼요','너무 화나요'],'ans':1,'hint':('excited','신나는'),'explain':'excited = 신나는, 흥분한'},
            {'en':"I'm bored.",'choices':['신나요','지루해요','신기해요','놀라요'],'ans':1,'hint':('bored','지루한'),'explain':'bored = 지루한'},
            {'en':"I'm scared.",'choices':['행복해요','무서워요','자랑스러워요','웃겨요'],'ans':1,'hint':('scared','무서운'),'explain':'scared = 무서운, 두려운'},
            {'en':"That's funny!",'choices':['그거 슬퍼!','그거 웃기다!','그거 이상해!','그거 좋아!'],'ans':1,'hint':('funny','웃긴'),'explain':'funny = 웃긴'},
            {'en':"I'm proud of you.",'choices':['네가 자랑스러워','네가 미워','네가 좋아','네가 부러워'],'ans':0,'hint':('proud','자랑스러운'),'explain':'proud = 자랑스러운'},
            {'en':"That's amazing!",'choices':['괜찮네','놀라워!','별로야','보통이야'],'ans':1,'hint':('amazing','놀라운'),'explain':'amazing = 놀라운, 굉장한'},
            {'en':"I'm fine, thank you.",'choices':['괜찮아요, 고마워요','아파요','피곤해요','슬퍼요'],'ans':0,'hint':('fine','괜찮은'),'explain':'fine = 괜찮은'},
            {'en':"I feel sick.",'choices':['배불러요','아파요','졸려요','신나요'],'ans':1,'hint':('sick','아픈'),'explain':'sick = 아픈, feel = 느끼다'},
            {'en':"I love this song!",'choices':['이 노래 너무 좋아!','이 노래 싫어!','이 노래 모르겠어','이 노래 어려워'],'ans':0,'hint':('love','정말 좋아하다'),'explain':'love = 매우 좋아하다'},
            {'en':"I miss you.",'choices':['너 미워','보고싶어 (그리워)','너 만났어','너 없어'],'ans':1,'hint':('miss','그리워하다'),'explain':'miss = 그리워하다'},
            {'en':"Don't be shy.",'choices':['수줍어 마','웃지 마','울지 마','자지 마'],'ans':0,'hint':('shy','수줍은'),'explain':'shy = 수줍은'},
            {'en':"Cheer up!",'choices':['힘내!','앉아!','일어나!','자!'],'ans':0,'hint':('cheer','격려하다'),'explain':'Cheer up! = 힘내! 기운내!'},
            {'en':"It's okay.",'choices':['괜찮아','아니야','싫어','몰라'],'ans':0,'hint':('okay','괜찮은'),'explain':'It\\\'s okay = 괜찮아요'},
        ]
    },

    # ─────────────────────────────────────────────
    # 5/15 (금) - 일상 활동
    # ─────────────────────────────────────────────
    '20260515': {
        'date': '2026-05-15',
        'day_ko': '금',
        'theme': '일상 활동',
        'theme_emoji': '🏃',
        'description': '오늘 뭐 해요?',
        'questions': [
            {'en':'What do you do?','choices':['어디 가요?','뭐 해요?','언제 가요?','왜 해요?'],'ans':1,'hint':('do','하다'),'explain':'What do you do? = 뭐 해요?'},
            {'en':'I read a book.','choices':['책을 읽어요','책을 사요','책을 만들어요','책을 줘요'],'ans':0,'hint':('read','읽다'),'explain':'read = 읽다'},
            {'en':'I write in my diary.','choices':['일기에 그림 그려요','일기를 써요','일기를 읽어요','일기를 사요'],'ans':1,'hint':('write','쓰다'),'explain':'write = 쓰다, diary = 일기'},
            {'en':'I play soccer.','choices':['축구 봐요','축구 해요','축구공 사요','축구 싫어해요'],'ans':1,'hint':('play','(운동/놀이) 하다'),'explain':'play soccer = 축구를 하다'},
            {'en':'I listen to music.','choices':['음악을 만들어요','음악을 들어요','음악을 봐요','음악을 사요'],'ans':1,'hint':('listen','듣다'),'explain':'listen to ~ = ~을 듣다'},
            {'en':'I watch TV.','choices':['TV를 봐요','TV를 들어요','TV를 사요','TV를 만들어요'],'ans':0,'hint':('watch','보다'),'explain':'watch = 시청하다'},
            {'en':'I draw a picture.','choices':['그림을 봐요','그림을 그려요','그림을 사요','그림을 줘요'],'ans':1,'hint':('draw','그리다'),'explain':'draw = 그리다'},
            {'en':'I sing a song.','choices':['노래를 불러요','노래를 들어요','노래를 만들어요','노래를 사요'],'ans':0,'hint':('sing','노래하다'),'explain':'sing = 노래하다'},
            {'en':'I dance with friends.','choices':['친구와 노래해요','친구와 춤춰요','친구와 놀아요','친구와 자요'],'ans':1,'hint':('dance','춤추다'),'explain':'dance = 춤추다'},
            {'en':'I do my homework.','choices':['숙제를 해요','숙제를 봐요','숙제를 사요','숙제가 없어요'],'ans':0,'hint':('homework','숙제'),'explain':'do homework = 숙제를 하다'},
            {'en':'I take a shower.','choices':['목욕해요 (샤워해요)','옷 입어요','요리해요','잠자요'],'ans':0,'hint':('shower','샤워'),'explain':'take a shower = 샤워하다'},
            {'en':'I brush my teeth.','choices':['머리 빗어요','이를 닦아요','얼굴 씻어요','옷 입어요'],'ans':1,'hint':('brush','솔질하다'),'explain':'brush teeth = 이를 닦다'},
            {'en':'I help my mom.','choices':['엄마를 봐요','엄마를 도와줘요','엄마를 만나요','엄마를 사랑해요'],'ans':1,'hint':('help','돕다'),'explain':'help = 돕다'},
            {'en':'I cook with my dad.','choices':['아빠와 청소해요','아빠와 요리해요','아빠와 놀아요','아빠와 자요'],'ans':1,'hint':('cook','요리하다'),'explain':'cook = 요리하다'},
            {'en':'I clean my room.','choices':['방을 청소해요','방을 봐요','방에 들어가요','방을 만들어요'],'ans':0,'hint':('clean','청소하다'),'explain':'clean = 청소하다'},
            {'en':'I ride my bike.','choices':['자전거를 사요','자전거를 봐요','자전거를 타요','자전거를 만들어요'],'ans':2,'hint':('ride','타다'),'explain':'ride = (자전거 등을) 타다'},
            {'en':'I swim in the pool.','choices':['수영장에 가요','수영장에서 수영해요','수영장이 좋아요','수영장에서 놀아요'],'ans':1,'hint':('swim','수영하다'),'explain':'swim = 수영하다, pool = 수영장'},
            {'en':'I run very fast.','choices':['천천히 걸어요','매우 빨리 달려요','빠르게 자요','빠르게 먹어요'],'ans':1,'hint':('fast','빠른'),'explain':'fast = 빠르게'},
            {'en':'I jump rope.','choices':['줄넘기 해요','밧줄을 사요','줄을 만들어요','달려요'],'ans':0,'hint':('rope','밧줄, 줄'),'explain':'jump rope = 줄넘기'},
            {'en':"I'm playing video games.",'choices':['게임 보고 있어요','게임 사고 있어요','게임 하고 있어요','게임 만들고 있어요'],'ans':2,'hint':('playing','하고 있는 (-ing)'),'explain':"I'm playing = 나는 (지금) 하고 있어요"},
        ]
    },

    # ─────────────────────────────────────────────
    # 5/16 (토) - 음식/주문
    # ─────────────────────────────────────────────
    '20260516': {
        'date': '2026-05-16',
        'day_ko': '토',
        'theme': '음식·주문',
        'theme_emoji': '🍔',
        'description': '뭐 먹을래요? 주문할게요!',
        'questions': [
            {'en':"What's your favorite food?",'choices':['뭐 먹어요?','가장 좋아하는 음식이 뭐예요?','얼마예요?','어디서 먹어요?'],'ans':1,'hint':('favorite','가장 좋아하는'),'explain':'favorite = 가장 좋아하는'},
            {'en':'I like pizza.','choices':['피자 싫어해요','피자 좋아해요','피자 만들어요','피자 봐요'],'ans':1,'hint':('like','좋아하다'),'explain':'like = 좋아하다'},
            {'en':'I love ice cream!','choices':['아이스크림 싫어!','아이스크림 정말 좋아!','아이스크림 사줘!','아이스크림 만들어!'],'ans':1,'hint':('love','매우 좋아하다'),'explain':'love = like보다 더 좋아함'},
            {'en':"I'm hungry. Let's eat.",'choices':['목말라. 마시자','졸려. 자자','배고파. 먹자','심심해. 놀자'],'ans':2,'hint':('eat','먹다'),'explain':"Let's eat = 먹자!"},
            {'en':"I'd like a hamburger, please.",'choices':['햄버거 한 개 주세요','햄버거 만들고 싶어요','햄버거 좋아해요','햄버거 어디예요?'],'ans':0,'hint':("I'd like",'~ 주세요 (정중한 주문)'),'explain':"I'd like = ~ 주세요"},
            {'en':'How much is this?','choices':['이거 얼마예요?','이거 뭐예요?','이거 어디 있어요?','이거 좋아해요?'],'ans':0,'hint':('how much','얼마'),'explain':'How much? = 얼마예요?'},
            {'en':"It's five dollars.",'choices':['5달러예요','5천원이에요','5명이에요','5시예요'],'ans':0,'hint':('dollars','달러'),'explain':'dollars = 달러 (미국 돈)'},
            {'en':'Here is the menu.','choices':['여기 메뉴판이에요','여기 음식이에요','여기 영수증이에요','여기 돈이에요'],'ans':0,'hint':('menu','메뉴'),'explain':'menu = 메뉴, 메뉴판'},
            {'en':"It's delicious!",'choices':['맛있어요!','맛없어요!','뜨거워요!','차가워요!'],'ans':0,'hint':('delicious','맛있는'),'explain':'delicious = 매우 맛있는'},
            {'en':"It's too sweet.",'choices':['너무 짜요','너무 달아요','너무 매워요','너무 셔요'],'ans':1,'hint':('sweet','단'),'explain':'sweet = 단, too = 너무'},
            {'en':"It's spicy!",'choices':['싱거워!','매워!','달아!','뜨거워!'],'ans':1,'hint':('spicy','매운'),'explain':'spicy = 매운'},
            {'en':'Can I have some milk?','choices':['우유 좀 주실래요?','우유 만들 수 있어요?','우유 좋아해요?','우유 살래요?'],'ans':0,'hint':('milk','우유'),'explain':'Can I have ~? = ~ 주세요'},
            {'en':'I want apple juice.','choices':['사과를 원해요','사과주스를 원해요','오렌지주스를 원해요','우유를 원해요'],'ans':1,'hint':('juice','주스'),'explain':'apple juice = 사과주스'},
            {'en':"What's for breakfast?",'choices':['저녁 메뉴는?','점심 메뉴는?','아침 메뉴는?','간식 메뉴는?'],'ans':2,'hint':('breakfast','아침 식사'),'explain':'breakfast = 아침 식사'},
            {'en':"Let's order pizza.",'choices':['피자 만들자','피자 주문하자','피자 사자','피자 먹지말자'],'ans':1,'hint':('order','주문하다'),'explain':'order = 주문하다'},
            {'en':"It's too hot.",'choices':['너무 차가워요','너무 뜨거워요','너무 비싸요','너무 작아요'],'ans':1,'hint':('hot','뜨거운/매운'),'explain':'hot = 뜨거운'},
            {'en':'I drink water every day.','choices':['매일 물을 마셔요','매일 우유를 마셔요','매일 주스를 마셔요','매일 차를 마셔요'],'ans':0,'hint':('drink','마시다'),'explain':'drink = 마시다'},
            {'en':'Try this cookie!','choices':['이 쿠키 보세요!','이 쿠키 먹어보세요!','이 쿠키 사세요!','이 쿠키 만들어요!'],'ans':1,'hint':('try','시도하다 / 먹어보다'),'explain':'Try ~ = ~을 한 번 해봐'},
            {'en':"That looks yummy!",'choices':['맛있어 보여요!','이상해 보여요!','커 보여요!','작아 보여요!'],'ans':0,'hint':('yummy','맛있는 (귀여운 표현)'),'explain':'yummy = 맛있어 보이는 (어린이가 자주 씀)'},
            {'en':"I'm full, thank you.",'choices':['배고파요, 고마워요','배불러요, 고마워요','목말라요, 고마워요','졸려요, 고마워요'],'ans':1,'hint':('full','가득 찬, 배부른'),'explain':'I\\\'m full = 배불러요'},
        ]
    },

    # ─────────────────────────────────────────────
    # 5/17 (일) - 가족/친구
    # ─────────────────────────────────────────────
    '20260517': {
        'date': '2026-05-17',
        'day_ko': '일',
        'theme': '가족·친구',
        'theme_emoji': '👨‍👩‍👧',
        'description': '내 가족과 친구를 소개해요!',
        'questions': [
            {'en':'This is my mom.','choices':['이 사람은 우리 아빠예요','이 사람은 우리 엄마예요','이 사람은 우리 형이에요','이 사람은 우리 동생이에요'],'ans':1,'hint':('mom','엄마'),'explain':'mom = 엄마'},
            {'en':'This is my dad.','choices':['우리 엄마예요','우리 아빠예요','우리 누나예요','우리 형이에요'],'ans':1,'hint':('dad','아빠'),'explain':'dad = 아빠'},
            {'en':'I have one brother.','choices':['형이 한 명 있어요','누나가 있어요','동생이 두 명 있어요','없어요'],'ans':0,'hint':('brother','형/오빠/남동생'),'explain':'brother = 형/오빠/남동생'},
            {'en':'She is my sister.','choices':['그는 우리 형이에요','그녀는 우리 자매예요','그녀는 우리 친구예요','그녀는 선생님이에요'],'ans':1,'hint':('sister','언니/누나/여동생'),'explain':'sister = 언니/누나/여동생'},
            {'en':'My grandma is kind.','choices':['우리 할머니는 친절해요','우리 할아버지는 친절해요','우리 엄마는 친절해요','우리 친구는 친절해요'],'ans':0,'hint':('grandma','할머니'),'explain':'grandma = 할머니'},
            {'en':'My grandpa is funny.','choices':['우리 할머니는 웃겨요','우리 할아버지는 웃겨요','우리 삼촌은 웃겨요','우리 형은 웃겨요'],'ans':1,'hint':('grandpa','할아버지'),'explain':'grandpa = 할아버지'},
            {'en':"He's my best friend.",'choices':['그는 모르는 사람이에요','그는 가장 친한 친구예요','그는 사촌이에요','그는 형이에요'],'ans':1,'hint':('best friend','가장 친한 친구'),'explain':'best friend = 베프, 가장 친한 친구'},
            {'en':"What's your name?",'choices':['몇 살이에요?','이름이 뭐예요?','어디 살아요?','뭐 좋아해요?'],'ans':1,'hint':('name','이름'),'explain':'What\\\'s your name? = 이름이 뭐예요?'},
            {'en':'My name is Hyewon.','choices':['이름은 혜원이에요','집은 혜원이에요','학교는 혜원이에요','친구는 혜원이에요'],'ans':0,'hint':('name','이름'),'explain':'My name is ~ = 제 이름은 ~예요'},
            {'en':'How old are you?','choices':['어디 살아요?','몇 살이에요?','뭐 해요?','누구예요?'],'ans':1,'hint':('old','나이가 든'),'explain':'How old? = 몇 살?'},
            {'en':"I'm eleven years old.",'choices':['10살이에요','11살이에요','12살이에요','13살이에요'],'ans':1,'hint':('eleven','11'),'explain':'eleven = 11'},
            {'en':"Nice to meet you.",'choices':['만나서 반가워요','잘 가요','죄송해요','고마워요'],'ans':0,'hint':('meet','만나다'),'explain':'Nice to meet you = 만나서 반가워요'},
            {'en':'See you later!','choices':['안녕!','빨리 가!','이따 봐!','지금 가!'],'ans':2,'hint':('later','나중에'),'explain':'See you later = 이따 봐, 나중에 봐'},
            {'en':'Where are you from?','choices':['어디 가요?','어디서 왔어요?','어디 살아요?','어디 있어요?'],'ans':1,'hint':('from','~로부터'),'explain':'Where are you from? = 어디 출신이에요?'},
            {'en':"I'm from Korea.",'choices':['한국에 가요','한국에서 왔어요','한국에 살아요','한국이 좋아요'],'ans':1,'hint':('Korea','한국'),'explain':"I'm from ~ = ~에서 왔어요"},
            {'en':'Do you have any pets?','choices':['반려동물 있어요?','애완동물 좋아해요?','동물원 가요?','강아지 봤어요?'],'ans':0,'hint':('pet','반려동물'),'explain':'pet = 반려동물 (강아지·고양이 등)'},
            {'en':'I have a cute puppy.','choices':['귀여운 고양이가 있어요','귀여운 강아지가 있어요','강아지를 원해요','강아지가 어디예요?'],'ans':1,'hint':('puppy','강아지'),'explain':'puppy = 강아지 (어린 강아지)'},
            {'en':"My uncle is very tall.",'choices':['이모는 키가 커요','삼촌은 키가 커요','삼촌은 키가 작아요','삼촌은 멋져요'],'ans':1,'hint':('uncle','삼촌, 이모부'),'explain':'uncle = 삼촌/외삼촌/이모부 등 남자 친척'},
            {'en':"My aunt lives in Busan.",'choices':['이모는 부산에 살아요','삼촌은 부산에 살아요','이모는 서울에 살아요','이모는 부산에 가요'],'ans':0,'hint':('aunt','이모, 고모'),'explain':'aunt = 이모/고모/숙모 등 여자 친척'},
            {'en':"I love my family.",'choices':['가족이 미워요','가족을 사랑해요','가족이 많아요','가족이 없어요'],'ans':1,'hint':('family','가족'),'explain':'I love my family = 우리 가족을 사랑해요!'},
        ]
    },
}


# ═══════════════════════════════════════════════
# HTML 템플릿
# ═══════════════════════════════════════════════
def build_quiz_html(date_key, data):
    questions_js = json.dumps(data['questions'], ensure_ascii=False, indent=2)
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0">
<title>🇺🇸 영어 표현 퀴즈 - {data['theme']}</title>
<link href="https://fonts.googleapis.com/css2?family=Jua&family=Gaegu:wght@400;700&family=Fredoka:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{
  min-height:100vh;
  background:linear-gradient(180deg,#74b9ff 0%,#a29bfe 50%,#fd79a8 100%);
  font-family:'Jua','Gaegu',sans-serif;
  color:#fff; overflow-x:hidden;
}}
.wrap{{max-width:560px;margin:0 auto;padding:18px 14px 60px;position:relative;}}
.screen{{display:none;}}.screen.active{{display:block;}}

/* ── 표지 ── */
.cover{{min-height:90vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:40px 20px;}}
.cover-icon{{font-size:90px;margin-bottom:14px;animation:bobble 2s ease-in-out infinite;filter:drop-shadow(0 6px 16px rgba(0,0,0,0.3));}}
@keyframes bobble{{0%,100%{{transform:rotate(-8deg);}}50%{{transform:rotate(8deg);}}}}
.cover-badge{{display:inline-block;background:#fff;color:#0984e3;font-size:.85em;font-weight:800;border-radius:20px;padding:6px 18px;margin-bottom:14px;font-family:'Jua',cursive;}}
.cover-title{{font-family:'Jua',cursive;font-size:2.4em;line-height:1.2;text-shadow:2px 4px 10px rgba(0,0,0,0.3);margin-bottom:6px;}}
.cover-day{{font-size:1em;color:rgba(255,255,255,0.85);margin-bottom:8px;}}
.cover-sub{{font-size:.92em;color:rgba(255,255,255,0.85);margin-bottom:28px;}}
.cover-card{{background:rgba(255,255,255,0.17);backdrop-filter:blur(10px);border:1.5px solid rgba(255,255,255,0.3);border-radius:18px;padding:18px 22px;margin-bottom:28px;max-width:380px;}}
.cover-card p{{font-size:.95em;line-height:1.7;color:#fff;}}
.cover-info{{font-size:.85em;color:rgba(255,255,255,0.8);margin-top:10px;}}
.btn-start{{background:#fff;color:#0984e3;border:none;border-radius:50px;padding:16px 50px;font-size:1.25em;font-weight:800;cursor:pointer;font-family:'Jua',cursive;box-shadow:0 6px 20px rgba(0,0,0,0.3);transition:.2s;}}
.btn-start:hover{{transform:translateY(-3px) scale(1.03);box-shadow:0 10px 28px rgba(0,0,0,0.4);}}

/* ── 진행 바 ── */
.prog-wrap{{margin-bottom:14px;padding-top:8px;}}
.prog-bg{{height:10px;background:rgba(255,255,255,0.2);border-radius:10px;overflow:hidden;}}
.prog-bar{{height:100%;background:linear-gradient(90deg,#fff,#fdcb6e);border-radius:10px;transition:.4s;}}
.prog-label{{font-size:.85em;color:rgba(255,255,255,0.85);text-align:right;margin-top:4px;}}
.score-bar{{display:flex;justify-content:space-between;margin-bottom:10px;font-size:.9em;}}
.score-bar span{{background:rgba(255,255,255,0.18);padding:5px 12px;border-radius:12px;font-family:'Jua',sans-serif;}}

/* ── 문제 카드 ── */
.q-num{{font-size:.9em;color:rgba(255,255,255,0.7);margin-bottom:6px;font-family:'Jua',sans-serif;}}
.q-card{{background:rgba(255,255,255,0.96);color:#2c3e50;border-radius:20px;padding:22px 18px;margin-bottom:14px;box-shadow:0 6px 20px rgba(0,0,0,0.2);}}
.en-row{{display:flex;align-items:center;gap:10px;margin-bottom:8px;}}
.en-text{{flex:1;font-family:'Fredoka',sans-serif;font-size:1.4em;font-weight:600;line-height:1.3;color:#2c3e50;}}
.speak-btn{{background:linear-gradient(135deg,#74b9ff,#0984e3);color:#fff;border:none;border-radius:50%;width:46px;height:46px;font-size:20px;cursor:pointer;box-shadow:0 4px 0 #0652a3,0 4px 10px rgba(9,132,227,0.4);transition:all 0.15s ease;flex-shrink:0;display:inline-flex;align-items:center;justify-content:center;}}
.speak-btn:active{{transform:translateY(2px);box-shadow:0 2px 0 #0652a3;}}
.speak-btn.speaking{{background:linear-gradient(135deg,#ffd700,#ff8c42);transform:scale(0.95);}}
.hint-row{{display:flex;justify-content:flex-end;margin:6px 0 12px;}}
.hint-btn{{background:#fff3bf;color:#92400e;border:1.5px solid #fbc02d;border-radius:14px;padding:6px 14px;font-size:.85em;cursor:pointer;font-family:'Jua',sans-serif;}}
.hint-btn:hover{{background:#ffe066;}}
.hint-box{{background:#fff8d8;border:1px dashed #fbc02d;border-radius:12px;padding:10px 14px;margin-bottom:12px;color:#92400e;font-size:.92em;display:none;}}
.hint-box.show{{display:block;}}

.choice{{display:block;width:100%;background:rgba(255,255,255,0.96);color:#2c3e50;border:2px solid rgba(255,255,255,0.5);border-radius:14px;padding:14px 16px;font-size:1em;font-weight:600;text-align:left;cursor:pointer;margin-top:10px;transition:.18s;font-family:'Gaegu',sans-serif;}}
.choice:hover:not(:disabled){{background:#fff;border-color:#fdcb6e;transform:translateX(4px);}}
.choice.correct{{background:#d1f7e2;border-color:#00b894;color:#00665e;}}
.choice.wrong{{background:#ffd6d6;border-color:#e17055;color:#a32d20;}}

/* ── 결과 팝업 ── */
.overlay{{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.65);z-index:200;align-items:center;justify-content:center;padding:20px;}}
.overlay.show{{display:flex;}}
.pop{{background:#fff;border-radius:24px;padding:26px 22px;max-width:380px;width:100%;text-align:center;color:#2c3e50;animation:popIn .35s cubic-bezier(.34,1.56,.64,1);}}
@keyframes popIn{{from{{transform:scale(.55);opacity:0;}}to{{transform:scale(1);opacity:1;}}}}
.pop-emoji{{font-size:64px;margin-bottom:8px;}}
.pop-title{{font-family:'Jua',cursive;font-size:2em;margin-bottom:6px;}}
.pop-title.ok{{color:#00b894;}}.pop-title.ng{{color:#e17055;}}
.pop-points{{display:inline-block;background:#fff3bf;color:#92400e;padding:5px 14px;border-radius:14px;font-weight:700;margin-bottom:10px;}}
.pop-explain{{font-size:.95em;color:#34495e;line-height:1.6;margin-bottom:20px;}}
.btn-next{{background:linear-gradient(135deg,#74b9ff,#0984e3);color:#fff;border:none;border-radius:50px;padding:13px 36px;font-size:1.05em;font-weight:800;cursor:pointer;font-family:'Jua',cursive;box-shadow:0 4px 12px rgba(9,132,227,0.4);}}

/* ── 결과 화면 ── */
.final{{text-align:center;padding:40px 20px;}}
.final-emoji{{font-size:90px;margin-bottom:14px;}}
.final-title{{font-family:'Jua',cursive;font-size:2em;margin-bottom:8px;}}
.final-score{{font-family:'Jua',cursive;font-size:3em;color:#fdcb6e;margin-bottom:4px;text-shadow:2px 4px 8px rgba(0,0,0,0.3);}}
.final-pts{{font-size:1.1em;color:#fff;margin-bottom:14px;font-family:'Jua',sans-serif;}}
.final-pts b{{color:#fdcb6e;font-size:1.4em;}}
.final-stars{{font-size:1.8em;color:#fdcb6e;margin-bottom:14px;letter-spacing:6px;}}
.final-msg{{font-size:1em;line-height:1.7;color:#fff;margin-bottom:20px;max-width:380px;margin-left:auto;margin-right:auto;}}
.btn-home{{background:rgba(255,255,255,0.95);color:#0984e3;border:none;border-radius:50px;padding:13px 36px;font-size:1.05em;font-weight:800;cursor:pointer;font-family:'Jua',cursive;text-decoration:none;display:inline-block;margin:6px 4px;}}
.btn-retry{{background:#fdcb6e;color:#2c3e50;border:none;border-radius:50px;padding:13px 36px;font-size:1.05em;font-weight:800;cursor:pointer;font-family:'Jua',cursive;margin:6px 4px;}}
</style>
</head>
<body>
<div class="wrap">

<!-- 표지 -->
<div id="startScreen" class="screen active">
  <div class="cover">
    <div class="cover-icon">{data['theme_emoji']}</div>
    <div class="cover-badge">✨ 초등 5학년 영어</div>
    <div class="cover-title">{data['theme']}</div>
    <div class="cover-day">{data['date']} ({data['day_ko']})</div>
    <div class="cover-sub">📝 총 20문제 · 🎁 정답 +10P</div>
    <div class="cover-card"><p>{data['description']}<br>🔊 발음 듣기 & 💡 힌트도 있어요!</p></div>
    <button class="btn-start" onclick="startQuiz()">🚀 시작하기!</button>
  </div>
</div>

<!-- 퀴즈 -->
<div id="quizScreen" class="screen">
  <div class="prog-wrap">
    <div class="prog-bg"><div class="prog-bar" id="progBar" style="width:0%"></div></div>
    <div class="prog-label" id="progLabel">1 / 20</div>
  </div>
  <div class="score-bar">
    <span>📝 문제 <b id="qNum">1</b></span>
    <span>⭐ 점수 <b id="liveScore">0</b></span>
    <span>🎁 +<b id="livePts">0</b>P</span>
  </div>
  <div class="q-card">
    <div class="en-row">
      <div class="en-text" id="qText"></div>
      <button class="speak-btn" id="speakBtn" onclick="speakCurrent()">🔊</button>
    </div>
    <div class="hint-row">
      <button class="hint-btn" onclick="showHint()">💡 힌트 보기</button>
    </div>
    <div class="hint-box" id="hintBox"></div>
  </div>
  <div id="choices"></div>
</div>

<!-- 결과 -->
<div id="finalScreen" class="screen">
  <div class="final">
    <div class="final-emoji" id="finalEmoji">🏆</div>
    <div class="final-title" id="finalTitle">완료!</div>
    <div class="final-score" id="scoreNum">0/20</div>
    <div class="final-stars" id="finalStars"></div>
    <div class="final-pts">획득: <b id="finalPts">0</b>P</div>
    <div class="final-msg" id="finalMsg"></div>
    <a class="btn-home" href="../">🏠 홈으로</a>
    <button class="btn-retry" onclick="restartQuiz()">🔄 다시!</button>
  </div>
</div>

</div>

<!-- 결과 팝업 (혜원이 사진 포함!) -->
<div class="overlay" id="overlay">
  <div class="pop">
    <img class="pop-photo" id="popPhoto" src="" alt="" style="display:none;width:130px;height:130px;border-radius:50%;object-fit:cover;border:4px solid #74b9ff;margin-bottom:10px;box-shadow:0 4px 18px rgba(0,0,0,0.25);">
    <div class="pop-emoji" id="popEmoji">🎉</div>
    <div class="pop-title" id="popTitle">정답!</div>
    <div class="pop-points" id="popPoints">+10P</div>
    <div class="pop-explain" id="popExplain"></div>
    <button class="btn-next" onclick="nextQuestion()">다음 문제 →</button>
  </div>
</div>

<script>
// ═══════ 데이터 ═══════
const QUESTIONS = {questions_js};
const TOTAL = QUESTIONS.length;
const POINTS_PER_CORRECT = 10;

// ═══════ 혜원이 사진 (랜덤) - hyewon/correct/, hyewon/wrong/ 폴더에서 ═══════
const CORRECT_PHOTOS = [
  '../hyewon/correct/photo_01.jpg',
  '../hyewon/correct/photo_02.jpg',
  '../hyewon/correct/photo_03.jpg',
  '../hyewon/correct/photo_04.jpg',
  '../hyewon/correct/photo_05.jpg',
  '../hyewon/correct/photo_06.jpg',
  '../hyewon/correct/photo_07.jpg',
  '../hyewon/correct/photo_08.jpg'
];
const WRONG_PHOTOS = [
  '../hyewon/wrong/photo_01.jpg',
  '../hyewon/wrong/photo_02.jpg',
  '../hyewon/wrong/photo_03.jpg',
  '../hyewon/wrong/photo_04.jpg',
  '../hyewon/wrong/photo_05.jpg',
  '../hyewon/wrong/photo_06.jpg'
];
function pickRandomPhoto(type) {{
  const arr = (type === 'correct') ? CORRECT_PHOTOS : WRONG_PHOTOS;
  return arr[Math.floor(Math.random() * arr.length)];
}}

// ═══════ 상태 ═══════
let currentQ = 0;
let score = 0;
let pointsEarned = 0;
let answered = false;

// ═══════ 발음 시스템 (단어장과 동일 - 안정성↑) ═══════
let _voicesCache = [];
let _userInteracted = false;
function _loadVoices() {{
  if (!('speechSynthesis' in window)) return;
  _voicesCache = window.speechSynthesis.getVoices();
}}
if ('speechSynthesis' in window) {{
  _loadVoices();
  if (window.speechSynthesis.onvoiceschanged !== undefined) {{
    window.speechSynthesis.onvoiceschanged = _loadVoices;
  }}
}}
function _pickVoice() {{
  if (_voicesCache.length === 0) _loadVoices();
  return _voicesCache.find(v => v.lang === 'en-US' && /Google|Samantha|Karen|Daniel|Microsoft/i.test(v.name))
      || _voicesCache.find(v => v.lang === 'en-US')
      || _voicesCache.find(v => v.lang && v.lang.startsWith('en'));
}}
function _primeSpeech() {{
  if (_userInteracted) return;
  _userInteracted = true;
  if (!('speechSynthesis' in window)) return;
  try {{
    const warm = new SpeechSynthesisUtterance(' ');
    warm.volume = 0.01;
    window.speechSynthesis.speak(warm);
  }} catch(e) {{}}
}}
document.addEventListener('click', _primeSpeech, {{capture: true}});
document.addEventListener('touchstart', _primeSpeech, {{capture: true, passive: true}});

function speakSentence(sentence, btn) {{
  if (!('speechSynthesis' in window)) {{
    alert('🔊 이 브라우저는 영어 발음을 지원하지 않아요!\\n크롬이나 사파리에서 열어주세요.');
    return;
  }}
  try {{
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(sentence);
    u.lang = 'en-US';
    u.rate = 0.85;
    u.pitch = 1.0;
    u.volume = 1.0;
    if (_voicesCache.length === 0) _loadVoices();
    const v = _pickVoice();
    if (v) u.voice = v;
    if (btn) btn.classList.add('speaking');
    u.onend = function() {{ if (btn) btn.classList.remove('speaking'); }};
    u.onerror = function() {{ if (btn) btn.classList.remove('speaking'); }};
    window.speechSynthesis.speak(u);
  }} catch(e) {{
    if (btn) btn.classList.remove('speaking');
  }}
}}

function speakCurrent() {{
  const q = QUESTIONS[currentQ];
  speakSentence(q.en, document.getElementById('speakBtn'));
}}

// ═══════ 힌트 ═══════
function showHint() {{
  const q = QUESTIONS[currentQ];
  const box = document.getElementById('hintBox');
  if (q.hint && q.hint.length === 2) {{
    box.innerHTML = '💡 <b>' + q.hint[0] + '</b> = ' + q.hint[1];
  }} else {{
    box.innerHTML = '💡 (힌트 없음)';
  }}
  box.classList.add('show');
}}

// ═══════ 퀴즈 시작 ═══════
function startQuiz() {{
  document.getElementById('startScreen').classList.remove('active');
  document.getElementById('quizScreen').classList.add('active');
  currentQ = 0;
  score = 0;
  pointsEarned = 0;
  renderQuestion();
}}

// ═══════ 문제 렌더 ═══════
function renderQuestion() {{
  const q = QUESTIONS[currentQ];
  answered = false;
  // 진행 바
  document.getElementById('progBar').style.width = ((currentQ / TOTAL) * 100) + '%';
  document.getElementById('progLabel').textContent = (currentQ + 1) + ' / ' + TOTAL;
  document.getElementById('qNum').textContent = currentQ + 1;
  document.getElementById('liveScore').textContent = score;
  document.getElementById('livePts').textContent = pointsEarned;
  // 문장
  document.getElementById('qText').textContent = q.en;
  document.getElementById('hintBox').classList.remove('show');
  document.getElementById('hintBox').innerHTML = '';
  // 보기
  const choicesDiv = document.getElementById('choices');
  choicesDiv.innerHTML = '';
  q.choices.forEach(function(choice, i) {{
    const btn = document.createElement('button');
    btn.className = 'choice';
    btn.textContent = (i+1) + '. ' + choice;
    btn.onclick = function() {{ answer(i); }};
    choicesDiv.appendChild(btn);
  }});
  // 자동 발음 (사용자 터치 후부터)
  if (_userInteracted) {{
    setTimeout(function() {{ speakCurrent(); }}, 250);
  }}
}}

// ═══════ 답 선택 ═══════
function answer(idx) {{
  if (answered) return;
  answered = true;
  const q = QUESTIONS[currentQ];
  const isCorrect = (idx === q.ans);
  const buttons = document.querySelectorAll('.choice');
  buttons.forEach(function(b) {{ b.disabled = true; }});
  if (isCorrect) {{
    buttons[idx].classList.add('correct');
    score++;
    pointsEarned += POINTS_PER_CORRECT;
    addPoints(POINTS_PER_CORRECT);
  }} else {{
    buttons[idx].classList.add('wrong');
    buttons[q.ans].classList.add('correct');
  }}
  setTimeout(function() {{ showResult(isCorrect, q); }}, 700);
}}

// ═══════ 결과 팝업 (혜원이 사진 + 이모지) ═══════
function showResult(isCorrect, q) {{
  const overlay = document.getElementById('overlay');
  const photoEl = document.getElementById('popPhoto');
  const emojiEl = document.getElementById('popEmoji');

  // 🖼️ 혜원이 사진 (랜덤)
  const photoUrl = pickRandomPhoto(isCorrect ? 'correct' : 'wrong');
  photoEl.src = photoUrl;
  photoEl.style.display = 'block';
  photoEl.style.borderColor = isCorrect ? '#00b894' : '#e17055';
  // 이모지는 작게
  emojiEl.style.fontSize = '38px';
  emojiEl.textContent = isCorrect ? '🎉' : '😢';
  // 사진 로드 실패 시 이모지로 폴백
  photoEl.onerror = function() {{
    photoEl.style.display = 'none';
    emojiEl.style.fontSize = '64px';
  }};

  const title = document.getElementById('popTitle');
  title.textContent = isCorrect ? '정답!' : '아쉬워요';
  title.className = 'pop-title ' + (isCorrect ? 'ok' : 'ng');
  document.getElementById('popPoints').style.display = isCorrect ? 'inline-block' : 'none';
  document.getElementById('popPoints').textContent = '+' + POINTS_PER_CORRECT + 'P';
  document.getElementById('popExplain').innerHTML = '📖 ' + q.explain;
  overlay.classList.add('show');
}}

// ═══════ 다음 문제 ═══════
function nextQuestion() {{
  document.getElementById('overlay').classList.remove('show');
  currentQ++;
  if (currentQ >= TOTAL) {{
    finishQuiz();
  }} else {{
    renderQuestion();
  }}
}}

// ═══════ 완료 ═══════
function finishQuiz() {{
  document.getElementById('quizScreen').classList.remove('active');
  document.getElementById('finalScreen').classList.add('active');

  document.getElementById('scoreNum').textContent = score + ' / ' + TOTAL;
  document.getElementById('finalPts').textContent = pointsEarned;

  const pct = (score / TOTAL) * 100;
  let stars = 0;
  if (pct === 100) stars = 5;
  else if (pct >= 90) stars = 4;
  else if (pct >= 75) stars = 3;
  else if (pct >= 60) stars = 2;
  else if (pct >= 40) stars = 1;
  document.getElementById('finalStars').textContent = '⭐'.repeat(stars) + '☆'.repeat(5-stars);

  let emoji = '🎉', title = '잘했어요!', msg = '계속 연습하면 더 잘할 수 있어요! 💪';
  if (pct === 100) {{ emoji = '🏆'; title = '완벽해요!'; msg = '와! 모두 정답! 혜원이 영어 천재! 🌟'; }}
  else if (pct >= 90) {{ emoji = '🌟'; title = '굉장해요!'; msg = '거의 다 맞췄어요! 정말 멋져요!'; }}
  else if (pct >= 75) {{ emoji = '✨'; title = '잘했어요!'; msg = '훌륭해요! 조금만 더 연습하면 완벽!'; }}
  else if (pct >= 60) {{ emoji = '👍'; title = '좋아요!'; msg = '괜찮아요! 다시 도전하면 더 잘 될 거예요!'; }}
  else {{ emoji = '💪'; title = '괜찮아!'; msg = '오늘 배운 것 잘 기억해요! 다시 해보면 더 잘할 수 있어요!'; }}

  document.getElementById('finalEmoji').textContent = emoji;
  document.getElementById('finalTitle').textContent = title;
  document.getElementById('finalMsg').innerHTML = msg;

  // 학습 기록 저장 (스트릭/홈 화면 카운트용)
  try {{
    const history = JSON.parse(localStorage.getItem('hyewon_quiz_history') || '[]');
    history.push({{
      date: '{data['date']}',
      day: '{data['day_ko']}',
      type: '영어표현퀴즈',
      theme: '{data['theme']}',
      score: score,
      total: TOTAL,
      pointsEarned: pointsEarned,
      time: new Date().toISOString()
    }});
    localStorage.setItem('hyewon_quiz_history', JSON.stringify(history));
  }} catch(e) {{}}
}}

// ═══════ 다시 시작 ═══════
function restartQuiz() {{
  document.getElementById('finalScreen').classList.remove('active');
  startQuiz();
}}

// ═══════ 포인트 적립 (홈 화면과 자동 동기화) ═══════
function addPoints(amt) {{
  try {{
    const cur = parseInt(localStorage.getItem('hyewon_points') || '0');
    const nv = cur + amt;
    localStorage.setItem('hyewon_points', String(nv));
    // 시트에도 동기화 (있으면)
    if (typeof GAS_URL !== 'undefined' && GAS_URL) {{
      fetch(GAS_URL, {{
        method: 'POST', mode: 'no-cors',
        headers: {{'Content-Type': 'text/plain'}},
        body: JSON.stringify({{sync_state: {{points: nv}}}})
      }}).catch(function(){{}});
    }}
  }} catch(e) {{}}
}}

// 시트 동기화용 GAS_URL (홈과 동일)
const GAS_URL = "https://script.google.com/macros/s/AKfycbyg0RNvnjzeUpWBu3KDrwre_ngHxjfSINUnI-JNEULMHSPYsVChf3eEogE7crF14BdpJg/exec";
</script>
</body>
</html>'''


# ═══════════════════════════════════════════════
# 메인
# ═══════════════════════════════════════════════
def main():
    print("\n" + "=" * 60)
    print("  🇺🇸 매일 영어 표현 퀴즈 일괄 생성")
    print("=" * 60)

    success = 0
    for date_key, data in QUIZZES.items():
        try:
            html = build_quiz_html(date_key, data)
            out_path = OUT_DIR / f"영어퀴즈_{date_key}.html"
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)
            size_kb = out_path.stat().st_size / 1024
            print(f"\n✅ {data['date']} ({data['day_ko']}) - {data['theme']}")
            print(f"   ({size_kb:.1f} KB) → english_quiz/영어퀴즈_{date_key}.html")
            success += 1
        except Exception as e:
            print(f"\n❌ {date_key} 실패: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 60)
    print(f"  ✅ {success}/{len(QUIZZES)}개 완료!")
    print("=" * 60)


if __name__ == '__main__':
    main()
