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

    # ═════════════════════════════════════════════
    # 5/18 (월) - 옷과 패션
    # ═════════════════════════════════════════════
    '20260518': {
        'date': '2026-05-18',
        'day_ko': '월',
        'theme': '옷과 패션',
        'theme_emoji': '👕',
        'description': '오늘 어떤 옷 입었어? 멋쟁이 영어!',
        'questions': [
            {'en':'What are you wearing?','choices':['뭐 먹어?','뭐 입었어?','어디 가?','뭐 해?'],'ans':1,'hint':('wear','입다'),'explain':'wear = 입다'},
            {'en':"I'm wearing a T-shirt.",'choices':['티셔츠 입었어','바지 입었어','신발 신었어','모자 썼어'],'ans':0,'hint':('T-shirt','티셔츠'),'explain':'T-shirt = 티셔츠'},
            {'en':'These pants are too long.','choices':['이 바지 너무 짧아','이 바지 너무 길어','이 바지 너무 작아','이 바지 너무 비싸'],'ans':1,'hint':('pants','바지'),'explain':'pants = 바지'},
            {'en':'Mom bought me a dress.','choices':['엄마가 가방 사줬어','엄마가 신발 사줬어','엄마가 원피스 사줬어','엄마가 모자 사줬어'],'ans':2,'hint':('dress','원피스, 드레스'),'explain':'dress = 원피스'},
            {'en':'My shoes are new.','choices':['내 신발이 낡았어','내 신발이 새 거야','내 신발이 작아','내 신발 잃어버렸어'],'ans':1,'hint':('shoes','신발'),'explain':'shoes = 신발 (한 켤레)'},
            {'en':"Don't forget your hat!",'choices':['모자 잊지 마!','우산 잊지 마!','가방 잊지 마!','책 잊지 마!'],'ans':0,'hint':('hat','모자'),'explain':'hat = 모자'},
            {'en':'I love this jacket.','choices':['이 바지 좋아','이 재킷 정말 좋아','이 셔츠 좋아','이 스커트 좋아'],'ans':1,'hint':('jacket','재킷, 자켓'),'explain':'jacket = 재킷'},
            {'en':"It's cold. Wear a coat.",'choices':['더우니 반팔','추우니 코트 입어','비오니 우비','맑으니 모자'],'ans':1,'hint':('coat','코트'),'explain':'coat = 두꺼운 외투'},
            {'en':'Put on your socks.','choices':['양말 신어','양말 빨아','양말 사','양말 벗어'],'ans':0,'hint':('put on','입다, 신다'),'explain':'put on = 입다/신다'},
            {'en':'Take off your shoes.','choices':['신발 신어','신발 벗어','신발 사','신발 닦아'],'ans':1,'hint':('take off','벗다'),'explain':'take off = 벗다'},
            {'en':'My uniform is blue.','choices':['교복이 빨간색','교복이 파란색','교복이 검은색','교복이 초록색'],'ans':1,'hint':('uniform','교복, 유니폼'),'explain':'uniform = 교복'},
            {'en':'I need new gloves.','choices':['새 장갑이 필요해','새 양말이 필요해','새 모자가 필요해','새 책이 필요해'],'ans':0,'hint':('gloves','장갑'),'explain':'gloves = 장갑'},
            {'en':'Where is my scarf?','choices':['내 가방 어디 있어?','내 목도리 어디 있어?','내 신발 어디 있어?','내 책 어디 있어?'],'ans':1,'hint':('scarf','목도리'),'explain':'scarf = 목도리'},
            {'en':'You look pretty today.','choices':['너 오늘 예뻐 보여','너 오늘 슬퍼 보여','너 오늘 피곤해 보여','너 오늘 화나 보여'],'ans':0,'hint':('pretty','예쁜'),'explain':'pretty = 예쁜'},
            {'en':'That sweater is warm.','choices':['그 스웨터 차가워','그 스웨터 따뜻해','그 스웨터 비싸','그 스웨터 작아'],'ans':1,'hint':('sweater','스웨터'),'explain':'sweater = 스웨터'},
            {'en':'I want a pink ribbon.','choices':['분홍 리본 원해','파란 모자 원해','노란 가방 원해','초록 옷 원해'],'ans':0,'hint':('ribbon','리본'),'explain':'ribbon = 리본'},
            {'en':'My new bag is cute.','choices':['내 새 가방 귀여워','내 새 신발 귀여워','내 새 옷 귀여워','내 새 모자 귀여워'],'ans':0,'hint':('bag','가방'),'explain':'bag = 가방'},
            {'en':'Try this on, please.','choices':['이거 한번 입어봐','이거 한번 들어봐','이거 한번 먹어봐','이거 한번 사봐'],'ans':0,'hint':('try on','입어보다'),'explain':'try on = 옷을 입어보다'},
            {'en':'It looks great on you!','choices':['너한테 잘 어울려!','너한테 안 어울려!','너 가져가!','너 신어봐!'],'ans':0,'hint':('look great','잘 어울리다'),'explain':'look great on you = 잘 어울려'},
            {'en':"Let's go shopping for clothes.",'choices':['옷 사러 가자','음식 사러 가자','책 사러 가자','약 사러 가자'],'ans':0,'hint':('clothes','옷'),'explain':'clothes = 옷'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/19 (화) - 학교 과목
    # ═════════════════════════════════════════════
    '20260519': {
        'date': '2026-05-19',
        'day_ko': '화',
        'theme': '학교 과목',
        'theme_emoji': '📚',
        'description': '어떤 과목 좋아해? 영어로 말해봐!',
        'questions': [
            {'en':"What's your favorite subject?",'choices':['좋아하는 음식?','좋아하는 과목?','좋아하는 색?','좋아하는 친구?'],'ans':1,'hint':('subject','과목'),'explain':'subject = 과목'},
            {'en':'I love math.','choices':['수학 좋아해','과학 좋아해','국어 좋아해','체육 좋아해'],'ans':0,'hint':('math','수학'),'explain':'math = 수학'},
            {'en':'Science is fun!','choices':['과학 재미없어!','과학 재미있어!','과학 어려워!','과학 끝났어!'],'ans':1,'hint':('science','과학'),'explain':'science = 과학'},
            {'en':'Korean class is hard.','choices':['수학 시간 어려워','국어 시간 어려워','영어 시간 어려워','과학 시간 어려워'],'ans':1,'hint':('Korean','국어'),'explain':'Korean = 국어'},
            {'en':"I'm good at art.",'choices':['미술 잘해','음악 잘해','체육 잘해','수학 잘해'],'ans':0,'hint':('art','미술'),'explain':'art = 미술'},
            {'en':'Music makes me happy.','choices':['음악이 행복하게 해줘','노래 슬퍼','악기 어려워','조용히 해'],'ans':0,'hint':('music','음악'),'explain':'music = 음악'},
            {'en':'P.E. is my favorite!','choices':['체육이 가장 좋아!','수학이 가장 좋아!','미술이 가장 좋아!','과학이 가장 좋아!'],'ans':0,'hint':('P.E.','체육 (Physical Education)'),'explain':'P.E. = 체육'},
            {'en':"I don't like history.",'choices':['역사 좋아해','역사 안 좋아해','역사 잘해','역사 어려워'],'ans':1,'hint':('history','역사'),'explain':'history = 역사'},
            {'en':'English is interesting.','choices':['영어 지루해','영어 흥미로워','영어 어려워','영어 쉬워'],'ans':1,'hint':('interesting','흥미로운'),'explain':'interesting = 흥미로운'},
            {'en':'Social studies is useful.','choices':['사회는 유용해','사회는 어려워','사회는 지루해','사회는 짧아'],'ans':0,'hint':('social studies','사회'),'explain':'social studies = 사회'},
            {'en':'I have homework today.','choices':['오늘 시험 있어','오늘 숙제 있어','오늘 휴일이야','오늘 쉬어'],'ans':1,'hint':('homework','숙제'),'explain':'homework = 숙제'},
            {'en':'The test is tomorrow.','choices':['시험은 어제였어','시험은 오늘이야','시험은 내일이야','시험은 다음 주야'],'ans':2,'hint':('test','시험'),'explain':'test = 시험'},
            {'en':'I got a good grade!','choices':['시험 잘 봤어!','선물 받았어!','놀러 가!','집에 가!'],'ans':0,'hint':('grade','성적, 학년'),'explain':'good grade = 좋은 성적'},
            {'en':'Study hard, please.','choices':['열심히 놀아','열심히 공부해','열심히 자','열심히 먹어'],'ans':1,'hint':('study','공부하다'),'explain':'study = 공부하다'},
            {'en':'I forgot my book.','choices':['책 잊고 왔어','책 사줘','책 줄게','책 봐'],'ans':0,'hint':('forgot','잊다(과거)'),'explain':'forgot = 잊었다'},
            {'en':'Open the textbook.','choices':['교과서 펴','교과서 닫아','교과서 사','교과서 줘'],'ans':0,'hint':('textbook','교과서'),'explain':'textbook = 교과서'},
            {'en':'Listen carefully.','choices':['빨리 와','조심히 들어','크게 말해','조용히 해'],'ans':1,'hint':('carefully','신중히'),'explain':'listen carefully = 잘 들어'},
            {'en':'I have a question.','choices':['답 있어','질문 있어','시간 있어','책 있어'],'ans':1,'hint':('question','질문'),'explain':'question = 질문'},
            {'en':'Thank you, teacher.','choices':['죄송해요, 선생님','감사해요, 선생님','안녕, 선생님','잘 가, 선생님'],'ans':1,'hint':('teacher','선생님'),'explain':'thank you = 감사합니다'},
            {'en':'School is over.','choices':['학교 시작이야','학교 끝났어','학교 어려워','학교 재미있어'],'ans':1,'hint':('over','끝난'),'explain':'be over = 끝나다'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/20 (수) - 취미·활동
    # ═════════════════════════════════════════════
    '20260520': {
        'date': '2026-05-20',
        'day_ko': '수',
        'theme': '취미와 활동',
        'theme_emoji': '🎨',
        'description': '쉬는 시간에 뭐 해? 취미가 뭐야?',
        'questions': [
            {'en':"What's your hobby?",'choices':['이름이 뭐야?','취미가 뭐야?','나이가 뭐야?','색깔이 뭐야?'],'ans':1,'hint':('hobby','취미'),'explain':'hobby = 취미'},
            {'en':'I like painting.','choices':['그림 그리기 좋아해','노래 좋아해','책 좋아해','게임 좋아해'],'ans':0,'hint':('painting','그림 그리기'),'explain':'painting = 그림 그리기'},
            {'en':'I enjoy singing.','choices':['노래하기 즐겨','춤추기 즐겨','읽기 즐겨','쓰기 즐겨'],'ans':0,'hint':('enjoy','즐기다'),'explain':'enjoy ~ing = ~을 즐기다'},
            {'en':'Reading is my hobby.','choices':['책 읽기가 취미','음악이 취미','요리가 취미','운동이 취미'],'ans':0,'hint':('reading','독서'),'explain':'reading = 독서'},
            {'en':'I collect stickers.','choices':['스티커 모아','우표 모아','동전 모아','조개 모아'],'ans':0,'hint':('collect','모으다'),'explain':'collect = 모으다, 수집하다'},
            {'en':'I play the piano.','choices':['피아노 쳐','기타 쳐','드럼 쳐','바이올린 켜'],'ans':0,'hint':('piano','피아노'),'explain':'play the piano = 피아노 치다'},
            {'en':'My favorite movie is funny.','choices':['좋아하는 영화는 슬퍼','좋아하는 영화는 웃겨','좋아하는 영화는 무서워','좋아하는 영화는 길어'],'ans':1,'hint':('movie','영화'),'explain':'movie = 영화'},
            {'en':'I love K-pop.','choices':['트로트 좋아해','케이팝 좋아해','클래식 좋아해','재즈 좋아해'],'ans':1,'hint':('K-pop','케이팝'),'explain':'K-pop = 한국 팝 음악'},
            {'en':'I take pictures with my phone.','choices':['전화 걸어','사진 찍어','문자 해','음악 들어'],'ans':1,'hint':('take pictures','사진 찍다'),'explain':'take pictures = 사진 찍다'},
            {'en':'Drawing is fun.','choices':['그림 그리기 재미있어','노래하기 재미있어','요리하기 재미있어','운동하기 재미있어'],'ans':0,'hint':('drawing','그림 그리기'),'explain':'drawing = 그림 그리기'},
            {'en':"Let's watch a movie!",'choices':['책 보자!','영화 보자!','산책 가자!','자자!'],'ans':1,'hint':('watch','보다'),'explain':"watch a movie = 영화를 보다"},
            {'en':'I read comic books.','choices':['만화책 읽어','동화책 읽어','잡지 읽어','신문 읽어'],'ans':0,'hint':('comic','만화'),'explain':'comic = 만화'},
            {'en':'I love computer games.','choices':['컴퓨터 게임 정말 좋아','보드 게임 정말 좋아','카드 게임 정말 좋아','퍼즐 정말 좋아'],'ans':0,'hint':('computer','컴퓨터'),'explain':'computer game = 컴퓨터 게임'},
            {'en':'My puzzle is hard.','choices':['내 퍼즐 쉬워','내 퍼즐 어려워','내 퍼즐 작아','내 퍼즐 새 거야'],'ans':1,'hint':('puzzle','퍼즐'),'explain':'puzzle = 퍼즐'},
            {'en':'I write a diary every day.','choices':['매일 일기 써','매일 운동해','매일 노래해','매일 그려'],'ans':0,'hint':('diary','일기'),'explain':'diary = 일기'},
            {'en':'I like making things.','choices':['만들기 좋아해','부수기 좋아해','사기 좋아해','보기 좋아해'],'ans':0,'hint':('make','만들다'),'explain':'making things = 무언가 만들기'},
            {'en':'I want to learn guitar.','choices':['기타 배우고 싶어','피아노 배우고 싶어','바이올린 배우고 싶어','드럼 배우고 싶어'],'ans':0,'hint':('learn','배우다'),'explain':'learn = 배우다'},
            {'en':"Let's go to the park.",'choices':['공원 가자','학교 가자','집에 가자','가게 가자'],'ans':0,'hint':('park','공원'),'explain':'park = 공원'},
            {'en':'I love watching cartoons.','choices':['만화영화 보는 거 좋아','뉴스 보는 거 좋아','드라마 보는 거 좋아','영화 보는 거 좋아'],'ans':0,'hint':('cartoons','만화영화'),'explain':'cartoons = 만화영화'},
            {'en':'My free time is precious.','choices':['내 자유시간은 소중해','내 시간 없어','내 시간 길어','내 시간 모자라'],'ans':0,'hint':('precious','소중한'),'explain':'free time = 자유시간, precious = 소중한'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/21 (목) - 몸·건강
    # ═════════════════════════════════════════════
    '20260521': {
        'date': '2026-05-21',
        'day_ko': '목',
        'theme': '몸과 건강',
        'theme_emoji': '🏥',
        'description': '내 몸과 건강을 영어로!',
        'questions': [
            {'en':'My head hurts.','choices':['머리 아파','배 아파','다리 아파','이 아파'],'ans':0,'hint':('head','머리'),'explain':'head = 머리'},
            {'en':'I have a stomachache.','choices':['머리 아파','배 아파','목 아파','다리 아파'],'ans':1,'hint':('stomachache','복통'),'explain':'stomach = 배'},
            {'en':'My eyes are tired.','choices':['눈이 피곤해','입이 피곤해','코가 피곤해','귀가 피곤해'],'ans':0,'hint':('eyes','눈'),'explain':'eyes = 눈 (양쪽)'},
            {'en':'Open your mouth wide.','choices':['눈 떠','입 크게 벌려','귀 막아','손 들어'],'ans':1,'hint':('mouth','입'),'explain':'mouth = 입'},
            {'en':'My teeth are clean.','choices':['내 이 깨끗해','내 손 깨끗해','내 발 깨끗해','내 옷 깨끗해'],'ans':0,'hint':('teeth','이(복수)'),'explain':'teeth = 이(여러 개)'},
            {'en':'My arm is strong.','choices':['내 팔 약해','내 팔 강해','내 다리 강해','내 머리 강해'],'ans':1,'hint':('arm','팔'),'explain':'arm = 팔'},
            {'en':'My legs are tired.','choices':['내 다리 아파','내 다리 피곤해','내 다리 길어','내 다리 빨라'],'ans':1,'hint':('legs','다리(복수)'),'explain':'legs = 다리'},
            {'en':'Wash your hands!','choices':['손 씻어!','발 씻어!','얼굴 씻어!','머리 감아!'],'ans':0,'hint':('hands','손(복수)'),'explain':'hands = 손'},
            {'en':'Be careful with your fingers.','choices':['손가락 조심해','발가락 조심해','머리 조심해','팔 조심해'],'ans':0,'hint':('fingers','손가락'),'explain':'fingers = 손가락들'},
            {'en':'I have a runny nose.','choices':['코 막혀','콧물 나','코 아파','코 안 보여'],'ans':1,'hint':('nose','코'),'explain':'runny nose = 콧물'},
            {'en':"I'm sick today.",'choices':['오늘 신나','오늘 아파','오늘 졸려','오늘 배고파'],'ans':1,'hint':('sick','아픈'),'explain':'sick = 아픈'},
            {'en':'Take medicine, please.','choices':['약 먹어','물 마셔','자','일어나'],'ans':0,'hint':('medicine','약'),'explain':'take medicine = 약을 먹다'},
            {'en':"I'm healthy.",'choices':['건강해','아파','피곤해','배고파'],'ans':0,'hint':('healthy','건강한'),'explain':'healthy = 건강한'},
            {'en':'Drink water often.','choices':['물 자주 마셔','음식 자주 먹어','잠 자주 자','책 자주 읽어'],'ans':0,'hint':('often','자주'),'explain':'drink water = 물을 마시다'},
            {'en':'Sleep well tonight.','choices':['오늘 밤 잘 자','오늘 밤 늦게 자','오늘 밤 일찍 가','오늘 밤 노래해'],'ans':0,'hint':('sleep','자다'),'explain':'sleep well = 잘 자다'},
            {'en':'Exercise is good for you.','choices':['운동은 너에게 좋아','운동은 너에게 나빠','책은 너에게 좋아','음식은 너에게 좋아'],'ans':0,'hint':('exercise','운동'),'explain':'exercise = 운동'},
            {'en':'I see a doctor today.','choices':['오늘 의사 만나','오늘 친구 만나','오늘 학교 가','오늘 집에 있어'],'ans':0,'hint':('doctor','의사'),'explain':'see a doctor = 의사를 만나러 가다'},
            {'en':'My heart is beating fast.','choices':['심장이 천천히 뛰어','심장이 빨리 뛰어','심장이 멈췄어','심장이 안 뛰어'],'ans':1,'hint':('heart','심장'),'explain':'heart = 심장'},
            {'en':'I feel better now.','choices':['지금 더 기분 좋아','지금 더 아파','지금 슬퍼','지금 화나'],'ans':0,'hint':('feel','느끼다'),'explain':'feel better = 더 좋아지다'},
            {'en':'Get well soon!','choices':['빨리 나아!','빨리 가!','잘 가!','빨리 먹어!'],'ans':0,'hint':('get well','낫다'),'explain':'get well soon = 빨리 나아!'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/22 (금) - 여행·교통
    # ═════════════════════════════════════════════
    '20260522': {
        'date': '2026-05-22',
        'day_ko': '금',
        'theme': '여행과 교통',
        'theme_emoji': '✈️',
        'description': '신나는 여행! 어디로 갈까?',
        'questions': [
            {'en':'I want to travel.','choices':['일하고 싶어','여행하고 싶어','자고 싶어','쉬고 싶어'],'ans':1,'hint':('travel','여행하다'),'explain':'travel = 여행하다'},
            {'en':"Let's take an airplane.",'choices':['자전거 타자','비행기 타자','차 타자','배 타자'],'ans':1,'hint':('airplane','비행기'),'explain':'airplane = 비행기'},
            {'en':'I packed my suitcase.','choices':['가방 정리했어','가방 잃었어','가방 샀어','가방 찾아'],'ans':0,'hint':('suitcase','여행가방'),'explain':'suitcase = 여행가방'},
            {'en':'Where is my ticket?','choices':['내 표 어디 있어?','내 가방 어디 있어?','내 시계 어디 있어?','내 책 어디 있어?'],'ans':0,'hint':('ticket','표, 티켓'),'explain':'ticket = 표'},
            {'en':"We'll stay at a hotel.",'choices':['호텔에서 묵을 거야','집에 갈 거야','학교 갈 거야','병원 갈 거야'],'ans':0,'hint':('hotel','호텔'),'explain':'stay = 묵다'},
            {'en':'I want to visit Paris.','choices':['파리에 가고 싶어','뉴욕에 가고 싶어','도쿄에 가고 싶어','서울에 가고 싶어'],'ans':0,'hint':('Paris','파리'),'explain':'visit = 방문하다'},
            {'en':"Let's take a train.",'choices':['기차 타자','버스 타자','자전거 타자','걸어가자'],'ans':0,'hint':('train','기차'),'explain':'take a train = 기차를 타다'},
            {'en':'The bus is late.','choices':['버스 늦었어','버스 일찍 왔어','버스 떠났어','버스 안 왔어'],'ans':0,'hint':('late','늦은'),'explain':'late = 늦은'},
            {'en':'How much is the ticket?','choices':['표 얼마야?','표 어디야?','표 누구 거야?','표 뭐야?'],'ans':0,'hint':('how much','얼마'),'explain':'how much = 얼마'},
            {'en':'I love the beach.','choices':['해변 정말 좋아','산 정말 좋아','강 정말 좋아','시내 정말 좋아'],'ans':0,'hint':('beach','해변'),'explain':'beach = 해변'},
            {'en':"I'm taking a boat.",'choices':['배 타고 있어','차 타고 있어','걸어가고 있어','달리고 있어'],'ans':0,'hint':('boat','배'),'explain':'boat = 배'},
            {'en':"Don't forget your passport.",'choices':['여권 잊지 마','지갑 잊지 마','전화 잊지 마','우산 잊지 마'],'ans':0,'hint':('passport','여권'),'explain':'passport = 여권'},
            {'en':'The flight is at 9 AM.','choices':['비행기는 오전 9시','비행기는 오후 9시','기차는 오전 9시','버스는 오전 9시'],'ans':0,'hint':('flight','항공편'),'explain':'flight = 비행기 편'},
            {'en':"Let's go to the airport.",'choices':['공항 가자','지하철역 가자','터미널 가자','정거장 가자'],'ans':0,'hint':('airport','공항'),'explain':'airport = 공항'},
            {'en':"I'm tired from walking.",'choices':['걸어서 피곤해','뛰어서 피곤해','자서 피곤해','놀아서 피곤해'],'ans':0,'hint':('walking','걷기'),'explain':'walking = 걷는 것'},
            {'en':'Look at the map.','choices':['지도 봐','책 봐','시계 봐','TV 봐'],'ans':0,'hint':('map','지도'),'explain':'map = 지도'},
            {'en':"I'm lost.",'choices':['길 잃었어','길 찾았어','집에 왔어','가게 갔어'],'ans':0,'hint':('lost','잃은'),'explain':"I'm lost = 길 잃었어"},
            {'en':"It's a long trip.",'choices':['짧은 여행이야','긴 여행이야','쉬운 여행이야','지루한 여행이야'],'ans':1,'hint':('trip','여행'),'explain':'trip = 여행'},
            {'en':'Have a safe trip!','choices':['안전한 여행!','즐거운 일!','맛있는 식사!','신나는 시간!'],'ans':0,'hint':('safe','안전한'),'explain':'safe trip = 안전한 여행'},
            {'en':"Let's take a taxi.",'choices':['택시 타자','버스 타자','걷자','자전거 타자'],'ans':0,'hint':('taxi','택시'),'explain':'take a taxi = 택시 타다'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/23 (토) - 쇼핑·돈
    # ═════════════════════════════════════════════
    '20260523': {
        'date': '2026-05-23',
        'day_ko': '토',
        'theme': '쇼핑과 돈',
        'theme_emoji': '🛍️',
        'description': '얼마예요? 살래요!',
        'questions': [
            {'en':'How much is it?','choices':['뭐예요?','얼마예요?','어디예요?','왜요?'],'ans':1,'hint':('how much','얼마'),'explain':'how much = 얼마'},
            {'en':"It's 5,000 won.",'choices':['5천원이에요','5만원이에요','5달러예요','5엔이에요'],'ans':0,'hint':('won','원 (한국 돈)'),'explain':'won = 한국 돈 단위'},
            {'en':"That's expensive.",'choices':['그거 싸요','그거 비싸요','그거 작아요','그거 커요'],'ans':1,'hint':('expensive','비싼'),'explain':'expensive = 비싼'},
            {'en':"It's cheap.",'choices':['비싸요','싸요','없어요','커요'],'ans':1,'hint':('cheap','싼'),'explain':'cheap = 싼'},
            {'en':"I'll buy this.",'choices':['이거 살게요','이거 안 살래요','이거 줄게요','이거 봐요'],'ans':0,'hint':('buy','사다'),'explain':'buy = 사다'},
            {'en':'Where is the store?','choices':['가게 어디?','학교 어디?','집 어디?','병원 어디?'],'ans':0,'hint':('store','가게'),'explain':'store = 가게'},
            {'en':"Let's go shopping.",'choices':['쇼핑하러 가자','자러 가자','놀러 가자','일하러 가자'],'ans':0,'hint':('shopping','쇼핑'),'explain':'go shopping = 쇼핑하러 가다'},
            {'en':'I need money.','choices':['돈 필요해','시간 필요해','음식 필요해','책 필요해'],'ans':0,'hint':('money','돈'),'explain':'money = 돈'},
            {'en':'I have 1,000 won.','choices':['천원 있어','만원 있어','오천원 있어','없어'],'ans':0,'hint':('have','가지고 있다'),'explain':'I have ~ = ~를 가지고 있다'},
            {'en':"Can I have a discount?",'choices':['할인 돼요?','선물 돼요?','반품 돼요?','교환 돼요?'],'ans':0,'hint':('discount','할인'),'explain':'discount = 할인'},
            {'en':'Cash or card?','choices':['현금? 카드?','크게? 작게?','빨리? 천천히?','뜨겁게? 차갑게?'],'ans':0,'hint':('cash','현금'),'explain':'cash = 현금'},
            {'en':"I'll pay by card.",'choices':['카드로 낼게요','현금으로 낼게요','수표로 낼게요','나중에 낼게요'],'ans':0,'hint':('pay','지불하다'),'explain':'pay by card = 카드로 결제'},
            {'en':"It doesn't work.",'choices':['이거 작동해','이거 작동 안 해','이거 새 거야','이거 헌 거야'],'ans':1,'hint':('work','작동하다'),'explain':"doesn't work = 작동 안 해"},
            {'en':"I want to return this.",'choices':['이거 반품하고 싶어','이거 사고 싶어','이거 줄게','이거 가질게'],'ans':0,'hint':('return','반품하다'),'explain':'return = 반품하다'},
            {'en':"It's on sale!",'choices':['할인 중!','매진!','새로 나옴!','품절!'],'ans':0,'hint':('sale','세일, 할인'),'explain':'on sale = 할인 중'},
            {'en':"Where's the receipt?",'choices':['영수증 어디?','가방 어디?','지갑 어디?','거스름돈 어디?'],'ans':0,'hint':('receipt','영수증'),'explain':'receipt = 영수증'},
            {'en':"I'm just looking.",'choices':['그냥 보고 있어요','살게요','갈게요','드릴게요'],'ans':0,'hint':('looking','보고 있는'),'explain':'just looking = 그냥 둘러보는 중'},
            {'en':"Do you have a smaller size?",'choices':['더 작은 사이즈 있어요?','더 큰 사이즈 있어요?','없어요?','맘에 들어요?'],'ans':0,'hint':('smaller','더 작은'),'explain':'smaller = 더 작은'},
            {'en':"I'll think about it.",'choices':['생각해 볼게요','지금 살게요','안 살래요','선물할게요'],'ans':0,'hint':('think about','~에 대해 생각하다'),'explain':'think about it = 생각해 보다'},
            {'en':'Thank you, come again!','choices':['감사합니다, 또 오세요!','죄송합니다','고마워요','잘 가요'],'ans':0,'hint':('come again','다시 오다'),'explain':'come again = 또 오세요'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/24 (일) - 의견·생각 표현
    # ═════════════════════════════════════════════
    '20260524': {
        'date': '2026-05-24',
        'day_ko': '일',
        'theme': '의견과 생각',
        'theme_emoji': '🤔',
        'description': '내 생각 영어로 말해보기!',
        'questions': [
            {'en':'I think so.','choices':['그렇게 생각해','안 그래','몰라','이상해'],'ans':0,'hint':('think','생각하다'),'explain':"I think so = 그렇게 생각해"},
            {'en':"I don't think so.",'choices':['그렇게 생각해','그렇게 생각 안 해','맞아','몰라'],'ans':1,'hint':("don't",'아니다'),'explain':"don't think = 생각 안 한다"},
            {'en':'I agree with you.','choices':['너랑 동의해','너랑 안 같아','몰라','싫어'],'ans':0,'hint':('agree','동의하다'),'explain':'agree = 동의하다'},
            {'en':"I disagree.",'choices':['동의해','동의 안 해','몰라','잠깐'],'ans':1,'hint':('disagree','반대하다'),'explain':'disagree = 동의하지 않다'},
            {'en':"That's a good idea!",'choices':['좋은 생각!','나쁜 생각!','지루해!','이상해!'],'ans':0,'hint':('idea','생각, 아이디어'),'explain':'good idea = 좋은 생각'},
            {'en':'In my opinion, ...','choices':['내 생각엔...','네 생각엔...','우리 생각엔...','다른 사람 생각'],'ans':0,'hint':('opinion','의견'),'explain':'in my opinion = 내 의견으로는'},
            {'en':'I prefer apples.','choices':['사과 더 좋아해','사과 싫어해','사과 안 먹어','사과 사줘'],'ans':0,'hint':('prefer','더 좋아하다'),'explain':'prefer = 더 좋아하다'},
            {'en':"That's interesting.",'choices':['지루해','흥미로워','이상해','쉬워'],'ans':1,'hint':('interesting','흥미로운'),'explain':'interesting = 흥미로운'},
            {'en':'I love it!','choices':['정말 좋아!','싫어!','몰라!','지루해!'],'ans':0,'hint':('love','매우 좋아하다'),'explain':'love = 매우 좋아하다'},
            {'en':"I hate it.",'choices':['좋아해','싫어','보통이야','새로워'],'ans':1,'hint':('hate','싫어하다'),'explain':'hate = 싫어하다'},
            {'en':"That's true.",'choices':['그건 사실이야','그건 거짓이야','그건 농담이야','몰라'],'ans':0,'hint':('true','사실의'),'explain':'true = 사실'},
            {'en':"That's not true!",'choices':['그건 사실이야!','그건 사실이 아니야!','몰라!','지루해!'],'ans':1,'hint':('not true','사실이 아닌'),'explain':"not true = 사실이 아니다"},
            {'en':'Are you sure?','choices':['확실해?','지루해?','피곤해?','배고파?'],'ans':0,'hint':('sure','확실한'),'explain':'sure = 확실한'},
            {'en':'Yes, I am sure.','choices':['응, 확실해','아니, 몰라','아마도','글쎄'],'ans':0,'hint':('yes','네, 응'),'explain':'I am sure = 확실해'},
            {'en':'Maybe.','choices':['아마도','확실해','아니','몰라'],'ans':0,'hint':('maybe','아마도'),'explain':'maybe = 아마도, 어쩌면'},
            {'en':"I don't know.",'choices':['알아','몰라','잘해','못해'],'ans':1,'hint':("don't know",'모르다'),'explain':"don't know = 모르다"},
            {'en':"Let me think.",'choices':['생각해 볼게','말해줄게','갈게','쉴게'],'ans':0,'hint':('think','생각하다'),'explain':"let me ~ = ~할게"},
            {'en':'I have an idea!','choices':['아이디어 있어!','문제 있어!','시간 없어!','책 있어!'],'ans':0,'hint':('idea','아이디어'),'explain':'have an idea = 아이디어가 있다'},
            {'en':"Why not?",'choices':['왜 안 돼?','어디?','언제?','누구?'],'ans':0,'hint':('why','왜'),'explain':'why not? = 왜 안 돼? / 그래!'},
            {'en':"That makes sense.",'choices':['말이 돼','말이 안 돼','이상해','어려워'],'ans':0,'hint':('sense','뜻, 의미'),'explain':'makes sense = 말이 되다'},
        ]
    },

    # ═════════════════════════════════════════════
    # 5/25~5/31 (Week 6) - 형용사·부사 활용 표현
    # ═════════════════════════════════════════════
    '20260525': {
        'date': '2026-05-25', 'day_ko': '월', 'theme': '감정 표현', 'theme_emoji': '😊',
        'description': '오늘 기분 어때? 감정 영어로!',
        'questions': [
            {'en':'I feel happy today.','choices':['오늘 슬퍼','오늘 행복해','오늘 화나','오늘 졸려'],'ans':1,'hint':('feel','느끼다'),'explain':'feel happy = 행복해'},
            {'en':'She looks tired.','choices':['그녀는 신나 보여','그녀는 피곤해 보여','그녀는 행복해 보여','그녀는 화나 보여'],'ans':1,'hint':('tired','피곤한'),'explain':'look + 형용사 = ~해 보여'},
            {'en':'Why are you sad?','choices':['왜 슬퍼?','어디 슬퍼?','왜 기뻐?','뭐 슬퍼?'],'ans':0,'hint':('sad','슬픈'),'explain':'Why ~? = 왜?'},
            {'en':"Don't be afraid.",'choices':['두려워 마','웃지 마','자지 마','가지 마'],'ans':0,'hint':('afraid','두려운'),'explain':'afraid = 무서운, 두려운'},
            {'en':"I'm proud of you.",'choices':['네가 자랑스러워','네가 미워','네가 부러워','네가 좋아'],'ans':0,'hint':('proud','자랑스러운'),'explain':'be proud of ~ = ~가 자랑스럽다'},
            {'en':'You make me happy.','choices':['너 때문에 슬퍼','너 때문에 화나','너 덕분에 행복해','너 때문에 외로워'],'ans':2,'hint':('make','만들다'),'explain':'make ~ + 형용사 = ~를 ~하게 만들다'},
            {'en':"I'm worried.",'choices':['걱정돼','신나','졸려','배고파'],'ans':0,'hint':('worried','걱정하는'),'explain':'worried = 걱정되는'},
            {'en':"Don't worry, be happy!",'choices':['걱정 마, 행복하자!','자, 일어나!','빨리, 가자!','조용히 해'],'ans':0,'hint':('worry','걱정하다'),'explain':"Don't worry = 걱정 마"},
            {'en':"I'm so excited!",'choices':['정말 신나!','정말 졸려!','정말 화나!','정말 슬퍼!'],'ans':0,'hint':('excited','신나는'),'explain':'so excited = 정말 신나는'},
            {'en':'How do you feel?','choices':['어떻게 가?','기분 어때?','어디 가?','뭐 해?'],'ans':1,'hint':('feel','느끼다'),'explain':'How do you feel? = 기분 어때?'},
            {'en':"Stay positive!",'choices':['긍정적으로 살아!','조용히!','앉아!','일어나!'],'ans':0,'hint':('positive','긍정적인'),'explain':'positive = 긍정적인'},
            {'en':'You can do it!','choices':['넌 할 수 있어!','넌 못해!','너 어디 가?','너 누구야?'],'ans':0,'hint':('can','~할 수 있다'),'explain':'You can do it = 넌 할 수 있어!'},
            {'en':"That's amazing!",'choices':['멋져!','이상해!','싫어!','지루해!'],'ans':0,'hint':('amazing','놀라운'),'explain':'amazing = 놀라운, 멋진'},
            {'en':'I love you, Mom.','choices':['엄마 사랑해요','엄마 안녕','엄마 미안해요','엄마 고마워요'],'ans':0,'hint':('love','사랑하다'),'explain':'love = 사랑하다'},
            {'en':"I'm thankful for you.",'choices':['너에게 감사해','너에게 미안해','너 미워','너 어디?'],'ans':0,'hint':('thankful','감사하는'),'explain':'thankful for ~ = ~에게 감사한'},
            {'en':"That's wonderful.",'choices':['멋져','이상해','지루해','보통이야'],'ans':0,'hint':('wonderful','멋진'),'explain':'wonderful = 멋진, 훌륭한'},
            {'en':'I miss you.','choices':['너가 보고 싶어','너 미워','너 좋아','너 가져'],'ans':0,'hint':('miss','그리워하다'),'explain':'miss = 그리워하다'},
            {'en':'Be brave!','choices':['용감해져!','조심해!','자!','일어나!'],'ans':0,'hint':('brave','용감한'),'explain':'Be + 형용사 = ~해져라'},
            {'en':"That's funny!",'choices':['웃겨!','슬퍼!','이상해!','지루해!'],'ans':0,'hint':('funny','웃긴'),'explain':'funny = 웃긴'},
            {'en':"It's okay.",'choices':['괜찮아','싫어','몰라','보통이야'],'ans':0,'hint':('okay','괜찮은'),'explain':"It's okay = 괜찮아"},
        ]
    },
    '20260526': {
        'date': '2026-05-26', 'day_ko': '화', 'theme': '빈도 표현', 'theme_emoji': '⏰',
        'description': '얼마나 자주 해? 빈도 영어!',
        'questions': [
            {'en':'I always eat breakfast.','choices':['절대 아침 안 먹어','항상 아침 먹어','가끔 아침 먹어','아침 안 좋아해'],'ans':1,'hint':('always','항상'),'explain':'always = 항상'},
            {'en':'She never lies.','choices':['항상 거짓말','거짓말 가끔','거짓말 절대 안 함','거짓말 자주'],'ans':2,'hint':('never','절대 ~ 안'),'explain':'never = 0%'},
            {'en':'We sometimes go to the park.','choices':['항상 공원 가','가끔 공원 가','절대 공원 안 가','공원 싫어'],'ans':1,'hint':('sometimes','가끔'),'explain':'sometimes = 가끔'},
            {'en':'How often do you read?','choices':['얼마나 자주 읽어?','어떻게 읽어?','왜 읽어?','어디서 읽어?'],'ans':0,'hint':('how often','얼마나 자주'),'explain':'How often ~? = 얼마나 자주?'},
            {'en':'I usually wake up at 7.','choices':['보통 7시 일어남','한 번도 안 일어남','7시 자','7시 가'],'ans':0,'hint':('usually','보통'),'explain':'usually = 보통'},
            {'en':'I often play soccer.','choices':['축구 자주 해','축구 절대 안 해','축구 싫어','축구 가끔'],'ans':0,'hint':('often','자주'),'explain':'often = 자주'},
            {'en':'See you tomorrow!','choices':['어제 봤어!','오늘 봐!','내일 봐!','다음 주 봐!'],'ans':2,'hint':('tomorrow','내일'),'explain':'tomorrow = 내일'},
            {'en':'I went there yesterday.','choices':['어제 거기 갔어','내일 갈 거야','오늘 가','자주 가'],'ans':0,'hint':('yesterday','어제'),'explain':'yesterday = 어제'},
            {'en':"I'm busy now.",'choices':['지금 바빠','내일 바빠','어제 바빴어','자주 바빠'],'ans':0,'hint':('now','지금'),'explain':'now = 지금'},
            {'en':"I'll call you soon.",'choices':['이미 전화함','곧 전화할게','절대 전화 안 함','어제 전화'],'ans':1,'hint':('soon','곧'),'explain':'soon = 곧'},
            {'en':'Do it quickly!','choices':['빨리 해!','천천히 해!','자!','자세히 해!'],'ans':0,'hint':('quickly','빠르게'),'explain':'quickly = 빠르게'},
            {'en':'Speak slowly, please.','choices':['빨리 말해','천천히 말해','크게 말해','조용히 해'],'ans':1,'hint':('slowly','천천히'),'explain':'slowly = 천천히'},
            {'en':'It takes one hour.','choices':['1초 걸려','1분 걸려','1시간 걸려','1년 걸려'],'ans':2,'hint':('hour','시간'),'explain':'hour = 시간'},
            {'en':'Wait a minute.','choices':['1년 기다려','1분 기다려','1주 기다려','1시간 기다려'],'ans':1,'hint':('minute','분'),'explain':'minute = 분'},
            {'en':'Next week is busy.','choices':['지난주 바빴어','다음 주 바빠','내년 바빠','어제 바빴어'],'ans':1,'hint':('week','주'),'explain':'next week = 다음 주'},
            {'en':"I'm hungry every day.",'choices':['가끔 배고파','매일 배고파','한 번도 안 배고파','내일 배고파'],'ans':1,'hint':('every day','매일'),'explain':'every day = 매일'},
            {'en':"It's almost time.",'choices':['시간 다 됐어','시간 없어','시간 많아','시간 모름'],'ans':0,'hint':('almost','거의'),'explain':'almost = 거의'},
            {'en':"It's too late.",'choices':['너무 빨라','너무 늦어','너무 일러','너무 가까워'],'ans':1,'hint':('too','너무'),'explain':'too late = 너무 늦은'},
            {'en':"It's just right.",'choices':['너무 늦어','딱 맞아','틀려','싫어'],'ans':1,'hint':('just','딱, 정확히'),'explain':'just right = 딱 적당해'},
            {'en':"I'll see you later.",'choices':['지금 봐','이따 봐','어제 봤어','한 번도 안 봤어'],'ans':1,'hint':('later','나중에'),'explain':'later = 나중에'},
        ]
    },
    '20260527': {
        'date': '2026-05-27', 'day_ko': '수', 'theme': '음식·맛 표현', 'theme_emoji': '🍱',
        'description': '맛있어? 무슨 맛이야?',
        'questions': [
            {'en':'This is delicious!','choices':['이거 맛없어!','이거 맛있어!','이거 차가워!','이거 짜!'],'ans':1,'hint':('delicious','맛있는'),'explain':'delicious = 매우 맛있는'},
            {'en':'The lemon is sour.','choices':['레몬은 달아','레몬은 시어','레몬은 짜','레몬은 매워'],'ans':1,'hint':('sour','신'),'explain':'sour = 신, 시큼한'},
            {'en':"It's too spicy!",'choices':['너무 매워!','너무 달아!','너무 차가워!','너무 짜!'],'ans':0,'hint':('spicy','매운'),'explain':'spicy = 매운'},
            {'en':'I love sweet candy.','choices':['짠 사탕 싫어','단 사탕 좋아','쓴 사탕 싫어','매운 사탕 싫어'],'ans':1,'hint':('sweet','달콤한'),'explain':'sweet = 달콤한'},
            {'en':"What's for dinner?",'choices':['저녁 메뉴는?','아침은?','점심은?','간식은?'],'ans':0,'hint':('dinner','저녁'),'explain':'dinner = 저녁 식사'},
            {'en':'I want to eat noodles.','choices':['밥 먹고 싶어','면 먹고 싶어','과일 먹고 싶어','빵 먹고 싶어'],'ans':1,'hint':('noodles','국수'),'explain':'noodles = 국수, 면'},
            {'en':'Pass the salt, please.','choices':['소금 좀 줘','후추 좀 줘','물 좀 줘','빵 좀 줘'],'ans':0,'hint':('pass','건네다'),'explain':'pass the ~ = ~ 건네다'},
            {'en':'Try this dessert!','choices':['이 음료 마셔봐!','이 디저트 먹어봐!','이 약 먹어봐!','이 옷 입어봐!'],'ans':1,'hint':('try','시도하다'),'explain':'try ~ = ~ 시도/먹어보다'},
            {'en':"It's hot, be careful.",'choices':['뜨거워, 조심해','차가워, 조심해','매워, 조심해','짜, 조심해'],'ans':0,'hint':('hot','뜨거운'),'explain':'hot = 뜨거운'},
            {'en':"It's cold and yummy.",'choices':['뜨겁고 매워','차갑고 맛있어','짜고 신선해','달고 매워'],'ans':1,'hint':('yummy','맛있는'),'explain':'yummy = 맛있는'},
            {'en':'Eat your vegetables.','choices':['고기 먹어','채소 먹어','과일 먹어','빵 먹어'],'ans':1,'hint':('vegetables','채소'),'explain':'vegetables = 채소'},
            {'en':'Drink some water.','choices':['물 마셔','우유 마셔','주스 마셔','커피 마셔'],'ans':0,'hint':('water','물'),'explain':'water = 물'},
            {'en':'I love fresh fruit.','choices':['신선한 과일 좋아','냉동 과일 좋아','말린 과일 좋아','썩은 과일'],'ans':0,'hint':('fresh','신선한'),'explain':'fresh = 신선한'},
            {'en':"This soup is too salty.",'choices':['수프 너무 짜','수프 너무 달아','수프 너무 매워','수프 너무 시어'],'ans':0,'hint':('salty','짠'),'explain':'salty = 짠'},
            {'en':"I'm full, thank you.",'choices':['배고파, 고마워','배불러, 고마워','목말라, 고마워','졸려, 고마워'],'ans':1,'hint':('full','배부른'),'explain':'full = 배부른'},
            {'en':'Want some snacks?','choices':['간식 줄까?','책 줄까?','옷 줄까?','자리 줄까?'],'ans':0,'hint':('snacks','간식'),'explain':'snacks = 간식'},
            {'en':'I drink milk every day.','choices':['매일 우유 마셔','한 번도 안 마셔','가끔 마셔','싫어해'],'ans':0,'hint':('every day','매일'),'explain':'every day = 매일'},
            {'en':'My favorite food is pizza.','choices':['좋아하는 음식 피자','싫어하는 피자','피자 안 먹어','피자 만들어'],'ans':0,'hint':('favorite','가장 좋아하는'),'explain':'favorite = 가장 좋아하는'},
            {'en':"Let's order chicken!",'choices':['치킨 주문하자!','치킨 만들자!','치킨 사자!','치킨 먹지 마!'],'ans':0,'hint':('order','주문하다'),'explain':'order = 주문하다'},
            {'en':"It's the best meal!",'choices':['최악의 식사!','최고의 식사!','평범한 식사!','마지막 식사!'],'ans':1,'hint':('best','최고의'),'explain':'best = 최고의'},
        ]
    },
    '20260528': {
        'date': '2026-05-28', 'day_ko': '목', 'theme': '묘사 표현', 'theme_emoji': '🌟',
        'description': '어떻게 생겼어? 어떤 느낌?',
        'questions': [
            {'en':'The cat is so cute!','choices':['고양이 못생겼어!','고양이 정말 귀여워!','고양이 무서워!','고양이 커!'],'ans':1,'hint':('cute','귀여운'),'explain':'cute = 귀여운'},
            {'en':'The pillow is soft.','choices':['베개가 단단해','베개가 부드러워','베개가 거칠어','베개가 작아'],'ans':1,'hint':('soft','부드러운'),'explain':'soft = 부드러운'},
            {'en':'Be careful, the knife is sharp.','choices':['칼이 무뎌','칼이 작아','칼이 날카로워','칼이 무거워'],'ans':2,'hint':('sharp','날카로운'),'explain':'sharp = 날카로운'},
            {'en':'The room is bright.','choices':['방이 어두워','방이 밝아','방이 작아','방이 좁아'],'ans':1,'hint':('bright','밝은'),'explain':'bright = 밝은'},
            {'en':"It's so dark outside.",'choices':['밖이 정말 어두워','밖이 정말 밝아','밖이 정말 추워','밖이 정말 더워'],'ans':0,'hint':('dark','어두운'),'explain':'dark = 어두운'},
            {'en':'My hands are clean.','choices':['손이 더러워','손이 깨끗해','손이 작아','손이 차가워'],'ans':1,'hint':('clean','깨끗한'),'explain':'clean = 깨끗한'},
            {'en':'My shoes are dirty.','choices':['신발이 깨끗해','신발이 더러워','신발이 새 거','신발이 작아'],'ans':1,'hint':('dirty','더러운'),'explain':'dirty = 더러운'},
            {'en':'The towel is wet.','choices':['수건이 마른','수건이 젖은','수건이 큰','수건이 작은'],'ans':1,'hint':('wet','젖은'),'explain':'wet = 젖은'},
            {'en':'Use a dry cloth.','choices':['젖은 천 써','마른 천 써','새 천 써','헌 천 써'],'ans':1,'hint':('dry','마른'),'explain':'dry = 마른'},
            {'en':'My cup is empty.','choices':['컵이 가득','컵이 비어','컵이 깨짐','컵이 새 거'],'ans':1,'hint':('empty','빈'),'explain':'empty = 빈'},
            {'en':'The box is full.','choices':['상자가 비었어','상자가 가득해','상자가 작아','상자가 새 거'],'ans':1,'hint':('full','가득 찬'),'explain':'full = 가득 찬'},
            {'en':"It's amazing!",'choices':['놀라워!','지루해!','이상해!','평범해!'],'ans':0,'hint':('amazing','놀라운'),'explain':'amazing = 놀라운'},
            {'en':"It's so boring.",'choices':['신나','지루해','쉬워','어려워'],'ans':1,'hint':('boring','지루한'),'explain':'boring = 지루한'},
            {'en':"That's perfect!",'choices':['완벽해!','이상해!','지루해!','쉬워!'],'ans':0,'hint':('perfect','완벽한'),'explain':'perfect = 완벽한'},
            {'en':'The street is noisy.','choices':['거리가 조용해','거리가 시끄러워','거리가 밝아','거리가 좁아'],'ans':1,'hint':('noisy','시끄러운'),'explain':'noisy = 시끄러운'},
            {'en':'The library is quiet.','choices':['도서관 조용해','도서관 시끄러워','도서관 밝아','도서관 어두워'],'ans':0,'hint':('quiet','조용한'),'explain':'quiet = 조용한'},
            {'en':"It's a simple game.",'choices':['어려운 게임','간단한 게임','지루한 게임','새 게임'],'ans':1,'hint':('simple','간단한'),'explain':'simple = 간단한'},
            {'en':'My ring is shiny.','choices':['반지가 반짝여','반지가 더러워','반지가 작아','반지가 깨짐'],'ans':0,'hint':('shiny','반짝이는'),'explain':'shiny = 반짝이는'},
            {'en':'Her dress is fancy.','choices':['드레스가 단순해','드레스가 화려해','드레스가 더러워','드레스가 작아'],'ans':1,'hint':('fancy','화려한'),'explain':'fancy = 화려한'},
            {'en':'The sky has vivid colors.','choices':['하늘 색이 흐려','하늘 색이 선명해','하늘이 어두워','하늘이 작아'],'ans':1,'hint':('vivid','선명한'),'explain':'vivid = 선명한'},
        ]
    },
    '20260529': {
        'date': '2026-05-29', 'day_ko': '금', 'theme': '위치·방법', 'theme_emoji': '📍',
        'description': '어디? 어떻게? 위치와 방법!',
        'questions': [
            {'en':'Come here, please.','choices':['저기 가','여기 와','밖에 나가','집에 가'],'ans':1,'hint':('here','여기'),'explain':'here = 여기'},
            {'en':'Look over there!','choices':['저기 봐!','여기 봐!','뒤를 봐!','땅을 봐!'],'ans':0,'hint':('there','거기'),'explain':'there = 저기'},
            {'en':"I'll go anywhere.",'choices':['아무 데도 안 가','어디든 갈게','집에만 갈게','도서관 갈게'],'ans':1,'hint':('anywhere','어디든'),'explain':'anywhere = 어디든'},
            {'en':'I see flowers everywhere.','choices':['꽃을 한 군데서 봐','꽃이 어디에나 있어','꽃이 없어','꽃이 가끔 있어'],'ans':1,'hint':('everywhere','어디에나'),'explain':'everywhere = 어디에나'},
            {'en':'Listen carefully.','choices':['빨리 들어','조심히 들어','크게 들어','조용히 들어'],'ans':1,'hint':('carefully','신중히'),'explain':'carefully = 신중히'},
            {'en':'Walk safely.','choices':['빨리 걸어','안전하게 걸어','크게 걸어','뛰어가'],'ans':1,'hint':('safely','안전하게'),'explain':'safely = 안전하게'},
            {'en':'I can do it easily!','choices':['쉽게 할 수 있어!','어렵게 해!','못해!','천천히 해!'],'ans':0,'hint':('easily','쉽게'),'explain':'easily = 쉽게'},
            {'en':"Don't speak loudly.",'choices':['크게 말해','크게 말하지 마','자세히 말해','빨리 말해'],'ans':1,'hint':('loudly','큰 소리로'),'explain':'loudly = 큰 소리로'},
            {'en':'Walk quietly.','choices':['시끄럽게 걸어','조용히 걸어','빨리 걸어','천천히 걸어'],'ans':1,'hint':('quietly','조용히'),'explain':'quietly = 조용히'},
            {'en':'She danced happily.','choices':['그녀는 슬프게 춤췄어','그녀는 행복하게 춤췄어','그녀는 빨리 춤췄어','그녀는 안 춤췄어'],'ans':1,'hint':('happily','행복하게'),'explain':'happily = 행복하게'},
            {'en':'I really like it!','choices':['진짜 좋아!','조금 좋아!','싫어!','몰라!'],'ans':0,'hint':('really','정말'),'explain':'really = 정말로'},
            {'en':"It's very cold.",'choices':['조금 추워','매우 추워','시원해','따뜻해'],'ans':1,'hint':('very','매우'),'explain':'very = 매우'},
            {'en':"We're almost done!",'choices':['이미 끝났어!','거의 끝났어!','막 시작했어!','오래 남았어!'],'ans':1,'hint':('almost','거의'),'explain':'almost = 거의'},
            {'en':"Let's eat together.",'choices':['혼자 먹자','같이 먹자','먹지 마','만들자'],'ans':1,'hint':('together','함께'),'explain':'together = 함께'},
            {'en':'I went alone.','choices':['혼자 갔어','같이 갔어','안 갔어','한참 갔어'],'ans':0,'hint':('alone','혼자'),'explain':'alone = 혼자'},
            {'en':"It's hot outside.",'choices':['안에 더워','밖에 더워','안에 추워','밖에 추워'],'ans':1,'hint':('outside','밖에'),'explain':'outside = 밖에'},
            {'en':'Stay inside.','choices':['안에 있어','밖에 있어','가까이 와','멀리 가'],'ans':0,'hint':('inside','안에'),'explain':'inside = 안에'},
            {'en':'She sang perfectly.','choices':['그녀는 노래 잘 못해','그녀는 완벽하게 노래','그녀는 안 노래','그녀는 빠르게 노래'],'ans':1,'hint':('perfectly','완벽하게'),'explain':'perfectly = 완벽하게'},
            {'en':"It's somewhere here.",'choices':['여기 어딘가에 있어','없어','집에 있어','학교에 있어'],'ans':0,'hint':('somewhere','어딘가에'),'explain':'somewhere = 어딘가에'},
            {'en':"There's nowhere to sit.",'choices':['앉을 데 없어','앉을 데 많아','어디든 앉아','집에 앉아'],'ans':0,'hint':('nowhere','아무 곳도 없는'),'explain':'nowhere = 아무 곳도 없는'},
        ]
    },
    '20260530': {
        'date': '2026-05-30', 'day_ko': '토', 'theme': '비교 표현', 'theme_emoji': '⚖️',
        'description': '더 크고 더 작고! 비교!',
        'questions': [
            {'en':'A cat is bigger than a mouse.','choices':['고양이가 쥐보다 작다','고양이가 쥐보다 크다','고양이와 쥐는 같다','쥐가 빠르다'],'ans':1,'hint':('bigger','더 큰'),'explain':'bigger than ~ = ~보다 큰'},
            {'en':'An ant is smaller than a bee.','choices':['개미가 벌보다 크다','개미가 벌보다 작다','벌이 작다','둘이 같다'],'ans':1,'hint':('smaller','더 작은'),'explain':'smaller than ~ = ~보다 작은'},
            {'en':'My brother is taller than me.','choices':['형이 나보다 작다','형이 나보다 크다','형이 같다','내가 더 커'],'ans':1,'hint':('taller','더 키 큰'),'explain':'taller than ~ = ~보다 키 큰'},
            {'en':'A turtle is slower than a rabbit.','choices':['거북이가 빠르다','거북이가 느리다','토끼가 느리다','둘이 같다'],'ans':1,'hint':('slower','더 느린'),'explain':'slower than ~ = ~보다 느린'},
            {'en':'A cheetah is faster than a dog.','choices':['치타가 느리다','치타가 빠르다','개가 빠르다','둘이 같다'],'ans':1,'hint':('faster','더 빠른'),'explain':'faster than ~ = ~보다 빠른'},
            {'en':'This is the biggest cake!','choices':['가장 큰 케이크!','가장 작은 케이크!','평범한 케이크!','없는 케이크!'],'ans':0,'hint':('biggest','가장 큰'),'explain':'biggest = 가장 큰'},
            {'en':"He's the tallest in class.",'choices':['반에서 가장 큰 키','반에서 가장 작은 키','반에서 보통 키','키 모름'],'ans':0,'hint':('tallest','가장 키 큰'),'explain':'tallest = 가장 키 큰'},
            {'en':'My math is better than yours.','choices':['내 수학이 못해','내 수학이 더 좋아','네 수학이 좋아','똑같아'],'ans':1,'hint':('better','더 좋은'),'explain':'better than ~ = ~보다 좋은'},
            {'en':"This pizza is the best!",'choices':['최악의 피자','최고의 피자','평범한 피자','매운 피자'],'ans':1,'hint':('best','최고의'),'explain':'best = 최고의'},
            {'en':'Today is hotter than yesterday.','choices':['오늘 어제보다 더워','오늘 어제보다 추워','똑같아','어제 더 더워'],'ans':0,'hint':('hotter','더 더운'),'explain':'hotter than ~ = ~보다 더운'},
            {'en':"It's colder in the mountains.",'choices':['산에서 더 추워','산에서 더 더워','산에서 시원해','산이 따뜻해'],'ans':0,'hint':('colder','더 추운'),'explain':'colder = 더 추운'},
            {'en':'Apples are cheaper than oranges.','choices':['사과가 더 비싸','사과가 더 싸','오렌지가 싸','똑같아'],'ans':1,'hint':('cheaper','더 싼'),'explain':'cheaper than ~ = ~보다 싼'},
            {'en':"Diamonds are the most expensive.",'choices':['가장 싼 보석','가장 비싼 보석','보통 보석','없는 보석'],'ans':1,'hint':('most expensive','가장 비싼'),'explain':'most expensive = 가장 비싼'},
            {'en':'A river is longer than a stream.','choices':['강이 개울보다 짧다','강이 개울보다 길다','똑같다','없다'],'ans':1,'hint':('longer','더 긴'),'explain':'longer than ~ = ~보다 긴'},
            {'en':'My bag is lighter than yours.','choices':['내 가방 더 무거워','내 가방 더 가벼워','네 가방 가벼워','똑같아'],'ans':1,'hint':('lighter','더 가벼운'),'explain':'lighter than ~ = ~보다 가벼운'},
            {'en':"He's stronger than me.",'choices':['그가 나보다 약해','그가 나보다 강해','우리는 같아','내가 강해'],'ans':1,'hint':('stronger','더 강한'),'explain':'stronger than ~ = ~보다 강한'},
            {'en':'This is the most beautiful flower!','choices':['가장 아름다운 꽃!','가장 못생긴 꽃!','평범한 꽃!','없는 꽃!'],'ans':0,'hint':('most beautiful','가장 아름다운'),'explain':'most beautiful = 가장 아름다운'},
            {'en':'Math is harder than English.','choices':['수학이 더 쉬워','수학이 더 어려워','영어가 어려워','똑같아'],'ans':1,'hint':('harder','더 어려운'),'explain':'harder than ~ = ~보다 어려운'},
            {'en':'My room is cleaner now.','choices':['내 방 더 더러워','내 방 더 깨끗해','내 방 같아','내 방 작아'],'ans':1,'hint':('cleaner','더 깨끗한'),'explain':'cleaner = 더 깨끗한'},
            {'en':"You're the best friend.",'choices':['최악의 친구','최고의 친구','평범한 친구','없는 친구'],'ans':1,'hint':('best friend','가장 친한 친구'),'explain':'best = 최고의'},
        ]
    },
    '20260531': {
        'date': '2026-05-31', 'day_ko': '일', 'theme': '능력·가능 표현', 'theme_emoji': '💪',
        'description': '할 수 있어! 못해! 가능 표현!',
        'questions': [
            {'en':'I can swim.','choices':['수영 할 수 있어','수영 못해','수영 좋아','수영 싫어'],'ans':0,'hint':('can','~할 수 있다'),'explain':'can = ~할 수 있다'},
            {'en':"I can't sing.",'choices':['노래 잘해','노래 못해','노래 좋아','노래 싫어'],'ans':1,'hint':("can't",'~할 수 없다'),'explain':"can't = ~할 수 없다"},
            {'en':'Can you help me?','choices':['도와줄 수 있어?','왜 도와줘?','어디 도와?','뭐 도와?'],'ans':0,'hint':('help','돕다'),'explain':'Can you ~? = ~할 수 있어?'},
            {'en':'Yes, I can.','choices':['응, 할 수 있어','아니, 못해','잘 모르겠어','싫어'],'ans':0,'hint':('yes','네'),'explain':'Yes, I can = 응, 가능해'},
            {'en':'No, I cannot.','choices':['응, 가능','아니, 못해','보통','싫어'],'ans':1,'hint':('cannot','할 수 없다'),'explain':'cannot = 할 수 없다'},
            {'en':'May I come in?','choices':['들어가도 돼?','왜 들어가?','어디 가?','집에 가?'],'ans':0,'hint':('may','~해도 좋다'),'explain':'May I ~? = ~해도 돼? (정중)'},
            {'en':'Yes, you may.','choices':['응, 돼','아니, 안 돼','잘 모름','싫어'],'ans':0,'hint':('you may','너는 ~해도 좋다'),'explain':'you may = 해도 좋아'},
            {'en':'You should study hard.','choices':['공부하지 마','열심히 공부해야 해','쉬어야 해','자야 해'],'ans':1,'hint':('should','~해야 한다'),'explain':'should = ~해야 한다'},
            {'en':"You shouldn't lie.",'choices':['거짓말 해야 해','거짓말 하면 안 돼','정직 해야 해','말 하지 마'],'ans':1,'hint':("shouldn't",'~하면 안 된다'),'explain':"shouldn't = ~하면 안 된다"},
            {'en':'I might come.','choices':['반드시 가','아마 가','절대 안 가','어제 갔어'],'ans':1,'hint':('might','아마 ~할 것이다'),'explain':'might = 아마 ~할지도'},
            {'en':'I have to go now.','choices':['지금 가야 해','지금 가지 마','지금 자','지금 와'],'ans':0,'hint':('have to','~해야 한다'),'explain':'have to = ~해야 한다'},
            {'en':"You don't have to come.",'choices':['꼭 와야 해','안 와도 돼','와','나가'],'ans':1,'hint':("don't have to",'~ 안 해도 된다'),'explain':"don't have to = 안 해도 된다"},
            {'en':"I'm able to ride a bike.",'choices':['자전거 못 타','자전거 탈 수 있어','자전거 좋아해','자전거 사'],'ans':1,'hint':('able to','~할 수 있다'),'explain':'be able to = ~할 수 있다'},
            {'en':'I want to learn.','choices':['배우기 싫어','배우고 싶어','이미 배웠어','가르치고 싶어'],'ans':1,'hint':('want to','~하고 싶다'),'explain':'want to ~ = ~하고 싶다'},
            {'en':"I'd like to try.",'choices':['해보고 싶어','하기 싫어','해봤어','잘해'],'ans':0,'hint':("'d like to",'~하고 싶다 (정중)'),'explain':"I'd like to = ~하고 싶다"},
            {'en':'Can you do it?','choices':['그거 할 수 있어?','그거 좋아?','그거 어디?','그거 누구?'],'ans':0,'hint':('do','하다'),'explain':'Can you do ~? = ~할 수 있어?'},
            {'en':"I'll try my best.",'choices':['최선을 다할게','포기할게','도와줘','잘 가'],'ans':0,'hint':('try','시도하다'),'explain':'try my best = 최선을 다하다'},
            {'en':'You can do anything!','choices':['아무것도 못해!','뭐든 할 수 있어!','가만히 있어!','잠 자!'],'ans':1,'hint':('anything','뭐든'),'explain':'can do anything = 뭐든 할 수 있다'},
            {'en':"Don't give up!",'choices':['포기하지 마!','포기해!','자!','쉬어!'],'ans':0,'hint':('give up','포기하다'),'explain':"Don't give up! = 포기하지 마!"},
            {'en':'Believe in yourself.','choices':['남을 믿어','자신을 믿어','책을 믿어','부모를 믿어'],'ans':1,'hint':('believe','믿다'),'explain':'believe in yourself = 자신을 믿어'},
        ]
    },

    # ═════════════════════════════════════════════
    # 6/1~6/7 - 일상 회화 (쉬운 표현 위주)
    # ═════════════════════════════════════════════
    '20260601': {
        'date': '2026-06-01', 'day_ko': '월', 'theme': '집에서 하는 말', 'theme_emoji': '🏠',
        'description': '집에서 자주 쓰는 영어!',
        'questions': [
            {'en':'I am at home.','choices':['집에 있어','학교에 있어','밖에 있어','없어'],'ans':0,'hint':('home','집'),'explain':'at home = 집에'},
            {'en':'Open the window.','choices':['창문 열어','문 열어','책 열어','가방 열어'],'ans':0,'hint':('open','열다'),'explain':'open = 열다'},
            {'en':'Close the door.','choices':['창문 닫아','문 닫아','책 닫아','가방 닫아'],'ans':1,'hint':('close','닫다'),'explain':'close = 닫다'},
            {'en':'Turn on the TV.','choices':['TV 꺼','TV 켜','TV 봐','TV 사'],'ans':1,'hint':('turn on','켜다'),'explain':'turn on = 켜다'},
            {'en':'Turn off the light.','choices':['불 켜','불 꺼','불 봐','불 사'],'ans':1,'hint':('turn off','끄다'),'explain':'turn off = 끄다'},
            {'en':'Wash the dishes.','choices':['설거지해','요리해','자','놀아'],'ans':0,'hint':('dishes','그릇'),'explain':'wash dishes = 설거지'},
            {'en':'Make your bed.','choices':['침대 만들어','이불 정리해','침대 사','침대 봐'],'ans':1,'hint':('make bed','침대 정리'),'explain':'make bed = 침대 정리'},
            {'en':'Brush your teeth.','choices':['이 닦아','머리 빗어','손 씻어','얼굴 닦아'],'ans':0,'hint':('brush teeth','이 닦다'),'explain':'brush teeth = 이 닦기'},
            {'en':'Take a shower.','choices':['샤워해','자','목욕탕 가','수영해'],'ans':0,'hint':('shower','샤워'),'explain':'take a shower = 샤워하다'},
            {'en':'Eat dinner.','choices':['아침 먹어','점심 먹어','저녁 먹어','간식 먹어'],'ans':2,'hint':('dinner','저녁'),'explain':'dinner = 저녁'},
            {'en':"Let's clean the room.",'choices':['방 청소하자','방에 가자','방 봐','방 만들자'],'ans':0,'hint':('clean','청소'),'explain':'clean = 청소하다'},
            {'en':'Where is my book?','choices':['내 책 어디?','내 가방 어디?','내 옷 어디?','내 친구 어디?'],'ans':0,'hint':('where','어디'),'explain':'Where is ~? = 어디?'},
            {'en':'I am hungry.','choices':['졸려요','배고파요','목말라요','피곤해요'],'ans':1,'hint':('hungry','배고픈'),'explain':'hungry = 배고픈'},
            {'en':'I want to sleep.','choices':['먹고 싶어','자고 싶어','놀고 싶어','가고 싶어'],'ans':1,'hint':('sleep','자다'),'explain':'want to ~ = ~하고 싶다'},
            {'en':'Can you help me?','choices':['도와줄래?','갈래?','자?','와?'],'ans':0,'hint':('help','돕다'),'explain':'Can you help? = 도와줄래?'},
            {'en':"It's hot today.",'choices':['오늘 추워','오늘 더워','오늘 비','오늘 눈'],'ans':1,'hint':('hot','더운'),'explain':'hot = 더운'},
            {'en':"It's cold inside.",'choices':['안에 춥다','밖에 춥다','안에 따뜻','밖에 따뜻'],'ans':0,'hint':('inside','안에'),'explain':'inside = 안에'},
            {'en':"Let's watch TV.",'choices':['TV 보자','책 보자','자자','놀자'],'ans':0,'hint':('watch','보다'),'explain':"Let's ~ = ~하자"},
            {'en':'Where is my phone?','choices':['내 전화 어디?','내 책 어디?','내 가방 어디?','내 친구 어디?'],'ans':0,'hint':('phone','전화'),'explain':'phone = 전화기'},
            {'en':'Time to sleep!','choices':['먹을 시간!','잘 시간!','놀 시간!','갈 시간!'],'ans':1,'hint':('time to','~할 시간'),'explain':'time to sleep = 잘 시간'},
        ]
    },
    '20260602': {
        'date': '2026-06-02', 'day_ko': '화', 'theme': '동물·반려동물', 'theme_emoji': '🐶',
        'description': '동물 친구들 영어로!',
        'questions': [
            {'en':'I have a puppy.','choices':['강아지 있어','고양이 있어','새 있어','없어'],'ans':0,'hint':('puppy','강아지'),'explain':'puppy = 강아지'},
            {'en':'My cat is cute.','choices':['고양이 못생겨','고양이 귀여워','고양이 커','고양이 작아'],'ans':1,'hint':('cute','귀여운'),'explain':'cute = 귀여운'},
            {'en':'The dog barks.','choices':['개가 짖어','개가 자','개가 먹어','개가 가'],'ans':0,'hint':('bark','짖다'),'explain':'bark = 짖다'},
            {'en':'Pet the rabbit.','choices':['토끼 쓰다듬어','토끼 봐','토끼 사','토끼 줘'],'ans':0,'hint':('pet','쓰다듬다'),'explain':'pet = 쓰다듬다'},
            {'en':'Feed the fish.','choices':['물고기 잡아','물고기 먹이 줘','물고기 사','물고기 봐'],'ans':1,'hint':('feed','먹이 주다'),'explain':'feed = 먹이 주다'},
            {'en':'My dog wags its tail.','choices':['개가 꼬리 흔들어','개가 짖어','개가 자','개가 뛰어'],'ans':0,'hint':('wag tail','꼬리 흔들다'),'explain':'wag tail = 꼬리 흔들기'},
            {'en':'The bunny is fluffy.','choices':['토끼 단단해','토끼 푹신해','토끼 차가워','토끼 빨라'],'ans':1,'hint':('fluffy','푹신'),'explain':'fluffy = 푹신한'},
            {'en':'I love animals.','choices':['동물 사랑해','동물 싫어','동물 무서워','동물 작아'],'ans':0,'hint':('love','사랑'),'explain':'love = 사랑하다'},
            {'en':"Let's go to the zoo.",'choices':['동물원 가자','집에 가자','학교 가자','병원 가자'],'ans':0,'hint':('zoo','동물원'),'explain':'zoo = 동물원'},
            {'en':'Birds can fly.','choices':['새는 헤엄','새는 달려','새는 날 수 있어','새는 자'],'ans':2,'hint':('fly','날다'),'explain':'fly = 날다'},
            {'en':'Walk the dog.','choices':['강아지 산책','강아지 먹이','강아지 자','강아지 잡아'],'ans':0,'hint':('walk','산책'),'explain':'walk the dog = 강아지 산책'},
            {'en':"Don't be afraid.",'choices':['무서워해','무서워 마','자','일어나'],'ans':1,'hint':('afraid','무서운'),'explain':"Don't ~ = ~하지 마"},
            {'en':'The cat is sleeping.','choices':['고양이 자고 있어','고양이 먹고 있어','고양이 놀고 있어','고양이 가'],'ans':0,'hint':('sleeping','자고 있는'),'explain':'sleeping = 자고 있는'},
            {'en':'Animals are friends.','choices':['동물은 적','동물은 친구','동물은 음식','동물은 무서워'],'ans':1,'hint':('friend','친구'),'explain':'animals = 동물들'},
            {'en':'My pet is small.','choices':['반려동물 커','반려동물 작아','반려동물 빨라','반려동물 느려'],'ans':1,'hint':('small','작은'),'explain':'small = 작은'},
            {'en':'I take care of my dog.','choices':['강아지 돌봐','강아지 사','강아지 봐','강아지 자'],'ans':0,'hint':('take care','돌보다'),'explain':'take care = 돌보다'},
            {'en':'Cats love fish.','choices':['고양이는 새 좋아','고양이는 물고기 좋아','고양이는 자','고양이는 빨라'],'ans':1,'hint':('love','좋아하다'),'explain':'love = 매우 좋아하다'},
            {'en':'Pets need love.','choices':['반려동물은 사랑 필요','반려동물은 음식 필요','반려동물은 자','반려동물은 가'],'ans':0,'hint':('need','필요'),'explain':'need = 필요하다'},
            {'en':"Don't pull the tail.",'choices':['꼬리 잡아','꼬리 놔','꼬리 당기지 마','꼬리 봐'],'ans':2,'hint':('pull','당기다'),'explain':"Don't pull = 당기지 마"},
            {'en':'Be gentle with pets.',
             'choices':['반려동물에게 친절해','반려동물 무시해','반려동물 화내','반려동물 자게 해'],'ans':0,'hint':('gentle','부드러운'),'explain':'gentle = 부드럽게'},
        ]
    },
    '20260603': {
        'date': '2026-06-03', 'day_ko': '수', 'theme': '과일·채소·맛', 'theme_emoji': '🍓',
        'description': '맛있는 과일과 채소!',
        'questions': [
            {'en':'I love grapes.','choices':['포도 정말 좋아','사과 정말 좋아','수박 정말 좋아','배 정말 좋아'],'ans':0,'hint':('grape','포도'),'explain':'grape = 포도'},
            {'en':'Watermelon is cold.','choices':['수박은 따뜻','수박은 차가워','수박은 매워','수박은 짜'],'ans':1,'hint':('cold','차가운'),'explain':'cold = 차가운'},
            {'en':'Eat your vegetables.','choices':['고기 먹어','채소 먹어','과일 먹어','사탕 먹어'],'ans':1,'hint':('vegetables','채소'),'explain':'vegetables = 채소'},
            {'en':'I want some strawberries.','choices':['딸기 좀 줘','사과 좀 줘','수박 좀 줘','배 좀 줘'],'ans':0,'hint':('strawberry','딸기'),'explain':'strawberries = 딸기들'},
            {'en':'Lemons are sour.','choices':['레몬은 달아','레몬은 셔','레몬은 짜','레몬은 매워'],'ans':1,'hint':('sour','신'),'explain':'sour = 신'},
            {'en':'Carrots are good for eyes.','choices':['당근은 눈에 좋아','당근은 머리에 좋아','당근은 발에 좋아','당근은 손에 좋아'],'ans':0,'hint':('eyes','눈'),'explain':'good for eyes = 눈에 좋은'},
            {'en':'Onions make me cry.','choices':['양파 자르면 졸려','양파 자르면 눈물','양파 자르면 화나','양파 자르면 행복'],'ans':1,'hint':('cry','울다'),'explain':'make me cry = 울게 한다'},
            {'en':'I drink fresh juice.','choices':['신선한 주스 마셔','오래된 주스 마셔','뜨거운 주스 마셔','매운 주스 마셔'],'ans':0,'hint':('fresh','신선한'),'explain':'fresh = 신선한'},
            {'en':"Don't waste food.",'choices':['음식 낭비 마','음식 더 먹어','음식 사','음식 봐'],'ans':0,'hint':('waste','낭비'),'explain':"Don't waste = 낭비 마"},
            {'en':"Let's make a salad.",'choices':['샐러드 만들자','음식 사자','요리 보자','파스타 만들자'],'ans':0,'hint':('salad','샐러드'),'explain':"Let's make ~ = ~ 만들자"},
            {'en':'Apples are healthy.','choices':['사과 건강해','사과 비싸','사과 작아','사과 빨라'],'ans':0,'hint':('healthy','건강한'),'explain':'healthy = 건강한'},
            {'en':'Wash the fruit.','choices':['과일 사','과일 씻어','과일 자','과일 봐'],'ans':1,'hint':('wash','씻다'),'explain':'wash = 씻다'},
            {'en':'I like sweet fruit.','choices':['단 과일 좋아','신 과일 좋아','쓴 과일 좋아','매운 과일 좋아'],'ans':0,'hint':('sweet','단'),'explain':'sweet = 달콤한'},
            {'en':'Tomato is red.','choices':['토마토는 노랑','토마토는 빨강','토마토는 초록','토마토는 검정'],'ans':1,'hint':('red','빨강'),'explain':'red = 빨간'},
            {'en':"Vegetables make you strong.",'choices':['채소는 약하게','채소는 튼튼하게','채소는 작게','채소는 빠르게'],'ans':1,'hint':('strong','강한'),'explain':'strong = 강한'},
            {'en':'Cucumber is cool.','choices':['오이는 더워','오이는 시원해','오이는 매워','오이는 짜'],'ans':1,'hint':('cool','시원'),'explain':'cool = 시원한'},
            {'en':'I cook with garlic.','choices':['마늘로 요리해','마늘 사','마늘 봐','마늘 줘'],'ans':0,'hint':('cook','요리'),'explain':'cook = 요리하다'},
            {'en':'Pineapple is yellow.','choices':['파인애플 노랑','파인애플 빨강','파인애플 초록','파인애플 검정'],'ans':0,'hint':('yellow','노랑'),'explain':'yellow = 노란'},
            {'en':'Mango tastes sweet.','choices':['망고 맛 셔','망고 맛 달아','망고 맛 짜','망고 맛 매워'],'ans':1,'hint':('taste','맛'),'explain':'tastes ~ = ~ 맛'},
            {'en':'I drink a smoothie.','choices':['스무디 마셔','커피 마셔','우유 마셔','물 마셔'],'ans':0,'hint':('smoothie','스무디'),'explain':'smoothie = 과일 갈은 음료'},
        ]
    },
    '20260604': {
        'date': '2026-06-04', 'day_ko': '목', 'theme': '동네에서', 'theme_emoji': '🏪',
        'description': '동네에서 만나는 장소!',
        'questions': [
            {'en':"Let's go to the mart.",'choices':['마트 가자','학교 가자','집 가자','병원 가자'],'ans':0,'hint':('mart','마트'),'explain':'mart = 마트'},
            {'en':"I'm going to the hospital.",'choices':['병원 가요','학교 가요','집 가요','시장 가요'],'ans':0,'hint':('hospital','병원'),'explain':'hospital = 병원'},
            {'en':'Buy bread at the bakery.','choices':['빵집서 빵 사','마트서 빵 사','집서 빵 사','시장서 빵 사'],'ans':0,'hint':('bakery','빵집'),'explain':'bakery = 빵집'},
            {'en':"Send a letter at the post office.",'choices':['편지 우체국서 보내','편지 학교서 보내','편지 집서 보내','편지 사'],'ans':0,'hint':('post office','우체국'),'explain':'post office = 우체국'},
            {'en':'Mom is at the bank.','choices':['엄마 은행에','엄마 학교에','엄마 집에','엄마 마트에'],'ans':0,'hint':('bank','은행'),'explain':'bank = 은행'},
            {'en':'I love the museum.','choices':['박물관 좋아','동물원 좋아','놀이공원 좋아','학교 좋아'],'ans':0,'hint':('museum','박물관'),'explain':'museum = 박물관'},
            {'en':"Let's go to the zoo!",'choices':['동물원 가자!','박물관 가자!','학교 가자!','집 가자!'],'ans':0,'hint':('zoo','동물원'),'explain':'zoo = 동물원'},
            {'en':'Watch a movie at the theater.','choices':['영화관서 영화','집서 영화','학교서 영화','마트서 영화'],'ans':0,'hint':('theater','영화관'),'explain':'theater = 영화관'},
            {'en':'Mom likes the café.','choices':['엄마는 카페 좋아','엄마는 빵집 좋아','엄마는 마트 좋아','엄마는 집 좋아'],'ans':0,'hint':('café','카페'),'explain':'café = 카페'},
            {'en':"Let's play at the park.",'choices':['공원서 놀자','집서 놀자','학교서 놀자','마트서 놀자'],'ans':0,'hint':('park','공원'),'explain':'park = 공원'},
            {'en':'Go shopping at the mall.','choices':['쇼핑몰서 쇼핑','마트서 쇼핑','시장서 쇼핑','집서 쇼핑'],'ans':0,'hint':('mall','쇼핑몰'),'explain':'mall = 쇼핑몰'},
            {'en':'Cross the street.','choices':['길 건너','길 만들어','길 봐','길 사'],'ans':0,'hint':('cross','건너다'),'explain':'cross = 건너다'},
            {'en':'My town is small.','choices':['우리 마을 커','우리 마을 작아','우리 마을 빨라','우리 마을 비싸'],'ans':1,'hint':('town','마을'),'explain':'town = 마을'},
            {'en':'Seoul is a big city.','choices':['서울은 작은 마을','서울은 큰 도시','서울은 시골','서울은 동물원'],'ans':1,'hint':('city','도시'),'explain':'city = 도시'},
            {'en':'Grandma lives in the country.','choices':['할머니 도시에','할머니 시골에','할머니 학교에','할머니 마트에'],'ans':1,'hint':('country','시골'),'explain':'country = 시골'},
            {'en':"What's your address?",'choices':['주소 뭐?','이름 뭐?','나이 뭐?','색깔 뭐?'],'ans':0,'hint':('address','주소'),'explain':'address = 주소'},
            {'en':'Cars drive on the road.','choices':['차는 길로 달려','차는 자','차는 날아','차는 헤엄쳐'],'ans':0,'hint':('road','길'),'explain':'road = 길'},
            {'en':"Let's meet downtown.",'choices':['시내서 만나자','집서 만나자','학교서 만나자','마트서 만나자'],'ans':0,'hint':('downtown','시내'),'explain':'downtown = 시내'},
            {'en':'The market is busy.','choices':['시장 한가해','시장 바빠','시장 비어','시장 작아'],'ans':1,'hint':('busy','바쁜'),'explain':'busy = 바쁜'},
            {'en':'I live in Seoul.','choices':['서울에 살아','서울에서 와','서울에 가','서울 봐'],'ans':0,'hint':('live','살다'),'explain':'live in ~ = ~에 살다'},
        ]
    },
    '20260605': {
        'date': '2026-06-05', 'day_ko': '금', 'theme': '인사·예의 표현', 'theme_emoji': '🤝',
        'description': '예의 바른 영어 표현!',
        'questions': [
            {'en':'Hi, friend!','choices':['친구야 안녕!','잘 가!','미안!','고마워!'],'ans':0,'hint':('hi','안녕'),'explain':'Hi = 안녕'},
            {'en':'Good morning!','choices':['좋은 아침!','좋은 저녁!','좋은 밤!','잘 가!'],'ans':0,'hint':('morning','아침'),'explain':'Good morning = 좋은 아침'},
            {'en':'Bye bye!','choices':['안녕!(만남)','잘 가!','고마워!','미안!'],'ans':1,'hint':('bye','잘 가'),'explain':'Bye = 잘 가'},
            {'en':'Please help me.','choices':['도와주세요','도와주지마','자','가'],'ans':0,'hint':('please','부디'),'explain':'please = 정중한 부탁'},
            {'en':'Thanks a lot!','choices':['정말 고마워!','정말 미안!','정말 싫어!','정말 모름!'],'ans':0,'hint':('thanks','고마워'),'explain':'Thanks = 고마워'},
            {'en':"I'm sorry.",'choices':['고마워','미안해','잘 가','반가워'],'ans':1,'hint':('sorry','미안'),'explain':'sorry = 미안'},
            {'en':"You're welcome.",'choices':['천만에','싫어','잘 가','미안'],'ans':0,'hint':('welcome','환영'),'explain':"You're welcome = 천만에"},
            {'en':'Excuse me.','choices':['실례합니다','잘 가요','고마워요','반가워요'],'ans':0,'hint':('excuse','실례'),'explain':'Excuse me = 실례합니다'},
            {'en':'Nice to meet you.','choices':['만나서 반가워','잘 가','고마워','미안'],'ans':0,'hint':('nice','좋은'),'explain':'Nice to meet = 만나서 반가워'},
            {'en':'OK!','choices':['알았어!','싫어!','몰라!','왜?'],'ans':0,'hint':('ok','알았어'),'explain':'OK = 알았어/좋아'},
            {'en':'Yes, I can.','choices':['응, 할 수 있어','아니, 못해','잘 가','고마워'],'ans':0,'hint':('yes','네'),'explain':'Yes = 네'},
            {'en':'No, thank you.','choices':['응 좋아','괜찮아요 (사양)','싫어','몰라'],'ans':1,'hint':('no thanks','정중한 사양'),'explain':'정중한 거절!'},
            {'en':'Wait for me!','choices':['기다려!','가!','자!','와!'],'ans':0,'hint':('wait','기다리다'),'explain':'wait = 기다리다'},
            {'en':'Stop right there.','choices':['그만 가','거기 멈춰','거기 와','거기 자'],'ans':1,'hint':('stop','멈춰'),'explain':'Stop = 멈춰'},
            {'en':"Let's go!",'choices':['가자!','자!','와!','보자!'],'ans':0,'hint':("let's go",'가자'),'explain':"Let's go = 가자"},
            {'en':'Come here!','choices':['저기 가!','여기 와!','잘 가!','자!'],'ans':1,'hint':('come','오다'),'explain':'come here = 여기 와'},
            {'en':'I love you.','choices':['사랑해','미안해','고마워','잘 가'],'ans':0,'hint':('love','사랑'),'explain':'love = 사랑'},
            {'en':'Have a nice day!','choices':['좋은 하루!','좋은 밤!','잘 가!','미안!'],'ans':0,'hint':('nice day','좋은 하루'),'explain':'좋은 하루 인사'},
            {'en':'See you later!','choices':['이따 봐!','잘 가!','만나서 반가워!','고마워!'],'ans':0,'hint':('later','나중에'),'explain':'See you later = 이따 봐'},
            {'en':'Take care!','choices':['조심해!','자!','가!','일어나!'],'ans':0,'hint':('take care','조심'),'explain':'Take care = 잘 지내!'},
        ]
    },
    '20260606': {
        'date': '2026-06-06', 'day_ko': '토', 'theme': '주말 활동', 'theme_emoji': '🎉',
        'description': '주말에 하는 활동들!',
        'questions': [
            {'en':"Let's relax today.",'choices':['오늘 쉬자','오늘 바빠','오늘 일해','오늘 공부'],'ans':0,'hint':('relax','쉬다'),'explain':'relax = 쉬다'},
            {'en':"It's the weekend!",'choices':['평일이야','주말이야','월요일이야','화요일이야'],'ans':1,'hint':('weekend','주말'),'explain':'weekend = 주말'},
            {'en':'I sleep late on Saturday.','choices':['토요일 일찍','토요일 늦게 자','토요일 안 자','토요일 학교'],'ans':1,'hint':('late','늦게'),'explain':'sleep late = 늦게 자다'},
            {'en':"Let's have fun!",'choices':['자자!','신나게 놀자!','일하자!','공부하자!'],'ans':1,'hint':('fun','재미'),'explain':"Let's have fun = 신나게 놀자"},
            {'en':"Let's go shopping.",'choices':['쇼핑 가자','자러 가자','학교 가자','병원 가자'],'ans':0,'hint':('shopping','쇼핑'),'explain':'shopping = 쇼핑'},
            {'en':'Watch a movie tonight.','choices':['오늘 밤 영화','오늘 아침 영화','오늘 점심 영화','내일 영화'],'ans':0,'hint':('tonight','오늘 밤'),'explain':'tonight = 오늘 밤'},
            {'en':"I'm going to the park.",'choices':['공원 가요','집 가요','학교 가요','병원 가요'],'ans':0,'hint':('park','공원'),'explain':'park = 공원'},
            {'en':'Family time is special.','choices':['가족 시간 특별','가족 시간 보통','가족 시간 짧아','가족 시간 없어'],'ans':0,'hint':('special','특별'),'explain':'special = 특별한'},
            {'en':"Let's make pizza.",'choices':['피자 만들자','피자 사자','피자 봐','피자 먹지마'],'ans':0,'hint':('make','만들다'),'explain':"Let's make ~ = ~ 만들자"},
            {'en':'Read a fun book.','choices':['책 읽어','책 사','책 봐','책 줘'],'ans':0,'hint':('read','읽다'),'explain':'read = 읽다'},
            {'en':"It's a beautiful day.",'choices':['좋은 날','지루한 날','피곤한 날','슬픈 날'],'ans':0,'hint':('beautiful','아름다운'),'explain':'beautiful = 아름다운'},
            {'en':'I want to play outside.','choices':['밖에서 놀고 싶어','안에서 자고 싶어','집서 일해','학교 가'],'ans':0,'hint':('outside','밖'),'explain':'outside = 밖'},
            {'en':"Don't forget your hat.",'choices':['모자 잊지 마','우산 잊지 마','책 잊지 마','가방 잊지 마'],'ans':0,'hint':('forget','잊다'),'explain':"Don't forget = 잊지 마"},
            {'en':'I love the sunshine.','choices':['햇빛 좋아','비 좋아','눈 좋아','구름 좋아'],'ans':0,'hint':('sunshine','햇빛'),'explain':'sunshine = 햇빛'},
            {'en':"Let's eat ice cream.",'choices':['아이스크림 먹자','자자','일하자','공부하자'],'ans':0,'hint':('ice cream','아이스크림'),'explain':"Let's eat = 먹자"},
            {'en':"It's so much fun!",'choices':['너무 재밌어!','너무 졸려!','너무 화나!','너무 슬퍼!'],'ans':0,'hint':('fun','재미'),'explain':'so much fun = 정말 재밌는'},
            {'en':'I love weekends!','choices':['주말 정말 좋아!','평일 정말 좋아!','월요일 좋아!','시험 좋아!'],'ans':0,'hint':('love','사랑'),'explain':'love weekends = 주말 사랑'},
            {'en':"Let's invite friends.",'choices':['친구 초대하자','친구 보자','친구 가','자'],'ans':0,'hint':('invite','초대'),'explain':'invite = 초대하다'},
            {'en':'Have a great day!','choices':['멋진 하루!','지루한 하루!','짧은 하루!','피곤한 하루!'],'ans':0,'hint':('great','멋진'),'explain':'great = 멋진'},
            {'en':"Let's celebrate!",'choices':['축하하자!','자자!','가자!','쉬자!'],'ans':0,'hint':('celebrate','축하'),'explain':'celebrate = 축하하다'},
        ]
    },
    '20260607': {
        'date': '2026-06-07', 'day_ko': '일', 'theme': '오늘 한 일', 'theme_emoji': '📅',
        'description': '오늘 뭐 했는지 영어로!',
        'questions': [
            {'en':'I went to school today.','choices':['오늘 학교 갔어','오늘 안 갔어','오늘 잤어','오늘 놀았어'],'ans':0,'hint':('went','갔다(과거)'),'explain':'went = go의 과거'},
            {'en':'I ate lunch.','choices':['점심 먹었어','아침 먹었어','저녁 먹었어','간식 먹었어'],'ans':0,'hint':('ate','먹었다'),'explain':'ate = eat의 과거'},
            {'en':'I saw my friend.','choices':['친구 봤어','친구 못 봤어','친구 만들었어','친구 가르쳤어'],'ans':0,'hint':('saw','봤다'),'explain':'saw = see의 과거'},
            {'en':'I played soccer.','choices':['축구 했어','농구 했어','야구 했어','테니스 했어'],'ans':0,'hint':('played','놀았다'),'explain':'played = play의 과거'},
            {'en':'I read a book.','choices':['책 읽었어','책 샀어','책 줬어','책 봤어'],'ans':0,'hint':('read','읽었다'),'explain':'read는 과거형도 read!'},
            {'en':'I drew a picture.','choices':['그림 그렸어','그림 봤어','그림 사','그림 줬어'],'ans':0,'hint':('drew','그렸다'),'explain':'drew = draw의 과거'},
            {'en':'I helped my mom.','choices':['엄마 도와줬어','엄마 만났어','엄마 봤어','엄마 가르쳤어'],'ans':0,'hint':('helped','도왔다'),'explain':'helped = help의 과거'},
            {'en':"It was fun.",'choices':['재밌었어','재미없었어','슬펐어','지루했어'],'ans':0,'hint':('was','였다'),'explain':'was = is의 과거'},
            {'en':'I had a great day.','choices':['좋은 하루였어','나쁜 하루였어','짧은 하루였어','피곤한 하루였어'],'ans':0,'hint':('had','가졌다'),'explain':'had = have의 과거'},
            {'en':'I felt happy.','choices':['행복했어','슬펐어','화났어','졸렸어'],'ans':0,'hint':('felt','느꼈다'),'explain':'felt = feel의 과거'},
            {'en':'I made cookies.','choices':['쿠키 만들었어','쿠키 먹었어','쿠키 봤어','쿠키 사'],'ans':0,'hint':('made','만들었다'),'explain':'made = make의 과거'},
            {'en':'I watched TV.','choices':['TV 봤어','TV 만들었어','TV 사','TV 줬어'],'ans':0,'hint':('watched','봤다'),'explain':'watched = watch의 과거'},
            {'en':'I went home.','choices':['집에 갔어','집에서 왔어','집 떠났어','집 봤어'],'ans':0,'hint':('went home','집 갔다'),'explain':'went home = 집 갔다'},
            {'en':'I slept early.','choices':['일찍 잤어','늦게 잤어','안 잤어','자면서 일했어'],'ans':0,'hint':('slept','잤다'),'explain':'slept = sleep의 과거'},
            {'en':'I was tired.','choices':['피곤했어','신났어','행복했어','졸렸어'],'ans':0,'hint':('tired','피곤한'),'explain':'I was = ~였어'},
            {'en':'I cleaned my room.','choices':['방 청소했어','방 만들었어','방 봤어','방 떠났어'],'ans':0,'hint':('cleaned','청소했다'),'explain':'cleaned = clean의 과거'},
            {'en':"What did you do?",'choices':['뭐 했어?','어디 갔어?','왜 왔어?','누구 봤어?'],'ans':0,'hint':('did','했다'),'explain':'did you do = 뭐 했어?'},
            {'en':'I learned new words.','choices':['새 단어 배웠어','새 단어 잊었어','새 단어 만들었어','새 단어 줬어'],'ans':0,'hint':('learned','배웠다'),'explain':'learned = learn의 과거'},
            {'en':'I called my friend.','choices':['친구한테 전화했어','친구 만났어','친구 봤어','친구 가르쳤어'],'ans':0,'hint':('called','전화했다'),'explain':'called = call의 과거'},
            {'en':'It was a good day.','choices':['좋은 날이었어','나쁜 날이었어','지루한 날이었어','피곤한 날이었어'],'ans':0,'hint':('good day','좋은 날'),'explain':'It was ~ = ~였어'},
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

    # ═════════════════════════════════════════════
    # 6/8~6/14 - 여름·계절·일상 (Week 8)
    # ═════════════════════════════════════════════
    '20260608': {
        'date': '2026-06-08', 'day_ko': '월', 'theme': '날씨 이야기', 'theme_emoji': '☀️',
        'description': '날씨 표현 익혀보기!',
        'questions': [
            {'en':'How is the weather?','choices':['날씨 어때?','시간 몇시?','어디 가?','뭐 해?'],'ans':0,'hint':('weather','날씨'),'explain':'weather = 날씨'},
            {'en':"It's sunny today.",'choices':['오늘 흐려','오늘 화창해','오늘 비와','오늘 추워'],'ans':1,'hint':('sunny','화창한'),'explain':'sunny = 햇살 가득한'},
            {'en':"It's raining.",'choices':['비 와요','눈 와요','바람 불어요','맑아요'],'ans':0,'hint':('rain','비'),'explain':'rain = 비'},
            {'en':'I love rainbows.','choices':['무지개 좋아','구름 좋아','눈 좋아','비 좋아'],'ans':0,'hint':('rainbow','무지개'),'explain':'rainbow = 무지개'},
            {'en':"It's so hot!",'choices':['너무 추워','너무 더워','너무 좋아','너무 싫어'],'ans':1,'hint':('hot','더운'),'explain':'hot = 더운'},
            {'en':"It's freezing!",'choices':['따뜻해','꽁꽁 추워','시원해','맑아'],'ans':1,'hint':('freezing','꽁꽁 추운'),'explain':'freezing = 꽁꽁 추운'},
            {'en':'Look at the clouds.','choices':['구름 좀 봐','별 좀 봐','달 좀 봐','해 좀 봐'],'ans':0,'hint':('clouds','구름들'),'explain':'cloud = 구름'},
            {'en':'I see lightning!','choices':['번개 봐!','무지개 봐!','별 봐!','달 봐!'],'ans':0,'hint':('lightning','번개'),'explain':'lightning = 번개'},
            {'en':'Take an umbrella.','choices':['우산 가져가','가방 가져가','책 가져가','옷 가져가'],'ans':0,'hint':('umbrella','우산'),'explain':'umbrella = 우산'},
            {'en':'Wear a jacket.','choices':['재킷 입어','신발 신어','모자 써','가방 메'],'ans':0,'hint':('wear','입다'),'explain':'wear jacket = 재킷 입기'},
            {'en':"It's a nice day.",'choices':['날씨 좋네','날씨 별로네','피곤하네','졸리네'],'ans':0,'hint':('nice','좋은'),'explain':'nice day = 좋은 날'},
            {'en':"It's windy.",'choices':['눈 와','바람 분다','비 와','더워'],'ans':1,'hint':('windy','바람 부는'),'explain':'windy = 바람 부는'},
            {'en':"It's foggy outside.",'choices':['밖이 안개껴','밖이 맑아','밖이 추워','밖이 더워'],'ans':0,'hint':('foggy','안개 낀'),'explain':'foggy = 안개 낀'},
            {'en':"It's cloudy today.",'choices':['오늘 흐려','오늘 맑아','오늘 비','오늘 눈'],'ans':0,'hint':('cloudy','흐린'),'explain':'cloudy = 흐린'},
            {'en':'Snow is falling.','choices':['비가 와','눈이 와','잎이 떨어져','꽃이 펴'],'ans':1,'hint':('snow','눈'),'explain':'snow falling = 눈 내림'},
            {'en':'The sky is blue.','choices':['하늘이 파래','하늘이 빨개','하늘이 검어','하늘이 노래'],'ans':0,'hint':('sky','하늘'),'explain':'sky = 하늘'},
            {'en':"What a beautiful sunrise!",'choices':['너무 어두워','일출 너무 예뻐','노을 봐','별 봐'],'ans':1,'hint':('sunrise','일출'),'explain':'sunrise = 일출'},
            {'en':"It's mild today.",'choices':['오늘 포근해','오늘 더워','오늘 비','오늘 눈'],'ans':0,'hint':('mild','포근한'),'explain':'mild = 온화한'},
            {'en':"It's so humid.",'choices':['너무 건조해','너무 습해','너무 더워','너무 추워'],'ans':1,'hint':('humid','습한'),'explain':'humid = 습한'},
            {'en':"Don't forget your umbrella!",'choices':['우산 챙겨!','책 챙겨!','옷 챙겨!','신발 챙겨!'],'ans':0,'hint':('umbrella','우산'),'explain':"Don't forget = 잊지마!"},
        ]
    },

    '20260609': {
        'date': '2026-06-09', 'day_ko': '화', 'theme': '여름·바다 표현', 'theme_emoji': '🏖️',
        'description': '바다와 여름 표현!',
        'questions': [
            {'en':"Let's go to the beach!",'choices':['해변 가자!','학교 가자!','집 가자!','마트 가자!'],'ans':0,'hint':('beach','해변'),'explain':'beach = 해변'},
            {'en':'I want to swim.','choices':['먹고 싶어','수영하고 싶어','자고 싶어','놀고 싶어'],'ans':1,'hint':('swim','수영'),'explain':'swim = 수영하다'},
            {'en':'Big waves!','choices':['큰 파도!','작은 돌!','큰 산!','작은 새!'],'ans':0,'hint':('wave','파도'),'explain':'wave = 파도'},
            {'en':'Soft sand.','choices':['딱딱한 돌','부드러운 모래','거친 풀','뜨거운 흙'],'ans':1,'hint':('sand','모래'),'explain':'sand = 모래'},
            {'en':'Wear sunglasses.','choices':['안경 써','선글라스 써','모자 써','신발 신어'],'ans':1,'hint':('sunglasses','선글라스'),'explain':'sunglasses = 선글라스'},
            {'en':'Put on sunscreen.','choices':['선크림 발라','로션 발라','립밤 발라','립스틱 발라'],'ans':0,'hint':('sunscreen','선크림'),'explain':'sunscreen = 선크림'},
            {'en':'I love ice cream.','choices':['아이스크림 좋아','과자 좋아','빵 좋아','과일 좋아'],'ans':0,'hint':('ice cream','아이스크림'),'explain':'ice cream = 아이스크림'},
            {'en':'Summer is fun.','choices':['겨울 재밌어','봄 재밌어','여름 재밌어','가을 재밌어'],'ans':2,'hint':('summer','여름'),'explain':'summer = 여름'},
            {'en':'I see a yacht.','choices':['배가 보여','요트가 보여','집이 보여','산이 보여'],'ans':1,'hint':('yacht','요트'),'explain':'yacht = 요트'},
            {'en':"Let's surf today!",'choices':['오늘 서핑하자!','오늘 자자!','오늘 먹자!','오늘 가자!'],'ans':0,'hint':('surf','서핑'),'explain':'surf = 파도타기'},
            {'en':'Splash in the water.','choices':['물에 첨벙','땅에 앉아','산에 올라','하늘 봐'],'ans':0,'hint':('splash','첨벙'),'explain':'splash = 첨벙거리다'},
            {'en':'Pretty seashells!','choices':['예쁜 조개!','예쁜 돌!','예쁜 꽃!','예쁜 새!'],'ans':0,'hint':('seashell','조개껍질'),'explain':'seashell = 조개껍질'},
            {'en':'I can float!','choices':['잠수할 수 있어','뜰 수 있어','뛸 수 있어','걸을 수 있어'],'ans':1,'hint':('float','뜨다'),'explain':'float = 물에 뜨다'},
            {'en':'Use a tube.','choices':['튜브 써','컵 써','책 써','연필 써'],'ans':0,'hint':('tube','튜브'),'explain':'tube = 튜브'},
            {'en':"What's that lighthouse?",'choices':['저 등대 뭐야?','저 산 뭐야?','저 배 뭐야?','저 새 뭐야?'],'ans':0,'hint':('lighthouse','등대'),'explain':'lighthouse = 등대'},
            {'en':"Let's sunbathe.",'choices':['일광욕하자','수영하자','놀자','먹자'],'ans':0,'hint':('sunbathe','일광욕'),'explain':'sunbathe = 일광욕하다'},
            {'en':'Happy holiday!','choices':['행복한 휴일!','행복한 학교!','행복한 시험!','행복한 일!'],'ans':0,'hint':('holiday','휴일'),'explain':'holiday = 휴일'},
            {'en':'I love the seaside.','choices':['바닷가 좋아','산 좋아','시내 좋아','시장 좋아'],'ans':0,'hint':('seaside','바닷가'),'explain':'seaside = 바닷가'},
            {'en':"Let's snorkel!",'choices':['스노클링하자!','스키타자!','스케이트타자!','달리자!'],'ans':0,'hint':('snorkel','스노클링'),'explain':'snorkel = 스노클링'},
            {'en':"Summer vacation starts!",'choices':['방학 시작!','학교 시작!','일 시작!','시험 시작!'],'ans':0,'hint':('vacation','방학'),'explain':'vacation = 방학'},
        ]
    },

    '20260610': {
        'date': '2026-06-10', 'day_ko': '수', 'theme': '옷·패션 표현', 'theme_emoji': '👕',
        'description': '옷 입을 때 영어!',
        'questions': [
            {'en':'Wear a tshirt.','choices':['티셔츠 입어','바지 입어','신발 신어','모자 써'],'ans':0,'hint':('tshirt','티셔츠'),'explain':'wear tshirt = 티셔츠 입기'},
            {'en':'Cool sneakers!','choices':['멋진 운동화!','멋진 모자!','멋진 가방!','멋진 옷!'],'ans':0,'hint':('sneakers','운동화'),'explain':'sneakers = 운동화'},
            {'en':'A pretty dress.','choices':['예쁜 드레스','예쁜 신발','예쁜 모자','예쁜 가방'],'ans':0,'hint':('dress','드레스'),'explain':'dress = 원피스/드레스'},
            {'en':'My favorite hoodie.','choices':['좋아하는 후드티','좋아하는 양말','좋아하는 신발','좋아하는 가방'],'ans':0,'hint':('hoodie','후드티'),'explain':'hoodie = 후드티'},
            {'en':'Put on socks.','choices':['양말 신어','신발 신어','모자 써','옷 입어'],'ans':0,'hint':('socks','양말'),'explain':'put on socks = 양말 신기'},
            {'en':'A cool cap!','choices':['멋진 야구모자!','멋진 신발!','멋진 양말!','멋진 옷!'],'ans':0,'hint':('cap','야구모자'),'explain':'cap = 야구모자'},
            {'en':'Wear a coat.','choices':['코트 입어','바지 입어','신발 신어','모자 써'],'ans':0,'hint':('coat','코트'),'explain':'coat = 코트'},
            {'en':"It's pajama time!",'choices':['잠옷 시간!','외출 시간!','학교 시간!','일 시간!'],'ans':0,'hint':('pajamas','잠옷'),'explain':'pajamas = 잠옷'},
            {'en':'School uniform.','choices':['학교 교복','학교 가방','학교 옷','학교 신발'],'ans':0,'hint':('uniform','교복'),'explain':'uniform = 교복'},
            {'en':'Cute outfit!','choices':['귀여운 옷차림!','귀여운 가방!','귀여운 신발!','귀여운 책!'],'ans':0,'hint':('outfit','옷차림'),'explain':'outfit = 옷차림'},
            {'en':'A warm scarf.','choices':['따뜻한 목도리','따뜻한 옷','따뜻한 가방','따뜻한 신발'],'ans':0,'hint':('scarf','목도리'),'explain':'scarf = 목도리'},
            {'en':'Wear gloves!','choices':['장갑 껴!','신발 신어!','모자 써!','옷 입어!'],'ans':0,'hint':('gloves','장갑'),'explain':'gloves = 장갑'},
            {'en':'Cool shorts!','choices':['멋진 반바지!','멋진 긴바지!','멋진 셔츠!','멋진 옷!'],'ans':0,'hint':('shorts','반바지'),'explain':'shorts = 반바지'},
            {'en':'Beach flipflops!','choices':['해변 쪼리!','해변 부츠!','해변 양말!','해변 모자!'],'ans':0,'hint':('flipflops','쪼리'),'explain':'flipflops = 쪼리'},
            {'en':'A soft cardigan.','choices':['부드러운 카디건','부드러운 옷','부드러운 가방','부드러운 신발'],'ans':0,'hint':('cardigan','카디건'),'explain':'cardigan = 카디건'},
            {'en':'Mom wears an apron.','choices':['엄마는 앞치마 둘러','엄마는 옷 입어','엄마는 가방 메','엄마는 모자 써'],'ans':0,'hint':('apron','앞치마'),'explain':'apron = 앞치마'},
            {'en':'A warm sweater.','choices':['따뜻한 스웨터','따뜻한 신발','따뜻한 모자','따뜻한 옷'],'ans':0,'hint':('sweater','스웨터'),'explain':'sweater = 스웨터'},
            {'en':'Cozy slippers.','choices':['편한 슬리퍼','편한 신발','편한 옷','편한 모자'],'ans':0,'hint':('slippers','슬리퍼'),'explain':'slippers = 슬리퍼'},
            {'en':'Cool tank top!','choices':['멋진 민소매!','멋진 긴팔!','멋진 옷!','멋진 신발!'],'ans':0,'hint':('tank top','민소매'),'explain':'tank top = 민소매'},
            {'en':'My swimwear is ready.','choices':['수영복 준비됐어','옷 준비됐어','신발 준비됐어','가방 준비됐어'],'ans':0,'hint':('swimwear','수영복'),'explain':'swimwear = 수영복'},
        ]
    },

    '20260611': {
        'date': '2026-06-11', 'day_ko': '목', 'theme': '운동·스포츠 표현', 'theme_emoji': '⚽',
        'description': '스포츠와 운동 영어!',
        'questions': [
            {'en':"Let's play soccer!",'choices':['축구하자!','농구하자!','야구하자!','테니스하자!'],'ans':0,'hint':('soccer','축구'),'explain':'soccer = 축구'},
            {'en':'I love basketball.','choices':['축구 좋아','농구 좋아','야구 좋아','배구 좋아'],'ans':1,'hint':('basketball','농구'),'explain':'basketball = 농구'},
            {'en':'A baseball game.','choices':['축구 경기','야구 경기','농구 경기','테니스 경기'],'ans':1,'hint':('baseball','야구'),'explain':'baseball = 야구'},
            {'en':'Play tennis with me.','choices':['테니스 같이 하자','축구 같이 하자','농구 같이 하자','달리자'],'ans':0,'hint':('tennis','테니스'),'explain':'tennis = 테니스'},
            {'en':"Let's play badminton.",'choices':['배드민턴하자','축구하자','농구하자','테니스하자'],'ans':0,'hint':('badminton','배드민턴'),'explain':'badminton = 배드민턴'},
            {'en':'I jog every day.','choices':['매일 조깅해','매일 자','매일 먹어','매일 놀아'],'ans':0,'hint':('jog','조깅'),'explain':'jog = 천천히 달리기'},
            {'en':'Stretch first!','choices':['먼저 자!','먼저 먹어!','먼저 스트레칭!','먼저 가!'],'ans':2,'hint':('stretch','스트레칭'),'explain':'stretch = 스트레칭'},
            {'en':"It's match day!",'choices':['경기날!','시험날!','학교날!','쉬는날!'],'ans':0,'hint':('match','경기'),'explain':'match = 경기'},
            {'en':'Score a goal!','choices':['골 넣어!','공 차!','뛰어!','쉬어!'],'ans':0,'hint':('goal','골'),'explain':'goal = 골'},
            {'en':'Won a gold medal!','choices':['금메달 땄어!','은메달 땄어!','동메달 땄어!','상 받았어!'],'ans':0,'hint':('medal','메달'),'explain':'gold medal = 금메달'},
            {'en':'A warmup first.','choices':['준비운동 먼저','시험 먼저','수업 먼저','놀이 먼저'],'ans':0,'hint':('warmup','준비운동'),'explain':'warmup = 준비운동'},
            {'en':'Do squats!','choices':['스쿼트해!','달려!','수영해!','자!'],'ans':0,'hint':('squat','스쿼트'),'explain':'squat = 스쿼트'},
            {'en':'A great player!','choices':['훌륭한 선수!','훌륭한 친구!','훌륭한 학생!','훌륭한 선생님!'],'ans':0,'hint':('player','선수'),'explain':'player = 선수'},
            {'en':'A morning workout.','choices':['아침 운동','아침 식사','아침 잠','아침 공부'],'ans':0,'hint':('workout','운동'),'explain':'workout = 운동'},
            {'en':'I do yoga.','choices':['요가해','달리기해','수영해','스키타'],'ans':0,'hint':('yoga','요가'),'explain':'yoga = 요가'},
            {'en':"Let's go bowling!",'choices':['볼링하자!','수영하자!','자자!','먹자!'],'ans':0,'hint':('bowling','볼링'),'explain':'bowling = 볼링'},
            {'en':'Korean archery is great.','choices':['한국 양궁 짱!','한국 축구 짱!','한국 농구 짱!','한국 야구 짱!'],'ans':0,'hint':('archery','양궁'),'explain':'archery = 양궁'},
            {'en':'A gold trophy!','choices':['금 트로피!','은 트로피!','동 트로피!','상장!'],'ans':0,'hint':('trophy','트로피'),'explain':'trophy = 트로피'},
            {'en':'Blow the whistle.','choices':['호루라기 불어','피리 불어','노래 해','말 해'],'ans':0,'hint':('whistle','호루라기'),'explain':'whistle = 호루라기'},
            {'en':'Ice skating is fun!','choices':['스케이팅 재밌어!','수영 재밌어!','달리기 재밌어!','자기 재밌어!'],'ans':0,'hint':('skating','스케이팅'),'explain':'skating = 스케이팅'},
        ]
    },

    '20260612': {
        'date': '2026-06-12', 'day_ko': '금', 'theme': '자연·식물 표현', 'theme_emoji': '🌳',
        'description': '자연 속 영어 표현!',
        'questions': [
            {'en':'A tall tree.','choices':['큰 나무','작은 꽃','큰 돌','작은 풀'],'ans':0,'hint':('tree','나무'),'explain':'tree = 나무'},
            {'en':'Green leaves.','choices':['초록 잎','빨간 꽃','노란 풀','파란 돌'],'ans':0,'hint':('leaves','잎'),'explain':'leaf/leaves = 잎'},
            {'en':'A red rose.','choices':['빨간 장미','노란 해바라기','분홍 튤립','흰 백합'],'ans':0,'hint':('rose','장미'),'explain':'rose = 장미'},
            {'en':'Tulips bloom.','choices':['튤립이 펴','장미가 펴','잔디가 자라','나무가 커'],'ans':0,'hint':('tulip','튤립'),'explain':'tulip = 튤립'},
            {'en':'Tall sunflowers.','choices':['큰 해바라기','작은 잔디','큰 나무','작은 꽃'],'ans':0,'hint':('sunflower','해바라기'),'explain':'sunflower = 해바라기'},
            {'en':'Walk in the forest.','choices':['숲을 걸어','산을 올라','강을 건너','바다 봐'],'ans':0,'hint':('forest','숲'),'explain':'forest = 숲'},
            {'en':'Climb a mountain.','choices':['산 올라','강 건너','바다 가','집 가'],'ans':0,'hint':('mountain','산'),'explain':'climb mountain = 등산'},
            {'en':'A long river.','choices':['긴 강','짧은 강','큰 산','작은 호수'],'ans':0,'hint':('river','강'),'explain':'river = 강'},
            {'en':'A quiet lake.','choices':['조용한 호수','시끄러운 강','조용한 바다','시끄러운 시장'],'ans':0,'hint':('lake','호수'),'explain':'lake = 호수'},
            {'en':'A pretty butterfly!','choices':['예쁜 나비!','예쁜 새!','예쁜 꽃!','예쁜 잎!'],'ans':0,'hint':('butterfly','나비'),'explain':'butterfly = 나비'},
            {'en':'Bees make honey.','choices':['벌은 꿀 만들어','새는 노래해','꽃은 펴','나무는 자라'],'ans':0,'hint':('bee','벌'),'explain':'bee = 벌'},
            {'en':'A tiny bug.','choices':['작은 벌레','큰 새','작은 풀','큰 돌'],'ans':0,'hint':('bug','벌레'),'explain':'bug = 벌레'},
            {'en':'Sit on the grass.','choices':['풀밭에 앉아','돌에 앉아','의자에 앉아','계단에 앉아'],'ans':0,'hint':('grass','풀'),'explain':'grass = 잔디/풀'},
            {'en':'Roots grow deep.','choices':['뿌리가 깊이 자라','잎이 떨어져','꽃이 펴','새가 날아'],'ans':0,'hint':('root','뿌리'),'explain':'root = 뿌리'},
            {'en':'A big rock.','choices':['큰 바위','작은 돌','큰 나무','작은 풀'],'ans':0,'hint':('rock','바위'),'explain':'rock = 바위'},
            {'en':'Plant a seed.','choices':['씨앗 심어','꽃 따','풀 베','나무 잘라'],'ans':0,'hint':('seed','씨앗'),'explain':'plant seed = 씨앗 심기'},
            {'en':'Pink petals.','choices':['분홍 꽃잎','빨간 잎','노란 꽃','흰 풀'],'ans':0,'hint':('petal','꽃잎'),'explain':'petal = 꽃잎'},
            {'en':'Squirrels love acorns.','choices':['다람쥐는 도토리 좋아','새는 벌레 좋아','곰은 꿀 좋아','토끼는 풀 좋아'],'ans':0,'hint':('acorn','도토리'),'explain':'acorn = 도토리'},
            {'en':'A clear stream... oh, a reef!','choices':['산호초!','폭포!','호수!','늪!'],'ans':0,'hint':('reef','산호초'),'explain':'reef = 산호초'},
            {'en':'Birds in the marsh.','choices':['습지의 새','산의 새','강의 새','집의 새'],'ans':0,'hint':('marsh','습지'),'explain':'marsh = 습지'},
        ]
    },

    '20260613': {
        'date': '2026-06-13', 'day_ko': '토', 'theme': '주말 야외 활동', 'theme_emoji': '🚴',
        'description': '주말에 쓰는 영어!',
        'questions': [
            {'en':"Let's go camping!",'choices':['캠핑 가자!','집에 있자!','학교 가자!','마트 가자!'],'ans':0,'hint':('camping','캠핑'),'explain':'camping = 캠핑'},
            {'en':"Let's have a picnic.",'choices':['소풍 가자','집 청소하자','자자','공부하자'],'ans':0,'hint':('picnic','소풍'),'explain':'picnic = 소풍'},
            {'en':'Ride a bike.','choices':['자전거 타','자동차 타','버스 타','지하철 타'],'ans':0,'hint':('bike','자전거'),'explain':'ride bike = 자전거 타기'},
            {'en':'Fly a kite!','choices':['연 날려!','새 봐!','공 차!','뛰어!'],'ans':0,'hint':('kite','연'),'explain':'fly kite = 연 날리기'},
            {'en':"Let's go fishing.",'choices':['낚시 가자','수영 가자','등산 가자','쇼핑 가자'],'ans':0,'hint':('fishing','낚시'),'explain':'fishing = 낚시'},
            {'en':"Let's visit the park.",'choices':['공원 가자','시장 가자','학교 가자','집에 있자'],'ans':0,'hint':('park','공원'),'explain':'park = 공원'},
            {'en':'I am hiking.','choices':['등산해','수영해','자','먹어'],'ans':0,'hint':('hiking','등산'),'explain':'hiking = 등산'},
            {'en':'A barbecue tonight!','choices':['오늘 바비큐!','오늘 피자!','오늘 라면!','오늘 김밥!'],'ans':0,'hint':('barbecue','바비큐'),'explain':'barbecue = 바비큐'},
            {'en':'Take photos.','choices':['사진 찍어','노래해','달려','놀아'],'ans':0,'hint':('photo','사진'),'explain':'photo = 사진'},
            {'en':"Let's play together.",'choices':['같이 놀자','혼자 자','혼자 먹어','혼자 가'],'ans':0,'hint':('together','함께'),'explain':'together = 함께'},
            {'en':'Have fun!','choices':['재밌게 놀아!','잘 자!','잘 가!','잘 먹어!'],'ans':0,'hint':('fun','재미'),'explain':'have fun = 재밌게 놀기'},
            {'en':"What a sunny day!",'choices':['화창한 날!','흐린 날!','비 오는 날!','눈 오는 날!'],'ans':0,'hint':('sunny','화창한'),'explain':'sunny day = 화창한 날'},
            {'en':"It's relaxing.",'choices':['편안해','피곤해','바빠','짜증나'],'ans':0,'hint':('relaxing','편안한'),'explain':'relaxing = 편안한'},
            {'en':"Let's go shopping.",'choices':['쇼핑 가자','학교 가자','자','먹자'],'ans':0,'hint':('shopping','쇼핑'),'explain':'shopping = 쇼핑'},
            {'en':"Let's watch a movie.",'choices':['영화 보자','책 읽자','자자','공부하자'],'ans':0,'hint':('movie','영화'),'explain':'movie = 영화'},
            {'en':'I had so much fun.','choices':['너무 재밌었어','너무 졸려','너무 더워','너무 추워'],'ans':0,'hint':('fun','재미'),'explain':'had fun = 재밌었다'},
            {'en':'Time to go home.','choices':['집에 갈 시간','학교 갈 시간','놀 시간','잘 시간'],'ans':0,'hint':('go home','집에 가다'),'explain':'go home = 집에 가다'},
            {'en':"Let's play games.",'choices':['게임하자','자자','먹자','가자'],'ans':0,'hint':('game','게임'),'explain':'play games = 게임하기'},
            {'en':'I love weekends!','choices':['주말 좋아!','평일 좋아!','학교 좋아!','시험 좋아!'],'ans':0,'hint':('weekend','주말'),'explain':'weekend = 주말'},
            {'en':"Let's go for a walk.",'choices':['산책 가자','자자','먹자','학교 가자'],'ans':0,'hint':('walk','산책'),'explain':'go for walk = 산책하다'},
        ]
    },

    '20260614': {
        'date': '2026-06-14', 'day_ko': '일', 'theme': '하루 마무리', 'theme_emoji': '🌙',
        'description': '하루 끝낼 때 표현!',
        'questions': [
            {'en':'I am tired.','choices':['졸려','피곤해','배고파','목말라'],'ans':1,'hint':('tired','피곤한'),'explain':'tired = 피곤한'},
            {'en':"It's bedtime.",'choices':['잘 시간','먹을 시간','놀 시간','갈 시간'],'ans':0,'hint':('bedtime','잘 시간'),'explain':'bedtime = 잘 시간'},
            {'en':'Good night!','choices':['좋은 밤!','좋은 아침!','좋은 점심!','좋은 저녁!'],'ans':0,'hint':('night','밤'),'explain':'good night = 잘 자!'},
            {'en':'Sweet dreams!','choices':['좋은 꿈 꿔!','잘 일어나!','잘 먹어!','잘 가!'],'ans':0,'hint':('dreams','꿈'),'explain':'sweet dreams = 좋은 꿈 꿔'},
            {'en':"I'm sleepy.",'choices':['졸려','신나','즐거워','심심해'],'ans':0,'hint':('sleepy','졸린'),'explain':'sleepy = 졸린'},
            {'en':'Brush your teeth.','choices':['이 닦아','얼굴 씻어','머리 빗어','샤워해'],'ans':0,'hint':('brush teeth','이 닦다'),'explain':'brush teeth = 이 닦기'},
            {'en':'Wash your face.','choices':['얼굴 씻어','발 씻어','이 닦아','샤워해'],'ans':0,'hint':('wash','씻다'),'explain':'wash face = 세수'},
            {'en':"Set the alarm.",'choices':['알람 맞춰','시계 봐','전화해','문 닫아'],'ans':0,'hint':('alarm','알람'),'explain':'alarm = 알람'},
            {'en':'Read a book.','choices':['책 읽어','TV 봐','놀아','자'],'ans':0,'hint':('read','읽다'),'explain':'read = 읽다'},
            {'en':"Let's pray.",'choices':['기도하자','노래하자','자자','먹자'],'ans':0,'hint':('pray','기도'),'explain':'pray = 기도하다'},
            {'en':'I had a great day!','choices':['멋진 하루!','피곤한 하루!','심심한 하루!','슬픈 하루!'],'ans':0,'hint':('great','멋진'),'explain':'great day = 멋진 하루'},
            {'en':'Tomorrow is a new day.','choices':['내일은 새 하루','어제는 끝났어','지금은 밤','오늘은 좋아'],'ans':0,'hint':('tomorrow','내일'),'explain':'tomorrow = 내일'},
            {'en':'See you tomorrow!','choices':['내일 봐!','지금 봐!','어제 봤어!','다음에 봐!'],'ans':0,'hint':('tomorrow','내일'),'explain':'see you tomorrow = 내일 봐'},
            {'en':'Hug your parents.','choices':['부모님 안아드려','부모님 봐','부모님 가','부모님 자'],'ans':0,'hint':('hug','안다'),'explain':'hug = 안기'},
            {'en':'I love you, mom!','choices':['엄마 사랑해!','엄마 미워!','엄마 와!','엄마 가!'],'ans':0,'hint':('love','사랑'),'explain':'I love you = 사랑해'},
            {'en':'Turn off the light.','choices':['불 꺼','불 켜','문 열어','문 닫아'],'ans':0,'hint':('turn off','끄다'),'explain':'turn off = 끄다'},
            {'en':'Put on pajamas.','choices':['잠옷 입어','옷 벗어','신발 신어','모자 써'],'ans':0,'hint':('pajamas','잠옷'),'explain':'put on pajamas = 잠옷 입기'},
            {'en':'Drink some water.','choices':['물 마셔','물 봐','물 줘','물 사'],'ans':0,'hint':('drink','마시다'),'explain':'drink water = 물 마시기'},
            {'en':"It's a beautiful night.",'choices':['아름다운 밤','시끄러운 밤','추운 밤','더운 밤'],'ans':0,'hint':('beautiful','아름다운'),'explain':'beautiful night = 아름다운 밤'},
            {'en':'Rest well.','choices':['푹 쉬어','일해','놀아','먹어'],'ans':0,'hint':('rest','쉬다'),'explain':'rest = 쉬다'},
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
  if (q.hint && Array.isArray(q.hint) && q.hint.length >= 2 && q.hint[0] && q.hint[1]) {{
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
  // 🛡️ 안전망: explain 없으면 정답 보기 표시
  const explainText = q.explain || ('정답: ' + (q.choices ? q.choices[q.ans] : '확인하세요'));
  document.getElementById('popExplain').innerHTML = '📖 ' + explainText;
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
