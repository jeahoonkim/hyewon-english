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

    # ═════════════════════════════════════════════
    # 6/15~6/21 - 디지털·음악·미술·이야기·우주 (Week 9)
    # ═════════════════════════════════════════════
    '20260615': {
        'date': '2026-06-15', 'day_ko': '월', 'theme': '컴퓨터·인터넷', 'theme_emoji': '💻',
        'description': '디지털 영어 표현!',
        'questions': [
            {'en':'Turn on the computer.','choices':['컴퓨터 켜','컴퓨터 꺼','컴퓨터 사','컴퓨터 봐'],'ans':0,'hint':('turn on','켜다'),'explain':'turn on = 켜다'},
            {'en':'Click the mouse.','choices':['마우스 사','마우스 클릭해','마우스 줘','마우스 던져'],'ans':1,'hint':('click','클릭'),'explain':'click = 클릭'},
            {'en':'Type your name.','choices':['이름 말해','이름 입력해','이름 잊어','이름 봐'],'ans':1,'hint':('type','입력'),'explain':'type = 키보드 입력'},
            {'en':'Download an app.','choices':['앱 다운로드','앱 삭제','앱 사','앱 봐'],'ans':0,'hint':('download','다운로드'),'explain':'download = 받기'},
            {'en':'Search on Google.','choices':['구글에서 검색','구글에서 사','구글에서 봐','구글에서 자'],'ans':0,'hint':('search','검색'),'explain':'search = 검색'},
            {'en':'Send an email.','choices':['이메일 보내','이메일 받아','이메일 사','이메일 봐'],'ans':0,'hint':('email','이메일'),'explain':'email = 이메일'},
            {'en':'Connect to wifi.','choices':['와이파이 끊어','와이파이 연결','와이파이 봐','와이파이 사'],'ans':1,'hint':('connect','연결'),'explain':'connect to = ~에 연결'},
            {'en':'My phone is charging.','choices':['전화 충전 중','전화 꺼짐','전화 분실','전화 부서짐'],'ans':0,'hint':('charge','충전'),'explain':'charge = 충전하다'},
            {'en':'Open the website.','choices':['웹사이트 열어','웹사이트 닫아','웹사이트 봐','웹사이트 사'],'ans':0,'hint':('open','열다'),'explain':'open = 열다'},
            {'en':"What's your password?",'choices':['이름이 뭐?','비밀번호가 뭐?','시간이 몇?','어디 가?'],'ans':1,'hint':('password','비밀번호'),'explain':'password = 비밀번호'},
            {'en':'The screen is bright.','choices':['화면 어두워','화면 밝아','화면 깨졌어','화면 작아'],'ans':1,'hint':('screen','화면'),'explain':'bright = 밝은'},
            {'en':'Upload a photo.','choices':['사진 올려','사진 지워','사진 봐','사진 줘'],'ans':0,'hint':('upload','올리기'),'explain':'upload = 올리기'},
            {'en':'I use my tablet.','choices':['태블릿 사용','태블릿 줘','태블릿 사','태블릿 봐'],'ans':0,'hint':('use','사용'),'explain':'use = 사용'},
            {'en':'A big monitor.','choices':['큰 모니터','작은 모니터','새 모니터','낡은 모니터'],'ans':0,'hint':('monitor','모니터'),'explain':'monitor = 모니터'},
            {'en':'Where is the charger?','choices':['충전기 어디?','컴퓨터 어디?','전화 어디?','책 어디?'],'ans':0,'hint':('charger','충전기'),'explain':'charger = 충전기'},
            {'en':'I love my laptop.','choices':['노트북 좋아','노트북 싫어','노트북 사고싶어','노트북 모름'],'ans':0,'hint':('laptop','노트북'),'explain':'laptop = 노트북'},
            {'en':"It's online.",'choices':['인터넷에 있어','오프라인이야','자고 있어','놀고 있어'],'ans':0,'hint':('online','온라인'),'explain':'online = 인터넷 연결됨'},
            {'en':"Don't share your password!",'choices':['비밀번호 공유 마!','비밀번호 알려!','비밀번호 잊어!','비밀번호 사!'],'ans':0,'hint':('share','공유'),'explain':"Don't = 하지마"},
            {'en':"It's a great app!",'choices':['좋은 앱!','나쁜 앱!','오래된 앱!','새 앱!'],'ans':0,'hint':('great','좋은'),'explain':'great = 멋진'},
            {'en':'Smartphones are useful.','choices':['스마트폰 유용','스마트폰 무거워','스마트폰 비싸','스마트폰 작아'],'ans':0,'hint':('useful','유용한'),'explain':'useful = 유용한'},
        ]
    },

    '20260616': {
        'date': '2026-06-16', 'day_ko': '화', 'theme': '음악·악기 표현', 'theme_emoji': '🎵',
        'description': '음악과 악기 영어!',
        'questions': [
            {'en':'I play the piano.','choices':['피아노 쳐','피아노 사','피아노 봐','피아노 들어'],'ans':0,'hint':('play','연주'),'explain':'play piano = 피아노 치다'},
            {'en':'Blow the trumpet.','choices':['트럼펫 봐','트럼펫 불어','트럼펫 사','트럼펫 줘'],'ans':1,'hint':('blow','불다'),'explain':'blow = 불다'},
            {'en':'Sing a song.','choices':['노래 사','노래 듣어','노래 불러','노래 봐'],'ans':2,'hint':('sing','부르다'),'explain':'sing = 노래하다'},
            {'en':'Listen to the melody.','choices':['멜로디 들어','멜로디 봐','멜로디 사','멜로디 만들어'],'ans':0,'hint':('listen','듣다'),'explain':'listen to = ~를 듣다'},
            {'en':'A great performance!','choices':['멋진 공연!','나쁜 공연!','조용한 공연!','짧은 공연!'],'ans':0,'hint':('performance','공연'),'explain':'performance = 공연'},
            {'en':"Let's go to a concert.",'choices':['음악회 가자','학교 가자','시장 가자','집 가자'],'ans':0,'hint':('concert','음악회'),'explain':'concert = 음악회'},
            {'en':'Join the choir!','choices':['합창단 들어와!','집에 가!','자!','놀자!'],'ans':0,'hint':('choir','합창단'),'explain':'choir = 합창단'},
            {'en':'Feel the rhythm.','choices':['리듬 느껴','음식 먹어','잠 자','놀아'],'ans':0,'hint':('rhythm','리듬'),'explain':'rhythm = 리듬'},
            {'en':'Big applause!','choices':['큰 박수!','큰 소리!','큰 노래!','큰 빵!'],'ans':0,'hint':('applause','박수'),'explain':'applause = 박수'},
            {'en':'Play the xylophone.','choices':['실로폰 쳐','실로폰 사','실로폰 줘','실로폰 봐'],'ans':0,'hint':('xylophone','실로폰'),'explain':'xylophone = 실로폰'},
            {'en':'A famous orchestra.','choices':['유명 오케스트라','작은 오케스트라','새 오케스트라','조용한 오케스트라'],'ans':0,'hint':('famous','유명한'),'explain':'famous = 유명한'},
            {'en':'On stage now!','choices':['지금 무대 위!','지금 집에!','지금 학교에!','지금 자!'],'ans':0,'hint':('stage','무대'),'explain':'on stage = 무대 위'},
            {'en':'Read the lyrics.','choices':['가사 읽어','가사 들어','가사 사','가사 잊어'],'ans':0,'hint':('lyrics','가사'),'explain':'lyrics = 가사'},
            {'en':'Watch the musical.','choices':['뮤지컬 봐','뮤지컬 자','뮤지컬 사','뮤지컬 줘'],'ans':0,'hint':('musical','뮤지컬'),'explain':'musical = 뮤지컬'},
            {'en':'A talented musician!','choices':['재능있는 음악가!','새 음악가!','오래된 음악가!','작은 음악가!'],'ans':0,'hint':('talented','재능있는'),'explain':'talented = 재능있는'},
            {'en':'Bring your recorder.','choices':['리코더 가져와','리코더 두고와','리코더 잊어','리코더 사'],'ans':0,'hint':('bring','가져오다'),'explain':'bring = 가져오다'},
            {'en':"Let's start the band.",'choices':['밴드 시작하자','밴드 그만하자','밴드 봐','밴드 자'],'ans':0,'hint':('band','밴드'),'explain':'start = 시작'},
            {'en':'I love this tune.','choices':['이 곡 좋아','이 곡 싫어','이 곡 안 들려','이 곡 짧아'],'ans':0,'hint':('tune','곡'),'explain':'tune = 곡'},
            {'en':'Watch the opera.','choices':['오페라 봐','오페라 사','오페라 만들어','오페라 줘'],'ans':0,'hint':('opera','오페라'),'explain':'opera = 오페라'},
            {'en':'Music makes me happy.','choices':['음악 슬프게 해','음악 행복하게 해','음악 졸리게 해','음악 화나게 해'],'ans':1,'hint':('happy','행복한'),'explain':'make me ~ = 나를 ~하게'},
        ]
    },

    '20260617': {
        'date': '2026-06-17', 'day_ko': '수', 'theme': '미술·그림 표현', 'theme_emoji': '🎨',
        'description': '미술 시간 영어!',
        'questions': [
            {'en':'I love art class.','choices':['미술 시간 좋아','수학 시간 좋아','체육 시간 좋아','과학 시간 좋아'],'ans':0,'hint':('art','미술'),'explain':'art = 미술'},
            {'en':"Let's paint together.",'choices':['같이 그리자','같이 자자','같이 먹자','같이 놀자'],'ans':0,'hint':('paint','색칠'),'explain':'paint = 물감으로 그리다'},
            {'en':'A beautiful painting.','choices':['아름다운 그림','오래된 그림','새 그림','작은 그림'],'ans':0,'hint':('painting','그림'),'explain':'painting = 회화'},
            {'en':'Use a palette.','choices':['팔레트 써','책 써','펜 써','지우개 써'],'ans':0,'hint':('palette','팔레트'),'explain':'palette = 팔레트'},
            {'en':'A colorful picture.','choices':['다채로운 그림','회색 그림','흰 그림','검은 그림'],'ans':0,'hint':('colorful','다채로운'),'explain':'colorful = 색 많은'},
            {'en':'Visit a gallery.','choices':['갤러리 가','집 가','학교 가','시장 가'],'ans':0,'hint':('gallery','갤러리'),'explain':'gallery = 미술관'},
            {'en':'Draw a portrait.','choices':['초상화 그려','풍경화 그려','꽃 그려','집 그려'],'ans':0,'hint':('portrait','초상화'),'explain':'portrait = 인물화'},
            {'en':'A pretty landscape.','choices':['예쁜 풍경화','예쁜 초상화','예쁜 사진','예쁜 인형'],'ans':0,'hint':('landscape','풍경화'),'explain':'landscape = 풍경'},
            {'en':'Use scissors.','choices':['가위 써','연필 써','풀 써','마커 써'],'ans':0,'hint':('scissors','가위'),'explain':'scissors = 가위'},
            {'en':'Stick with glue.','choices':['풀로 붙여','테이프로 붙여','못으로 붙여','손으로 붙여'],'ans':0,'hint':('glue','풀'),'explain':'glue = 접착제'},
            {'en':'A big statue.','choices':['큰 조각상','큰 그림','큰 책','큰 집'],'ans':0,'hint':('statue','조각상'),'explain':'statue = 조각상'},
            {'en':'Press the stamp.','choices':['도장 찍어','도장 봐','도장 사','도장 던져'],'ans':0,'hint':('stamp','도장'),'explain':'stamp = 도장'},
            {'en':'Design a poster.','choices':['포스터 디자인','포스터 사','포스터 던져','포스터 잊어'],'ans':0,'hint':('design','디자인'),'explain':'design = 디자인'},
            {'en':'Shape the clay.','choices':['찰흙 모양 만들어','찰흙 먹어','찰흙 봐','찰흙 사'],'ans':0,'hint':('shape','모양'),'explain':'shape = 모양 만들기'},
            {'en':'Pottery class is fun.','choices':['도자기 수업 재밌어','수학 수업 재밌어','음악 수업 재밌어','국어 수업 재밌어'],'ans':0,'hint':('pottery','도자기'),'explain':'pottery = 도자기'},
            {'en':'Put it in a frame.','choices':['액자에 넣어','가방에 넣어','책에 넣어','상자에 넣어'],'ans':0,'hint':('frame','액자'),'explain':'frame = 액자'},
            {'en':'Hang the poster.','choices':['포스터 걸어','포스터 던져','포스터 잘라','포스터 봐'],'ans':0,'hint':('hang','걸다'),'explain':'hang = 걸다'},
            {'en':'First draft only.','choices':['첫 초안일 뿐','완성작이야','마지막이야','잘못됐어'],'ans':0,'hint':('draft','초안'),'explain':'draft = 초안'},
            {'en':'Make a paper craft.','choices':['종이 공예 만들어','종이 그림 그려','종이 사','종이 봐'],'ans':0,'hint':('craft','공예'),'explain':'craft = 공예'},
            {'en':'A perfect drawing!','choices':['완벽한 그림!','나쁜 그림!','작은 그림!','오래된 그림!'],'ans':0,'hint':('perfect','완벽한'),'explain':'perfect = 완벽한'},
        ]
    },

    '20260618': {
        'date': '2026-06-18', 'day_ko': '목', 'theme': '책·이야기 표현', 'theme_emoji': '📖',
        'description': '동화책 속 영어!',
        'questions': [
            {'en':'Tell me a story.','choices':['이야기 들려줘','노래 불러줘','책 사줘','놀아줘'],'ans':0,'hint':('story','이야기'),'explain':'story = 이야기'},
            {'en':'Once upon a time...','choices':['옛날 옛적에...','내일은...','지금은...','어제...'],'ans':0,'hint':('once upon','옛날에'),'explain':'동화 시작 표현!'},
            {'en':'A brave prince.','choices':['용감한 왕자','겁먹은 왕자','약한 왕자','졸린 왕자'],'ans':0,'hint':('brave','용감한'),'explain':'brave = 용감한'},
            {'en':'A kind princess.','choices':['친절한 공주','나쁜 공주','늙은 공주','슬픈 공주'],'ans':0,'hint':('kind','친절한'),'explain':'kind = 친절한'},
            {'en':'The dragon flies.','choices':['용이 날아','용이 자','용이 먹어','용이 놀아'],'ans':0,'hint':('fly','날다'),'explain':'fly = 날다'},
            {'en':'An old witch.','choices':['늙은 마녀','젊은 마녀','새 마녀','친절한 마녀'],'ans':0,'hint':('witch','마녀'),'explain':'witch = 마녀'},
            {'en':'A pretty fairy.','choices':['예쁜 요정','무서운 요정','큰 요정','작은 요정'],'ans':0,'hint':('fairy','요정'),'explain':'fairy = 요정'},
            {'en':'In a big castle.','choices':['큰 성에서','작은 집에서','학교에서','마트에서'],'ans':0,'hint':('castle','성'),'explain':'castle = 성'},
            {'en':'The villain laughs.','choices':['악당이 웃어','왕자가 웃어','공주가 웃어','요정이 웃어'],'ans':0,'hint':('villain','악당'),'explain':'villain = 악당'},
            {'en':'A famous author.','choices':['유명한 작가','새 작가','어린 작가','조용한 작가'],'ans':0,'hint':('author','작가'),'explain':'author = 작가'},
            {'en':'Read chapter one.','choices':['1장 읽어','1장 써','1장 봐','1장 사'],'ans':0,'hint':('chapter','장'),'explain':'chapter = 장'},
            {'en':'The book title.','choices':['책 제목','책 끝','책 책','책 가방'],'ans':0,'hint':('title','제목'),'explain':'title = 제목'},
            {'en':'A happy ending!','choices':['행복한 결말!','슬픈 결말!','나쁜 결말!','조용한 결말!'],'ans':0,'hint':('ending','결말'),'explain':'ending = 결말'},
            {'en':'A great adventure!','choices':['멋진 모험!','짧은 일!','조용한 시간!','나쁜 날!'],'ans':0,'hint':('adventure','모험'),'explain':'adventure = 모험'},
            {'en':'Hidden treasure!','choices':['숨겨진 보물!','잃어버린 책!','새 옷!','오래된 모자!'],'ans':0,'hint':('treasure','보물'),'explain':'treasure = 보물'},
            {'en':'A powerful wizard.','choices':['강력한 마법사','약한 마법사','졸린 마법사','조용한 마법사'],'ans':0,'hint':('wizard','마법사'),'explain':'wizard = 마법사'},
            {'en':'A brave knight.','choices':['용감한 기사','겁먹은 기사','졸린 기사','어린 기사'],'ans':0,'hint':('knight','기사'),'explain':'knight = 기사'},
            {'en':'Greek myth.','choices':['그리스 신화','한국 음식','중국 영화','일본 책'],'ans':0,'hint':('myth','신화'),'explain':'myth = 신화'},
            {'en':"Aesop's fable.",'choices':['이솝 우화','이솝 시','이솝 노래','이솝 동요'],'ans':0,'hint':('fable','우화'),'explain':'fable = 우화'},
            {'en':'Write a poem.','choices':['시 써','시 읽어','시 사','시 봐'],'ans':0,'hint':('poem','시'),'explain':'poem = 시'},
        ]
    },

    '20260619': {
        'date': '2026-06-19', 'day_ko': '금', 'theme': '우주·과학 표현', 'theme_emoji': '🚀',
        'description': '우주 탐험 영어!',
        'questions': [
            {'en':'Rocket launch!','choices':['로켓 발사!','로켓 멈춰!','로켓 봐!','로켓 사!'],'ans':0,'hint':('launch','발사'),'explain':'launch = 발사'},
            {'en':'Wear a spacesuit.','choices':['우주복 입어','옷 벗어','신발 신어','모자 써'],'ans':0,'hint':('spacesuit','우주복'),'explain':'spacesuit = 우주복'},
            {'en':'Put on a helmet.','choices':['헬멧 써','신발 신어','옷 입어','장갑 껴'],'ans':0,'hint':('helmet','헬멧'),'explain':'helmet = 헬멧'},
            {'en':'Space mission!','choices':['우주 임무!','우주 끝!','우주 가게!','우주 학교!'],'ans':0,'hint':('mission','임무'),'explain':'mission = 임무'},
            {'en':'Moon craters.','choices':['달 분화구','달 거리','달 마을','달 가게'],'ans':0,'hint':('crater','분화구'),'explain':'crater = 분화구'},
            {'en':'A scary blackhole.','choices':['무서운 블랙홀','예쁜 별','파란 하늘','노란 해'],'ans':0,'hint':('blackhole','블랙홀'),'explain':'blackhole = 블랙홀'},
            {'en':'Did you see the ufo?','choices':['유에프오 봤어?','달 봤어?','별 봤어?','해 봤어?'],'ans':0,'hint':('ufo','유에프오'),'explain':'ufo = 외계 비행체'},
            {'en':'Observe the stars.','choices':['별 관찰해','별 사','별 잊어','별 줘'],'ans':0,'hint':('observe','관찰'),'explain':'observe = 관찰'},
            {'en':'A great discovery!','choices':['큰 발견!','큰 책!','큰 가방!','큰 집!'],'ans':0,'hint':('discovery','발견'),'explain':'discovery = 발견'},
            {'en':'A science experiment.','choices':['과학 실험','과학 책','과학 시험','과학 영화'],'ans':0,'hint':('experiment','실험'),'explain':'experiment = 실험'},
            {'en':'Work in the lab.','choices':['실험실에서 일해','집에서 일해','학교에서 일해','공원에서 일해'],'ans':0,'hint':('lab','실험실'),'explain':'lab = 실험실'},
            {'en':'Use a microscope.','choices':['현미경 사용','컴퓨터 사용','마우스 사용','책 사용'],'ans':0,'hint':('microscope','현미경'),'explain':'microscope = 현미경'},
            {'en':'A strong magnet.','choices':['강한 자석','약한 자석','새 자석','오래된 자석'],'ans':0,'hint':('magnet','자석'),'explain':'magnet = 자석'},
            {'en':'A helpful robot.','choices':['도와주는 로봇','무서운 로봇','오래된 로봇','작은 로봇'],'ans':0,'hint':('robot','로봇'),'explain':'robot = 로봇'},
            {'en':'Save electricity.','choices':['전기 아껴','전기 써','전기 끄지마','전기 사'],'ans':0,'hint':('electricity','전기'),'explain':'electricity = 전기'},
            {'en':'A laser beam.','choices':['레이저 광선','달빛','햇빛','별빛'],'ans':0,'hint':('laser','레이저'),'explain':'laser = 레이저'},
            {'en':'Use binoculars.','choices':['쌍안경 사용','컴퓨터 사용','책 사용','연필 사용'],'ans':0,'hint':('binoculars','쌍안경'),'explain':'binoculars = 쌍안경'},
            {'en':'Push with force.','choices':['힘으로 밀어','약하게 밀어','놀이로 밀어','부드럽게 밀어'],'ans':0,'hint':('force','힘'),'explain':'force = 힘'},
            {'en':'Top speed!','choices':['최고 속도!','낮은 속도!','중간 속도!','없는 속도!'],'ans':0,'hint':('speed','속도'),'explain':'speed = 속도'},
            {'en':'Moon dust.','choices':['달 먼지','달 모래','달 돌','달 물'],'ans':0,'hint':('dust','먼지'),'explain':'dust = 먼지'},
        ]
    },

    '20260620': {
        'date': '2026-06-20', 'day_ko': '토', 'theme': '시간·계획 표현', 'theme_emoji': '🕐',
        'description': '시간 말하기 영어!',
        'questions': [
            {'en':"What time is it?",'choices':['몇 시야?','어디야?','뭐 해?','누구야?'],'ans':0,'hint':('time','시간'),'explain':'시간 묻기!'},
            {'en':"It's three o'clock.",'choices':['3시야','2시야','4시야','5시야'],'ans':0,'hint':('three','3'),'explain':'three = 3'},
            {'en':'In the morning.','choices':['아침에','저녁에','밤에','점심에'],'ans':0,'hint':('morning','아침'),'explain':'in the morning = 아침에'},
            {'en':'At noon.','choices':['정오에','자정에','새벽에','저녁에'],'ans':0,'hint':('noon','정오'),'explain':'noon = 12시 정오'},
            {'en':'In the afternoon.','choices':['오후에','아침에','밤에','새벽에'],'ans':0,'hint':('afternoon','오후'),'explain':'afternoon = 오후'},
            {'en':'At night.','choices':['밤에','아침에','오후에','점심에'],'ans':0,'hint':('night','밤'),'explain':'at night = 밤에'},
            {'en':'See you tomorrow.','choices':['내일 봐','어제 봐','지금 봐','다음에 봐'],'ans':0,'hint':('tomorrow','내일'),'explain':'tomorrow = 내일'},
            {'en':"It's Monday.",'choices':['월요일','화요일','수요일','목요일'],'ans':0,'hint':('Monday','월요일'),'explain':'Monday = 월요일'},
            {'en':'Today is Sunday.','choices':['오늘 일요일','오늘 토요일','오늘 월요일','오늘 금요일'],'ans':0,'hint':('Sunday','일요일'),'explain':'Sunday = 일요일'},
            {'en':'Next week.','choices':['다음 주','지난 주','이번 주','매주'],'ans':0,'hint':('next','다음'),'explain':'next = 다음'},
            {'en':'Last month.','choices':['지난 달','이번 달','다음 달','매달'],'ans':0,'hint':('last','지난'),'explain':'last = 지난'},
            {'en':"I'm busy now.",'choices':['지금 바빠','지금 한가해','지금 졸려','지금 배고파'],'ans':0,'hint':('busy','바쁜'),'explain':'busy = 바쁜'},
            {'en':"I'll be there soon.",'choices':['곧 갈게','지금 가','내일 가','안 가'],'ans':0,'hint':('soon','곧'),'explain':'soon = 곧'},
            {'en':"Let's meet at 5.",'choices':['5시에 만나자','5시에 자자','5시에 먹자','5시에 가자'],'ans':0,'hint':('meet','만나다'),'explain':'meet = 만나다'},
            {'en':'Just a minute.','choices':['잠깐만','오래 기다려','빨리','지금'],'ans':0,'hint':('minute','분'),'explain':'just a minute = 잠깐만!'},
            {'en':'Hurry up!','choices':['서둘러!','천천히!','자!','놀아!'],'ans':0,'hint':('hurry','서두르다'),'explain':'hurry up = 빨리'},
            {'en':"I'm late.",'choices':['늦었어','일찍 왔어','지금 와','내일 와'],'ans':0,'hint':('late','늦은'),'explain':'late = 늦은'},
            {'en':'See you later.','choices':['이따 봐','내일 봐','어제 봐','다음에 봐'],'ans':0,'hint':('later','나중에'),'explain':'see you later = 이따 봐'},
            {'en':'Good morning!','choices':['좋은 아침!','좋은 밤!','좋은 점심!','좋은 저녁!'],'ans':0,'hint':('morning','아침'),'explain':'good morning = 안녕 (아침)'},
            {'en':'Good night!','choices':['잘 자!','잘 와!','잘 먹어!','잘 가!'],'ans':0,'hint':('night','밤'),'explain':'good night = 잘 자'},
        ]
    },

    '20260621': {
        'date': '2026-06-21', 'day_ko': '일', 'theme': '약속·초대 표현', 'theme_emoji': '🤝',
        'description': '친구와 약속 영어!',
        'questions': [
            {'en':"Let's meet at the park.",'choices':['공원에서 만나자','학교에서 만나자','집에서 만나자','시장에서 만나자'],'ans':0,'hint':('meet','만나다'),'explain':'meet at = ~에서 만나다'},
            {'en':'Are you free today?','choices':['오늘 한가해?','오늘 바빠?','오늘 자?','오늘 가?'],'ans':0,'hint':('free','한가한'),'explain':'free = 한가한'},
            {'en':"Let's hang out.",'choices':['같이 놀자','같이 자자','같이 먹자','같이 가자'],'ans':0,'hint':('hang out','놀다'),'explain':'hang out = 함께 놀기'},
            {'en':'Come to my house.','choices':['우리 집에 와','너네 집에 가','학교 와','마트 가'],'ans':0,'hint':('come','오다'),'explain':'come to = ~에 오다'},
            {'en':"Let's have dinner together.",'choices':['같이 저녁 먹자','같이 놀자','같이 자자','같이 가자'],'ans':0,'hint':('dinner','저녁'),'explain':'have dinner = 저녁 먹다'},
            {'en':"Are you coming?",'choices':['올 거야?','갈 거야?','자?','먹어?'],'ans':0,'hint':('coming','오는 중'),'explain':'are you coming = 오니?'},
            {'en':'I will be there.','choices':['거기 갈게','거기 안 가','지금 가','다음에 가'],'ans':0,'hint':('will','~할게'),'explain':'will = 미래 의지'},
            {'en':"I can't come.",'choices':['못 가','갈게','가고싶어','가지마'],'ans':0,'hint':("can't",'못해'),'explain':"can't = ~할 수 없다"},
            {'en':"How about Saturday?",'choices':['토요일 어때?','월요일 어때?','일요일 어때?','금요일 어때?'],'ans':0,'hint':('Saturday','토요일'),'explain':'how about ~? = ~ 어때?'},
            {'en':'Sounds good!','choices':['좋아!','별로!','싫어!','몰라!'],'ans':0,'hint':('good','좋은'),'explain':'sounds good = 좋아!'},
            {'en':"Let's invite them.",'choices':['그들 초대하자','그들 보내자','그들 봐','그들 잊자'],'ans':0,'hint':('invite','초대'),'explain':'invite = 초대'},
            {'en':'A birthday party!','choices':['생일 파티!','학교 파티!','졸업 파티!','새해 파티!'],'ans':0,'hint':('birthday','생일'),'explain':'birthday party = 생일 파티'},
            {'en':"Happy birthday!",'choices':['생일 축하!','새해 복!','즐거운 명절!','크리스마스 축하!'],'ans':0,'hint':('birthday','생일'),'explain':'happy birthday = 생일 축하'},
            {'en':"Thanks for coming!",'choices':['와줘서 고마워!','가서 고마워!','자서 고마워!','먹어서 고마워!'],'ans':0,'hint':('thanks','고마워'),'explain':'thanks for ~ing = ~해줘서 고마워'},
            {'en':'I had so much fun!','choices':['너무 재밌었어!','너무 슬펐어!','너무 졸렸어!','너무 더웠어!'],'ans':0,'hint':('fun','재미'),'explain':'had fun = 재밌었다'},
            {'en':"Don't be late!",'choices':['늦지마!','일찍 와!','오지마!','자지마!'],'ans':0,'hint':('late','늦은'),'explain':"don't be ~ = ~하지 마"},
            {'en':"Where shall we go?",'choices':['어디 갈까?','어디 자?','어디 먹어?','어디 봐?'],'ans':0,'hint':('where','어디'),'explain':'where shall we = 어디 ~?'},
            {'en':'See you on Sunday.','choices':['일요일에 봐','월요일에 봐','지금 봐','내일 봐'],'ans':0,'hint':('Sunday','일요일'),'explain':'see you on ~ = ~요일에 봐'},
            {'en':"Let's go together.",'choices':['같이 가자','혼자 가자','자','먹자'],'ans':0,'hint':('together','함께'),'explain':"let's go together = 같이 가자"},
            {'en':'Goodbye, friends!','choices':['친구들 잘 가!','친구들 와!','친구들 자!','친구들 먹어!'],'ans':0,'hint':('goodbye','잘 가'),'explain':'goodbye = 작별 인사'},
        ]
    },

    # ═════════════════════════════════════════════
    # 6/22~7/5 - 2주치 (Week 10·11)
    # ═════════════════════════════════════════════
    '20260622': {
        'date':'2026-06-22','day_ko':'월','theme':'요리·부엌','theme_emoji':'🍳','description':'요리할 때 영어!',
        'questions':[
            {'en':'Boil the water.','choices':['물 끓여','물 마셔','물 부어','물 사'],'ans':0,'hint':('boil','끓이다'),'explain':'boil = 끓이다'},
            {'en':'Fry an egg.','choices':['계란 튀겨','계란 삶아','계란 사','계란 깨'],'ans':0,'hint':('fry','튀기다'),'explain':'fry = 기름에 굽다'},
            {'en':'Chop the onion.','choices':['양파 썰어','양파 봐','양파 던져','양파 사'],'ans':0,'hint':('chop','썰다'),'explain':'chop = 썰다'},
            {'en':'Stir the soup.','choices':['국 휘저어','국 먹어','국 끓여','국 봐'],'ans':0,'hint':('stir','휘젓다'),'explain':'stir = 휘저어 섞기'},
            {'en':'Pour the milk.','choices':['우유 부어','우유 마셔','우유 사','우유 봐'],'ans':0,'hint':('pour','붓다'),'explain':'pour = 따르다'},
            {'en':'Peel a banana.','choices':['바나나 껍질 벗겨','바나나 먹어','바나나 사','바나나 봐'],'ans':0,'hint':('peel','껍질 벗기다'),'explain':'peel = 껍질 벗기기'},
            {'en':'Slice the bread.','choices':['빵 썰어','빵 던져','빵 먹어','빵 사'],'ans':0,'hint':('slice','얇게 썰다'),'explain':'slice = 얇게 자르기'},
            {'en':'Use a knife.','choices':['칼 써','숟가락 써','포크 써','젓가락 써'],'ans':0,'hint':('knife','칼'),'explain':'knife = 칼'},
            {'en':'Use chopsticks.','choices':['젓가락 써','포크 써','칼 써','손 써'],'ans':0,'hint':('chopsticks','젓가락'),'explain':'chopsticks = 젓가락'},
            {'en':'A clean plate.','choices':['깨끗한 접시','더러운 접시','새 접시','오래된 접시'],'ans':0,'hint':('plate','접시'),'explain':'plate = 접시'},
            {'en':'A cup of tea.','choices':['차 한 잔','우유 한 잔','물 한 잔','주스 한 잔'],'ans':0,'hint':('tea','차'),'explain':'cup of ~ = ~한 잔'},
            {'en':'Mix the dough.','choices':['반죽 섞어','반죽 던져','반죽 사','반죽 봐'],'ans':0,'hint':('mix','섞다'),'explain':'mix = 섞다'},
            {'en':'Add flour.','choices':['밀가루 넣어','설탕 넣어','소금 넣어','우유 넣어'],'ans':0,'hint':('flour','밀가루'),'explain':'flour = 밀가루'},
            {'en':'Add sugar.','choices':['설탕 넣어','소금 넣어','밀가루 넣어','우유 넣어'],'ans':0,'hint':('sugar','설탕'),'explain':'sugar = 설탕'},
            {'en':'Hot pan!','choices':['뜨거운 팬!','차가운 팬!','새 팬!','낡은 팬!'],'ans':0,'hint':('pan','팬'),'explain':'pan = 프라이팬'},
            {'en':'Boil in a pot.','choices':['냄비에 끓여','컵에 끓여','병에 끓여','접시에 끓여'],'ans':0,'hint':('pot','냄비'),'explain':'pot = 냄비'},
            {'en':'Use a napkin.','choices':['냅킨 써','수건 써','종이 써','옷 써'],'ans':0,'hint':('napkin','냅킨'),'explain':'napkin = 냅킨'},
            {'en':'A glass of water.','choices':['물 한 잔','차 한 잔','우유 한 잔','주스 한 잔'],'ans':0,'hint':('water','물'),'explain':'glass of ~ = ~한 잔'},
            {'en':'Eat with a spoon.','choices':['숟가락으로 먹어','포크로 먹어','칼로 먹어','손으로 먹어'],'ans':0,'hint':('spoon','숟가락'),'explain':'spoon = 숟가락'},
            {'en':"Let's cook together.",'choices':['같이 요리하자','같이 자자','같이 놀자','같이 가자'],'ans':0,'hint':('cook','요리'),'explain':'cook = 요리하다'},
        ]
    },

    '20260623': {
        'date':'2026-06-23','day_ko':'화','theme':'영화·미디어','theme_emoji':'🎬','description':'영화 영어!',
        'questions':[
            {'en':'A funny film.','choices':['재밌는 영화','슬픈 영화','무서운 영화','지루한 영화'],'ans':0,'hint':('film','영화'),'explain':'film = 영화'},
            {'en':'A famous director.','choices':['유명 감독','새 감독','어린 감독','조용한 감독'],'ans':0,'hint':('director','감독'),'explain':'director = 감독'},
            {'en':'Watch a video.','choices':['영상 봐','노래 들어','책 읽어','자'],'ans':0,'hint':('video','영상'),'explain':'video = 영상'},
            {'en':'Funny cartoon!','choices':['재밌는 만화!','슬픈 만화!','오래된 만화!','조용한 만화!'],'ans':0,'hint':('cartoon','만화'),'explain':'cartoon = 만화·애니'},
            {'en':'Watch a drama.','choices':['드라마 봐','뉴스 봐','만화 봐','자'],'ans':0,'hint':('drama','드라마'),'explain':'drama = 드라마'},
            {'en':'A scary horror.','choices':['무서운 공포물','재밌는 코미디','슬픈 드라마','로맨틱 영화'],'ans':0,'hint':('horror','공포'),'explain':'horror = 공포'},
            {'en':'A funny comedy.','choices':['재밌는 코미디','무서운 영화','슬픈 영화','액션 영화'],'ans':0,'hint':('comedy','코미디'),'explain':'comedy = 코미디'},
            {'en':'A romance story.','choices':['로맨스 이야기','액션 이야기','공포 이야기','코미디'],'ans':0,'hint':('romance','로맨스'),'explain':'romance = 사랑 이야기'},
            {'en':'A fantasy movie.','choices':['판타지 영화','드라마 영화','액션 영화','다큐'],'ans':0,'hint':('fantasy','판타지'),'explain':'fantasy = 판타지'},
            {'en':'Action movie!','choices':['액션 영화!','로맨스 영화!','만화 영화!','다큐!'],'ans':0,'hint':('action','액션'),'explain':'action = 액션'},
            {'en':'Watch the news.','choices':['뉴스 봐','만화 봐','영화 봐','드라마 봐'],'ans':0,'hint':('news','뉴스'),'explain':'news = 뉴스'},
            {'en':'Change the channel.','choices':['채널 바꿔','채널 봐','채널 사','채널 줘'],'ans':0,'hint':('channel','채널'),'explain':'channel = 채널'},
            {'en':'Watch the trailer.','choices':['예고편 봐','본편 봐','자','놀아'],'ans':0,'hint':('trailer','예고편'),'explain':'trailer = 예고편'},
            {'en':'Eat popcorn.','choices':['팝콘 먹어','과자 먹어','케이크 먹어','빵 먹어'],'ans':0,'hint':('popcorn','팝콘'),'explain':'popcorn = 팝콘'},
            {'en':'A big audience.','choices':['많은 관객','적은 관객','새 관객','어린 관객'],'ans':0,'hint':('audience','관객'),'explain':'audience = 관객'},
            {'en':'Read the subtitles.','choices':['자막 읽어','책 읽어','뉴스 읽어','편지 읽어'],'ans':0,'hint':('subtitle','자막'),'explain':'subtitle = 자막'},
            {'en':'Where is the remote?','choices':['리모컨 어디?','전화 어디?','TV 어디?','책 어디?'],'ans':0,'hint':('remote','리모컨'),'explain':'remote = 리모컨'},
            {'en':'A short clip.','choices':['짧은 영상','긴 영상','새 영상','오래된 영상'],'ans':0,'hint':('clip','짧은 영상'),'explain':'clip = 짧은 영상'},
            {'en':'Speak into the microphone.','choices':['마이크에 말해','전화에 말해','책에 말해','벽에 말해'],'ans':0,'hint':('microphone','마이크'),'explain':'microphone = 마이크'},
            {'en':'A funny scene.','choices':['웃긴 장면','슬픈 장면','무서운 장면','지루한 장면'],'ans':0,'hint':('scene','장면'),'explain':'scene = 장면'},
        ]
    },

    '20260624': {
        'date':'2026-06-24','day_ko':'수','theme':'게임·놀이','theme_emoji':'🎮','description':'놀이 영어!',
        'questions':[
            {'en':"Let's play a game.",'choices':['게임하자','공부하자','자자','먹자'],'ans':0,'hint':('game','게임'),'explain':'game = 게임'},
            {'en':'Roll the dice!','choices':['주사위 굴려!','주사위 봐!','주사위 사!','주사위 던져!'],'ans':0,'hint':('dice','주사위'),'explain':'dice = 주사위'},
            {'en':'Solve the puzzle.','choices':['퍼즐 풀어','퍼즐 봐','퍼즐 던져','퍼즐 사'],'ans':0,'hint':('puzzle','퍼즐'),'explain':'puzzle = 퍼즐'},
            {'en':"Let's play checkers.",'choices':['체커 두자','체스 두자','자자','먹자'],'ans':0,'hint':('checkers','체커'),'explain':'checkers = 체커 게임'},
            {'en':'Play cards.','choices':['카드 놀이','책 읽기','자기','달리기'],'ans':0,'hint':('cards','카드'),'explain':'play cards = 카드 놀이'},
            {'en':'A pretty doll.','choices':['예쁜 인형','예쁜 책','예쁜 옷','예쁜 가방'],'ans':0,'hint':('doll','인형'),'explain':'doll = 인형'},
            {'en':'A cute toy.','choices':['귀여운 장난감','귀여운 옷','귀여운 책','귀여운 음식'],'ans':0,'hint':('toy','장난감'),'explain':'toy = 장난감'},
            {'en':'Fly a kite!','choices':['연 날려!','새 봐!','공 차!','공 던져!'],'ans':0,'hint':('kite','연'),'explain':'fly kite = 연 날리기'},
            {'en':"Let's compete!",'choices':['경쟁하자!','자자!','먹자!','놀자!'],'ans':0,'hint':('compete','경쟁'),'explain':'compete = 경쟁하다'},
            {'en':"It's my turn.",'choices':['내 차례','네 차례','쟤 차례','없어'],'ans':0,'hint':('turn','차례'),'explain':'turn = 차례'},
            {'en':'Follow the rules.','choices':['규칙 따라','뛰어','자','놀아'],'ans':0,'hint':('rule','규칙'),'explain':'rule = 규칙'},
            {'en':'Play hideandseek!','choices':['숨바꼭질 하자!','술래잡기 하자!','자자!','먹자!'],'ans':0,'hint':('hideandseek','숨바꼭질'),'explain':'숨고 찾기 놀이'},
            {'en':'Play tag!','choices':['술래잡기 하자!','자자!','먹자!','놀자!'],'ans':0,'hint':('tag','술래잡기'),'explain':'tag = 술래잡기'},
            {'en':'Roll the marble.','choices':['구슬 굴려','공 굴려','자','놀아'],'ans':0,'hint':('marble','구슬'),'explain':'marble = 구슬'},
            {'en':'Pass the level!','choices':['레벨 통과!','책 봐!','자!','달려!'],'ans':0,'hint':('level','레벨'),'explain':'level = 단계'},
            {'en':'A big jigsaw.','choices':['큰 직소퍼즐','큰 책','큰 공','큰 인형'],'ans':0,'hint':('jigsaw','직소퍼즐'),'explain':'jigsaw = 직소퍼즐'},
            {'en':"It's a draw!",'choices':['무승부!','승리!','패배!','없음!'],'ans':0,'hint':('draw','무승부'),'explain':'draw = 비기다'},
            {'en':'A tough opponent.','choices':['강한 상대','약한 상대','새 친구','오래된 친구'],'ans':0,'hint':('opponent','상대'),'explain':'opponent = 상대편'},
            {'en':'Spin the yoyo.','choices':['요요 돌려','공 돌려','책 돌려','음식 돌려'],'ans':0,'hint':('yoyo','요요'),'explain':'yoyo = 요요'},
            {'en':"Let's pretend!",'choices':['~인 척하자!','자자!','먹자!','가자!'],'ans':0,'hint':('pretend','~인 척'),'explain':'pretend = 흉내내다'},
        ]
    },

    '20260625': {
        'date':'2026-06-25','day_ko':'목','theme':'환경 보호','theme_emoji':'♻️','description':'환경 영어!',
        'questions':[
            {'en':'Recycle paper.','choices':['종이 재활용','종이 버려','종이 사','종이 봐'],'ans':0,'hint':('recycle','재활용'),'explain':'recycle = 다시 쓰기'},
            {'en':'Reuse the bag.','choices':['가방 다시 써','가방 버려','가방 사','가방 봐'],'ans':0,'hint':('reuse','다시 쓰다'),'explain':'reuse = 재사용'},
            {'en':'Reduce waste.','choices':['쓰레기 줄여','쓰레기 늘려','쓰레기 봐','쓰레기 사'],'ans':0,'hint':('reduce','줄이다'),'explain':'reduce = 줄이기'},
            {'en':'Plastic bottle.','choices':['플라스틱 병','유리 병','종이 컵','금속 캔'],'ans':0,'hint':('plastic','플라스틱'),'explain':'plastic = 플라스틱'},
            {'en':'Take out the trash.','choices':['쓰레기 버려','쓰레기 모아','쓰레기 봐','쓰레기 사'],'ans':0,'hint':('trash','쓰레기'),'explain':'take out trash = 쓰레기 내놓기'},
            {'en':"Don't waste water.",'choices':['물 낭비 마','물 사','물 마셔','물 봐'],'ans':0,'hint':('waste','낭비'),'explain':"don't waste = 낭비 마"},
            {'en':'Air pollution.','choices':['공기 오염','공기 깨끗','공기 차가움','공기 따뜻'],'ans':0,'hint':('pollution','오염'),'explain':'pollution = 오염'},
            {'en':'Protect nature.','choices':['자연 보호','자연 파괴','자연 봐','자연 사'],'ans':0,'hint':('protect','보호'),'explain':'protect = 지키다'},
            {'en':'Save energy.','choices':['에너지 아껴','에너지 써','에너지 봐','에너지 사'],'ans':0,'hint':('save','아끼다'),'explain':'save = 아끼다'},
            {'en':'Save our planet.','choices':['우리 행성 지켜','우리 행성 봐','우리 행성 사','우리 행성 떠나'],'ans':0,'hint':('planet','행성'),'explain':'planet = 행성/지구'},
            {'en':'Love nature.','choices':['자연 사랑','자연 미워','자연 봐','자연 떠나'],'ans':0,'hint':('nature','자연'),'explain':'nature = 자연'},
            {'en':'A water bottle.','choices':['물병','종이컵','유리잔','캔'],'ans':0,'hint':('bottle','병'),'explain':'bottle = 병'},
            {'en':'Soda can.','choices':['음료수 캔','물병','유리잔','종이컵'],'ans':0,'hint':('can','캔'),'explain':'can = 캔'},
            {'en':'Old batteries.','choices':['오래된 배터리','새 배터리','큰 배터리','작은 배터리'],'ans':0,'hint':('battery','배터리'),'explain':'battery = 배터리'},
            {'en':'Make compost.','choices':['퇴비 만들어','쓰레기 만들어','음식 만들어','책 만들어'],'ans':0,'hint':('compost','퇴비'),'explain':'compost = 퇴비'},
            {'en':'Organic food.','choices':['유기농 음식','일반 음식','매운 음식','달콤 음식'],'ans':0,'hint':('organic','유기농'),'explain':'organic = 유기농'},
            {'en':'Go eco!','choices':['친환경 가자!','쇼핑 가자!','학교 가자!','자자!'],'ans':0,'hint':('eco','친환경'),'explain':'eco = 친환경'},
            {'en':'Pick up litter.','choices':['쓰레기 주워','쓰레기 버려','쓰레기 봐','쓰레기 사'],'ans':0,'hint':('litter','쓰레기'),'explain':'litter = 길가 쓰레기'},
            {'en':'Climate change.','choices':['기후 변화','시간 변화','날짜 변화','계절 변화'],'ans':0,'hint':('climate','기후'),'explain':'climate = 기후'},
            {'en':'Sustain nature.','choices':['자연 지속','자연 파괴','자연 봐','자연 사'],'ans':0,'hint':('sustain','지속'),'explain':'sustain = 유지·지속'},
        ]
    },

    '20260626': {
        'date':'2026-06-26','day_ko':'금','theme':'명절·기념일','theme_emoji':'🎊','description':'기념일 영어!',
        'questions':[
            {'en':'A fun festival!','choices':['재밌는 축제!','지루한 축제!','새 축제!','오래된 축제!'],'ans':0,'hint':('festival','축제'),'explain':'festival = 축제'},
            {'en':'A big celebration.','choices':['큰 축하 행사','작은 행사','조용한 행사','슬픈 행사'],'ans':0,'hint':('celebration','축하'),'explain':'celebration = 축하'},
            {'en':'Open the present.','choices':['선물 열어','책 열어','문 열어','창문 열어'],'ans':0,'hint':('present','선물'),'explain':'present = 선물'},
            {'en':'Happy birthday!','choices':['생일 축하!','새해 복!','크리스마스!','부활절!'],'ans':0,'hint':('birthday','생일'),'explain':'birthday = 생일'},
            {'en':'Merry Christmas!','choices':['메리 크리스마스!','새해 복!','부활절!','생일 축하!'],'ans':0,'hint':('Christmas','크리스마스'),'explain':'Christmas = 크리스마스'},
            {'en':'Happy Halloween!','choices':['즐거운 할로윈!','새해!','부활절!','크리스마스!'],'ans':0,'hint':('Halloween','할로윈'),'explain':'Halloween = 할로윈'},
            {'en':'Happy Easter!','choices':['부활절 축하!','새해!','크리스마스!','할로윈!'],'ans':0,'hint':('Easter','부활절'),'explain':'Easter = 부활절'},
            {'en':'Wedding anniversary.','choices':['결혼 기념일','생일','크리스마스','새해'],'ans':0,'hint':('anniversary','기념일'),'explain':'anniversary = 기념일'},
            {'en':'A scary costume!','choices':['무서운 의상!','예쁜 옷!','새 옷!','오래된 옷!'],'ans':0,'hint':('costume','의상'),'explain':'costume = 분장 의상'},
            {'en':'Wear a mask.','choices':['가면 써','옷 입어','신발 신어','모자 써'],'ans':0,'hint':('mask','가면'),'explain':'mask = 가면'},
            {'en':'Watch the fireworks.','choices':['불꽃놀이 봐','달 봐','별 봐','구름 봐'],'ans':0,'hint':('firework','불꽃놀이'),'explain':'firework = 불꽃놀이'},
            {'en':'Watch the parade.','choices':['퍼레이드 봐','영화 봐','자','먹어'],'ans':0,'hint':('parade','퍼레이드'),'explain':'parade = 행진'},
            {'en':'Eat chocolate.','choices':['초콜릿 먹어','빵 먹어','사탕 먹어','과자 먹어'],'ans':0,'hint':('chocolate','초콜릿'),'explain':'chocolate = 초콜릿'},
            {'en':'A pretty ribbon.','choices':['예쁜 리본','예쁜 옷','예쁜 책','예쁜 가방'],'ans':0,'hint':('ribbon','리본'),'explain':'ribbon = 리본'},
            {'en':'A tiny cupcake!','choices':['작은 컵케이크!','큰 케이크!','새 케이크!','오래된 케이크!'],'ans':0,'hint':('cupcake','컵케이크'),'explain':'cupcake = 컵케이크'},
            {'en':'Christmas wreath.','choices':['크리스마스 화환','크리스마스 트리','크리스마스 인형','크리스마스 선물'],'ans':0,'hint':('wreath','화환'),'explain':'wreath = 화환'},
            {'en':'A big feast!','choices':['큰 잔치!','큰 책!','큰 가게!','큰 학교!'],'ans':0,'hint':('feast','잔치'),'explain':'feast = 진수성찬'},
            {'en':'Throw confetti!','choices':['색종이 뿌려!','꽃 뿌려!','책 뿌려!','자!'],'ans':0,'hint':('confetti','색종이 조각'),'explain':'confetti = 작은 색종이'},
            {'en':'Send an invitation.','choices':['초대장 보내','편지 보내','선물 보내','책 보내'],'ans':0,'hint':('invitation','초대장'),'explain':'invitation = 초대장'},
            {'en':'Happy Thanksgiving!','choices':['추수감사절!','크리스마스!','새해!','부활절!'],'ans':0,'hint':('Thanksgiving','추수감사절'),'explain':'Thanksgiving = 추수감사절'},
        ]
    },

    '20260627': {
        'date':'2026-06-27','day_ko':'토','theme':'쇼핑·시장','theme_emoji':'🛍️','description':'쇼핑 영어 표현!',
        'questions':[
            {'en':"Let's go shopping!",'choices':['쇼핑 가자!','학교 가자!','집 가자!','자!'],'ans':0,'hint':('shopping','쇼핑'),'explain':'shopping = 쇼핑'},
            {'en':'How much is this?','choices':['이거 얼마?','이거 뭐?','이거 어디?','이거 누구?'],'ans':0,'hint':('how much','얼마'),'explain':'how much = 얼마'},
            {'en':"It's too expensive.",'choices':['너무 비싸','너무 싸','너무 좋아','너무 작아'],'ans':0,'hint':('expensive','비싼'),'explain':'expensive = 비싼'},
            {'en':"It's cheap.",'choices':['싸요','비싸요','새거','오래됨'],'ans':0,'hint':('cheap','싼'),'explain':'cheap = 싼'},
            {'en':'On sale!','choices':['할인 중!','새거!','오래된거!','없음!'],'ans':0,'hint':('sale','할인'),'explain':'on sale = 할인 중'},
            {'en':"I'll buy this.",'choices':['이거 살게','이거 싫어','이거 봐','이거 줘'],'ans':0,'hint':('buy','사다'),'explain':'buy = 사다'},
            {'en':"I want to try this on.",'choices':['입어볼래','먹어볼래','자볼래','갈래'],'ans':0,'hint':('try on','입어보다'),'explain':'try on = 입어보기'},
            {'en':'Cash or card?','choices':['현금? 카드?','이름은?','어디 가?','뭐 해?'],'ans':0,'hint':('cash','현금'),'explain':'cash or card?'},
            {'en':"Here's the receipt.",'choices':['영수증 여기','책 여기','선물 여기','옷 여기'],'ans':0,'hint':('receipt','영수증'),'explain':'receipt = 영수증'},
            {'en':"It's a good deal.",'choices':['좋은 가격','나쁜 가격','새 거','오래된 거'],'ans':0,'hint':('deal','거래'),'explain':'good deal = 좋은 거래'},
            {'en':'A discount, please.','choices':['할인해 주세요','선물해 주세요','자게 해 주세요','보여 주세요'],'ans':0,'hint':('discount','할인'),'explain':'discount = 할인'},
            {'en':"Where's the cashier?",'choices':['계산대 어디?','문 어디?','옷 어디?','책 어디?'],'ans':0,'hint':('cashier','계산대'),'explain':'cashier = 계산대'},
            {'en':"It's sold out.",'choices':['품절','할인','새 상품','다 있음'],'ans':0,'hint':('sold out','품절'),'explain':'sold out = 다 팔림'},
            {'en':'Different size?','choices':['다른 사이즈?','다른 색?','다른 가격?','다른 모양?'],'ans':0,'hint':('size','사이즈'),'explain':'size = 크기'},
            {'en':'Different color?','choices':['다른 색?','다른 사이즈?','다른 가격?','다른 모양?'],'ans':0,'hint':('color','색'),'explain':'color = 색'},
            {'en':'It looks good!','choices':['잘 어울려!','별로!','싫어!','이상해!'],'ans':0,'hint':('look','보이다'),'explain':'looks good = 잘 어울림'},
            {'en':'A shopping bag.','choices':['쇼핑백','책가방','학교 가방','여행 가방'],'ans':0,'hint':('bag','가방'),'explain':'shopping bag = 쇼핑백'},
            {'en':'Free delivery!','choices':['배송 무료!','배송 유료!','배송 없음!','배송 늦음!'],'ans':0,'hint':('delivery','배송'),'explain':'delivery = 배송'},
            {'en':"I'll take it.",'choices':['이걸로 할게','싫어요','다음에','지금'],'ans':0,'hint':('take','가지다'),'explain':"I'll take it = 살게요"},
            {'en':'Have a nice day!','choices':['좋은 하루!','잘 가요!','다시 와요!','감사!'],'ans':0,'hint':('nice day','좋은 하루'),'explain':'have a nice day = 좋은 하루!'},
        ]
    },

    '20260628': {
        'date':'2026-06-28','day_ko':'일','theme':'친구·우정','theme_emoji':'🤝','description':'친구 영어 표현!',
        'questions':[
            {'en':"You're my best friend.",'choices':['너는 내 최고 친구','너는 모르는 사람','너는 가족','너는 선생님'],'ans':0,'hint':('friend','친구'),'explain':'best friend = 베프'},
            {'en':"Let's hang out.",'choices':['같이 놀자','혼자 자자','같이 가자','혼자 먹자'],'ans':0,'hint':('hang out','놀다'),'explain':'hang out = 어울리기'},
            {'en':'Thanks a lot!','choices':['정말 고마워!','정말 미안!','정말 화나!','정말 슬퍼!'],'ans':0,'hint':('thanks','고마워'),'explain':'thanks a lot = 정말 고마워'},
            {'en':"You're welcome.",'choices':['천만에요','잘 가요','싫어요','안녕'],'ans':0,'hint':('welcome','환영'),'explain':"you're welcome = 천만에요"},
            {'en':"I'm sorry.",'choices':['미안해','고마워','반가워','안녕'],'ans':0,'hint':('sorry','미안'),'explain':'sorry = 미안'},
            {'en':"It's OK.",'choices':['괜찮아','싫어','안돼','없어'],'ans':0,'hint':('OK','괜찮아'),'explain':"it's OK = 괜찮아"},
            {'en':"Don't worry.",'choices':['걱정마','조심해','자','놀자'],'ans':0,'hint':('worry','걱정'),'explain':"don't worry = 걱정마"},
            {'en':"Cheer up!",'choices':['힘내!','자!','놀아!','먹어!'],'ans':0,'hint':('cheer','힘내다'),'explain':'cheer up = 힘내!'},
            {'en':'Good job!','choices':['잘했어!','못했어!','새거!','오래됨!'],'ans':0,'hint':('good job','잘했어'),'explain':'good job = 잘했어'},
            {'en':"You can do it!",'choices':['넌 할 수 있어!','넌 못해!','넌 자!','넌 가!'],'ans':0,'hint':('can','할 수 있다'),'explain':'you can do it = 할 수 있어'},
            {'en':"I miss you.",'choices':['보고 싶어','싫어','잊어','만나기 싫어'],'ans':0,'hint':('miss','그리워'),'explain':'miss = 그리워하다'},
            {'en':"Let's be friends.",'choices':['친구하자','싸우자','자자','가자'],'ans':0,'hint':('friends','친구'),'explain':'be friends = 친구되기'},
            {'en':"I love you.",'choices':['사랑해','미워해','싫어','반가워'],'ans':0,'hint':('love','사랑'),'explain':'love = 사랑'},
            {'en':"Are you OK?",'choices':['괜찮아?','어디 가?','뭐 해?','잘 자?'],'ans':0,'hint':('OK','괜찮'),'explain':'are you OK = 괜찮아?'},
            {'en':"What's up?",'choices':['뭐해? 잘 지내?','어디 가?','이름 뭐?','시간 몇?'],'ans':0,'hint':("what's up",'뭐해'),'explain':"what's up = 뭐해"},
            {'en':'Nice to see you!','choices':['만나서 반가워!','잘 가!','싫어!','없어!'],'ans':0,'hint':('nice','반가운'),'explain':'nice to see you = 반가워'},
            {'en':"Let's stay in touch.",'choices':['연락하자','만나지 마','싸우자','자자'],'ans':0,'hint':('touch','연락'),'explain':'stay in touch = 연락 유지'},
            {'en':"You're amazing.",'choices':['너 멋져','너 별로','너 싫어','너 자'],'ans':0,'hint':('amazing','멋진'),'explain':'amazing = 놀라운'},
            {'en':"Don't be sad.",'choices':['슬퍼하지마','자지마','가지마','오지마'],'ans':0,'hint':('sad','슬픈'),'explain':"don't be sad = 슬퍼 마"},
            {'en':'Friends forever!','choices':['영원한 친구!','잠깐 친구!','새 친구!','오래된 친구!'],'ans':0,'hint':('forever','영원'),'explain':'forever = 영원히'},
        ]
    },

    '20260629': {
        'date':'2026-06-29','day_ko':'월','theme':'건강·병원','theme_emoji':'💊','description':'아플 때 영어!',
        'questions':[
            {'en':'I am sick.','choices':['아파요','건강해요','졸려요','피곤해요'],'ans':0,'hint':('sick','아픈'),'explain':'sick = 아픈'},
            {'en':'I have a flu.','choices':['독감 걸렸어요','감기 안 걸렸어요','건강해요','피곤해요'],'ans':0,'hint':('flu','독감'),'explain':'flu = 독감'},
            {'en':'I have a headache.','choices':['머리 아파요','배 아파요','이 아파요','다리 아파요'],'ans':0,'hint':('headache','두통'),'explain':'headache = 두통'},
            {'en':'My stomach aches.','choices':['배 아파요','머리 아파요','이 아파요','다리 아파요'],'ans':0,'hint':('stomach','배'),'explain':'stomach = 배'},
            {'en':'A bad toothache.','choices':['심한 치통','심한 두통','심한 복통','심한 감기'],'ans':0,'hint':('toothache','치통'),'explain':'toothache = 치통'},
            {'en':'Take your medicine.','choices':['약 먹어','물 마셔','자','놀아'],'ans':0,'hint':('medicine','약'),'explain':'medicine = 약'},
            {'en':'Swallow the pill.','choices':['알약 삼켜','물 마셔','자','놀아'],'ans':0,'hint':('pill','알약'),'explain':'pill = 알약'},
            {'en':'Put on a bandage.','choices':['붕대 감아','옷 입어','신발 신어','자'],'ans':0,'hint':('bandage','붕대'),'explain':'bandage = 붕대'},
            {'en':'A small injury.','choices':['작은 상처','큰 상처','새 상처','오래된 상처'],'ans':0,'hint':('injury','상처'),'explain':'injury = 부상'},
            {'en':'A health checkup.','choices':['건강 검진','학교 시험','일','놀이'],'ans':0,'hint':('checkup','검진'),'explain':'checkup = 검진'},
            {'en':'Eat healthy food.','choices':['건강 음식 먹어','단 거 먹어','짠 거 먹어','매운 거 먹어'],'ans':0,'hint':('healthy','건강한'),'explain':'healthy = 건강한'},
            {'en':'A healthy diet.','choices':['건강한 식단','맛있는 식단','매운 식단','달콤 식단'],'ans':0,'hint':('diet','식단'),'explain':'diet = 식단'},
            {'en':'Fast recovery!','choices':['빠른 회복!','느린 회복!','새 회복!','없는 회복!'],'ans':0,'hint':('recovery','회복'),'explain':'recovery = 회복'},
            {'en':'Good hygiene.','choices':['좋은 위생','나쁜 위생','조용한 사람','시끄러운 사람'],'ans':0,'hint':('hygiene','위생'),'explain':'hygiene = 위생'},
            {'en':'I keep sneezing.','choices':['계속 재채기해','계속 자','계속 먹어','계속 놀아'],'ans':0,'hint':('sneeze','재채기'),'explain':'sneezing = 재채기'},
            {'en':'Wash germs away.','choices':['세균 씻어내','세균 모아','세균 봐','세균 사'],'ans':0,'hint':('germ','세균'),'explain':'germ = 세균'},
            {'en':'Get a vaccine.','choices':['백신 맞아','약 먹어','자','놀아'],'ans':0,'hint':('vaccine','백신'),'explain':'vaccine = 백신'},
            {'en':'Call an ambulance!','choices':['구급차 불러!','택시 불러!','버스 타!','집에 가!'],'ans':0,'hint':('ambulance','구급차'),'explain':'ambulance = 구급차'},
            {'en':'An emergency!','choices':['응급!','휴식!','노는 시간!','자는 시간!'],'ans':0,'hint':('emergency','응급'),'explain':'emergency = 응급 상황'},
            {'en':'Are you OK?','choices':['괜찮아?','어디 가?','뭐 해?','자?'],'ans':0,'hint':('OK','괜찮'),'explain':'안부 묻기!'},
        ]
    },

    '20260630': {
        'date':'2026-06-30','day_ko':'화','theme':'발명·도구','theme_emoji':'🔧','description':'도구·발명 영어!',
        'questions':[
            {'en':'A great invention!','choices':['멋진 발명품!','오래된 책!','지루한 영화!','쉬는 시간!'],'ans':0,'hint':('invention','발명품'),'explain':'invention = 발명품'},
            {'en':'A famous inventor.','choices':['유명한 발명가','오래된 친구','새 학생','조용한 사람'],'ans':0,'hint':('inventor','발명가'),'explain':'inventor = 발명가'},
            {'en':'Invent a new thing.','choices':['새 것 발명해','새 것 사','새 것 봐','새 것 잊어'],'ans':0,'hint':('invent','발명'),'explain':'invent = 발명하다'},
            {'en':'Roll the wheel.','choices':['바퀴 굴려','공 굴려','책 굴려','컵 굴려'],'ans':0,'hint':('wheel','바퀴'),'explain':'wheel = 바퀴'},
            {'en':'Start the engine.','choices':['엔진 시동','엔진 끄기','엔진 봐','엔진 사'],'ans':0,'hint':('engine','엔진'),'explain':'engine = 엔진'},
            {'en':'Use a tool.','choices':['도구 써','음식 써','책 써','옷 써'],'ans':0,'hint':('tool','도구'),'explain':'tool = 도구'},
            {'en':'Use a hammer.','choices':['망치 써','드라이버 써','칼 써','연필 써'],'ans':0,'hint':('hammer','망치'),'explain':'hammer = 망치'},
            {'en':'Hammer the nail.','choices':['못 박아','못 빼','못 봐','못 사'],'ans':0,'hint':('nail','못'),'explain':'nail = 못'},
            {'en':'Tighten the screw.','choices':['나사 조여','나사 풀어','나사 봐','나사 사'],'ans':0,'hint':('screw','나사'),'explain':'screw = 나사'},
            {'en':'Climb the ladder.','choices':['사다리 올라','계단 올라','산 올라','지붕 올라'],'ans':0,'hint':('ladder','사다리'),'explain':'ladder = 사다리'},
            {'en':'Tie with rope.','choices':['밧줄로 묶어','실로 묶어','종이로 묶어','테이프로 묶어'],'ans':0,'hint':('rope','밧줄'),'explain':'rope = 밧줄'},
            {'en':'Flip the switch.','choices':['스위치 켜','문 열어','책 봐','자'],'ans':0,'hint':('switch','스위치'),'explain':'switch = 스위치'},
            {'en':'Connect the wire.','choices':['전선 연결','전선 끊어','전선 봐','전선 사'],'ans':0,'hint':('wire','전선'),'explain':'wire = 전선'},
            {'en':'A small motor.','choices':['작은 모터','큰 모터','새 모터','오래된 모터'],'ans':0,'hint':('motor','모터'),'explain':'motor = 모터'},
            {'en':'Turn the gear.','choices':['기어 돌려','기어 봐','기어 사','기어 던져'],'ans':0,'hint':('gear','기어'),'explain':'gear = 톱니바퀴'},
            {'en':'Use a screwdriver.','choices':['드라이버 써','망치 써','칼 써','연필 써'],'ans':0,'hint':('screwdriver','드라이버'),'explain':'screwdriver = 드라이버'},
            {'en':'Pull the lever.','choices':['레버 당겨','레버 봐','레버 사','레버 던져'],'ans':0,'hint':('lever','레버'),'explain':'lever = 레버'},
            {'en':'Electric circuit.','choices':['전기 회로','전기 끊기','전기 봐','전기 사'],'ans':0,'hint':('circuit','회로'),'explain':'circuit = 회로'},
            {'en':'A real genius!','choices':['진짜 천재!','진짜 바보!','진짜 새 거!','진짜 오래!'],'ans':0,'hint':('genius','천재'),'explain':'genius = 천재'},
            {'en':'Use the machine.','choices':['기계 써','음식 써','책 써','옷 써'],'ans':0,'hint':('machine','기계'),'explain':'machine = 기계'},
        ]
    },

    '20260701': {
        'date':'2026-07-01','day_ko':'수','theme':'역사·왕국','theme_emoji':'🏛️','description':'역사 영어!',
        'questions':[
            {'en':'Learn history.','choices':['역사 배워','수학 배워','과학 배워','음악 배워'],'ans':0,'hint':('history','역사'),'explain':'history = 역사'},
            {'en':'Ancient Egypt.','choices':['고대 이집트','현대 이집트','새 이집트','오래된 이집트'],'ans':0,'hint':('ancient','고대'),'explain':'ancient = 고대'},
            {'en':'Modern city.','choices':['현대 도시','옛 도시','새 도시','오래된 도시'],'ans':0,'hint':('modern','현대'),'explain':'modern = 현대'},
            {'en':'A great king.','choices':['위대한 왕','어린 왕','약한 왕','조용한 왕'],'ans':0,'hint':('king','왕'),'explain':'king = 왕'},
            {'en':'The queen smiles.','choices':['여왕이 웃어','왕이 웃어','왕자가 웃어','공주가 웃어'],'ans':0,'hint':('queen','여왕'),'explain':'queen = 여왕'},
            {'en':'Roman emperor.','choices':['로마 황제','중국 황제','일본 황제','한국 황제'],'ans':0,'hint':('emperor','황제'),'explain':'emperor = 황제'},
            {'en':'A long war.','choices':['긴 전쟁','짧은 전쟁','새 전쟁','옛 전쟁'],'ans':0,'hint':('war','전쟁'),'explain':'war = 전쟁'},
            {'en':'World peace!','choices':['세계 평화!','세계 전쟁!','세계 끝!','세계 시작!'],'ans':0,'hint':('peace','평화'),'explain':'peace = 평화'},
            {'en':'Brave soldiers.','choices':['용감한 군인','약한 군인','새 군인','오래된 군인'],'ans':0,'hint':('soldier','군인'),'explain':'soldier = 군인'},
            {'en':'A sharp sword.','choices':['날카로운 검','무딘 검','새 검','오래된 검'],'ans':0,'hint':('sword','검'),'explain':'sword = 칼·검'},
            {'en':'Hold a shield.','choices':['방패 들어','책 들어','검 들어','꽃 들어'],'ans':0,'hint':('shield','방패'),'explain':'shield = 방패'},
            {'en':'Wear armor.','choices':['갑옷 입어','옷 입어','신발 신어','모자 써'],'ans':0,'hint':('armor','갑옷'),'explain':'armor = 갑옷'},
            {'en':'Raise the flag.','choices':['깃발 올려','깃발 내려','깃발 봐','깃발 사'],'ans':0,'hint':('flag','깃발'),'explain':'flag = 깃발'},
            {'en':'A golden crown.','choices':['금 왕관','은 왕관','새 왕관','오래된 왕관'],'ans':0,'hint':('crown','왕관'),'explain':'crown = 왕관'},
            {'en':'Sit on the throne.','choices':['왕좌에 앉아','의자에 앉아','땅에 앉아','풀에 앉아'],'ans':0,'hint':('throne','왕좌'),'explain':'throne = 왕좌'},
            {'en':'Ancient empire.','choices':['고대 제국','현대 제국','새 제국','조용한 제국'],'ans':0,'hint':('empire','제국'),'explain':'empire = 제국'},
            {'en':'An old tomb.','choices':['오래된 무덤','새 무덤','큰 무덤','작은 무덤'],'ans':0,'hint':('tomb','무덤'),'explain':'tomb = 무덤'},
            {'en':'Visit the pyramid.','choices':['피라미드 방문','학교 방문','마트 방문','집 방문'],'ans':0,'hint':('pyramid','피라미드'),'explain':'pyramid = 피라미드'},
            {'en':'A strong warrior.','choices':['강한 전사','약한 전사','새 전사','오래된 전사'],'ans':0,'hint':('warrior','전사'),'explain':'warrior = 전사'},
            {'en':'An old legend.','choices':['오래된 전설','새 전설','짧은 전설','긴 전설'],'ans':0,'hint':('legend','전설'),'explain':'legend = 전설'},
        ]
    },

    '20260702': {
        'date':'2026-07-02','day_ko':'목','theme':'감각·맛','theme_emoji':'👃','description':'느낌·맛 영어!',
        'questions':[
            {'en':"Don't touch!",'choices':['만지지마!','자!','먹지마!','달리지마!'],'ans':0,'hint':('touch','만지다'),'explain':'touch = 만지기'},
            {'en':'A good taste.','choices':['좋은 맛','나쁜 맛','새 맛','오래된 맛'],'ans':0,'hint':('taste','맛'),'explain':'taste = 맛'},
            {'en':'A nice smell.','choices':['좋은 냄새','나쁜 냄새','새 냄새','오래된 냄새'],'ans':0,'hint':('smell','냄새'),'explain':'smell = 냄새'},
            {'en':'I hear music.','choices':['음악 들려','음악 안 들려','음악 사','음악 봐'],'ans':0,'hint':('hear','듣다'),'explain':'hear = 듣다'},
            {'en':'I see a bird.','choices':['새 보여','새 안 보여','새 사','새 들어'],'ans':0,'hint':('see','보다'),'explain':'see = 보다'},
            {'en':'Silky hair!','choices':['비단같은 머리!','거친 머리!','새 머리!','오래된 머리!'],'ans':0,'hint':('silky','비단같은'),'explain':'silky = 비단같은'},
            {'en':'A firm grip.','choices':['단단한 잡기','약한 잡기','새 잡기','오래된 잡기'],'ans':0,'hint':('firm','단단한'),'explain':'firm = 단단한'},
            {'en':'Glossy paper.','choices':['반짝이는 종이','거친 종이','새 종이','오래된 종이'],'ans':0,'hint':('glossy','반짝이는'),'explain':'glossy = 광택있는'},
            {'en':'Prickly cactus!','choices':['따끔한 선인장!','부드러운 선인장!','새 선인장!','오래된 선인장!'],'ans':0,'hint':('prickly','따끔한'),'explain':'prickly = 가시같은'},
            {'en':'Sticky honey.','choices':['끈적한 꿀','단 꿀','쓴 꿀','짠 꿀'],'ans':0,'hint':('sticky','끈적한'),'explain':'sticky = 끈적'},
            {'en':'Creamy yogurt.','choices':['크리미한 요거트','거친 요거트','새 요거트','오래된 요거트'],'ans':0,'hint':('creamy','크리미'),'explain':'creamy = 크리미'},
            {'en':'Tangy lemon!','choices':['톡 쏘는 레몬!','단 레몬!','쓴 레몬!','짠 레몬!'],'ans':0,'hint':('tangy','톡쏘는'),'explain':'tangy = 톡 쏘는'},
            {'en':'Plain rice.','choices':['담백한 밥','달콤한 밥','매운 밥','짠 밥'],'ans':0,'hint':('plain','담백한'),'explain':'plain = 담백한'},
            {'en':'Savory snacks.','choices':['짭짤한 간식','달콤 간식','쓴 간식','매운 간식'],'ans':0,'hint':('savory','짭짤'),'explain':'savory = 고소·짭짤'},
            {'en':'Juicy peach.','choices':['즙많은 복숭아','마른 복숭아','오래된 복숭아','새 복숭아'],'ans':0,'hint':('juicy','즙많은'),'explain':'juicy = 수분 가득'},
            {'en':'Flower fragrance.','choices':['꽃 향기','꽃 색','꽃 크기','꽃 이름'],'ans':0,'hint':('fragrance','향기'),'explain':'fragrance = 좋은 향기'},
            {'en':'Stinky socks!','choices':['고약 양말!','새 양말!','예쁜 양말!','파란 양말!'],'ans':0,'hint':('stinky','고약한'),'explain':'stinky = 냄새 나는'},
            {'en':'A silent room.','choices':['조용한 방','시끄러운 방','새 방','오래된 방'],'ans':0,'hint':('silent','조용한'),'explain':'silent = 조용한'},
            {'en':'Hear the echo!','choices':['메아리 들려!','노래 들려!','책 봐!','자!'],'ans':0,'hint':('echo','메아리'),'explain':'echo = 메아리'},
            {'en':'Five senses.','choices':['오감','이감','삼감','육감'],'ans':0,'hint':('sense','감각'),'explain':'5 senses = 오감'},
        ]
    },

    '20260703': {
        'date':'2026-07-03','day_ko':'금','theme':'꿈·미래','theme_emoji':'🌟','description':'꿈·미래 영어!',
        'questions':[
            {'en':'Have a vision.','choices':['비전 가져','꿈 잊어','책 봐','자'],'ans':0,'hint':('vision','비전'),'explain':'vision = 꿈·비전'},
            {'en':'I have hope.','choices':['희망 있어','희망 없어','희망 사','희망 봐'],'ans':0,'hint':('hope','희망'),'explain':'hope = 희망'},
            {'en':'Make a wish... a deep desire.','choices':['깊은 바람','짧은 바람','새 바람','오래 바람'],'ans':0,'hint':('desire','바람'),'explain':'desire = 강한 바람'},
            {'en':'Make a plan.','choices':['계획 세워','선물 사','자','놀아'],'ans':0,'hint':('plan','계획'),'explain':'plan = 계획'},
            {'en':'Hit the target.','choices':['목표 맞춰','공 차','책 봐','자'],'ans':0,'hint':('target','목표'),'explain':'target = 목표'},
            {'en':'Make an attempt.','choices':['시도해 봐','자','놀아','먹어'],'ans':0,'hint':('attempt','시도'),'explain':'attempt = 시도'},
            {'en':'Succeed in life.','choices':['인생 성공','인생 실패','인생 끝','인생 시작'],'ans':0,'hint':('succeed','성공'),'explain':'succeed = 성공하다'},
            {'en':'Big success!','choices':['큰 성공!','큰 실패!','새 시작!','오래된 일!'],'ans':0,'hint':('success','성공'),'explain':'success = 성공'},
            {'en':'Try your best!','choices':['최선 다해!','쉬어!','자!','놀아!'],'ans':1 if False else 0,'hint':('try','노력'),'explain':'try = 노력'},
            {'en':'Believe in yourself.','choices':['자신 믿어','자신 싫어','자신 봐','자신 사'],'ans':0,'hint':('believe','믿다'),'explain':'believe = 믿다'},
            {'en':"Don't daydream!",'choices':['멍 때리지마!','자지마!','먹지마!','가지마!'],'ans':0,'hint':('daydream','백일몽'),'explain':'daydream = 망상'},
            {'en':'You inspire me!','choices':['너 덕에 힘나!','너 미워!','너 자!','너 가!'],'ans':0,'hint':('inspire','영감'),'explain':'inspire = 영감 주다'},
            {'en':'A big ambition.','choices':['큰 포부','작은 포부','새 포부','오래 포부'],'ans':0,'hint':('ambition','포부'),'explain':'ambition = 야망'},
            {'en':'A clever idea.','choices':['영리한 생각','나쁜 생각','새 생각','오래 생각'],'ans':0,'hint':('clever','영리한'),'explain':'clever = 영리'},
            {'en':'Originate here.','choices':['여기서 시작','여기서 끝','여기서 자','여기서 가'],'ans':0,'hint':('originate','시작'),'explain':'originate = 시작·비롯'},
            {'en':'Design a plan.','choices':['계획 설계','계획 봐','계획 사','계획 잊어'],'ans':0,'hint':('design','설계'),'explain':'design = 설계'},
            {'en':'Accomplish goals!','choices':['목표 완수!','목표 잊어!','목표 봐!','목표 사!'],'ans':0,'hint':('accomplish','완수'),'explain':'accomplish = 해내다'},
            {'en':'Plants grow tall.','choices':['식물 크게 자라','식물 작아져','식물 봐','식물 사'],'ans':0,'hint':('grow','자라다'),'explain':'grow = 자라다'},
            {'en':'Have courage!','choices':['용기 가져!','약해져!','자!','놀아!'],'ans':0,'hint':('courage','용기'),'explain':'courage = 용기'},
            {'en':'A bright prospect!','choices':['밝은 전망!','어두운 전망!','새 전망!','오래된 전망!'],'ans':0,'hint':('prospect','전망'),'explain':'prospect = 전망'},
        ]
    },

    '20260704': {
        'date':'2026-07-04','day_ko':'토','theme':'운전·교통','theme_emoji':'🚗','description':'길거리·이동 영어!',
        'questions':[
            {'en':'Turn left.','choices':['왼쪽 돌아','오른쪽 돌아','직진','뒤로'],'ans':0,'hint':('left','왼쪽'),'explain':'left = 왼쪽'},
            {'en':'Turn right.','choices':['오른쪽 돌아','왼쪽 돌아','직진','뒤로'],'ans':0,'hint':('right','오른쪽'),'explain':'right = 오른쪽'},
            {'en':'Go straight.','choices':['직진','왼쪽','오른쪽','뒤로'],'ans':0,'hint':('straight','직진'),'explain':'straight = 똑바로'},
            {'en':'Stop here.','choices':['여기 멈춰','계속 가','뒤로 가','자'],'ans':0,'hint':('stop','멈추다'),'explain':'stop = 멈추다'},
            {'en':"It's a red light.",'choices':['빨간 불','초록 불','노란 불','파란 불'],'ans':0,'hint':('red','빨강'),'explain':'red light = 빨간불'},
            {'en':"It's a green light.",'choices':['초록 불','빨간 불','노란 불','파란 불'],'ans':0,'hint':('green','초록'),'explain':'green light = 초록불'},
            {'en':'Slow down.','choices':['속도 줄여','빨리 가','자','뒤로'],'ans':0,'hint':('slow','느린'),'explain':'slow down = 천천히'},
            {'en':'Speed up!','choices':['속도 올려!','속도 줄여!','자!','놀아!'],'ans':0,'hint':('speed','속도'),'explain':'speed up = 빨리'},
            {'en':'Fasten your seatbelt.','choices':['안전벨트 매','옷 입어','신발 신어','모자 써'],'ans':0,'hint':('seatbelt','안전벨트'),'explain':'seatbelt = 안전벨트'},
            {'en':'Take the bus.','choices':['버스 타','걸어가','자전거 타','뛰어가'],'ans':0,'hint':('bus','버스'),'explain':'take = 타다'},
            {'en':'Get off at the next stop.','choices':['다음 정거장 내려','다음 정거장 가','다음 정거장 자','다음 정거장 봐'],'ans':0,'hint':('get off','내리다'),'explain':'get off = 내리기'},
            {'en':'Buy a ticket.','choices':['표 사','책 사','옷 사','음식 사'],'ans':0,'hint':('ticket','표'),'explain':'ticket = 표'},
            {'en':'Cross the road.','choices':['길 건너','길 가','길 봐','길 사'],'ans':0,'hint':('cross','건너다'),'explain':'cross = 건너다'},
            {'en':'Wait at the crosswalk.','choices':['횡단보도 기다려','학교 기다려','집 기다려','자'],'ans':0,'hint':('crosswalk','횡단보도'),'explain':'crosswalk = 횡단보도'},
            {'en':'Hold the handle.','choices':['손잡이 잡아','책 잡아','옷 잡아','음식 잡아'],'ans':0,'hint':('handle','손잡이'),'explain':'handle = 손잡이'},
            {'en':'Push the button.','choices':['버튼 눌러','버튼 봐','버튼 사','버튼 던져'],'ans':0,'hint':('push','누르다'),'explain':'push = 밀다·누르다'},
            {'en':'How far?','choices':['얼마나 멀어?','얼마나 비싸?','얼마나 좋아?','얼마나 새?'],'ans':0,'hint':('far','먼'),'explain':'how far = 얼마 멀리'},
            {'en':'How long does it take?','choices':['얼마나 걸려?','얼마나 비싸?','얼마나 새?','얼마나 좋아?'],'ans':0,'hint':('how long','얼마나'),'explain':'how long = 얼마나 (시간)'},
            {'en':"It's not far.",'choices':['멀지 않아','매우 멀어','새 거','오래된 거'],'ans':0,'hint':('far','먼'),'explain':"not far = 가깝다"},
            {'en':'Have a safe trip!','choices':['안전 여행!','즐거운 여행!','짧은 여행!','새 여행!'],'ans':0,'hint':('safe','안전한'),'explain':'safe trip = 안전 여행'},
        ]
    },

    '20260705': {
        'date':'2026-07-05','day_ko':'일','theme':'한 주 마무리','theme_emoji':'🌅','description':'주말 마무리 영어!',
        'questions':[
            {'en':'What a great week!','choices':['멋진 한 주!','피곤한 한 주!','지루한 한 주!','짧은 한 주!'],'ans':0,'hint':('great','멋진'),'explain':'great week = 멋진 한 주'},
            {'en':'I had so much fun!','choices':['너무 재밌었어!','너무 슬펐어!','너무 추웠어!','너무 졸렸어!'],'ans':0,'hint':('fun','재미'),'explain':'had fun = 재밌었다'},
            {'en':"Let's relax.",'choices':['쉬자','일하자','자자','달리자'],'ans':0,'hint':('relax','쉬다'),'explain':'relax = 쉬다'},
            {'en':'A peaceful Sunday.','choices':['평화로운 일요일','바쁜 일요일','시끄러운 일요일','슬픈 일요일'],'ans':0,'hint':('peaceful','평화로운'),'explain':'peaceful = 평화'},
            {'en':'Sleep in.','choices':['늦잠 자','일찍 일어나','자지마','놀아'],'ans':0,'hint':('sleep in','늦잠'),'explain':'sleep in = 늦잠'},
            {'en':'Plan for next week.','choices':['다음 주 계획','지난 주 봐','자','놀아'],'ans':0,'hint':('plan','계획'),'explain':'plan for = ~ 계획'},
            {'en':'See you next week!','choices':['다음 주 봐!','내일 봐!','지금 봐!','어제 봤어!'],'ans':0,'hint':('next','다음'),'explain':'next week = 다음 주'},
            {'en':"I'm tired.",'choices':['피곤해','신나','즐거워','졸려'],'ans':0,'hint':('tired','피곤'),'explain':'tired = 피곤'},
            {'en':'Get some rest.',  'choices':['좀 쉬어','좀 자','좀 가','좀 먹어'],'ans':0,'hint':('rest','쉬다'),'explain':'get rest = 쉬기'},
            {'en':'A new week starts.','choices':['새 한 주 시작','옛 한 주 끝','자고 있어','지나갔어'],'ans':0,'hint':('start','시작'),'explain':'start = 시작'},
            {'en':"I'm ready.",'choices':['준비됐어','준비 안됐어','자','놀아'],'ans':0,'hint':('ready','준비'),'explain':'ready = 준비된'},
            {'en':"Let's review.",'choices':['복습하자','자자','놀자','먹자'],'ans':0,'hint':('review','복습'),'explain':'review = 복습'},
            {'en':'I learned a lot!','choices':['많이 배웠어!','적게 배웠어!','안 배웠어!','잊었어!'],'ans':0,'hint':('learn','배우다'),'explain':'learned a lot = 많이 배움'},
            {'en':"I'm proud of you.",'choices':['네가 자랑스러워','네가 싫어','네가 슬퍼','네가 자'],'ans':0,'hint':('proud','자랑스러운'),'explain':'proud = 자랑스러운'},
            {'en':'Well done!','choices':['잘했어!','못했어!','자!','놀아!'],'ans':0,'hint':('well done','잘했어'),'explain':'well done = 잘했어'},
            {'en':"Keep it up!",'choices':['계속해!','그만해!','자!','놀아!'],'ans':0,'hint':('keep','계속'),'explain':'keep it up = 계속!'},
            {'en':'You did great.','choices':['잘했어','못했어','자','갔어'],'ans':0,'hint':('great','멋진'),'explain':'did great = 잘했어'},
            {'en':"Let's do this again!",'choices':['또 하자!','그만!','자!','가!'],'ans':0,'hint':('again','다시'),'explain':'again = 다시'},
            {'en':"You're awesome!",'choices':['넌 멋져!','넌 별로!','넌 자!','넌 가!'],'ans':0,'hint':('awesome','멋진'),'explain':'awesome = 끝내주는'},
            {'en':'See you tomorrow!','choices':['내일 봐!','어제 봤어!','지금 봐!','다음에 봐!'],'ans':0,'hint':('tomorrow','내일'),'explain':'tomorrow = 내일'},
        ]
    },

    # ═════════════════════════════════════════════
    # 7/6~7/12 (Week 12) - 성격·학교·소통·곤충·취미
    # ═════════════════════════════════════════════
    '20260706': {
        'date':'2026-07-06','day_ko':'월','theme':'성격 표현','theme_emoji':'🎭','description':'성격 표현 영어!',
        'questions':[
            {'en':'A sincere smile.','choices':['진실한 미소','거짓 미소','새 미소','오래된 미소'],'ans':0,'hint':('sincere','진실한'),'explain':'sincere = 진실한'},
            {'en':"Be courteous.",'choices':['공손하게','무례하게','조용히','크게'],'ans':0,'hint':('courteous','공손한'),'explain':'courteous = 매우 예의'},
            {'en':'A wise choice.','choices':['현명한 선택','나쁜 선택','새 선택','없는 선택'],'ans':0,'hint':('wise','현명한'),'explain':'wise = 지혜로움'},
            {'en':"Don't be rude.",'choices':['무례 마','자지 마','오지 마','가지 마'],'ans':0,'hint':('rude','무례'),'explain':'rude = 예의 없음'},
            {'en':"I'm sleepy.",'choices':['졸려','신나','즐거워','피곤'],'ans':0,'hint':('sleepy','졸린'),'explain':'sleepy = 졸린'},
            {'en':'A diligent student.','choices':['부지런한 학생','게으른 학생','새 학생','조용한 학생'],'ans':0,'hint':('diligent','부지런한'),'explain':'diligent = 부지런'},
            {'en':"Don't be selfish.",'choices':['이기적이지 마','자지 마','오지 마','웃지 마'],'ans':0,'hint':('selfish','이기적'),'explain':'selfish = 자기만'},
            {'en':"A warmhearted teacher.",'choices':['따뜻한 선생님','차가운 선생님','새 선생님','오래된 선생님'],'ans':0,'hint':('warmhearted','따뜻한'),'explain':'warmhearted = 마음 따뜻'},
            {'en':'A thoughtful gift.','choices':['사려 깊은 선물','싼 선물','새 선물','큰 선물'],'ans':0,'hint':('thoughtful','사려깊은'),'explain':'thoughtful = 마음 써줌'},
            {'en':'A gentle touch.','choices':['부드러운 손길','강한 손길','새 손길','오래된 손길'],'ans':0,'hint':('gentle','부드러운'),'explain':'gentle = 살살'},
            {'en':"He is humble.",'choices':['그는 겸손해','그는 자만해','그는 졸려','그는 화났어'],'ans':0,'hint':('humble','겸손'),'explain':'humble = 잘난 척 안 함'},
            {'en':"I'm proud of you.",'choices':['네가 자랑스러워','네가 싫어','네가 졸려','네가 미워'],'ans':0,'hint':('proud','자랑'),'explain':'proud = 자랑스러움'},
            {'en':'A witty joke.','choices':['재치 있는 농담','지루한 농담','새 농담','오래된 농담'],'ans':0,'hint':('witty','재치'),'explain':'witty = 센스 있음'},
            {'en':'A talented kid.','choices':['재능 있는 아이','평범한 아이','새 아이','오래된 아이'],'ans':0,'hint':('talented','재능있는'),'explain':'talented = 재능'},
            {'en':"An optimistic view.",'choices':['낙천적 시각','어두운 시각','새 시각','없는 시각'],'ans':0,'hint':('optimistic','낙천적'),'explain':'optimistic = 긍정'},
            {'en':"A mischievous kid!",'choices':['장난꾸러기!','조용한 아이!','새 아이!','잘 자는 아이!'],'ans':0,'hint':('mischievous','장난꾸러기'),'explain':'mischievous = 개구쟁이'},
            {'en':'A loyal friend.','choices':['충실한 친구','배신한 친구','새 친구','오래된 친구'],'ans':0,'hint':('loyal','충실'),'explain':'loyal = 의리'},
            {'en':"A bossy sister.",'choices':['대장 행세 언니','조용한 언니','새 언니','어린 언니'],'ans':0,'hint':('bossy','대장'),'explain':'bossy = 명령 많음'},
            {'en':'A reliable friend.','choices':['믿음직한 친구','오래된 친구','새 친구','조용한 친구'],'ans':0,'hint':('reliable','믿음직'),'explain':'reliable = 의지 가능'},
            {'en':"An inquisitive child.",'choices':['궁금해 하는 아이','조용한 아이','새 아이','잘 자는 아이'],'ans':0,'hint':('inquisitive','궁금'),'explain':'inquisitive = 호기심'},
        ]
    },

    '20260707': {
        'date':'2026-07-07','day_ko':'화','theme':'학교생활 표현','theme_emoji':'📚','description':'학교 활동 영어!',
        'questions':[
            {'en':"What's your favorite subject?",'choices':['좋아하는 과목?','이름?','시간?','어디?'],'ans':0,'hint':('subject','과목'),'explain':'subject = 과목'},
            {'en':"I love math.",'choices':['수학 좋아','과학 좋아','국어 좋아','영어 좋아'],'ans':0,'hint':('math','수학'),'explain':'math = 수학'},
            {'en':'Science is fun!','choices':['과학 재밌어!','수학 재밌어!','체육 재밌어!','음악 재밌어!'],'ans':0,'hint':('science','과학'),'explain':'science = 과학'},
            {'en':'Chemistry class today.','choices':['오늘 화학 시간','오늘 음악 시간','오늘 체육 시간','오늘 국어 시간'],'ans':0,'hint':('chemistry','화학'),'explain':'chemistry = 화학'},
            {'en':'Geography lesson.','choices':['지리 수업','음악 수업','국어 수업','수학 수업'],'ans':0,'hint':('geography','지리'),'explain':'geography = 지리'},
            {'en':'PE class is fun!','choices':['체육 재밌어!','수학 재밌어!','과학 재밌어!','음악 재밌어!'],'ans':0,'hint':('PE','체육'),'explain':'PE = 체육'},
            {'en':"It's recess time!",'choices':['쉬는 시간!','수업 시간!','집 갈 시간!','잘 시간!'],'ans':0,'hint':('recess','쉬는시간'),'explain':'recess = 쉬는 시간'},
            {'en':'Finish the assignment.','choices':['과제 끝내','자','놀아','먹어'],'ans':0,'hint':('assignment','과제'),'explain':'assignment = 과제'},
            {'en':'Give a presentation.','choices':['발표해','자','놀아','먹어'],'ans':0,'hint':('presentation','발표'),'explain':'presentation = 발표'},
            {'en':'A math workbook.','choices':['수학 문제집','수학 책','수학 시험','수학 노트'],'ans':0,'hint':('workbook','문제집'),'explain':'workbook = 문제집'},
            {'en':'Class discussion.','choices':['수업 토론','수업 자기','수업 놀기','수업 먹기'],'ans':0,'hint':('discussion','토론'),'explain':'discussion = 토론'},
            {'en':'A book report.','choices':['독후감','책 사기','책 던지기','책 자기'],'ans':0,'hint':('report','보고서'),'explain':'report = 보고서'},
            {'en':'Talk to the counselor.','choices':['상담사 만나','선생님 만나','친구 만나','부모님 만나'],'ans':0,'hint':('counselor','상담사'),'explain':'counselor = 상담사'},
            {'en':"Don't be tardy!",'choices':['지각 마!','자지 마!','오지 마!','가지 마!'],'ans':0,'hint':('tardy','지각'),'explain':'tardy = 늦은'},
            {'en':'Fun fieldtrip!','choices':['재밌는 체험학습!','지루한 시험!','새 학교!','오래된 책!'],'ans':0,'hint':('fieldtrip','체험'),'explain':'fieldtrip = 현장학습'},
            {'en':'In the auditorium.','choices':['강당에서','교실에서','집에서','시장에서'],'ans':0,'hint':('auditorium','강당'),'explain':'auditorium = 강당'},
            {'en':'Write in a diary.','choices':['일기 써','책 봐','자','놀아'],'ans':0,'hint':('diary','일기'),'explain':'diary = 일기'},
            {'en':'Write an essay.','choices':['글 쓰기','책 읽기','자기','놀기'],'ans':0,'hint':('essay','글'),'explain':'essay = 작문'},
            {'en':'Fifth grade!','choices':['5학년!','3학년!','7학년!','없음!'],'ans':0,'hint':('grade','학년'),'explain':'grade = 학년'},
            {'en':'Take attendance.','choices':['출석 확인','시험 봐','자','먹어'],'ans':0,'hint':('attendance','출석'),'explain':'attendance = 출석'},
        ]
    },

    '20260708': {
        'date':'2026-07-08','day_ko':'수','theme':'소통·대화','theme_emoji':'✉️','description':'소통 영어 표현!',
        'questions':[
            {'en':'Write a letter.','choices':['편지 써','일기 써','책 사','노래 불러'],'ans':0,'hint':('letter','편지'),'explain':'letter = 편지'},
            {'en':'Seal the envelope.','choices':['봉투 봉해','책 닫아','문 닫아','자'],'ans':0,'hint':('envelope','봉투'),'explain':'envelope = 봉투'},
            {'en':'Send a postcard.','choices':['엽서 보내','책 보내','선물 보내','꽃 보내'],'ans':0,'hint':('postcard','엽서'),'explain':'postcard = 엽서'},
            {'en':'Your signature here.','choices':['여기 서명해','여기 자','여기 가','여기 봐'],'ans':0,'hint':('signature','서명'),'explain':'signature = 사인'},
            {'en':'Send a message.','choices':['메시지 보내','선물 보내','책 보내','노래 보내'],'ans':0,'hint':('message','메시지'),'explain':'message = 메시지'},
            {'en':'Text me later.','choices':['나중에 문자','지금 봐','내일 가','어제 했어'],'ans':0,'hint':('text','문자'),'explain':'text = 문자하다'},
            {'en':'Call your mom.','choices':['엄마에게 전화','엄마 만나','엄마 안아','엄마 자'],'ans':0,'hint':('call','전화'),'explain':'call = 전화'},
            {'en':'Send a reply.','choices':['답장 보내','답장 받아','답장 봐','답장 사'],'ans':0,'hint':('reply','답장'),'explain':'reply = 답장'},
            {'en':"Let's chat.",'choices':['수다 떨자','자자','먹자','가자'],'ans':0,'hint':('chat','수다'),'explain':'chat = 채팅'},
            {'en':'Talk to me.','choices':['나에게 말해','나에게 와','나에게 자','나에게 가'],'ans':0,'hint':('talk','말하다'),'explain':'talk = 이야기'},
            {'en':'Whisper softly.','choices':['조용히 속삭여','크게 말해','자','노래해'],'ans':0,'hint':('whisper','속삭임'),'explain':'whisper = 속삭이기'},
            {'en':"Don't shout!",'choices':['소리치지 마!','자지 마!','오지 마!','가지 마!'],'ans':0,'hint':('shout','외치다'),'explain':'shout = 소리치기'},
            {'en':'A pretty voice.','choices':['예쁜 목소리','예쁜 옷','예쁜 책','예쁜 가방'],'ans':0,'hint':('voice','목소리'),'explain':'voice = 목소리'},
            {'en':'Many languages.','choices':['많은 언어','많은 책','많은 음식','많은 옷'],'ans':0,'hint':('language','언어'),'explain':'language = 언어'},
            {'en':'Stop sign.','choices':['정지 표지','정지 책','정지 음식','정지 옷'],'ans':0,'hint':('sign','표지'),'explain':'sign = 신호'},
            {'en':'A friendly gesture.','choices':['친근 몸짓','무서운 몸짓','새 몸짓','오래된 몸짓'],'ans':0,'hint':('gesture','몸짓'),'explain':'gesture = 손짓'},
            {'en':'Express your feelings.','choices':['감정 표현해','감정 숨겨','감정 사','감정 잊어'],'ans':0,'hint':('express','표현'),'explain':'express = 표현하다'},
            {'en':"Don't mumble!",'choices':['중얼거리지 마!','자지 마!','노래 마!','놀지 마!'],'ans':0,'hint':('mumble','중얼'),'explain':'mumble = 우물우물'},
            {'en':'A good listener.','choices':['좋은 청자','나쁜 친구','새 학생','오래된 책'],'ans':0,'hint':('listener','듣는 사람'),'explain':'listener = 청자'},
            {'en':'Speak slowly.','choices':['천천히 말해','빨리 자','빨리 가','빨리 먹어'],'ans':0,'hint':('speak','말하다'),'explain':'speak = 말하기'},
        ]
    },

    '20260709': {
        'date':'2026-07-09','day_ko':'목','theme':'곤충·작은 생물','theme_emoji':'🐝','description':'벌레 영어!',
        'questions':[
            {'en':'A tiny ant.','choices':['작은 개미','큰 개미','새 개미','오래된 개미'],'ans':0,'hint':('ant','개미'),'explain':'ant = 개미'},
            {'en':'A red ladybug.','choices':['빨간 무당벌레','파란 새','새 모자','오래된 책'],'ans':0,'hint':('ladybug','무당벌레'),'explain':'ladybug = 무당벌레'},
            {'en':"Spider's web.",'choices':['거미줄','책 표지','옷 줄','벌집'],'ans':0,'hint':('web','거미줄'),'explain':'web = 거미줄'},
            {'en':'A green caterpillar.','choices':['초록 애벌레','초록 개구리','초록 풀','초록 잎'],'ans':0,'hint':('caterpillar','애벌레'),'explain':'caterpillar = 애벌레'},
            {'en':'In the cocoon.','choices':['고치 안에서','집 안에서','학교 안에서','상자 안에서'],'ans':0,'hint':('cocoon','고치'),'explain':'cocoon = 고치'},
            {'en':'A big ant hill.','choices':['큰 개미집','큰 산','큰 집','큰 들판'],'ans':0,'hint':('ant hill','개미집'),'explain':'ant hill = 개미 동네'},
            {'en':'Honey from beehive.','choices':['벌집의 꿀','벌집의 빵','벌집의 우유','벌집의 물'],'ans':0,'hint':('beehive','벌집'),'explain':'beehive = 벌의 집'},
            {'en':'Sweet honey!','choices':['달콤한 꿀!','달콤한 빵!','달콤한 케이크!','달콤한 사탕!'],'ans':0,'hint':('honey','꿀'),'explain':'honey = 꿀'},
            {'en':'Pretty fireflies.','choices':['예쁜 반딧불','예쁜 나비','예쁜 별','예쁜 꽃'],'ans':0,'hint':('firefly','반딧불'),'explain':'firefly = 반딧불이'},
            {'en':'A slow snail.','choices':['느린 달팽이','빠른 토끼','느린 거북이','빠른 새'],'ans':0,'hint':('snail','달팽이'),'explain':'snail = 달팽이'},
            {'en':'A wet slug.','choices':['축축한 민달팽이','축축한 풀','축축한 흙','축축한 잎'],'ans':0,'hint':('slug','민달팽이'),'explain':'slug = 민달팽이'},
            {'en':'A long worm.','choices':['긴 지렁이','긴 뱀','긴 줄','긴 머리'],'ans':0,'hint':('worm','지렁이'),'explain':'worm = 지렁이'},
            {'en':'A black beetle.','choices':['검은 딱정벌레','검은 개구리','검은 새','검은 강아지'],'ans':0,'hint':('beetle','딱정벌레'),'explain':'beetle = 딱정벌레'},
            {'en':'A jumping grasshopper.','choices':['뛰는 메뚜기','뛰는 강아지','뛰는 새','뛰는 아이'],'ans':0,'hint':('grasshopper','메뚜기'),'explain':'grasshopper = 메뚜기'},
            {'en':'Cricket sounds.','choices':['귀뚜라미 소리','새 소리','강아지 소리','종소리'],'ans':0,'hint':('cricket','귀뚜라미'),'explain':'cricket = 귀뚜라미'},
            {'en':'A buzzing mosquito.','choices':['윙윙 모기','윙윙 벌','윙윙 파리','윙윙 새'],'ans':0,'hint':('mosquito','모기'),'explain':'mosquito = 모기'},
            {'en':'A red dragonfly.','choices':['빨간 잠자리','빨간 나비','빨간 새','빨간 풍선'],'ans':0,'hint':('dragonfly','잠자리'),'explain':'dragonfly = 잠자리'},
            {'en':'A night moth.','choices':['밤 나방','밤 별','밤 달','밤 새'],'ans':0,'hint':('moth','나방'),'explain':'moth = 나방'},
            {'en':'Pretty wings.','choices':['예쁜 날개','예쁜 다리','예쁜 머리','예쁜 옷'],'ans':0,'hint':('wing','날개'),'explain':'wing = 날개'},
            {'en':'Bees make honey.','choices':['벌이 꿀 만들어','새가 꿀 만들어','개미가 꿀 만들어','다 만들어'],'ans':0,'hint':('bee','벌'),'explain':'bee = 벌'},
        ]
    },

    '20260710': {
        'date':'2026-07-10','day_ko':'금','theme':'취미·여가','theme_emoji':'🎯','description':'취미 영어 표현!',
        'questions':[
            {'en':"What's your hobby?",'choices':['취미 뭐?','이름 뭐?','시간 몇?','어디 가?'],'ans':0,'hint':('hobby','취미'),'explain':'hobby = 취미'},
            {'en':'I collect stamps.','choices':['우표 수집','책 수집','신발 수집','옷 수집'],'ans':0,'hint':('collect','수집'),'explain':'collect = 모으다'},
            {'en':'A coin collection.','choices':['동전 수집','책 수집','음식 수집','옷 수집'],'ans':0,'hint':('collection','수집품'),'explain':'collection = 모은 것'},
            {'en':'Cute stickers!','choices':['귀여운 스티커!','귀여운 인형!','귀여운 옷!','귀여운 가방!'],'ans':0,'hint':('sticker','스티커'),'explain':'sticker = 스티커'},
            {'en':'A photo album.','choices':['사진 앨범','음식 앨범','옷 앨범','책 앨범'],'ans':0,'hint':('album','앨범'),'explain':'album = 앨범'},
            {'en':'Old coins.','choices':['오래된 동전','오래된 책','오래된 옷','오래된 인형'],'ans':0,'hint':('coin','동전'),'explain':'coin = 동전'},
            {'en':'A red toy car.','choices':['빨간 장난감 차','빨간 책','빨간 옷','빨간 가방'],'ans':0,'hint':('toy car','장난감차'),'explain':'toy car = 미니카'},
            {'en':'Hero figures.','choices':['영웅 피규어','영웅 책','영웅 옷','영웅 노래'],'ans':0,'hint':('figure','피규어'),'explain':'figure = 인물 모형'},
            {'en':'Build with lego.','choices':['레고 조립','레고 던지기','레고 자기','레고 먹기'],'ans':0,'hint':('lego','레고'),'explain':'lego = 블록 장난감'},
            {'en':'Fun papercraft.','choices':['재밌는 종이공예','재밌는 책','재밌는 게임','재밌는 영화'],'ans':0,'hint':('papercraft','종이공예'),'explain':'papercraft = 종이공예'},
            {'en':'Grandma knits.','choices':['할머니 뜨개질','할머니 요리','할머니 책 읽기','할머니 자기'],'ans':0,'hint':('knit','뜨개'),'explain':'knit = 뜨개질'},
            {'en':'Cooking is fun.','choices':['요리는 재밌어','요리는 어려워','요리는 졸려','요리는 더러워'],'ans':0,'hint':('cooking','요리'),'explain':'cooking = 요리'},
            {'en':'Baking bread.','choices':['빵 굽기','빵 사기','빵 먹기','빵 던지기'],'ans':0,'hint':('baking','제빵'),'explain':'baking = 굽기'},
            {'en':'Gardening on weekends.','choices':['주말 정원 가꾸기','주말 자기','주말 먹기','주말 놀기'],'ans':0,'hint':('gardening','정원가꾸기'),'explain':'gardening = 정원'},
            {'en':'Cute doodle!','choices':['귀여운 낙서!','귀여운 책!','귀여운 강아지!','귀여운 옷!'],'ans':0,'hint':('doodle','낙서'),'explain':'doodle = 낙서'},
            {'en':'Write in a journal.','choices':['일지 쓰기','책 읽기','자기','놀기'],'ans':0,'hint':('journal','일지'),'explain':'journal = 일지'},
            {'en':'Solve the rubik!','choices':['루빅 풀기!','책 읽기!','자기!','먹기!'],'ans':0,'hint':('rubik','루빅'),'explain':'rubik = 큐브'},
            {'en':'I love reading.','choices':['독서 좋아','요리 좋아','자는 거 좋아','달리기 좋아'],'ans':0,'hint':('reading','독서'),'explain':'reading = 책 읽기'},
            {'en':'Dancing is joy.','choices':['춤이 즐거움','노래가 즐거움','자는 게 즐거움','먹는 게 즐거움'],'ans':0,'hint':('dancing','춤'),'explain':'dancing = 춤추기'},
            {'en':'Family camping.','choices':['가족 캠핑','가족 식사','가족 영화','가족 잠'],'ans':0,'hint':('camping','캠핑'),'explain':'camping = 캠핑'},
        ]
    },

    '20260711': {
        'date':'2026-07-11','day_ko':'토','theme':'감정 표현 (심화)','theme_emoji':'💖','description':'감정 영어 응용!',
        'questions':[
            {'en':"I'm so excited!",'choices':['너무 신나!','너무 슬퍼!','너무 졸려!','너무 피곤!'],'ans':0,'hint':('excited','신난'),'explain':'excited = 신난'},
            {'en':"I'm nervous.",'choices':['긴장돼','즐거워','졸려','신나'],'ans':0,'hint':('nervous','긴장한'),'explain':'nervous = 긴장'},
            {'en':"I'm worried.",'choices':['걱정돼','신나','졸려','즐거워'],'ans':0,'hint':('worried','걱정'),'explain':'worried = 걱정'},
            {'en':"I'm relieved.",'choices':['안도해','걱정해','졸려','피곤해'],'ans':0,'hint':('relieved','안도'),'explain':'relieved = 안심'},
            {'en':"I'm jealous.",'choices':['질투나','신나','즐거워','졸려'],'ans':0,'hint':('jealous','질투'),'explain':'jealous = 질투'},
            {'en':"I'm grateful.",'choices':['감사해','미안해','졸려','피곤해'],'ans':0,'hint':('grateful','감사'),'explain':'grateful = 감사'},
            {'en':"I'm bored.",'choices':['지루해','신나','즐거워','졸려'],'ans':0,'hint':('bored','지루'),'explain':'bored = 지루'},
            {'en':"I'm confused.",'choices':['헷갈려','확실해','졸려','피곤'],'ans':0,'hint':('confused','혼란'),'explain':'confused = 혼란'},
            {'en':"I'm disappointed.",'choices':['실망했어','신나','즐거워','졸려'],'ans':0,'hint':('disappointed','실망'),'explain':'disappointed = 실망'},
            {'en':"I'm embarrassed.",'choices':['창피해','신나','즐거워','졸려'],'ans':0,'hint':('embarrassed','창피'),'explain':'embarrassed = 부끄러움'},
            {'en':"I'm scared.",'choices':['무서워','신나','즐거워','졸려'],'ans':0,'hint':('scared','무서운'),'explain':'scared = 무섬'},
            {'en':"I'm lonely.",'choices':['외로워','신나','즐거워','졸려'],'ans':0,'hint':('lonely','외로운'),'explain':'lonely = 외로움'},
            {'en':"I'm furious.",'choices':['몹시 화나','신나','즐거워','졸려'],'ans':0,'hint':('furious','격노'),'explain':'furious = 매우 화'},
            {'en':"I'm content.",'choices':['만족해','불만족해','졸려','피곤해'],'ans':0,'hint':('content','만족'),'explain':'content = 만족'},
            {'en':"I'm anxious.",'choices':['불안해','신나','졸려','즐거워'],'ans':0,'hint':('anxious','불안'),'explain':'anxious = 불안'},
            {'en':"I'm thrilled!",'choices':['엄청 신나!','엄청 슬퍼!','엄청 졸려!','엄청 피곤!'],'ans':0,'hint':('thrilled','짜릿'),'explain':'thrilled = 매우 흥분'},
            {'en':"I'm exhausted.",'choices':['완전 지쳤어','완전 신나','완전 즐거워','완전 졸려'],'ans':0,'hint':('exhausted','탈진'),'explain':'exhausted = 완전 피곤'},
            {'en':"I'm impressed.",'choices':['감명받았어','지루해','졸려','피곤'],'ans':0,'hint':('impressed','감명'),'explain':'impressed = 감명'},
            {'en':"I'm hopeful.",'choices':['희망적이야','절망적이야','졸려','피곤해'],'ans':0,'hint':('hopeful','희망적'),'explain':'hopeful = 희망'},
            {'en':"I'm pleased.",'choices':['기뻐','슬퍼','졸려','피곤해'],'ans':0,'hint':('pleased','기쁜'),'explain':'pleased = 기쁨'},
        ]
    },

    '20260712': {
        'date':'2026-07-12','day_ko':'일','theme':'마무리·다짐','theme_emoji':'🌅','description':'한 주 마무리 영어!',
        'questions':[
            {'en':'A new start!','choices':['새로운 시작!','오래된 끝!','중간!','없음!'],'ans':0,'hint':('start','시작'),'explain':'start = 시작'},
            {'en':"Let's do our best!",'choices':['최선 다하자!','쉬자!','자자!','놀자!'],'ans':0,'hint':('best','최선'),'explain':'do best = 최선'},
            {'en':'Never give up!','choices':['절대 포기 마!','쉬어!','자!','가!'],'ans':0,'hint':('give up','포기'),'explain':'never give up = 포기 X'},
            {'en':'Step by step.','choices':['천천히 한 걸음씩','빨리','뛰어','자'],'ans':0,'hint':('step','단계'),'explain':'step by step = 차근차근'},
            {'en':'Practice makes perfect.','choices':['연습이 완벽 만들어','자면 완벽','놀면 완벽','먹으면 완벽'],'ans':0,'hint':('practice','연습'),'explain':'practice = 연습'},
            {'en':"Don't worry, be happy!",'choices':['걱정마, 행복하자!','걱정해, 슬프자!','자!','놀아!'],'ans':0,'hint':('happy','행복'),'explain':'be happy = 행복하자'},
            {'en':'You can do it!','choices':['넌 할 수 있어!','넌 못해!','넌 자!','넌 가!'],'ans':0,'hint':('can','할 수 있다'),'explain':'can do = 가능'},
            {'en':"I believe in you.",'choices':['너 믿어','너 안 믿어','너 자','너 가'],'ans':0,'hint':('believe','믿다'),'explain':'believe = 믿음'},
            {'en':'Keep trying!','choices':['계속 시도해!','그만!','자!','놀아!'],'ans':0,'hint':('keep','계속'),'explain':'keep trying = 계속!'},
            {'en':'Stay positive!','choices':['긍정적으로!','부정적으로!','자!','놀아!'],'ans':0,'hint':('positive','긍정'),'explain':'positive = 긍정'},
            {'en':'Be brave!','choices':['용감해져!','약해져!','자!','놀아!'],'ans':0,'hint':('brave','용감'),'explain':'be brave = 용기'},
            {'en':'Smile more!','choices':['더 웃어!','덜 웃어!','자!','놀아!'],'ans':0,'hint':('smile','웃다'),'explain':'smile = 미소'},
            {'en':'Take a deep breath.','choices':['깊게 숨 쉬어','빨리 뛰어','자','놀아'],'ans':0,'hint':('breath','숨'),'explain':'breath = 호흡'},
            {'en':"It's okay to fail.",'choices':['실패해도 괜찮아','실패하면 안 돼','자!','가!'],'ans':0,'hint':('fail','실패'),'explain':'fail = 실패'},
            {'en':'Learn from mistakes.','choices':['실수에서 배워','실수해서 자','실수해서 가','실수해서 먹어'],'ans':0,'hint':('mistake','실수'),'explain':'mistake = 실수'},
            {'en':'Be yourself!','choices':['너답게!','다른 사람처럼!','자!','놀아!'],'ans':0,'hint':('yourself','너자신'),'explain':'be yourself = 너답게'},
            {'en':'Have a great week!','choices':['멋진 한 주!','슬픈 한 주!','자는 한 주!','피곤한 한 주!'],'ans':0,'hint':('great','멋진'),'explain':'great week = 멋진 주'},
            {'en':"Cheer up!",'choices':['힘내!','자!','놀아!','먹어!'],'ans':0,'hint':('cheer','응원'),'explain':'cheer up = 힘내!'},
            {'en':"You're amazing!",'choices':['넌 멋져!','넌 별로!','넌 자!','넌 가!'],'ans':0,'hint':('amazing','놀라운'),'explain':'amazing = 멋짐'},
            {'en':"Let's go!",'choices':['가자!','자자!','먹자!','쉬자!'],'ans':0,'hint':('go','가다'),'explain':"let's go = 가자!"},
        ]
    },

    # ═════════════════════════════════════════════
    # 7/13~7/19 (Week 13) - 농장·바다·공룡·모험·동작
    # ═════════════════════════════════════════════
    '20260713': {
        'date':'2026-07-13','day_ko':'월','theme':'농장 생활','theme_emoji':'🚜','description':'농장 영어!',
        'questions':[
            {'en':'A big farm.','choices':['큰 농장','큰 학교','큰 시장','큰 가게'],'ans':0,'hint':('farm','농장'),'explain':'farm = 농장'},
            {'en':'A kind rancher.','choices':['친절한 목장주','친절한 의사','친절한 선생님','친절한 학생'],'ans':0,'hint':('rancher','목장주'),'explain':'rancher = 목장 주인'},
            {'en':'Cows in the barn.','choices':['헛간 속 소','집 속 소','학교 속 소','시장 속 소'],'ans':0,'hint':('barn','헛간'),'explain':'barn = 헛간'},
            {'en':'On the haystack.','choices':['건초 더미 위','책상 위','의자 위','산 위'],'ans':0,'hint':('haystack','건초더미'),'explain':'haystack = 마른 풀 산'},
            {'en':'Drive a tractor.','choices':['트랙터 운전','차 운전','자전거 타기','걷기'],'ans':0,'hint':('tractor','트랙터'),'explain':'tractor = 농장 차'},
            {'en':'Plow the field.','choices':['밭 갈기','책 읽기','자기','놀기'],'ans':0,'hint':('plow','쟁기'),'explain':'plow = 밭갈이'},
            {'en':'Grow crops.','choices':['농작물 기르기','책 기르기','자기 기르기','동물 기르기'],'ans':0,'hint':('crop','농작물'),'explain':'crop = 농작물'},
            {'en':'Fall harvest!','choices':['가을 수확!','봄 수확!','여름 수확!','겨울 수확!'],'ans':0,'hint':('harvest','수확'),'explain':'harvest = 수확'},
            {'en':'A baby calf.','choices':['아기 송아지','아기 강아지','아기 새','아기 양'],'ans':0,'hint':('calf','송아지'),'explain':'calf = 송아지'},
            {'en':'A cute piglet!','choices':['귀여운 아기돼지!','귀여운 강아지!','귀여운 고양이!','귀여운 곰!'],'ans':0,'hint':('piglet','아기돼지'),'explain':'piglet = 새끼 돼지'},
            {'en':'A little lamb.','choices':['작은 아기 양','작은 사슴','작은 토끼','작은 닭'],'ans':0,'hint':('lamb','아기양'),'explain':'lamb = 양 새끼'},
            {'en':'A young foal.','choices':['어린 망아지','어린 송아지','어린 돼지','어린 새'],'ans':0,'hint':('foal','망아지'),'explain':'foal = 말 새끼'},
            {'en':'A yellow chick.','choices':['노란 병아리','노란 새','노란 별','노란 꽃'],'ans':0,'hint':('chick','병아리'),'explain':'chick = 닭 새끼'},
            {'en':'A jumping goat.','choices':['뛰는 염소','뛰는 토끼','뛰는 새','뛰는 강아지'],'ans':0,'hint':('goat','염소'),'explain':'goat = 염소'},
            {'en':'Rooster crows.','choices':['수탉이 울어','암탉이 울어','병아리가 울어','오리가 울어'],'ans':0,'hint':('rooster','수탉'),'explain':'rooster = 수탉'},
            {'en':'A big turkey.','choices':['큰 칠면조','큰 닭','큰 오리','큰 거위'],'ans':0,'hint':('turkey','칠면조'),'explain':'turkey = 칠면조'},
            {'en':'A big goose.','choices':['큰 거위','큰 닭','큰 오리','큰 칠면조'],'ans':0,'hint':('goose','거위'),'explain':'goose = 거위'},
            {'en':'Wheat field.','choices':['밀밭','쌀밭','보리밭','옥수수밭'],'ans':0,'hint':('wheat','밀'),'explain':'wheat = 밀'},
            {'en':'Sweet corn!','choices':['달콤한 옥수수!','달콤한 밀!','달콤한 쌀!','달콤한 보리!'],'ans':0,'hint':('corn','옥수수'),'explain':'corn = 옥수수'},
            {'en':'Barley field.','choices':['보리밭','쌀밭','콩밭','옥수수밭'],'ans':0,'hint':('barley','보리'),'explain':'barley = 보리'},
        ]
    },

    '20260714': {
        'date':'2026-07-14','day_ko':'화','theme':'바다 생물','theme_emoji':'🐙','description':'바다 생물 영어!',
        'questions':[
            {'en':'A big shark!','choices':['큰 상어!','큰 고래!','큰 물고기!','큰 거북이!'],'ans':0,'hint':('shark','상어'),'explain':'shark = 상어'},
            {'en':'A blue whale.','choices':['파란 고래','파란 새','파란 물고기','파란 새우'],'ans':0,'hint':('whale','고래'),'explain':'whale = 고래'},
            {'en':'Smart swordfish.','choices':['똑똑한 황새치','똑똑한 상어','똑똑한 고래','똑똑한 새우'],'ans':0,'hint':('swordfish','황새치'),'explain':'swordfish = 황새치'},
            {'en':'Eight legs!','choices':['다리 8개! (문어)','다리 4개','다리 2개','다리 6개'],'ans':0,'hint':('octopus','문어'),'explain':'octopus = 8 다리'},
            {'en':'A fresh squid.','choices':['신선한 오징어','신선한 새우','신선한 게','신선한 회'],'ans':0,'hint':('squid','오징어'),'explain':'squid = 오징어'},
            {'en':"Don't touch jellyfish!",'choices':['해파리 만지지마!','새 만지지마!','꽃 만지지마!','강아지 만지지마!'],'ans':0,'hint':('jellyfish','해파리'),'explain':'jellyfish = 해파리'},
            {'en':'A pink starfish.','choices':['분홍 불가사리','분홍 게','분홍 새우','분홍 굴'],'ans':0,'hint':('starfish','불가사리'),'explain':'starfish = 불가사리'},
            {'en':'A red crab.','choices':['빨간 게','빨간 새우','빨간 굴','빨간 조개'],'ans':0,'hint':('crab','게'),'explain':'crab = 게'},
            {'en':'A big lobster!','choices':['큰 바닷가재!','큰 새우!','큰 게!','큰 굴!'],'ans':0,'hint':('lobster','바닷가재'),'explain':'lobster = 바닷가재'},
            {'en':'Eat shrimp.','choices':['새우 먹기','게 먹기','조개 먹기','굴 먹기'],'ans':0,'hint':('shrimp','새우'),'explain':'shrimp = 새우'},
            {'en':'Tuna sushi.','choices':['참치 초밥','연어 초밥','새우 초밥','오징어 초밥'],'ans':0,'hint':('tuna','참치'),'explain':'tuna = 참치'},
            {'en':'A cute seal.','choices':['귀여운 물범','귀여운 강아지','귀여운 새','귀여운 펭귄'],'ans':0,'hint':('seal','물범'),'explain':'seal = 물범'},
            {'en':'A big walrus.','choices':['큰 바다코끼리','큰 펭귄','큰 곰','큰 사자'],'ans':0,'hint':('walrus','바다코끼리'),'explain':'walrus = 바다코끼리'},
            {'en':'Sealion claps.','choices':['바다사자 박수','새 박수','강아지 박수','곰 박수'],'ans':0,'hint':('sealion','바다사자'),'explain':'sealion = 바다사자'},
            {'en':'Open the clam.','choices':['조개 열기','문 열기','책 열기','상자 열기'],'ans':0,'hint':('clam','조개'),'explain':'clam = 조개'},
            {'en':'Fresh oyster.','choices':['신선한 굴','신선한 조개','신선한 새우','신선한 게'],'ans':0,'hint':('oyster','굴'),'explain':'oyster = 굴'},
            {'en':'Pretty coral.','choices':['예쁜 산호','예쁜 꽃','예쁜 별','예쁜 새'],'ans':0,'hint':('coral','산호'),'explain':'coral = 산호'},
            {'en':'Green seaweed.','choices':['초록 해초','초록 풀','초록 잎','초록 꽃'],'ans':0,'hint':('seaweed','해초'),'explain':'seaweed = 미역·김'},
            {'en':'A fish fin.','choices':['물고기 지느러미','물고기 머리','물고기 꼬리','물고기 배'],'ans':0,'hint':('fin','지느러미'),'explain':'fin = 지느러미'},
            {'en':'Fish have gills.','choices':['물고기 아가미 있어','물고기 다리 있어','물고기 손 있어','물고기 코 있어'],'ans':0,'hint':('gill','아가미'),'explain':'gill = 아가미'},
        ]
    },

    '20260715': {
        'date':'2026-07-15','day_ko':'수','theme':'공룡과 화석','theme_emoji':'🦕','description':'공룡 영어!',
        'questions':[
            {'en':'Huge dinosaur!','choices':['거대한 공룡!','작은 공룡!','새 공룡!','오래된 공룡!'],'ans':0,'hint':('dinosaur','공룡'),'explain':'dinosaur = 공룡'},
            {'en':'Scary T-rex!','choices':['무서운 티라노!','귀여운 강아지!','작은 새!','큰 곰!'],'ans':0,'hint':('trex','티라노'),'explain':'T-rex = 공룡 왕'},
            {'en':'Three horns!','choices':['뿔 3개! (트리케라톱스)','뿔 1개','뿔 5개','뿔 없음'],'ans':0,'hint':('triceratops','트리케'),'explain':'triceratops = 3뿔'},
            {'en':'Long neck!','choices':['긴 목! (브론토)','짧은 목','없는 목','두꺼운 목'],'ans':0,'hint':('brontosaurus','브론토'),'explain':'brontosaurus = 긴 목'},
            {'en':'Spiked back!','choices':['등 가시! (스테고)','매끈한 등','없는 등','부드러운 등'],'ans':0,'hint':('stegosaurus','스테고'),'explain':'stegosaurus = 등 가시'},
            {'en':'Smart raptor!','choices':['똑똑한 랩터!','똑똑한 강아지!','똑똑한 새!','똑똑한 곰!'],'ans':0,'hint':('raptor','랩터'),'explain':'raptor = 영리한 공룡'},
            {'en':'Find a fossil.','choices':['화석 찾기','책 찾기','보물 찾기','동물 찾기'],'ans':0,'hint':('fossil','화석'),'explain':'fossil = 화석'},
            {'en':'A dinosaur skeleton.','choices':['공룡 골격','공룡 다리','공룡 머리','공룡 꼬리'],'ans':0,'hint':('skeleton','골격'),'explain':'skeleton = 전체 뼈'},
            {'en':'A dinosaur skull.','choices':['공룡 두개골','공룡 발','공룡 꼬리','공룡 배'],'ans':0,'hint':('skull','두개골'),'explain':'skull = 머리뼈'},
            {'en':'Sharp claws!','choices':['날카로운 발톱!','부드러운 손!','없는 손!','짧은 손!'],'ans':0,'hint':('claw','발톱'),'explain':'claw = 발톱'},
            {'en':'Big horns!','choices':['큰 뿔!','큰 다리!','큰 꼬리!','큰 배!'],'ans':0,'hint':('horn','뿔'),'explain':'horn = 뿔'},
            {'en':'Prehistoric times.','choices':['선사시대','현대','미래','중세'],'ans':0,'hint':('prehistoric','선사'),'explain':'prehistoric = 역사 이전'},
            {'en':'Dinosaurs are extinct.','choices':['공룡은 멸종','공룡은 살아 있음','공룡은 새','공룡은 작음'],'ans':0,'hint':('extinct','멸종'),'explain':'extinct = 사라짐'},
            {'en':'A new epoch.','choices':['새 시대','옛 시대','짧은 시대','없는 시대'],'ans':0,'hint':('epoch','시대'),'explain':'epoch = 시대'},
            {'en':'A paleontologist.','choices':['고생물학자','요리사','선생님','학생'],'ans':0,'hint':('paleontologist','고생물학자'),'explain':'화석 연구자!'},
            {'en':'A giant beast.','choices':['거대한 짐승','작은 동물','새 강아지','오래된 새'],'ans':0,'hint':('giant','거대한'),'explain':'giant = 엄청 큰'},
            {'en':'Hairy mammoth!','choices':['털북숭이 매머드!','대머리 코끼리!','작은 곰!','큰 새!'],'ans':0,'hint':('mammoth','매머드'),'explain':'mammoth = 털 코끼리'},
            {'en':'Cavemen lived here.','choices':['동굴인이 살았어요','거인이 살았어요','새가 살았어요','로봇이 살았어요'],'ans':0,'hint':('cavemen','동굴인'),'explain':'cavemen = 옛 사람'},
            {'en':'Dinosaur egg shell.','choices':['공룡알 껍데기','조개 껍데기','문 손잡이','책 표지'],'ans':0,'hint':('shell','껍데기'),'explain':'shell = 외피'},
            {'en':'Dinosaur scales.','choices':['공룡 비늘','공룡 머리','공룡 다리','공룡 발톱'],'ans':0,'hint':('scale','비늘'),'explain':'scale = 비늘'},
        ]
    },

    '20260716': {
        'date':'2026-07-16','day_ko':'목','theme':'모험과 탐험','theme_emoji':'🗺️','description':'모험 영어!',
        'questions':[
            {'en':'Read the map.','choices':['지도 봐','책 봐','TV 봐','강아지 봐'],'ans':0,'hint':('map','지도'),'explain':'map = 지도'},
            {'en':'Use a compass.','choices':['나침반 써','연필 써','책 써','옷 써'],'ans':0,'hint':('compass','나침반'),'explain':'compass = 방향 도구'},
            {'en':'Fill the canteen.','choices':['수통 채워','컵 채워','병 채워','상자 채워'],'ans':0,'hint':('canteen','수통'),'explain':'canteen = 물병'},
            {'en':'Turn on the flashlight.','choices':['손전등 켜','TV 켜','컴퓨터 켜','불 켜'],'ans':0,'hint':('flashlight','손전등'),'explain':'flashlight = 손전등'},
            {'en':'Put up the tent.','choices':['텐트 치기','문 닫기','자기','먹기'],'ans':0,'hint':('tent','텐트'),'explain':'tent = 천막'},
            {'en':'Warm sleeping bag.','choices':['따뜻한 침낭','따뜻한 옷','따뜻한 음식','따뜻한 차'],'ans':0,'hint':('sleeping bag','침낭'),'explain':'sleeping bag = 침낭'},
            {'en':'Follow the path.','choices':['오솔길 따라','집 따라','학교 따라','산 따라'],'ans':0,'hint':('path','오솔길'),'explain':'path = 좁은 길'},
            {'en':'Hike the trail.','choices':['산길 걷기','집 가기','학교 가기','자기'],'ans':0,'hint':('trail','산길'),'explain':'trail = 등산로'},
            {'en':'A hidden grotto.','choices':['숨겨진 작은 동굴','숨겨진 큰 산','숨겨진 호수','숨겨진 집'],'ans':0,'hint':('grotto','작은동굴'),'explain':'grotto = 작은 동굴'},
            {'en':'Reach the summit!','choices':['정상 도달!','집 도달!','학교 도달!','시장 도달!'],'ans':0,'hint':('summit','정상'),'explain':'summit = 꼭대기'},
            {'en':'In the wilderness.','choices':['야생에서','집에서','학교에서','마트에서'],'ans':0,'hint':('wilderness','야생'),'explain':'wilderness = 야생'},
            {'en':'Find an oasis.','choices':['오아시스 발견','집 발견','학교 발견','산 발견'],'ans':0,'hint':('oasis','오아시스'),'explain':'oasis = 사막 샘'},
            {'en':'Korean peninsula.','choices':['한반도','한국 도시','한국 산','한국 강'],'ans':0,'hint':('peninsula','반도'),'explain':'peninsula = 3면 바다'},
            {'en':'A brave explorer.','choices':['용감한 탐험가','용감한 학생','용감한 선생님','용감한 친구'],'ans':0,'hint':('explorer','탐험가'),'explain':'explorer = 탐험가'},
            {'en':'A boy scout.','choices':['보이스카우트','학생','선생님','친구'],'ans':0,'hint':('scout','스카우트'),'explain':'scout = 정찰병'},
            {'en':'Survive in the wild.','choices':['야생에서 생존','집에서 자기','학교에서 공부','마트에서 쇼핑'],'ans':0,'hint':('survive','생존'),'explain':'survive = 버티기'},
            {'en':'Around the campfire.','choices':['모닥불 주위','학교 주위','집 주위','마트 주위'],'ans':0,'hint':('campfire','모닥불'),'explain':'campfire = 캠핑 불'},
            {'en':'A binocular set.','choices':['쌍안경 세트','책 세트','옷 세트','음식 세트'],'ans':0,'hint':('binocular','쌍안경'),'explain':'binocular = 두 눈 망원경'},
            {'en':'Use a hook.','choices':['갈고리 사용','연필 사용','책 사용','문 사용'],'ans':0,'hint':('hook','갈고리'),'explain':'hook = 갈고리'},
            {'en':'A long journey.','choices':['긴 여정','짧은 여정','새 여정','오래된 여정'],'ans':0,'hint':('journey','여정'),'explain':'journey = 긴 여행'},
        ]
    },

    '20260717': {
        'date':'2026-07-17','day_ko':'금','theme':'동작·움직임','theme_emoji':'🏃','description':'동작 영어!',
        'questions':[
            {'en':'Sprint to the goal!','choices':['목표까지 질주!','목표까지 걷기!','목표까지 자기!','목표까지 먹기!'],'ans':0,'hint':('sprint','질주'),'explain':'sprint = 빠른 달리기'},
            {'en':'Dash forward!','choices':['앞으로 돌진!','뒤로 걷기!','자기!','놀기!'],'ans':0,'hint':('dash','돌진'),'explain':'dash = 빠르게'},
            {'en':'Leap over!','choices':['훌쩍 넘기!','자기!','걷기!','먹기!'],'ans':0,'hint':('leap','뛰기'),'explain':'leap = 큰 점프'},
            {'en':'Bounce the ball.','choices':['공 튕기기','공 던지기','공 잡기','공 차기'],'ans':0,'hint':('bounce','튕김'),'explain':'bounce = 통통!'},
            {'en':'Hover in air!','choices':['공중에 떠 있기!','땅에 자기!','집에 가기!','학교 가기!'],'ans':0,'hint':('hover','공중'),'explain':'hover = 떠 있기'},
            {'en':'Ascend the stairs.','choices':['계단 올라가기','계단 내려가기','계단 자기','계단 먹기'],'ans':0,'hint':('ascend','올라가다'),'explain':'ascend = 위로'},
            {'en':'Babies crawl.','choices':['아기는 기어가요','아기는 뛰어요','아기는 자요','아기는 먹어요'],'ans':0,'hint':('crawl','기어가다'),'explain':'crawl = 기기'},
            {'en':'Tumble down!','choices':['굴러 떨어지기!','일어나기!','앉기!','자기!'],'ans':0,'hint':('tumble','구르다'),'explain':'tumble = 구르기'},
            {'en':'Slide down!','choices':['미끄러져 내려가기!','걸어 내려가기!','뛰어가기!','자기!'],'ans':0,'hint':('slide','미끄러짐'),'explain':'slide = 슈웅'},
            {'en':'Spin around!','choices':['한 바퀴 돌기!','걷기!','자기!','먹기!'],'ans':0,'hint':('spin','회전'),'explain':'spin = 빙글'},
            {'en':'Twist your body.','choices':['몸 비틀기','몸 펴기','몸 자기','몸 먹기'],'ans':0,'hint':('twist','비틀'),'explain':'twist = 꼬기'},
            {'en':'Crouch down.','choices':['웅크려 앉기','일어서기','뛰기','자기'],'ans':0,'hint':('crouch','웅크림'),'explain':'crouch = 낮게'},
            {'en':'Flex your muscles!','choices':['근육 자랑!','근육 숨기기!','근육 자기!','근육 먹기!'],'ans':0,'hint':('flex','구부림'),'explain':'flex = 힘 주기'},
            {'en':'Reach the top.','choices':['꼭대기 손 닿기','꼭대기 자기','꼭대기 먹기','꼭대기 가기'],'ans':0,'hint':('reach','뻗다'),'explain':'reach = 닿기'},
            {'en':'Grab the ball!','choices':['공 잡기!','공 던지기!','공 차기!','공 봐기!'],'ans':0,'hint':('grab','잡다'),'explain':'grab = 잡기'},
            {'en':"Don't shove me!",'choices':['세게 밀지 마!','자지 마!','오지 마!','가지 마!'],'ans':0,'hint':('shove','세게밀다'),'explain':'shove = 강한 밀기'},
            {'en':'Yank it open!','choices':['홱 잡아당겨!','살살 당겨!','자!','놀아!'],'ans':0,'hint':('yank','홱'),'explain':'yank = 확 당기기'},
            {'en':'Toss the coin.','choices':['동전 던지기','동전 잡기','동전 잃기','동전 먹기'],'ans':0,'hint':('toss','던짐'),'explain':'toss = 가볍게'},
            {'en':'Snatch the ball!','choices':['공 잽싸게 잡기!','공 던지기!','공 차기!','공 보기!'],'ans':0,'hint':('snatch','잽싸'),'explain':'snatch = 순간 포착'},
            {'en':"Don't stumble!",'choices':['비틀거리지 마!','자지 마!','오지 마!','가지 마!'],'ans':0,'hint':('stumble','비틀'),'explain':'stumble = 휘청'},
        ]
    },

    '20260718': {
        'date':'2026-07-18','day_ko':'토','theme':'주말 휴식','theme_emoji':'🛌','description':'주말 편안한 영어!',
        'questions':[
            {'en':'I want to relax.','choices':['쉬고 싶어','일하고 싶어','뛰고 싶어','공부하고 싶어'],'ans':0,'hint':('relax','쉬다'),'explain':'relax = 쉬다'},
            {'en':'Take it easy.','choices':['여유롭게','빨리','자','놀아'],'ans':0,'hint':('easy','쉬운'),'explain':'take it easy = 천천히'},
            {'en':'Sleep in today.','choices':['오늘 늦잠','오늘 일찍','오늘 일!','오늘 학교!'],'ans':0,'hint':('sleep in','늦잠'),'explain':'sleep in = 늦게까지 자기'},
            {'en':'Stay in bed.','choices':['침대에 누워있어','일어나서 가','뛰어','일해'],'ans':0,'hint':('stay','머무르다'),'explain':'stay in = 머물기'},
            {'en':'Have a lazy day.','choices':['게으른 날 보내','바쁜 날 보내','자','일해'],'ans':0,'hint':('lazy','게으른'),'explain':'lazy day = 한가한 날'},
            {'en':'Watch movies all day.','choices':['하루 종일 영화','하루 종일 일','하루 종일 자','하루 종일 공부'],'ans':0,'hint':('all day','종일'),'explain':'all day = 종일'},
            {'en':'Eat snacks.','choices':['간식 먹기','밥 먹기','자기','일하기'],'ans':0,'hint':('snack','간식'),'explain':'snack = 간식'},
            {'en':'Call a friend.','choices':['친구에게 전화','친구 만나','친구 자','친구 보내'],'ans':0,'hint':('call','전화'),'explain':'call = 통화'},
            {'en':'Read comics.','choices':['만화 읽기','책 읽기','자기','일하기'],'ans':0,'hint':('comics','만화'),'explain':'comics = 만화'},
            {'en':'Play board games.','choices':['보드게임 하기','일하기','자기','공부'],'ans':0,'hint':('board game','보드게임'),'explain':'board game = 보드게임'},
            {'en':'Order pizza.','choices':['피자 주문','피자 만들기','피자 자기','피자 던지기'],'ans':0,'hint':('order','주문'),'explain':'order = 주문하다'},
            {'en':'Watch the sunset.','choices':['일몰 보기','일출 보기','자기','일하기'],'ans':0,'hint':('sunset','일몰'),'explain':'sunset = 해질녘'},
            {'en':'Take a bath.','choices':['목욕하기','자기','뛰기','일하기'],'ans':0,'hint':('bath','목욕'),'explain':'take bath = 목욕'},
            {'en':'Light a candle.','choices':['초 켜기','불 끄기','자기','일하기'],'ans':0,'hint':('candle','초'),'explain':'candle = 양초'},
            {'en':'Listen to music.','choices':['음악 듣기','음악 끄기','자기','일하기'],'ans':0,'hint':('listen','듣다'),'explain':'listen = 듣기'},
            {'en':'Enjoy the moment.','choices':['이 순간 즐기기','자기','일하기','뛰기'],'ans':0,'hint':('moment','순간'),'explain':'moment = 순간'},
            {'en':'Sip some tea.','choices':['차 한 모금','뛰기','자기','일하기'],'ans':0,'hint':('sip','홀짝'),'explain':'sip = 홀짝 마시기'},
            {'en':'Cozy blanket.','choices':['포근한 담요','차가운 담요','새 담요','오래된 담요'],'ans':0,'hint':('cozy','포근한'),'explain':'cozy = 포근'},
            {'en':"Don't worry, be lazy!",'choices':['걱정마, 느긋!','걱정해, 빨리!','자!','놀아!'],'ans':0,'hint':('worry','걱정'),'explain':'be lazy = 느긋하게'},
            {'en':'Sweet weekend!','choices':['달콤한 주말!','쓴 주말!','짠 주말!','매운 주말!'],'ans':0,'hint':('weekend','주말'),'explain':'weekend = 주말'},
        ]
    },

    '20260719': {
        'date':'2026-07-19','day_ko':'일','theme':'한 주 반성','theme_emoji':'📔','description':'반성·계획 영어!',
        'questions':[
            {'en':'What did you learn?','choices':['뭐 배웠어?','뭐 먹었어?','어디 갔어?','왜 슬퍼?'],'ans':0,'hint':('learn','배우다'),'explain':'learn = 배우다'},
            {'en':'I made a mistake.','choices':['실수했어','잘했어','놀았어','잤어'],'ans':0,'hint':('mistake','실수'),'explain':'mistake = 실수'},
            {'en':"I'll try again.",'choices':['다시 해볼게','포기할게','자버릴게','갈게'],'ans':0,'hint':('try','시도'),'explain':'try again = 다시 시도'},
            {'en':'Practice more.','choices':['연습 더','연습 덜','자기 더','놀기 더'],'ans':0,'hint':('practice','연습'),'explain':'practice = 연습'},
            {'en':'Set a goal.','choices':['목표 세우기','자기','놀기','먹기'],'ans':0,'hint':('goal','목표'),'explain':'set goal = 목표 세우기'},
            {'en':'Believe in yourself.','choices':['자신 믿어','자신 의심','자기','놀기'],'ans':0,'hint':('believe','믿다'),'explain':'believe = 믿음'},
            {'en':'Never give up!','choices':['절대 포기 마!','쉬어!','자!','놀아!'],'ans':0,'hint':('give up','포기'),'explain':"never give up = 포기 X"},
            {'en':'Step by step.','choices':['한 걸음씩','빨리','뛰어','자'],'ans':0,'hint':('step','단계'),'explain':'step by step = 차근차근'},
            {'en':'Plan for tomorrow.','choices':['내일 계획','어제 계획','오늘 자기','지금 놀기'],'ans':0,'hint':('plan','계획'),'explain':'plan = 계획'},
            {'en':'I did my best.','choices':['최선을 다했어','대충 했어','자버렸어','놀았어'],'ans':0,'hint':('best','최선'),'explain':'did best = 최선'},
            {'en':"I'm proud of myself.",'choices':['내가 자랑스러워','내가 싫어','내가 자','내가 가'],'ans':0,'hint':('proud','자랑'),'explain':'proud = 자랑스럽다'},
            {'en':'Look on the bright side.','choices':['긍정적으로 봐','부정적으로 봐','자','자버려'],'ans':0,'hint':('bright','밝은'),'explain':'bright side = 좋은 면'},
            {'en':'Be patient!','choices':['인내심을!','빨리해!','자!','놀아!'],'ans':0,'hint':('patient','인내'),'explain':'patient = 참기'},
            {'en':"You're improving.",'choices':['너 발전하고 있어','너 후퇴해','너 자','너 가'],'ans':0,'hint':('improve','발전'),'explain':'improve = 향상'},
            {'en':'Keep going!','choices':['계속해!','그만!','자!','놀아!'],'ans':0,'hint':('keep','계속'),'explain':'keep going = 계속!'},
            {'en':"It's a new week.",'choices':['새로운 한 주야','오래된 한 주','짧은 한 주','없는 한 주'],'ans':0,'hint':('week','주'),'explain':'new week = 새 주'},
            {'en':'Stay positive!','choices':['긍정 유지!','부정 유지!','자!','놀아!'],'ans':0,'hint':('positive','긍정'),'explain':'positive = 긍정'},
            {'en':"You'll get better.",'choices':['더 잘하게 될 거야','더 못해질 거야','자','놀아'],'ans':0,'hint':('better','더 좋은'),'explain':'better = 향상'},
            {'en':'Dream big!','choices':['크게 꿈꿔!','작게 자!','크게 자!','크게 먹어!'],'ans':0,'hint':('dream','꿈'),'explain':'dream big = 큰 꿈'},
            {'en':'See you next week!','choices':['다음 주 봐!','어제 봤어!','지금 봐!','내일 봐!'],'ans':0,'hint':('next','다음'),'explain':'next week = 다음 주'},
        ]
    },

    # ═════════════════════════════════════════════
    # 7/20~7/26 (Week 14) - 여행·재료·신체·건축·방향
    # ═════════════════════════════════════════════
    '20260720': {
        'date':'2026-07-20','day_ko':'월','theme':'여행 표현','theme_emoji':'✈️','description':'여행 영어!',
        'questions':[
            {'en':'Pack the suitcase.','choices':['여행 가방 싸요','책가방 싸요','음식 싸요','옷 정리'],'ans':0,'hint':('suitcase','여행가방'),'explain':'suitcase = 여행가방'},
            {'en':'Stay at a hotel.','choices':['호텔에 묵어요','집에 가요','학교 가요','공원 가요'],'ans':0,'hint':('hotel','호텔'),'explain':'hotel = 숙소'},
            {'en':'Make a reservation.','choices':['예약해요','자기','놀기','먹기'],'ans':0,'hint':('reservation','예약'),'explain':'reservation = 예약'},
            {'en':'Buy a memento.','choices':['추억의 물건 사기','책 사기','음식 사기','옷 사기'],'ans':0,'hint':('memento','추억의 물건'),'explain':'memento = 추억'},
            {'en':'Weekend getaway!','choices':['주말 짧은 여행!','학교 가기!','자기!','일하기!'],'ans':0,'hint':('getaway','짧은휴가'),'explain':'getaway = 짧은 휴가'},
            {'en':'Check in at the hotel.','choices':['호텔 체크인','호텔 체크아웃','학교 가기','집 가기'],'ans':0,'hint':('check in','체크인'),'explain':'check in = 도착 등록'},
            {'en':'Check out by 11.','choices':['11시까지 체크아웃','11시까지 체크인','11시까지 자기','11시까지 먹기'],'ans':0,'hint':('check out','체크아웃'),'explain':'check out = 떠날 때'},
            {'en':'Plan the itinerary.','choices':['여행 일정 계획','음식 계획','학교 계획','집 청소'],'ans':0,'hint':('itinerary','일정표'),'explain':'itinerary = 일정'},
            {'en':'Best route.','choices':['최고의 경로','최고의 가게','최고의 음식','최고의 옷'],'ans':0,'hint':('route','경로'),'explain':'route = 가는 길'},
            {'en':'Go sightseeing.','choices':['관광 가기','쇼핑 가기','학교 가기','자기'],'ans':0,'hint':('sightseeing','관광'),'explain':'sightseeing = 구경'},
            {'en':'Famous landmark.','choices':['유명 랜드마크','유명 음식','유명 책','유명 학교'],'ans':0,'hint':('landmark','랜드마크'),'explain':'landmark = 명소'},
            {'en':'A beach resort.','choices':['바닷가 리조트','바닷가 학교','바닷가 시장','바닷가 집'],'ans':0,'hint':('resort','리조트'),'explain':'resort = 휴양지'},
            {'en':'Take a cruise.','choices':['크루즈 타기','버스 타기','자전거 타기','걷기'],'ans':0,'hint':('cruise','유람선'),'explain':'cruise = 큰 배 여행'},
            {'en':'A long flight.','choices':['긴 항공편','긴 책','긴 노래','긴 영화'],'ans':0,'hint':('flight','항공편'),'explain':'flight = 비행'},
            {'en':'Gate 5 please.','choices':['5번 게이트','5번 의자','5번 책','5번 음식'],'ans':0,'hint':('gate','탑승구'),'explain':'gate = 공항 문'},
            {'en':'Go through customs.','choices':['세관 통과','학교 통과','집 통과','마트 통과'],'ans':0,'hint':('customs','세관'),'explain':'customs = 공항 검사'},
            {'en':'Apply for a visa.','choices':['비자 신청','선물 신청','학교 신청','직업 신청'],'ans':0,'hint':('visa','비자'),'explain':'visa = 입국 허가'},
            {'en':'Exchange currency.','choices':['환전하기','쇼핑하기','자기','놀기'],'ans':0,'hint':('currency','통화'),'explain':'currency = 화폐'},
            {'en':'Travel overseas!','choices':['해외 여행!','집 가기!','학교 가기!','자기!'],'ans':0,'hint':('overseas','해외'),'explain':'overseas = 바다 너머'},
            {'en':'Lie on a sunbed.','choices':['선베드에 누워요','책상에 누워요','땅에 누워요','자기'],'ans':0,'hint':('sunbed','선베드'),'explain':'sunbed = 햇볕 의자'},
        ]
    },

    '20260721': {
        'date':'2026-07-21','day_ko':'화','theme':'재료·물질','theme_emoji':'🪵','description':'재료 영어!',
        'questions':[
            {'en':'A wood table.','choices':['나무 책상','철 책상','종이 책상','옷 책상'],'ans':0,'hint':('wood','나무'),'explain':'wood = 목재'},
            {'en':'Metal door.','choices':['금속 문','나무 문','종이 문','유리 문'],'ans':0,'hint':('metal','금속'),'explain':'metal = 금속'},
            {'en':'Iron gate.','choices':['철문','나무 문','금 문','은 문'],'ans':0,'hint':('iron','철'),'explain':'iron = 철'},
            {'en':'Steel building.','choices':['강철 건물','나무 건물','종이 건물','유리 건물'],'ans':0,'hint':('steel','강철'),'explain':'steel = 강철'},
            {'en':'Aluminum foil.','choices':['알루미늄 호일','종이 호일','유리 호일','나무 호일'],'ans':0,'hint':('aluminum','알루미늄'),'explain':'aluminum = 가벼움'},
            {'en':'Silver coin.','choices':['은 동전','금 동전','동 동전','종이 동전'],'ans':0,'hint':('silver','은'),'explain':'silver = 은'},
            {'en':'Copper wire.','choices':['구리 전선','은 전선','금 전선','종이 전선'],'ans':0,'hint':('copper','구리'),'explain':'copper = 구리'},
            {'en':'Denim jeans.','choices':['데님 청바지','나무 옷','금 옷','종이 옷'],'ans':0,'hint':('denim','데님'),'explain':'denim = 청바지 천'},
            {'en':'Leather bag.','choices':['가죽 가방','나무 가방','종이 가방','유리 가방'],'ans':0,'hint':('leather','가죽'),'explain':'leather = 가죽'},
            {'en':'Cotton shirt.','choices':['면 셔츠','나무 셔츠','금 셔츠','종이 셔츠'],'ans':0,'hint':('cotton','면'),'explain':'cotton = 솜'},
            {'en':'Wool scarf.','choices':['털 스카프','나무 스카프','금 스카프','종이 스카프'],'ans':0,'hint':('wool','양털'),'explain':'wool = 양털'},
            {'en':'Silk dress.','choices':['비단 드레스','나무 드레스','금 드레스','종이 드레스'],'ans':0,'hint':('silk','비단'),'explain':'silk = 누에 실'},
            {'en':'A heavy stone.','choices':['무거운 돌','무거운 종이','무거운 옷','무거운 책'],'ans':0,'hint':('stone','돌'),'explain':'stone = 돌'},
            {'en':'A brick house.','choices':['벽돌 집','나무 집','종이 집','유리 집'],'ans':0,'hint':('brick','벽돌'),'explain':'brick = 빨간 돌'},
            {'en':'Mix cement.','choices':['시멘트 섞기','음식 섞기','색 섞기','책 섞기'],'ans':0,'hint':('cement','시멘트'),'explain':'cement = 건축 재료'},
            {'en':'Concrete road.','choices':['콘크리트 도로','나무 도로','금 도로','종이 도로'],'ans':0,'hint':('concrete','콘크리트'),'explain':'concrete = 매우 단단'},
            {'en':'Rubber ball.','choices':['고무공','나무공','금공','종이공'],'ans':0,'hint':('rubber','고무'),'explain':'rubber = 늘어남'},
            {'en':'A clear liquid.','choices':['투명한 액체','투명한 고체','투명한 기체','없음'],'ans':0,'hint':('liquid','액체'),'explain':'liquid = 흐름'},
            {'en':'Ice is solid.','choices':['얼음은 고체','얼음은 액체','얼음은 기체','얼음 없음'],'ans':0,'hint':('solid','고체'),'explain':'solid = 단단함'},
            {'en':'Air is gas.','choices':['공기는 기체','공기는 액체','공기는 고체','없음'],'ans':0,'hint':('gas','기체'),'explain':'gas = 보이지 않음'},
        ]
    },

    '20260722': {
        'date':'2026-07-22','day_ko':'수','theme':'신체 부위','theme_emoji':'🦵','description':'몸 영어!',
        'questions':[
            {'en':'Touch collarbone.','choices':['쇄골 만지기','이마 만지기','턱 만지기','발 만지기'],'ans':0,'hint':('collarbone','쇄골'),'explain':'collarbone = 목 아래 뼈'},
            {'en':'Strong thigh.','choices':['강한 허벅지','강한 손','강한 머리','강한 발'],'ans':0,'hint':('thigh','허벅지'),'explain':'thigh = 무릎 위'},
            {'en':'Twist my ankle.','choices':['발목 삐어요','손목 삐어요','목 삐어요','허리 삐어요'],'ans':0,'hint':('ankle','발목'),'explain':'ankle = 발과 다리'},
            {'en':'Wear on the wrist.','choices':['손목에 차요','발에 차요','목에 차요','허리에 차요'],'ans':0,'hint':('wrist','손목'),'explain':'wrist = 손과 팔'},
            {'en':'Crack the knuckles.','choices':['손가락 꺾기','목 꺾기','발 꺾기','허리 꺾기'],'ans':0,'hint':('knuckle','손가락 관절'),'explain':'knuckle = 마디'},
            {'en':'Thumbs up!','choices':['엄지 척!','새끼 척!','중지 척!','검지 척!'],'ans':0,'hint':('thumb','엄지'),'explain':'thumb = 엄지'},
            {'en':'Open your palm.','choices':['손바닥 펴기','발바닥 펴기','얼굴 펴기','책 펴기'],'ans':0,'hint':('palm','손바닥'),'explain':'palm = 손 안쪽'},
            {'en':'Touch your chin.','choices':['턱 만지기','이마 만지기','코 만지기','귀 만지기'],'ans':0,'hint':('chin','턱'),'explain':'chin = 얼굴 아래'},
            {'en':'Pink cheeks.','choices':['분홍 볼','분홍 발','분홍 손','분홍 머리'],'ans':0,'hint':('cheek','볼'),'explain':'cheek = 얼굴 양쪽'},
            {'en':'High forehead.','choices':['넓은 이마','넓은 손','넓은 발','넓은 어깨'],'ans':0,'hint':('forehead','이마'),'explain':'forehead = 눈썹 위'},
            {'en':'Heart in chest.','choices':['가슴의 심장','발의 심장','손의 심장','머리의 심장'],'ans':0,'hint':('chest','가슴'),'explain':'chest = 몸 앞쪽'},
            {'en':'Slim waist.','choices':['가는 허리','가는 머리','가는 다리','가는 손'],'ans':0,'hint':('waist','허리'),'explain':'waist = 몸 가운데'},
            {'en':'Hands on hips.','choices':['허리에 손','발에 손','머리에 손','목에 손'],'ans':0,'hint':('hip','엉덩이'),'explain':'hip = 몸 옆 아래'},
            {'en':'My heel hurts.','choices':['뒤꿈치 아파','이마 아파','턱 아파','손 아파'],'ans':0,'hint':('heel','뒤꿈치'),'explain':'heel = 발 뒤쪽'},
            {'en':'Wiggle your toes.','choices':['발가락 꼼지락','손가락 꼼지락','머리 꼼지락','얼굴 꼼지락'],'ans':0,'hint':('toe','발가락'),'explain':'toe = 발 끝'},
            {'en':'Sensitive nerve.','choices':['예민한 신경','예민한 손','예민한 발','예민한 머리'],'ans':0,'hint':('nerve','신경'),'explain':'nerve = 느낌 전달'},
            {'en':'Small pore.','choices':['작은 모공','작은 손','작은 발','작은 옷'],'ans':0,'hint':('pore','모공'),'explain':'pore = 피부 구멍'},
            {'en':'Healthy liver.','choices':['건강한 간','건강한 발','건강한 손','건강한 머리'],'ans':0,'hint':('liver','간'),'explain':'liver = 정화기'},
            {'en':'Straight spine.','choices':['곧은 척추','곧은 손','곧은 다리','곧은 머리'],'ans':0,'hint':('spine','척추'),'explain':'spine = 등뼈'},
            {'en':'Heart beats!','choices':['심장 뛰어!','발 뛰어!','손 뛰어!','얼굴 뛰어!'],'ans':0,'hint':('heart','심장'),'explain':'heart = 피 펌프'},
        ]
    },

    '20260723': {
        'date':'2026-07-23','day_ko':'목','theme':'건축물','theme_emoji':'🏛️','description':'건축 영어!',
        'questions':[
            {'en':'Tall skyscraper.','choices':['높은 빌딩','낮은 집','작은 가게','중간 학교'],'ans':0,'hint':('skyscraper','고층빌딩'),'explain':'skyscraper = 하늘에 닿을 듯'},
            {'en':'A famous monument.','choices':['유명한 기념비','유명한 음식','유명한 사람','유명한 책'],'ans':0,'hint':('monument','기념비'),'explain':'monument = 기억용'},
            {'en':'A pretty fountain.','choices':['예쁜 분수','예쁜 옷','예쁜 책','예쁜 음식'],'ans':0,'hint':('fountain','분수'),'explain':'fountain = 물 뿜기'},
            {'en':'Eiffel tower.','choices':['에펠탑','에펠빌딩','에펠집','에펠학교'],'ans':0,'hint':('tower','탑'),'explain':'tower = 높이 솟음'},
            {'en':'A grand palace.','choices':['웅장한 궁전','작은 집','평범한 학교','오래된 가게'],'ans':0,'hint':('palace','궁전'),'explain':'palace = 왕의 집'},
            {'en':'A big mansion.','choices':['큰 대저택','큰 학교','큰 시장','큰 도서관'],'ans':0,'hint':('mansion','대저택'),'explain':'mansion = 부자 집'},
            {'en':'A small cottage.','choices':['작은 시골집','큰 빌딩','새 호텔','오래된 학교'],'ans':0,'hint':('cottage','시골집'),'explain':'cottage = 오두막'},
            {'en':'My apartment.','choices':['우리 아파트','우리 집','우리 학교','우리 시장'],'ans':0,'hint':('apartment','아파트'),'explain':'apartment = 여러 층'},
            {'en':'A pretty villa.','choices':['예쁜 별장','예쁜 학교','예쁜 가게','예쁜 책'],'ans':0,'hint':('villa','별장'),'explain':'villa = 휴양 집'},
            {'en':'A car factory.','choices':['자동차 공장','자동차 가게','자동차 학교','자동차 시장'],'ans':0,'hint':('factory','공장'),'explain':'factory = 만드는 곳'},
            {'en':'A big warehouse.','choices':['큰 창고','큰 집','큰 학교','큰 가게'],'ans':0,'hint':('warehouse','창고'),'explain':'warehouse = 보관'},
            {'en':'A grand cathedral.','choices':['웅장한 대성당','큰 집','학교','시장'],'ans':0,'hint':('cathedral','대성당'),'explain':'cathedral = 큰 교회'},
            {'en':'Visit the observatory.','choices':['천문대 방문','학교 방문','집 방문','마트 방문'],'ans':0,'hint':('observatory','천문대'),'explain':'observatory = 별 보기'},
            {'en':'A big aquarium.','choices':['큰 수족관','큰 집','큰 가게','큰 학교'],'ans':0,'hint':('aquarium','수족관'),'explain':'aquarium = 물고기 구경'},
            {'en':'Amusement park!','choices':['놀이공원!','학교!','집!','시장!'],'ans':0,'hint':('amusement','놀이'),'explain':'amusement park = 놀이동산'},
            {'en':'A glass dome.','choices':['유리 돔','유리 컵','유리 창','유리 책'],'ans':0,'hint':('dome','돔'),'explain':'dome = 둥근 천장'},
            {'en':'A stone arch.','choices':['돌 아치','돌 책','돌 의자','돌 컵'],'ans':0,'hint':('arch','아치'),'explain':'arch = 활 모양'},
            {'en':'Tall pillars.','choices':['높은 기둥','높은 책','높은 사람','높은 의자'],'ans':0,'hint':('pillar','기둥'),'explain':'pillar = 받침'},
            {'en':'Sit on the balcony.','choices':['발코니에 앉기','의자에 앉기','땅에 앉기','자기'],'ans':0,'hint':('balcony','발코니'),'explain':'balcony = 바깥 발'},
            {'en':'Smoke from chimney.','choices':['굴뚝의 연기','책의 연기','옷의 연기','음식의 연기'],'ans':0,'hint':('chimney','굴뚝'),'explain':'chimney = 연기 빠짐'},
        ]
    },

    '20260724': {
        'date':'2026-07-24','day_ko':'금','theme':'방향과 위치','theme_emoji':'🧭','description':'방향 영어!',
        'questions':[
            {'en':'Go north.','choices':['북쪽으로','남쪽으로','동쪽으로','서쪽으로'],'ans':0,'hint':('north','북쪽'),'explain':'north = 북'},
            {'en':'Head south.','choices':['남쪽으로','북쪽으로','동쪽으로','서쪽으로'],'ans':0,'hint':('south','남쪽'),'explain':'south = 남'},
            {'en':'The east.','choices':['동쪽','서쪽','북쪽','남쪽'],'ans':0,'hint':('east','동쪽'),'explain':'east = 해 뜸'},
            {'en':'The west.','choices':['서쪽','동쪽','북쪽','남쪽'],'ans':0,'hint':('west','서쪽'),'explain':'west = 해 짐'},
            {'en':'Go northeast.','choices':['북동쪽으로','남서쪽으로','북서쪽으로','남동쪽으로'],'ans':0,'hint':('northeast','북동'),'explain':'NE = 북+동'},
            {'en':'From southwest.','choices':['남서쪽에서','북동쪽에서','동쪽에서','서쪽에서'],'ans':0,'hint':('southwest','남서'),'explain':'SW = 남+서'},
            {'en':'Move forward.','choices':['앞으로 가기','뒤로 가기','위로 가기','아래로 가기'],'ans':0,'hint':('forward','앞'),'explain':'forward = 전진'},
            {'en':'Step backward.','choices':['뒤로 한 걸음','앞으로','위로','아래로'],'ans':0,'hint':('backward','뒤'),'explain':'backward = 후진'},
            {'en':'Look upward.','choices':['위를 봐요','아래를 봐요','앞을 봐요','뒤를 봐요'],'ans':0,'hint':('upward','위로'),'explain':'upward = 위쪽'},
            {'en':'Slope downward.','choices':['아래로 경사','위로 경사','평평','오르막'],'ans':0,'hint':('downward','아래로'),'explain':'downward = 아래'},
            {'en':'Turn inward.','choices':['안쪽으로 돌기','바깥으로 돌기','자기','놀기'],'ans':0,'hint':('inward','안쪽'),'explain':'inward = 속으로'},
            {'en':'Push outward.','choices':['바깥으로 밀기','안쪽으로 밀기','위로 밀기','아래로 밀기'],'ans':0,'hint':('outward','바깥'),'explain':'outward = 밖으로'},
            {'en':'A short distance.','choices':['가까운 거리','먼 거리','새 거리','오래된 거리'],'ans':0,'hint':('distance','거리'),'explain':'distance = 떨어진 정도'},
            {'en':'Find the location.','choices':['위치 찾기','이름 찾기','음식 찾기','책 찾기'],'ans':0,'hint':('location','위치'),'explain':'location = 있는 곳'},
            {'en':'This area.','choices':['이 지역','저 지역','새 지역','오래된 지역'],'ans':0,'hint':('area','지역'),'explain':'area = 영역'},
            {'en':'Cold region.','choices':['추운 지방','더운 지방','새 지방','오래된 지방'],'ans':0,'hint':('region','지방'),'explain':'region = 큰 지역'},
            {'en':'The midpoint.','choices':['중간 지점','시작 지점','끝 지점','없음'],'ans':0,'hint':('midpoint','중간'),'explain':'midpoint = 한 가운데'},
            {'en':'At the corner.','choices':['모퉁이에서','한 가운데서','시작에서','끝에서'],'ans':0,'hint':('corner','모퉁이'),'explain':'corner = 꺾이는 곳'},
            {'en':'A clear boundary.','choices':['분명한 경계선','분명한 책','분명한 음식','분명한 옷'],'ans':0,'hint':('boundary','경계'),'explain':'boundary = 영역의 끝'},
            {'en':'Smooth surface.','choices':['매끄러운 표면','매끄러운 옷','매끄러운 책','매끄러운 손'],'ans':0,'hint':('surface','표면'),'explain':'surface = 겉면'},
        ]
    },

    '20260725': {
        'date':'2026-07-25','day_ko':'토','theme':'일상 회화 응용','theme_emoji':'💬','description':'심화 회화!',
        'questions':[
            {'en':'How was your day?','choices':['오늘 어땠어?','이름 뭐?','어디 가?','뭐 해?'],'ans':0,'hint':('day','하루'),'explain':'how was = 어땠어'},
            {'en':"I had a great time.",'choices':['좋은 시간 보냈어','나쁜 시간','잘 안 했어','없어'],'ans':0,'hint':('great time','좋은 시간'),'explain':'great time = 즐거웠다'},
            {'en':"Could you help me?",'choices':['도와줄 수 있어?','자줘?','놀아줘?','먹어줘?'],'ans':0,'hint':('help','돕다'),'explain':'could you = 정중한 요청'},
            {'en':"What do you mean?",'choices':['무슨 뜻이야?','어디 가?','뭐 먹어?','잘 자?'],'ans':0,'hint':('mean','뜻'),'explain':'what do you mean = 무슨 의미'},
            {'en':"I'm not sure.",'choices':['잘 모르겠어','확실해','졸려','피곤해'],'ans':0,'hint':('not sure','확실하지 않음'),'explain':'not sure = 모호'},
            {'en':"That sounds fun!",'choices':['재밌어 보여!','지루해 보여!','자고 싶어!','피곤해 보여!'],'ans':0,'hint':('fun','재미'),'explain':'sounds fun = 재밌게 들림'},
            {'en':"What's wrong?",'choices':['뭐가 문제야?','이름 뭐?','어디 가?','잘 자?'],'ans':0,'hint':('wrong','잘못된'),'explain':"what's wrong = 무슨 일?"},
            {'en':"I'm worried about you.",'choices':['네가 걱정돼','네가 좋아','네가 미워','네가 졸려'],'ans':0,'hint':('worried','걱정'),'explain':'worried about = 걱정'},
            {'en':"Take it easy.",'choices':['천천히 해','빨리 해','자','놀아'],'ans':0,'hint':('easy','쉬운'),'explain':'take it easy = 여유롭게'},
            {'en':"I'll do my best.",'choices':['최선을 다할게','대충 할게','자버릴게','놀아버릴게'],'ans':0,'hint':('best','최선'),'explain':'do my best = 최선'},
            {'en':"I owe you one.",'choices':['신세 졌어','싸웠어','잊었어','잘 자'],'ans':0,'hint':('owe','빚지다'),'explain':'owe = 신세'},
            {'en':"I changed my mind.",'choices':['마음 바뀌었어','이름 바꿨어','옷 바꿨어','음식 바꿨어'],'ans':0,'hint':('change','바꾸다'),'explain':'change mind = 마음 바꿈'},
            {'en':"Sounds like a plan!",'choices':['좋은 계획이야!','싫은 계획이야!','자야지!','놀자!'],'ans':0,'hint':('plan','계획'),'explain':'좋은 동의!'},
            {'en':"I can't wait!",'choices':['너무 기대돼!','기다리기 싫어!','자야지!','놀자!'],'ans':0,'hint':("can't wait",'기대'),'explain':"can't wait = 기대돼"},
            {'en':"It depends.",'choices':['상황에 따라','확실해','자','놀아'],'ans':0,'hint':('depend','달려있다'),'explain':'depends = 경우에 따라'},
            {'en':"I forgot.",'choices':['잊어버렸어','기억했어','졸려','피곤해'],'ans':0,'hint':('forgot','잊다'),'explain':'forgot = 까먹음'},
            {'en':"Hold on a sec!",'choices':['잠깐만!','빨리!','자!','놀아!'],'ans':0,'hint':('hold on','잠깐'),'explain':'잠깐 기다려'},
            {'en':"What a coincidence!",'choices':['우연이네!','이상해!','자!','놀자!'],'ans':0,'hint':('coincidence','우연'),'explain':'coincidence = 우연'},
            {'en':"Tell me more.",'choices':['더 말해줘','그만 말해','자','놀아'],'ans':0,'hint':('more','더'),'explain':'tell me more = 자세히'},
            {'en':"I see what you mean.",'choices':['이해돼','모르겠어','자','놀아'],'ans':0,'hint':('see','이해'),'explain':'알아 듣겠다'},
        ]
    },

    '20260726': {
        'date':'2026-07-26','day_ko':'일','theme':'다음 주 준비','theme_emoji':'🎒','description':'한 주 준비 영어!',
        'questions':[
            {'en':'A fresh start!','choices':['새 출발!','옛 끝!','자!','놀자!'],'ans':0,'hint':('fresh','새로운'),'explain':'fresh = 새 시작'},
            {'en':'Get ready!','choices':['준비해!','자!','놀아!','먹어!'],'ans':0,'hint':('ready','준비'),'explain':'ready = 준비'},
            {'en':'Pack your bag.','choices':['가방 싸기','자기','놀기','먹기'],'ans':0,'hint':('pack','싸다'),'explain':'pack = 짐 싸다'},
            {'en':'Set the alarm.','choices':['알람 맞추기','시계 봐','전화하기','자기'],'ans':0,'hint':('alarm','알람'),'explain':'set alarm = 알람'},
            {'en':'Go to bed early.','choices':['일찍 자기','늦게 자기','일찍 일어나기','늦게 일어나기'],'ans':0,'hint':('early','일찍'),'explain':'go to bed = 자다'},
            {'en':'Wake up on time.','choices':['제 시간에 일어나기','늦게 일어나기','자기','놀기'],'ans':0,'hint':('on time','제시간'),'explain':'on time = 제 시간에'},
            {'en':'Make your bed.','choices':['침대 정리','책 정리','옷 정리','신발 정리'],'ans':0,'hint':('make bed','침대정리'),'explain':'make bed = 이불 개기'},
            {'en':'Do homework first.','choices':['숙제 먼저','놀기 먼저','자기 먼저','먹기 먼저'],'ans':0,'hint':('homework','숙제'),'explain':'homework = 숙제'},
            {'en':'Pack lunchbox.','choices':['도시락 싸기','책 싸기','옷 싸기','신발 싸기'],'ans':0,'hint':('lunchbox','도시락'),'explain':'lunchbox = 도시락'},
            {'en':'Eat breakfast.','choices':['아침 먹기','점심 먹기','저녁 먹기','간식 먹기'],'ans':0,'hint':('breakfast','아침'),'explain':'breakfast = 아침'},
            {'en':'Brush your hair.','choices':['머리 빗기','이 닦기','손 씻기','얼굴 닦기'],'ans':0,'hint':('brush','빗다'),'explain':'brush hair = 머리'},
            {'en':'Tie your shoes.','choices':['신발 끈 묶기','옷 묶기','책 묶기','선물 묶기'],'ans':0,'hint':('tie','묶다'),'explain':'tie shoes = 끈 묶기'},
            {'en':'Pack school supplies.','choices':['학용품 챙기기','음식 챙기기','옷 챙기기','신발 챙기기'],'ans':0,'hint':('supplies','용품'),'explain':'school supplies = 학용품'},
            {'en':'Charge your phone.','choices':['전화 충전','전화 사기','전화 던지기','전화 보기'],'ans':0,'hint':('charge','충전'),'explain':'charge = 충전'},
            {'en':'Wash your face.','choices':['얼굴 씻기','발 씻기','이 닦기','머리 빗기'],'ans':0,'hint':('wash face','세수'),'explain':'wash face = 세수'},
            {'en':"Don't be late!",'choices':['늦지 마!','일찍 와!','자!','놀아!'],'ans':0,'hint':('late','늦은'),'explain':"don't be late = 늦지마"},
            {'en':'Have a great week!','choices':['멋진 한 주!','피곤한 한 주!','자는 한 주!','없는 한 주!'],'ans':0,'hint':('great','멋진'),'explain':'great week = 좋은 주'},
            {'en':'Stay focused.','choices':['집중해','자','놀아','먹어'],'ans':0,'hint':('focus','집중'),'explain':'stay focused = 집중'},
            {'en':"You've got this!",'choices':['넌 할 수 있어!','넌 못해!','자!','놀아!'],'ans':0,'hint':('got this','할 수 있다'),'explain':'got this = 가능!'},
            {'en':"Good luck!",'choices':['행운을!','잘 가!','자!','놀자!'],'ans':0,'hint':('luck','행운'),'explain':'good luck = 행운!'},
        ]
    },

    # ═════════════════════════════════════════════
    # 7/27~8/2 (Week 15) - 모양·직업·교통·숫자·축제
    # ═════════════════════════════════════════════
    '20260727': {
        'date':'2026-07-27','day_ko':'월','theme':'모양·패턴','theme_emoji':'🔷','description':'모양 영어!',
        'questions':[
            {'en':'An oval face.','choices':['타원형 얼굴','네모 얼굴','동그란 얼굴','세모 얼굴'],'ans':0,'hint':('oval','타원형'),'explain':'oval = 길쭉한 동그라미'},
            {'en':'Diamond shape.','choices':['마름모 모양','동그란 모양','세모 모양','네모 모양'],'ans':0,'hint':('diamond','마름모'),'explain':'diamond = 보석 모양'},
            {'en':'Hexagon honeycomb.','choices':['육각형 벌집','오각형 벌집','삼각형 벌집','사각형 벌집'],'ans':0,'hint':('hexagon','육각형'),'explain':'hexagon = 6변'},
            {'en':'Stop sign is octagon.','choices':['정지 표지 팔각형','정지 표지 사각형','정지 표지 원','정지 표지 별'],'ans':0,'hint':('octagon','팔각형'),'explain':'octagon = 8변'},
            {'en':'A pentagon star.','choices':['오각형 별','육각형 별','사각형 별','없음'],'ans':0,'hint':('pentagon','오각형'),'explain':'pentagon = 5변'},
            {'en':'An ice cube.','choices':['얼음 큐브','얼음 공','얼음 원','얼음 컵'],'ans':0,'hint':('cube','정육면체'),'explain':'cube = 6면 같음'},
            {'en':'A glass sphere.','choices':['유리 구','유리 컵','유리 잔','유리 책'],'ans':0,'hint':('sphere','구'),'explain':'sphere = 완벽한 공'},
            {'en':'A can is a cylinder.','choices':['캔은 원기둥','캔은 정육면체','캔은 구','캔은 원'],'ans':0,'hint':('cylinder','원기둥'),'explain':'cylinder = 둥근 기둥'},
            {'en':'Ice cream cone!','choices':['아이스크림 콘!','아이스크림 컵!','아이스크림 상자!','아이스크림 공!'],'ans':0,'hint':('cone','원뿔'),'explain':'cone = 위 뾰족'},
            {'en':'Zebra stripes.','choices':['얼룩말 줄무늬','얼룩말 점','얼룩말 큰 그림','얼룩말 도형'],'ans':0,'hint':('stripe','줄무늬'),'explain':'stripe = 길게 그어진 선'},
            {'en':'Polka dots.','choices':['물방울 무늬','별 무늬','세모 무늬','동그라미 무늬'],'ans':0,'hint':('dot','점'),'explain':'dot = 점'},
            {'en':'Checkered flag.','choices':['체크 깃발','민 깃발','꽃 깃발','별 깃발'],'ans':0,'hint':('checkered','체크무늬'),'explain':'checkered = 네모 패턴'},
            {'en':'Plaid shirt.','choices':['격자 셔츠','민 셔츠','꽃 셔츠','별 셔츠'],'ans':0,'hint':('plaid','격자'),'explain':'plaid = 교차 선'},
            {'en':'A zigzag line.','choices':['지그재그 선','직선','곡선','없음'],'ans':0,'hint':('zigzag','지그재그'),'explain':'zigzag = 왔다 갔다'},
            {'en':'A smooth curve.','choices':['매끄러운 곡선','매끄러운 직선','매끄러운 점','매끄러운 별'],'ans':0,'hint':('curve','곡선'),'explain':'curve = 휘어진 선'},
            {'en':'Right angle.','choices':['직각','곡각','없음','다 같음'],'ans':0,'hint':('angle','각도'),'explain':'right angle = 90도'},
            {'en':'Perfect symmetry!','choices':['완벽한 대칭!','완벽한 차이!','완벽한 색!','완벽한 크기!'],'ans':0,'hint':('symmetry','대칭'),'explain':'symmetry = 양쪽 같음'},
            {'en':'A swirl pattern.','choices':['소용돌이 무늬','직선 무늬','곡선 무늬','별 무늬'],'ans':0,'hint':('swirl','소용돌이'),'explain':'swirl = 빙글빙글'},
            {'en':'A crescent moon.','choices':['초승달','보름달','별','해'],'ans':0,'hint':('crescent','초승달'),'explain':'crescent = C 모양'},
            {'en':'A spiral shell.','choices':['나선형 조개','직선 조개','별 조개','없음'],'ans':0,'hint':('spiral','나선'),'explain':'spiral = 빙빙'},
        ]
    },

    '20260728': {
        'date':'2026-07-28','day_ko':'화','theme':'직업 표현','theme_emoji':'💼','description':'직업 영어!',
        'questions':[
            {'en':'The waiter brings food.','choices':['웨이터가 음식을','요리사가 음식을','손님이 음식을','자기'],'ans':0,'hint':('waiter','웨이터'),'explain':'waiter = 서빙'},
            {'en':'Call a plumber.','choices':['배관공 불러요','경찰 불러요','의사 불러요','학생 불러요'],'ans':0,'hint':('plumber','배관공'),'explain':'plumber = 수도 고침'},
            {'en':'A car mechanic.','choices':['자동차 정비공','자동차 운전사','자동차 디자이너','자동차 청소부'],'ans':0,'hint':('mechanic','정비공'),'explain':'mechanic = 기계 고침'},
            {'en':'A skilled carpenter.','choices':['솜씨 좋은 목수','솜씨 좋은 의사','솜씨 좋은 학생','솜씨 좋은 가수'],'ans':0,'hint':('carpenter','목수'),'explain':'carpenter = 나무 만듦'},
            {'en':'Call an electrician.','choices':['전기 기사 불러요','학생 불러요','의사 불러요','경찰 불러요'],'ans':0,'hint':('electrician','전기기사'),'explain':'electrician = 전선 고침'},
            {'en':'A kind gardener.','choices':['친절한 정원사','친절한 의사','친절한 학생','친절한 어부'],'ans':0,'hint':('gardener','정원사'),'explain':'gardener = 식물 가꿈'},
            {'en':'Visit the hairdresser.','choices':['미용사 방문','의사 방문','학생 방문','선생님 방문'],'ans':0,'hint':('hairdresser','미용사'),'explain':'hairdresser = 머리 자름'},
            {'en':'A pro photographer.','choices':['프로 사진작가','프로 가수','프로 학생','프로 의사'],'ans':0,'hint':('photographer','사진작가'),'explain':'photographer = 사진 찍음'},
            {'en':'A news reporter.','choices':['뉴스 기자','뉴스 모델','뉴스 의사','뉴스 학생'],'ans':0,'hint':('reporter','기자'),'explain':'reporter = 소식 전함'},
            {'en':'The judge decides.','choices':['판사가 결정','학생이 결정','의사가 결정','요리사가 결정'],'ans':0,'hint':('judge','판사'),'explain':'judge = 법정 결정자'},
            {'en':'A famous architect.','choices':['유명 건축가','유명 의사','유명 가수','유명 학생'],'ans':0,'hint':('architect','건축가'),'explain':'architect = 건물 설계'},
            {'en':'My math professor.','choices':['수학 교수님','수학 학생','수학 책','수학 시험'],'ans':0,'hint':('professor','교수'),'explain':'professor = 대학 교수'},
            {'en':'A brave sailor.','choices':['용감한 선원','용감한 의사','용감한 학생','용감한 가수'],'ans':0,'hint':('sailor','선원'),'explain':'sailor = 배에서 일함'},
            {'en':'A great magician.','choices':['멋진 마술사','멋진 의사','멋진 학생','멋진 가수'],'ans':0,'hint':('magician','마술사'),'explain':'magician = 마술 부림'},
            {'en':'A funny comedian.','choices':['웃긴 코미디언','웃긴 의사','웃긴 학생','웃긴 가수'],'ans':0,'hint':('comedian','코미디언'),'explain':'comedian = 웃겨주는 사람'},
            {'en':'A fashion model.','choices':['패션 모델','패션 의사','패션 학생','패션 가수'],'ans':0,'hint':('model','모델'),'explain':'model = 옷 보여줌'},
            {'en':'A skilled florist.','choices':['솜씨 좋은 꽃집 주인','솜씨 좋은 의사','솜씨 좋은 학생','솜씨 좋은 어부'],'ans':0,'hint':('florist','꽃집'),'explain':'florist = 꽃 다발'},
            {'en':'A clever detective.','choices':['영리한 탐정','영리한 의사','영리한 학생','영리한 가수'],'ans':0,'hint':('detective','탐정'),'explain':'detective = 수수께끼 풂'},
            {'en':'A skilled fisherman.','choices':['노련한 어부','노련한 의사','노련한 학생','노련한 가수'],'ans':0,'hint':('fisherman','어부'),'explain':'fisherman = 물고기 잡음'},
            {'en':'Visit the barber.','choices':['이발사 방문','의사 방문','학생 방문','선생님 방문'],'ans':0,'hint':('barber','이발사'),'explain':'barber = 남자 머리'},
        ]
    },

    '20260729': {
        'date':'2026-07-29','day_ko':'수','theme':'교통수단','theme_emoji':'🏎️','description':'교통 영어!',
        'questions':[
            {'en':'A new sedan.','choices':['새 세단','새 트럭','새 자전거','새 배'],'ans':0,'hint':('sedan','세단'),'explain':'sedan = 승용차'},
            {'en':'A big SUV.','choices':['큰 SUV','큰 자전거','큰 비행기','큰 배'],'ans':0,'hint':('suv','SUV'),'explain':'SUV = 높은 차'},
            {'en':'A red convertible.','choices':['빨간 오픈카','빨간 비행기','빨간 배','빨간 자전거'],'ans':0,'hint':('convertible','오픈카'),'explain':'convertible = 지붕 열림'},
            {'en':'Ride a motorcycle.','choices':['오토바이 타기','자전거 타기','버스 타기','지하철 타기'],'ans':0,'hint':('motorcycle','오토바이'),'explain':'motorcycle = 두 바퀴'},
            {'en':'A kick scooter.','choices':['킥보드','자전거','오토바이','자동차'],'ans':0,'hint':('scooter','스쿠터'),'explain':'scooter = 작은 차'},
            {'en':'A flying helicopter.','choices':['나는 헬리콥터','나는 새','나는 비행기','나는 풍선'],'ans':0,'hint':('helicopter','헬리콥터'),'explain':'helicopter = 위 날개'},
            {'en':'A yellow submarine.','choices':['노란 잠수함','노란 비행기','노란 배','노란 자동차'],'ans':0,'hint':('submarine','잠수함'),'explain':'submarine = 물 속'},
            {'en':'A fast jet.','choices':['빠른 제트기','빠른 자전거','빠른 자동차','빠른 배'],'ans':0,'hint':('jet','제트기'),'explain':'jet = 매우 빠름'},
            {'en':'A delivery van.','choices':['배달 승합차','배달 자전거','배달 사람','배달 음식'],'ans':0,'hint':('van','승합차'),'explain':'van = 많이 탑승'},
            {'en':'Call an ambulance.','choices':['구급차 불러','경찰 불러','소방차 불러','택시 불러'],'ans':0,'hint':('ambulance','구급차'),'explain':'ambulance = 응급'},
            {'en':'A red firetruck.','choices':['빨간 소방차','빨간 자동차','빨간 자전거','빨간 비행기'],'ans':0,'hint':('firetruck','소방차'),'explain':'firetruck = 불 끔'},
            {'en':'Call a taxicab.','choices':['택시 불러','버스 불러','자전거 불러','걸어'],'ans':0,'hint':('taxicab','택시'),'explain':'taxicab = yellow cab'},
            {'en':'A rocket ship!','choices':['우주선!','자동차!','자전거!','비행기!'],'ans':0,'hint':('rocket ship','우주선'),'explain':'rocket = 우주로'},
            {'en':'A white sailboat.','choices':['하얀 돛단배','하얀 자동차','하얀 비행기','하얀 자전거'],'ans':0,'hint':('sailboat','돛단배'),'explain':'sailboat = 돛으로'},
            {'en':'Paddle a canoe.','choices':['카누를 저어','자전거 타','자동차 운전','달려'],'ans':0,'hint':('canoe','카누'),'explain':'canoe = 좁은 배'},
            {'en':'Press the brake!','choices':['브레이크 밟아!','액셀 밟아!','경적 울려!','문 닫아!'],'ans':0,'hint':('brake','브레이크'),'explain':'brake = 멈춤'},
            {'en':'Press the pedal.','choices':['페달 밟아','버튼 눌러','문 열어','자'],'ans':0,'hint':('pedal','페달'),'explain':'pedal = 발판'},
            {'en':'Flat tire!','choices':['펑크 난 타이어!','새 타이어!','큰 타이어!','작은 타이어!'],'ans':0,'hint':('tire','타이어'),'explain':'tire = 바퀴'},
            {'en':'Through the tunnel.','choices':['터널 통과','도로 통과','다리 통과','학교 통과'],'ans':0,'hint':('tunnel','터널'),'explain':'tunnel = 산 아래'},
            {'en':'At the intersection.','choices':['교차로에서','학교에서','집에서','공원에서'],'ans':0,'hint':('intersection','교차로'),'explain':'intersection = 길 만남'},
        ]
    },

    '20260730': {
        'date':'2026-07-30','day_ko':'목','theme':'숫자·계산','theme_emoji':'🔢','description':'숫자 영어!',
        'questions':[
            {'en':'One thousand.','choices':['천','백','만','억'],'ans':0,'hint':('thousand','천'),'explain':'thousand = 1,000'},
            {'en':'A million stars.','choices':['백만 개 별','천 개 별','만 개 별','억 개 별'],'ans':0,'hint':('million','백만'),'explain':'million = 1,000,000'},
            {'en':'A billion years.','choices':['십억 년','백만 년','천만 년','만 년'],'ans':0,'hint':('billion','십억'),'explain':'billion = 10억'},
            {'en':'A dozen eggs.','choices':['계란 12개','계란 10개','계란 6개','계란 20개'],'ans':0,'hint':('dozen','12개'),'explain':'dozen = 12'},
            {'en':'A pair of shoes.','choices':['신발 한 켤레','신발 한 짝','신발 많이','신발 없음'],'ans':0,'hint':('pair','쌍'),'explain':'pair = 2개 한 묶음'},
            {'en':'Two plus two.','choices':['2 더하기 2','2 빼기 2','2 곱하기 2','2 나누기 2'],'ans':0,'hint':('plus','+'),'explain':'plus = 더하기'},
            {'en':'Five minus one.','choices':['5 빼기 1','5 더하기 1','5 곱하기 1','5 나누기 1'],'ans':0,'hint':('minus','-'),'explain':'minus = 빼기'},
            {'en':'Three times four.','choices':['3 곱하기 4','3 더하기 4','3 빼기 4','3 나누기 4'],'ans':0,'hint':('times','×'),'explain':'times = 곱하기'},
            {'en':'Ten divided by two.','choices':['10 나누기 2','10 빼기 2','10 더하기 2','10 곱하기 2'],'ans':0,'hint':('divided','÷'),'explain':'divided = 나누기'},
            {'en':'Equal numbers.','choices':['같은 숫자','다른 숫자','큰 숫자','작은 숫자'],'ans':0,'hint':('equal','='),'explain':'equal = 같음'},
            {'en':'Odd number.','choices':['홀수','짝수','없음','큰수'],'ans':0,'hint':('odd','홀수'),'explain':'odd = 1,3,5...'},
            {'en':'Even number.','choices':['짝수','홀수','없음','큰수'],'ans':0,'hint':('even','짝수'),'explain':'even = 2,4,6...'},
            {'en':'Learn fractions.','choices':['분수 배워','소수 배워','음수 배워','없음'],'ans':0,'hint':('fraction','분수'),'explain':'fraction = 1/2 같은'},
            {'en':'Decimal point.','choices':['소수점','분수점','정수점','없음'],'ans':0,'hint':('decimal','소수'),'explain':'decimal = 0.5 같은'},
            {'en':'Fifty percent.','choices':['50 퍼센트','5 퍼센트','500 퍼센트','없음'],'ans':0,'hint':('percent','%'),'explain':'percent = %'},
            {'en':'Calculate the sum.','choices':['합 계산','뺄셈 계산','곱셈 계산','나눗셈 계산'],'ans':0,'hint':('calculate','계산'),'explain':'calculate = 계산하기'},
            {'en':'The total sum.','choices':['총합','평균','최소','최대'],'ans':0,'hint':('sum','합'),'explain':'sum = 다 더한 값'},
            {'en':'Total price.','choices':['총 가격','평균 가격','싼 가격','비싼 가격'],'ans':0,'hint':('total','총'),'explain':'total = 합계'},
            {'en':'Find the average.','choices':['평균 구해','최대 구해','최소 구해','없음'],'ans':0,'hint':('average','평균'),'explain':'average = 가운데'},
            {'en':'Roman numeral.','choices':['로마 숫자','한국 숫자','중국 숫자','일본 숫자'],'ans':0,'hint':('numeral','숫자'),'explain':'numeral = I, II, III'},
        ]
    },

    '20260731': {
        'date':'2026-07-31','day_ko':'금','theme':'축제·이벤트','theme_emoji':'🎉','description':'축제 영어!',
        'questions':[
            {'en':'A fun carnival.','choices':['재밌는 카니발','지루한 카니발','새 카니발','오래된 카니발'],'ans':0,'hint':('carnival','카니발'),'explain':'carnival = 큰 야외 축제'},
            {'en':'Watch the circus.','choices':['서커스 봐요','영화 봐요','TV 봐요','자기'],'ans':0,'hint':('circus','서커스'),'explain':'circus = 광대·곡예'},
            {'en':'A funny clown.','choices':['웃긴 광대','웃긴 곰','웃긴 강아지','웃긴 새'],'ans':0,'hint':('clown','광대'),'explain':'clown = 웃겨줌'},
            {'en':'A skilled acrobat.','choices':['능숙한 곡예사','능숙한 의사','능숙한 학생','능숙한 가수'],'ans':0,'hint':('acrobat','곡예사'),'explain':'acrobat = 공중 묘기'},
            {'en':'A juggler at the park.','choices':['공원의 저글러','공원의 학생','공원의 의사','공원의 친구'],'ans':0,'hint':('juggler','저글러'),'explain':'juggler = 공 던지기'},
            {'en':'Ride the ferris wheel.','choices':['대관람차 타기','자전거 타기','자동차 타기','버스 타기'],'ans':0,'hint':('ferris wheel','대관람차'),'explain':'ferris wheel = 큰 바퀴'},
            {'en':'Fast roller coaster!','choices':['빠른 롤러코스터!','빠른 자전거!','빠른 차!','빠른 버스!'],'ans':0,'hint':('roller coaster','롤러코스터'),'explain':'롤러코스터'},
            {'en':'Watch the parade.','choices':['퍼레이드 봐','자','놀아','먹어'],'ans':0,'hint':('parade','퍼레이드'),'explain':'parade = 행진'},
            {'en':'A music festival.','choices':['음악 축제','음악 학교','음악 시험','음악 책'],'ans':0,'hint':('festival','축제'),'explain':'festival = 즐거운 행사'},
            {'en':'Opening ceremony.','choices':['개막식','폐막식','졸업식','시험식'],'ans':0,'hint':('ceremony','의식'),'explain':'ceremony = 공식 행사'},
            {'en':'Win an award!','choices':['상 받기!','자기!','놀기!','먹기!'],'ans':0,'hint':('award','상'),'explain':'award = 잘했을 때 받음'},
            {'en':'First prize!','choices':['1등상!','꼴찌!','없음!','보통!'],'ans':0,'hint':('prize','상'),'explain':'prize = 이긴 사람 선물'},
            {'en':'The announcer speaks.','choices':['아나운서 말해','학생 말해','선생님 말해','부모님 말해'],'ans':0,'hint':('announcer','아나운서'),'explain':'announcer = 무대 안내'},
            {'en':'Singing contest!','choices':['노래 대회!','수학 대회!','체육 대회!','없음!'],'ans':0,'hint':('contest','대회'),'explain':'contest = 누가 잘하나'},
            {'en':'A tough competition.','choices':['치열한 시합','쉬운 시합','새 시합','오래된 시합'],'ans':0,'hint':('competition','시합'),'explain':'competition = 겨룸'},
            {'en':'Hang the banner.','choices':['현수막 걸기','옷 걸기','사진 걸기','책 걸기'],'ans':0,'hint':('banner','현수막'),'explain':'banner = 큰 천 광고'},
            {'en':'A huge crowd.','choices':['엄청난 군중','엄청난 산','엄청난 강','엄청난 책'],'ans':0,'hint':('crowd','군중'),'explain':'crowd = 많은 사람'},
            {'en':'A charity gala.','choices':['자선 갈라','자선 학교','자선 시장','자선 책'],'ans':0,'hint':('gala','갈라쇼'),'explain':'gala = 큰 행사'},
            {'en':'A wooden plaque.','choices':['나무 상패','나무 의자','나무 책','나무 그릇'],'ans':0,'hint':('plaque','상패'),'explain':'plaque = 벽 상패'},
            {'en':'Watch fireworks!','choices':['불꽃놀이 봐!','불 봐!','해 봐!','달 봐!'],'ans':0,'hint':('fireworks','불꽃놀이'),'explain':'fireworks = 하늘 불꽃'},
        ]
    },

    '20260801': {
        'date':'2026-08-01','day_ko':'토','theme':'여름 야외 활동','theme_emoji':'☀️','description':'8월 여름 영어!',
        'questions':[
            {'en':"It's August!",'choices':['8월이야!','7월이야!','6월이야!','5월이야!'],'ans':0,'hint':('August','8월'),'explain':'August = 8월'},
            {'en':'Hot summer!','choices':['더운 여름!','추운 겨울!','맑은 봄!','시원한 가을!'],'ans':0,'hint':('hot','더운'),'explain':'summer = 여름'},
            {'en':"Let's go to the pool.",'choices':['수영장 가자','학교 가자','시장 가자','집 가자'],'ans':0,'hint':('pool','수영장'),'explain':'pool = 수영장'},
            {'en':'Wear sunscreen!','choices':['선크림 발라!','옷 입어!','신발 신어!','모자 써!'],'ans':0,'hint':('sunscreen','선크림'),'explain':'sunscreen = 햇볕 막기'},
            {'en':'Eat watermelon.','choices':['수박 먹기','사과 먹기','바나나 먹기','포도 먹기'],'ans':0,'hint':('watermelon','수박'),'explain':'watermelon = 여름 과일'},
            {'en':'Drink cold water.','choices':['차가운 물 마시기','뜨거운 물','우유 마시기','주스 마시기'],'ans':0,'hint':('cold','차가운'),'explain':'cold = 시원함'},
            {'en':"Let's go camping.",'choices':['캠핑 가자','학교 가자','집 가자','시장 가자'],'ans':0,'hint':('camping','캠핑'),'explain':'camping = 야외 잠'},
            {'en':'Family vacation!','choices':['가족 휴가!','가족 학교!','가족 시장!','가족 집!'],'ans':0,'hint':('vacation','휴가'),'explain':'vacation = 휴가'},
            {'en':'Catch fireflies!','choices':['반딧불이 잡기!','새 잡기!','강아지 잡기!','쥐 잡기!'],'ans':0,'hint':('firefly','반딧불이'),'explain':'firefly = 밤에 반짝'},
            {'en':"It's so humid.",'choices':['너무 습해','너무 건조해','너무 추워','너무 더워'],'ans':0,'hint':('humid','습한'),'explain':'humid = 끈적'},
            {'en':'Play in the sprinkler.','choices':['스프링클러에서 놀기','학교에서 놀기','집에서 놀기','시장에서 놀기'],'ans':0,'hint':('sprinkler','스프링클러'),'explain':'sprinkler = 물 뿌리는 기계'},
            {'en':'Build a sandcastle!','choices':['모래성 만들기!','집 만들기!','학교 만들기!','책 만들기!'],'ans':0,'hint':('sandcastle','모래성'),'explain':'sandcastle = 해변 놀이'},
            {'en':'Watch fireworks!','choices':['불꽃놀이 봐!','TV 봐!','책 봐!','별 봐!'],'ans':0,'hint':('fireworks','불꽃놀이'),'explain':'fireworks = 하늘 불꽃'},
            {'en':'Sleep with AC on.','choices':['에어컨 켜고 자기','에어컨 꺼고 자기','TV 켜고 자기','불 켜고 자기'],'ans':0,'hint':('AC','에어컨'),'explain':'AC = air conditioner'},
            {'en':"Don't forget your hat!",'choices':['모자 챙겨!','옷 챙겨!','신발 챙겨!','가방 챙겨!'],'ans':0,'hint':('hat','모자'),'explain':'hat = 모자'},
            {'en':'Stay hydrated!','choices':['수분 보충해!','자!','놀아!','먹어!'],'ans':0,'hint':('hydrated','수분 보충'),'explain':'물 마시자'},
            {'en':'BBQ time!','choices':['바비큐 시간!','학교 시간!','시험 시간!','자는 시간!'],'ans':0,'hint':('BBQ','바비큐'),'explain':'BBQ = 굽기'},
            {'en':"It's a beautiful sunset.",'choices':['아름다운 일몰','아름다운 일출','아름다운 비','아름다운 눈'],'ans':0,'hint':('sunset','일몰'),'explain':'sunset = 해질녘'},
            {'en':'Beach day!','choices':['해변에 가는 날!','학교 가는 날!','집 청소!','시험 날!'],'ans':0,'hint':('beach','해변'),'explain':'beach = 바닷가'},
            {'en':'I love summer!','choices':['여름 좋아!','겨울 좋아!','봄 좋아!','가을 좋아!'],'ans':0,'hint':('summer','여름'),'explain':'love summer = 여름 좋아'},
        ]
    },

    '20260802': {
        'date':'2026-08-02','day_ko':'일','theme':'8월의 시작','theme_emoji':'🌞','description':'새 달 시작 영어!',
        'questions':[
            {'en':'New month, new start!','choices':['새 달, 새 시작!','옛 달, 옛 시작!','자!','놀자!'],'ans':0,'hint':('new','새로운'),'explain':'new start = 새 출발'},
            {'en':'A new goal.','choices':['새 목표','옛 목표','없는 목표','짧은 목표'],'ans':0,'hint':('goal','목표'),'explain':'goal = 이루고 싶은 것'},
            {'en':'Make a plan.','choices':['계획 세우기','자기','놀기','먹기'],'ans':0,'hint':('plan','계획'),'explain':'plan = 계획'},
            {'en':'Stay healthy!','choices':['건강 유지!','아프기!','자!','놀자!'],'ans':0,'hint':('healthy','건강'),'explain':'healthy = 튼튼'},
            {'en':'Drink lots of water.','choices':['물 많이 마셔','우유 많이','주스 많이','없음'],'ans':0,'hint':('water','물'),'explain':'drink water = 물 마시기'},
            {'en':'Eat fruits!','choices':['과일 먹어!','과자 먹어!','케이크 먹어!','초콜릿 먹어!'],'ans':0,'hint':('fruit','과일'),'explain':'fruit = 과일'},
            {'en':'Exercise daily.','choices':['매일 운동','매일 자','매일 놀아','매일 먹어'],'ans':0,'hint':('exercise','운동'),'explain':'daily = 매일'},
            {'en':'Read more books.','choices':['책 더 많이 읽어','자','놀아','먹어'],'ans':0,'hint':('read','읽다'),'explain':'read books = 책 읽기'},
            {'en':'Help others.','choices':['남을 도와','남을 미워','자','놀아'],'ans':0,'hint':('help','돕다'),'explain':'help = 도와주기'},
            {'en':'Smile every day!','choices':['매일 웃기!','매일 울기!','매일 자기!','매일 먹기!'],'ans':0,'hint':('smile','미소'),'explain':'smile = 웃기'},
            {'en':'Try something new.','choices':['새로운 것 시도','옛것 시도','자','놀기'],'ans':0,'hint':('try','시도'),'explain':'try new = 새 도전'},
            {'en':'Save your money.','choices':['돈 아끼기','돈 쓰기','돈 잃기','돈 없음'],'ans':0,'hint':('save','아끼다'),'explain':'save = 저축'},
            {'en':'Be kind.','choices':['친절해','무례해','조용해','시끄러워'],'ans':0,'hint':('kind','친절'),'explain':'be kind = 친절히'},
            {'en':'Be brave.','choices':['용감해','겁먹어','자','놀아'],'ans':0,'hint':('brave','용감'),'explain':'be brave = 용기'},
            {'en':'Stay positive.','choices':['긍정적으로','부정적으로','자','놀아'],'ans':0,'hint':('positive','긍정'),'explain':'positive = 좋은 생각'},
            {'en':'Learn every day.','choices':['매일 배워','매일 자','매일 놀아','매일 먹어'],'ans':0,'hint':('learn','배우다'),'explain':'learn = 배움'},
            {'en':'Make new friends.','choices':['새 친구 만들기','옛 친구만','자기','놀기'],'ans':0,'hint':('friend','친구'),'explain':'make friends = 친구 사귀기'},
            {'en':'Spend time with family.','choices':['가족과 시간 보내기','혼자 자기','학교에서 시간','시장에서 시간'],'ans':0,'hint':('family','가족'),'explain':'family time = 가족 시간'},
            {'en':"You're doing great!",'choices':['너 잘하고 있어!','너 못해!','너 자!','너 가!'],'ans':0,'hint':('great','잘'),'explain':'great = 멋지게'},
            {'en':"Let's have a great August!",'choices':['멋진 8월 보내자!','피곤한 8월!','자!','놀자!'],'ans':0,'hint':('August','8월'),'explain':'August = 8월'},
        ]
    },

    # ═════════════════════════════════════════════
    # 8/3~8/9 (Week 16) - 새·양념·디저트·별자리·응급
    # ═════════════════════════════════════════════
    '20260803': {
        'date':'2026-08-03','day_ko':'월','theme':'새와 조류','theme_emoji':'🦅','description':'새 영어!',
        'questions':[
            {'en':'A flying eagle.','choices':['나는 독수리','나는 새','나는 비행기','나는 사람'],'ans':0,'hint':('eagle','독수리'),'explain':'eagle = 새의 왕'},
            {'en':'A wise owl.','choices':['현명한 부엉이','현명한 강아지','현명한 새','현명한 곰'],'ans':0,'hint':('owl','부엉이'),'explain':'owl = 밤 새'},
            {'en':'A colorful parrot.','choices':['화려한 앵무새','화려한 비둘기','화려한 까마귀','화려한 매'],'ans':0,'hint':('parrot','앵무새'),'explain':'parrot = 말해요'},
            {'en':'A beautiful peacock.','choices':['아름다운 공작','아름다운 닭','아름다운 오리','아름다운 거위'],'ans':0,'hint':('peacock','공작'),'explain':'peacock = 꼬리 화려'},
            {'en':'A pink flamingo.','choices':['분홍 홍학','분홍 새','분홍 강아지','분홍 곰'],'ans':0,'hint':('flamingo','홍학'),'explain':'flamingo = 한 다리'},
            {'en':'A white swan.','choices':['하얀 백조','하얀 닭','하얀 새','하얀 강아지'],'ans':0,'hint':('swan','백조'),'explain':'swan = 우아함'},
            {'en':'A black crow.','choices':['검은 까마귀','검은 매','검은 새','검은 강아지'],'ans':0,'hint':('crow','까마귀'),'explain':'crow = 똑똑함'},
            {'en':'A small sparrow.','choices':['작은 참새','작은 강아지','작은 새','작은 닭'],'ans':0,'hint':('sparrow','참새'),'explain':'sparrow = 우리 동네'},
            {'en':'City pigeons.','choices':['도시 비둘기','산 비둘기','집 비둘기','학교 비둘기'],'ans':0,'hint':('pigeon','비둘기'),'explain':'pigeon = 평화'},
            {'en':'A sharp-eyed hawk.','choices':['눈 좋은 매','눈 좋은 새','눈 좋은 강아지','눈 좋은 사람'],'ans':0,'hint':('hawk','매'),'explain':'hawk = 사냥꾼'},
            {'en':'A loud woodpecker.','choices':['시끄러운 딱따구리','시끄러운 새','시끄러운 강아지','시끄러운 사람'],'ans':0,'hint':('woodpecker','딱따구리'),'explain':'woodpecker = 나무 쪼기'},
            {'en':'A graceful crane.','choices':['우아한 두루미','우아한 새','우아한 곰','우아한 강아지'],'ans':0,'hint':('crane','두루미'),'explain':'crane = 긴 목'},
            {'en':'A tiny hummingbird.','choices':['작은 벌새','작은 새','작은 곤충','작은 나비'],'ans':0,'hint':('hummingbird','벌새'),'explain':'hummingbird = 날개 빨라요'},
            {'en':'A fast falcon.','choices':['빠른 송골매','빠른 강아지','빠른 새','빠른 자동차'],'ans':0,'hint':('falcon','송골매'),'explain':'falcon = 가장 빠름'},
            {'en':'A toucan beak.','choices':['투칸 부리','투칸 다리','투칸 머리','투칸 발'],'ans':0,'hint':('toucan','투칸'),'explain':'toucan = 부리 커요'},
            {'en':'A sharp beak.','choices':['날카로운 부리','날카로운 발톱','날카로운 칼','날카로운 가위'],'ans':0,'hint':('beak','부리'),'explain':'beak = 새의 입'},
            {'en':'A soft feather.','choices':['부드러운 깃털','부드러운 옷','부드러운 머리','부드러운 손'],'ans':0,'hint':('feather','깃털'),'explain':'feather = 가벼움'},
            {'en':'Birds in a nest.','choices':['둥지 속 새들','집 속 새','학교 속 새','시장 속 새'],'ans':0,'hint':('nest','둥지'),'explain':'nest = 새의 집'},
            {'en':'Birds chirp.','choices':['새들이 짹짹','새들이 자','새들이 먹어','새들이 놀아'],'ans':0,'hint':('chirp','짹짹'),'explain':'chirp = 새 소리'},
            {'en':'A flock of birds.','choices':['새 한 무리','새 한 마리','새 두 마리','없음'],'ans':0,'hint':('flock','떼'),'explain':'flock = 여러 마리'},
        ]
    },

    '20260804': {
        'date':'2026-08-04','day_ko':'화','theme':'양념과 향신료','theme_emoji':'🧂','description':'요리 영어!',
        'questions':[
            {'en':'Add salt.','choices':['소금 넣어','설탕 넣어','후추 넣어','없음'],'ans':0,'hint':('salt','소금'),'explain':'salt = 짠 맛'},
            {'en':'Black pepper.','choices':['검은 후추','검은 깨','검은 소금','검은 설탕'],'ans':0,'hint':('pepper','후추'),'explain':'pepper = 매콤'},
            {'en':'Ginger tea.','choices':['생강차','녹차','홍차','없음'],'ans':0,'hint':('ginger','생강'),'explain':'ginger = 감기'},
            {'en':'Slice the paprika.','choices':['파프리카 썰어','양파 썰어','감자 썰어','당근 썰어'],'ans':0,'hint':('paprika','파프리카'),'explain':'paprika = 붉은 가루'},
            {'en':'Fresh thyme.','choices':['신선한 타임','신선한 양파','신선한 마늘','신선한 사과'],'ans':0,'hint':('thyme','타임'),'explain':'thyme = 허브'},
            {'en':'Tomato sauce.','choices':['토마토 소스','토마토 주스','토마토 케이크','토마토 빵'],'ans':0,'hint':('sauce','소스'),'explain':'sauce = 음식 곁들임'},
            {'en':'Maple syrup.','choices':['메이플 시럽','꿀','우유','주스'],'ans':0,'hint':('syrup','시럽'),'explain':'syrup = 달콤한 액체'},
            {'en':'Apple vinegar.','choices':['사과 식초','사과 주스','사과 잼','사과 차'],'ans':0,'hint':('vinegar','식초'),'explain':'vinegar = 신 맛'},
            {'en':'Olive oil.','choices':['올리브 기름','올리브 잼','올리브 차','올리브 주스'],'ans':0,'hint':('oil','기름'),'explain':'oil = 요리 기름'},
            {'en':'Spread butter.','choices':['버터 발라','잼 발라','꿀 발라','마요 발라'],'ans':0,'hint':('butter','버터'),'explain':'butter = 빵에 발라'},
            {'en':'Add mustard.','choices':['겨자 넣어','꿀 넣어','잼 넣어','우유 넣어'],'ans':0,'hint':('mustard','겨자'),'explain':'mustard = 노란 양념'},
            {'en':'Mayonnaise sauce.','choices':['마요네즈 소스','케첩 소스','꿀 소스','잼 소스'],'ans':0,'hint':('mayonnaise','마요네즈'),'explain':'mayonnaise = 흰 소스'},
            {'en':'Tomato ketchup.','choices':['토마토 케첩','토마토 잼','토마토 차','토마토 우유'],'ans':0,'hint':('ketchup','케첩'),'explain':'ketchup = 빨간 소스'},
            {'en':'Cinnamon roll.','choices':['계피 롤','버터 롤','꿀 롤','초콜릿 롤'],'ans':0,'hint':('cinnamon','계피'),'explain':'cinnamon = 달콤한 향'},
            {'en':'Fresh herbs.','choices':['신선한 허브','신선한 빵','신선한 우유','신선한 책'],'ans':0,'hint':('herb','허브'),'explain':'herb = 향 풀'},
            {'en':'Hot chili.','choices':['매운 고추','매운 양파','매운 빵','매운 우유'],'ans':0,'hint':('chili','고추'),'explain':'chili = 매워요'},
            {'en':'Fresh basil.','choices':['신선한 바질','신선한 시금치','신선한 양파','신선한 사과'],'ans':0,'hint':('basil','바질'),'explain':'basil = 이탈리아 향초'},
            {'en':'Dip in soy sauce.','choices':['간장에 찍어','케첩에 찍어','마요에 찍어','꿀에 찍어'],'ans':0,'hint':('soy sauce','간장'),'explain':'soy sauce = 한국 필수'},
            {'en':'Sesame oil.','choices':['참기름','올리브 기름','버터','마요'],'ans':0,'hint':('sesame','참깨'),'explain':'sesame = 고소한 향'},
            {'en':'Add spices.','choices':['향신료 넣어','물 넣어','우유 넣어','잼 넣어'],'ans':0,'hint':('spice','향신료'),'explain':'spice = 맛 더해요'},
        ]
    },

    '20260805': {
        'date':'2026-08-05','day_ko':'수','theme':'디저트·간식','theme_emoji':'🍩','description':'디저트 영어!',
        'questions':[
            {'en':'A sweet donut.','choices':['달콤한 도넛','달콤한 빵','달콤한 사탕','달콤한 케이크'],'ans':0,'hint':('donut','도넛'),'explain':'donut = 동그란 빵'},
            {'en':'A fruit tart.','choices':['과일 타르트','과일 케이크','과일 주스','과일 빵'],'ans':0,'hint':('tart','타르트'),'explain':'tart = 미니 파이'},
            {'en':'Apple pie.','choices':['사과 파이','사과 주스','사과 케이크','사과 빵'],'ans':0,'hint':('pie','파이'),'explain':'pie = 속이 가득'},
            {'en':'Vanilla pudding.','choices':['바닐라 푸딩','바닐라 우유','바닐라 빵','바닐라 사탕'],'ans':0,'hint':('pudding','푸딩'),'explain':'pudding = 말랑말랑'},
            {'en':'Chocolate brownie.','choices':['초콜릿 브라우니','초콜릿 사탕','초콜릿 우유','초콜릿 빵'],'ans':0,'hint':('brownie','브라우니'),'explain':'brownie = 진한 케이크'},
            {'en':'Blueberry muffin.','choices':['블루베리 머핀','블루베리 케이크','블루베리 주스','블루베리 잼'],'ans':0,'hint':('muffin','머핀'),'explain':'muffin = 컵 케이크'},
            {'en':'Crispy waffle.','choices':['바삭한 와플','바삭한 빵','바삭한 사탕','바삭한 케이크'],'ans':0,'hint':('waffle','와플'),'explain':'waffle = 격자 무늬'},
            {'en':'Fluffy pancakes.','choices':['폭신한 팬케이크','폭신한 빵','폭신한 사탕','폭신한 우유'],'ans':0,'hint':('pancake','팬케이크'),'explain':'pancake = 아침 식사'},
            {'en':'Creamy cheesecake.','choices':['부드러운 치즈케이크','부드러운 빵','부드러운 사탕','부드러운 우유'],'ans':0,'hint':('cheesecake','치즈케이크'),'explain':'cheesecake = 진한 맛'},
            {'en':'Pink macaron.','choices':['분홍 마카롱','분홍 케이크','분홍 사탕','분홍 우유'],'ans':0,'hint':('macaron','마카롱'),'explain':'macaron = 프랑스'},
            {'en':'Chocolate sundae.','choices':['초콜릿 선데','초콜릿 케이크','초콜릿 사탕','초콜릿 우유'],'ans':0,'hint':('sundae','선데'),'explain':'sundae = 아이스크림'},
            {'en':'Fruit jelly.','choices':['과일 젤리','과일 케이크','과일 사탕','과일 우유'],'ans':0,'hint':('jelly','젤리'),'explain':'jelly = 말랑 간식'},
            {'en':'Caramel candy.','choices':['카라멜 사탕','카라멜 빵','카라멜 우유','카라멜 케이크'],'ans':0,'hint':('caramel','카라멜'),'explain':'caramel = 진한 단맛'},
            {'en':'Soft marshmallow.','choices':['부드러운 마시멜로','부드러운 빵','부드러운 케이크','부드러운 우유'],'ans':0,'hint':('marshmallow','마시멜로'),'explain':'marshmallow = 구름'},
            {'en':'A big lollipop.','choices':['큰 막대사탕','큰 빵','큰 케이크','큰 우유'],'ans':0,'hint':('lollipop','막대사탕'),'explain':'lollipop = 막대'},
            {'en':'Chew bubblegum.','choices':['풍선껌 씹어','빵 먹어','우유 마셔','케이크 먹어'],'ans':0,'hint':('bubblegum','풍선껌'),'explain':'bubblegum = 풍선'},
            {'en':'Lemon sorbet.','choices':['레몬 셔벗','레몬 케이크','레몬 사탕','레몬 우유'],'ans':0,'hint':('sorbet','셔벗'),'explain':'sorbet = 얼린 디저트'},
            {'en':'Vanilla frosting.','choices':['바닐라 크림','바닐라 사탕','바닐라 빵','바닐라 우유'],'ans':0,'hint':('frosting','크림'),'explain':'frosting = 케이크 위'},
            {'en':'Add sprinkles.','choices':['토핑 뿌려','빵 뿌려','케이크 뿌려','우유 뿌려'],'ans':0,'hint':('sprinkles','토핑'),'explain':'sprinkles = 색색 알갱이'},
            {'en':'Yum, yum!','choices':['냠냠!','자!','놀아!','먹어!'],'ans':0,'hint':('yum','맛있다'),'explain':'yum = 맛있을 때'},
        ]
    },

    '20260806': {
        'date':'2026-08-06','day_ko':'목','theme':'별자리·우주','theme_emoji':'✨','description':'우주 영어!',
        'questions':[
            {'en':'A constellation.','choices':['별자리','별','달','해'],'ans':0,'hint':('constellation','별자리'),'explain':'constellation = 별 모양'},
            {'en':'Zodiac signs.','choices':['황도 12궁','별 12개','달 12개','없음'],'ans':0,'hint':('zodiac','황도12궁'),'explain':'zodiac = 12 별자리'},
            {'en':'A large asteroid.','choices':['큰 소행성','큰 달','큰 별','큰 해'],'ans':0,'hint':('asteroid','소행성'),'explain':'asteroid = 우주 돌'},
            {'en':'A beautiful nebula.','choices':['아름다운 성운','아름다운 별','아름다운 달','아름다운 해'],'ans':0,'hint':('nebula','성운'),'explain':'nebula = 우주 구름'},
            {'en':"Earth gravity.",'choices':['지구 중력','지구 모양','지구 색','지구 크기'],'ans':0,'hint':('gravity','중력'),'explain':'gravity = 끌어당김'},
            {'en':"Earth's axis.",'choices':['지구의 축','지구의 색','지구의 크기','지구의 이름'],'ans':0,'hint':('axis','축'),'explain':'axis = 자전 중심'},
            {'en':'Solar eclipse.','choices':['일식','월식','별식','없음'],'ans':0,'hint':('eclipse','일식·월식'),'explain':'eclipse = 가림'},
            {'en':'Stars twinkle.','choices':['별이 반짝','별이 자','별이 가','별이 먹어'],'ans':0,'hint':('twinkle','반짝'),'explain':'twinkle = 반짝'},
            {'en':'Make a wish!','choices':['소원 빌어요!','자!','놀아!','먹어!'],'ans':0,'hint':('shooting star','별똥별'),'explain':'shooting star = 소원'},
            {'en':'Milky Way galaxy.','choices':['은하수','별','달','해'],'ans':0,'hint':('milky way','은하수'),'explain':'milky way = 우리 은하'},
            {'en':'Saturn has rings.','choices':['토성은 고리','토성은 없음','토성은 별','토성은 달'],'ans':0,'hint':('saturn','토성'),'explain':'saturn = 고리'},
            {'en':'Jupiter is biggest.','choices':['목성이 가장 큼','지구가 가장 큼','달이 가장 큼','별이 가장 큼'],'ans':0,'hint':('jupiter','목성'),'explain':'jupiter = 최대'},
            {'en':'Red Mars.','choices':['붉은 화성','파란 지구','노란 해','하얀 달'],'ans':0,'hint':('mars','화성'),'explain':'mars = 붉은 행성'},
            {'en':'Bright Venus.','choices':['밝은 금성','밝은 달','밝은 별','밝은 해'],'ans':0,'hint':('venus','금성'),'explain':'venus = 새벽별'},
            {'en':'Tiny Mercury.','choices':['작은 수성','작은 별','작은 달','작은 해'],'ans':0,'hint':('mercury','수성'),'explain':'mercury = 가장 가까움'},
            {'en':'Tiny Pluto.','choices':['작은 명왕성','작은 별','작은 달','작은 해'],'ans':0,'hint':('pluto','명왕성'),'explain':'pluto = 준행성'},
            {'en':'A warm sunbeam.','choices':['따뜻한 햇살','따뜻한 별','따뜻한 달','따뜻한 옷'],'ans':0,'hint':('sunbeam','햇살'),'explain':'sunbeam = 광선'},
            {'en':'A new spacecraft.','choices':['새 우주선','새 비행기','새 자동차','새 배'],'ans':0,'hint':('spacecraft','우주선'),'explain':'spacecraft = 우주 기계'},
            {'en':'The vast cosmos.','choices':['광대한 우주','광대한 바다','광대한 산','광대한 들'],'ans':0,'hint':('cosmos','우주'),'explain':'cosmos = 전 우주'},
            {'en':'A starlit night.','choices':['별빛 가득 밤','달빛 가득 밤','해빛 가득 낮','구름 가득 밤'],'ans':0,'hint':('starlit','별빛'),'explain':'starlit = 별 가득'},
        ]
    },

    '20260807': {
        'date':'2026-08-07','day_ko':'금','theme':'응급·안전','theme_emoji':'🚨','description':'안전 영어!',
        'questions':[
            {'en':'Danger ahead!','choices':['앞에 위험!','앞에 안전!','앞에 학교!','앞에 집!'],'ans':0,'hint':('danger','위험'),'explain':'danger = 위험'},
            {'en':'Stay safe.','choices':['안전하게 지내요','위험하게 지내요','자','놀아'],'ans':0,'hint':('safe','안전'),'explain':'safe = 안전한'},
            {'en':'A warning sign.','choices':['경고 표시','학교 표시','집 표시','시장 표시'],'ans':0,'hint':('warning','경고'),'explain':'warning = 알림'},
            {'en':'Fire alarm.','choices':['화재 경보','학교 알람','집 알람','시장 알람'],'ans':0,'hint':('alarm','경보'),'explain':'alarm = 위험 알림'},
            {'en':'Brave paramedic.','choices':['용감한 응급구조사','용감한 학생','용감한 친구','용감한 부모'],'ans':0,'hint':('paramedic','응급구조사'),'explain':'paramedic = 구급차'},
            {'en':'A police officer.','choices':['경찰관','학생','선생님','친구'],'ans':0,'hint':('officer','경찰관'),'explain':'officer = 경찰'},
            {'en':'Wear goggles.','choices':['고글 써요','옷 입어요','신발 신어요','모자 써요'],'ans':0,'hint':('goggle','고글'),'explain':'goggle = 눈 보호'},
            {'en':'Wear your seatbelt.','choices':['안전벨트 매','옷 입어','신발 신어','모자 써'],'ans':0,'hint':('seatbelt','안전벨트'),'explain':'seatbelt = 차 필수'},
            {'en':'Wear a lifejacket.','choices':['구명조끼 입어','옷 입어','신발 신어','모자 써'],'ans':0,'hint':('lifejacket','구명조끼'),'explain':'lifejacket = 물에서'},
            {'en':'First aid kit.','choices':['응급처치 키트','요리 키트','학용품 키트','옷 키트'],'ans':0,'hint':('firstaid','응급처치'),'explain':'first aid = 다쳤을 때'},
            {'en':'Escape route.','choices':['탈출 경로','학교 경로','시장 경로','집 경로'],'ans':0,'hint':('escape','탈출'),'explain':'escape = 빠져나옴'},
            {'en':'Rescue team.','choices':['구조대','학생 팀','요리팀','운동팀'],'ans':0,'hint':('rescue','구조'),'explain':'rescue = 구해줌'},
            {'en':'Find shelter.','choices':['대피소 찾아','학교 찾아','시장 찾아','집 찾아'],'ans':0,'hint':('shelter','대피소'),'explain':'shelter = 안전한 곳'},
            {'en':'A deep wound.','choices':['깊은 상처','얕은 상처','새 상처','오래된 상처'],'ans':0,'hint':('wound','상처'),'explain':'wound = 다친 자국'},
            {'en':'Fire hazard.','choices':['화재 위험','화재 안전','화재 경고','화재 없음'],'ans':0,'hint':('hazard','위험요소'),'explain':'hazard = 위험'},
            {'en':'Use caution.','choices':['주의하세요','자세요','놀아요','먹어요'],'ans':0,'hint':('caution','주의'),'explain':'caution = 조심'},
            {'en':'A bright beacon.','choices':['밝은 신호등','밝은 별','밝은 달','밝은 해'],'ans':0,'hint':('beacon','신호등'),'explain':'beacon = 멀리 보임'},
            {'en':'Loud siren.','choices':['시끄러운 사이렌','시끄러운 새','시끄러운 강아지','시끄러운 사람'],'ans':0,'hint':('siren','사이렌'),'explain':'siren = 비상 소리'},
            {'en':'Defend yourself.','choices':['자신을 방어해요','자신을 미워해요','자','놀아'],'ans':0,'hint':('defend','방어'),'explain':'defend = 공격 막기'},
            {'en':'Evacuate now!','choices':['지금 대피!','지금 자!','지금 놀아!','지금 먹어!'],'ans':0,'hint':('evacuate','대피'),'explain':'evacuate = 위험할 때'},
        ]
    },

    '20260808': {
        'date':'2026-08-08','day_ko':'토','theme':'더운 여름 살기','theme_emoji':'🌞','description':'여름 생존 영어!',
        'questions':[
            {'en':"It's so hot today!",'choices':['오늘 너무 더워!','오늘 너무 추워!','오늘 비!','오늘 눈!'],'ans':0,'hint':('hot','더운'),'explain':'hot = 더위'},
            {'en':'Stay cool.','choices':['시원하게 지내','뜨겁게 지내','자','놀아'],'ans':0,'hint':('cool','시원'),'explain':'stay cool = 시원'},
            {'en':'Drink cold water.','choices':['차가운 물 마셔','뜨거운 물 마셔','우유 마셔','주스 마셔'],'ans':0,'hint':('cold','차가운'),'explain':'cold water = 차가운 물'},
            {'en':'Eat ice cream.','choices':['아이스크림 먹어','밥 먹어','빵 먹어','과일 먹어'],'ans':0,'hint':('ice cream','아이스크림'),'explain':'ice cream = 시원'},
            {'en':'Stay in the shade.','choices':['그늘에 있어','햇볕에 있어','자','놀아'],'ans':0,'hint':('shade','그늘'),'explain':'shade = 그늘'},
            {'en':'Turn on the fan.','choices':['선풍기 켜','TV 켜','컴퓨터 켜','불 켜'],'ans':0,'hint':('fan','선풍기'),'explain':'fan = 시원한 바람'},
            {'en':'Use the air conditioner.','choices':['에어컨 사용','TV 사용','컴퓨터 사용','책 사용'],'ans':0,'hint':('AC','에어컨'),'explain':'AC = 시원함'},
            {'en':"I'm sweating.",'choices':['땀나','졸려','신나','피곤'],'ans':0,'hint':('sweat','땀'),'explain':'sweat = 땀'},
            {'en':"It's humid.",'choices':['습해','건조해','시원해','추워'],'ans':0,'hint':('humid','습한'),'explain':'humid = 끈적'},
            {'en':'Eat watermelon.','choices':['수박 먹기','사과 먹기','바나나 먹기','포도 먹기'],'ans':0,'hint':('watermelon','수박'),'explain':'watermelon = 여름'},
            {'en':"Let's swim.",'choices':['수영하자','자자','놀자','먹자'],'ans':0,'hint':('swim','수영'),'explain':'swim = 수영'},
            {'en':'Wear sunglasses.','choices':['선글라스 써','옷 입어','신발 신어','모자 써'],'ans':0,'hint':('sunglasses','선글라스'),'explain':'sunglasses = 햇빛 막기'},
            {'en':'Apply sunscreen.','choices':['선크림 발라','잼 발라','꿀 발라','버터 발라'],'ans':0,'hint':('sunscreen','선크림'),'explain':'sunscreen = 햇볕 화상 막기'},
            {'en':'Walk in the morning.','choices':['아침에 산책','저녁에 산책','밤에 산책','낮에 산책'],'ans':0,'hint':('morning','아침'),'explain':'morning walk = 아침 산책'},
            {'en':'Have a popsicle.','choices':['아이스바 먹어','케이크 먹어','빵 먹어','우유 마셔'],'ans':0,'hint':('popsicle','아이스바'),'explain':'popsicle = 막대 아이스'},
            {'en':"Don't forget your hat.",'choices':['모자 챙겨','옷 챙겨','신발 챙겨','가방 챙겨'],'ans':0,'hint':('hat','모자'),'explain':'hat = 모자'},
            {'en':'Take a cool shower.','choices':['시원한 샤워','뜨거운 샤워','새 샤워','오래된 샤워'],'ans':0,'hint':('shower','샤워'),'explain':'cool shower = 시원 샤워'},
            {'en':'Stay hydrated.','choices':['수분 보충','음식 먹기','자기','놀기'],'ans':0,'hint':('hydrated','수분'),'explain':'hydrated = 물 마시기'},
            {'en':'Avoid the heat.','choices':['더위 피해','더위 즐겨','자','놀아'],'ans':0,'hint':('avoid','피하다'),'explain':'avoid = 피하기'},
            {'en':'Summer is beautiful!','choices':['여름이 아름다워!','겨울이 아름다워!','봄이 아름다워!','가을이 아름다워!'],'ans':0,'hint':('summer','여름'),'explain':'summer = 여름'},
        ]
    },

    '20260809': {
        'date':'2026-08-09','day_ko':'일','theme':'한 주 복습','theme_emoji':'📚','description':'한 주 정리 영어!',
        'questions':[
            {'en':'Time to review.','choices':['복습 시간','놀 시간','자 시간','먹을 시간'],'ans':0,'hint':('review','복습'),'explain':'review = 다시 보기'},
            {'en':'Open your notebook.','choices':['노트 열어','책 열어','문 열어','창문 열어'],'ans':0,'hint':('notebook','노트'),'explain':'open notebook = 노트 펴기'},
            {'en':'Take notes.','choices':['필기 해','자','놀아','먹어'],'ans':0,'hint':('notes','필기'),'explain':'take notes = 메모하기'},
            {'en':'Memorize the words.','choices':['단어 외워','단어 잊어','단어 던져','단어 사'],'ans':0,'hint':('memorize','외우다'),'explain':'memorize = 기억'},
            {'en':"Don't give up.",'choices':['포기 마','쉬어','자','놀아'],'ans':0,'hint':('give up','포기'),'explain':"don't give up = 끝까지!"},
            {'en':'Try harder.','choices':['더 노력해','덜 노력해','자','놀아'],'ans':0,'hint':('harder','더 열심히'),'explain':'try harder = 더 노력'},
            {'en':'Focus on the lesson.','choices':['수업에 집중','수업 잊어','자','놀아'],'ans':0,'hint':('focus','집중'),'explain':'focus = 집중'},
            {'en':'Practice every day.','choices':['매일 연습','매일 자','매일 놀아','매일 먹어'],'ans':0,'hint':('practice','연습'),'explain':'practice = 연습'},
            {'en':"You're improving.",'choices':['너 향상되고 있어','너 후퇴해','자','놀아'],'ans':0,'hint':('improving','향상'),'explain':'improving = 발전'},
            {'en':'Be confident.','choices':['자신감 가져','약하게','자','놀아'],'ans':0,'hint':('confident','자신감'),'explain':'confident = 자신감'},
            {'en':'Ask questions.','choices':['질문해','자','놀아','먹어'],'ans':0,'hint':('ask','묻다'),'explain':'ask = 묻기'},
            {'en':'Listen carefully.','choices':['주의 깊게 들어','대충 들어','자','놀아'],'ans':0,'hint':('listen','듣다'),'explain':'listen carefully = 집중 듣기'},
            {'en':'Read the book.','choices':['책 읽어','책 던져','책 사','책 찢어'],'ans':0,'hint':('read','읽다'),'explain':'read = 읽기'},
            {'en':'Write it down.','choices':['적어 둬','말해','노래해','자'],'ans':0,'hint':('write','쓰다'),'explain':'write = 쓰기'},
            {'en':'Remember the rule.','choices':['규칙 기억','규칙 잊어','자','놀아'],'ans':0,'hint':('remember','기억'),'explain':'remember = 기억'},
            {'en':'You can do it!','choices':['넌 할 수 있어!','넌 못해!','자!','놀아!'],'ans':0,'hint':('can','할 수 있다'),'explain':'can do = 가능!'},
            {'en':'Be proud!','choices':['자랑스러워해!','싫어해!','자!','놀아!'],'ans':0,'hint':('proud','자랑스러운'),'explain':'be proud = 자부심'},
            {'en':'Celebrate your win.','choices':['승리를 축하해','패배를 축하해','자','놀아'],'ans':0,'hint':('celebrate','축하'),'explain':'celebrate = 기뻐하기'},
            {'en':'Rest well.','choices':['푹 쉬어','일해','자','놀아'],'ans':0,'hint':('rest','쉬다'),'explain':'rest = 휴식'},
            {'en':'See you next week!','choices':['다음 주 봐!','어제 봤어!','지금 봐!','내일 봐!'],'ans':0,'hint':('next','다음'),'explain':'next week = 다음 주'},
        ]
    },

    # ═════════════════════════════════════════════
    # 8/10~8/16 (Week 17) - 한식·가전·정원·문구·한국사 + 광복절!
    # ═════════════════════════════════════════════
    '20260810': {
        'date':'2026-08-10','day_ko':'월','theme':'한국 음식','theme_emoji':'🍚','description':'한식 영어!',
        'questions':[
            {'en':'I love bibimbap.','choices':['비빔밥 좋아','비빔밥 싫어','자','놀아'],'ans':0,'hint':('bibimbap','비빔밥'),'explain':'bibimbap = 섞어 먹어요'},
            {'en':'Spicy tteokbokki.','choices':['매운 떡볶이','달콤 떡볶이','새 떡볶이','오래된 떡볶이'],'ans':0,'hint':('tteokbokki','떡볶이'),'explain':'tteokbokki = 매콤'},
            {'en':'Kimchi jjigae.','choices':['김치찌개','김치국','김치반찬','김치말이'],'ans':0,'hint':('jjigae','찌개'),'explain':'jjigae = 진한 국'},
            {'en':'Yummy japchae.','choices':['맛있는 잡채','맛있는 김밥','맛있는 떡','맛있는 빵'],'ans':0,'hint':('japchae','잡채'),'explain':'japchae = 당면 요리'},
            {'en':'Sweet bulgogi.','choices':['달콤한 불고기','달콤한 떡','달콤한 빵','달콤한 사탕'],'ans':0,'hint':('bulgogi','불고기'),'explain':'bulgogi = 한식 대표'},
            {'en':'BBQ galbi.','choices':['바비큐 갈비','바비큐 닭','바비큐 새우','바비큐 빵'],'ans':0,'hint':('galbi','갈비'),'explain':'galbi = 갈비!'},
            {'en':'Fresh kimchi.','choices':['신선한 김치','신선한 빵','신선한 우유','신선한 사탕'],'ans':0,'hint':('kimchi','김치'),'explain':'kimchi = 한국 대표'},
            {'en':'Many banchan.','choices':['많은 반찬','많은 빵','많은 우유','많은 음료'],'ans':0,'hint':('banchan','반찬'),'explain':'banchan = 곁들임'},
            {'en':'Grill samgyeopsal.','choices':['삼겹살 구워','빵 구워','떡 구워','쿠키 구워'],'ans':0,'hint':('samgyeopsal','삼겹살'),'explain':'samgyeopsal = 돼지 배'},
            {'en':'Crispy jeon.','choices':['바삭한 전','바삭한 빵','바삭한 사탕','바삭한 과자'],'ans':0,'hint':('jeon','전'),'explain':'jeon = 부침개'},
            {'en':'Steamed mandu.','choices':['찐 만두','찐 빵','찐 떡','찐 감자'],'ans':0,'hint':('mandu','만두'),'explain':'mandu = 한국식'},
            {'en':'Spicy ramyeon.','choices':['매운 라면','달콤 라면','짠 라면','새 라면'],'ans':0,'hint':('ramyeon','라면'),'explain':'ramyeon = 한국 라면'},
            {'en':'Cold naengmyeon.','choices':['차가운 냉면','뜨거운 국수','새 면','오래된 면'],'ans':0,'hint':('naengmyeon','냉면'),'explain':'naengmyeon = 여름!'},
            {'en':'Sweet hotteok.','choices':['달콤한 호떡','달콤한 빵','달콤한 떡','달콤한 케이크'],'ans':0,'hint':('hotteok','호떡'),'explain':'hotteok = 겨울 간식'},
            {'en':'Mango bingsu.','choices':['망고 빙수','망고 케이크','망고 사탕','망고 빵'],'ans':0,'hint':('bingsu','빙수'),'explain':'bingsu = 여름 디저트'},
            {'en':'Tuna gimbap.','choices':['참치 김밥','참치 죽','참치 빵','참치 떡'],'ans':0,'hint':('gimbap','김밥'),'explain':'gimbap = 한국 롤'},
            {'en':'Traditional hangwa.','choices':['전통 한과','새 한과','외국 한과','없음'],'ans':0,'hint':('hangwa','한과'),'explain':'hangwa = 전통 과자'},
            {'en':'Sweet sikhye.','choices':['달콤한 식혜','달콤한 우유','달콤한 차','달콤한 주스'],'ans':0,'hint':('sikhye','식혜'),'explain':'sikhye = 전통 음료'},
            {'en':'Korean sundae.','choices':['한국 순대','한국 떡','한국 빵','한국 만두'],'ans':0,'hint':('sundae','순대'),'explain':'sundae = 길거리'},
            {'en':'Rice makgeolli.','choices':['쌀 막걸리','쌀 빵','쌀 떡','쌀 우유'],'ans':0,'hint':('makgeolli','막걸리'),'explain':'makgeolli = 전통 술'},
        ]
    },

    '20260811': {
        'date':'2026-08-11','day_ko':'화','theme':'가전제품','theme_emoji':'🔌','description':'가전 영어!',
        'questions':[
            {'en':'Open the refrigerator.','choices':['냉장고 열어','문 열어','책 열어','창문 열어'],'ans':0,'hint':('refrigerator','냉장고'),'explain':'refrigerator = 정식'},
            {'en':'Ice in the freezer.','choices':['냉동고 얼음','냉장고 얼음','없음','다 가능'],'ans':0,'hint':('freezer','냉동고'),'explain':'freezer = 꽁꽁'},
            {'en':'Use the washer.','choices':['세탁기 써','TV 써','컴퓨터 써','전화 써'],'ans':0,'hint':('washer','세탁기'),'explain':'washer = 빨래'},
            {'en':'In the dryer.','choices':['건조기 안','세탁기 안','오븐 안','냉장고 안'],'ans':0,'hint':('dryer','건조기'),'explain':'dryer = 말리기'},
            {'en':'Vacuum the floor.','choices':['바닥 청소','바닥 닦아','자기','놀기'],'ans':0,'hint':('vacuum','청소기'),'explain':'vacuum = 빨아들임'},
            {'en':'Heat in microwave.','choices':['전자레인지 데워','오븐 구워','자','놀아'],'ans':0,'hint':('microwave','전자레인지'),'explain':'microwave = 빠른 데움'},
            {'en':'Bake in the oven.','choices':['오븐에 구워','전자레인지에 데워','자','놀아'],'ans':0,'hint':('oven','오븐'),'explain':'oven = 빵 굽기'},
            {'en':'Toast bread.','choices':['빵 굽기','빵 사기','빵 던지기','빵 자기'],'ans':0,'hint':('toaster','토스터'),'explain':'toast = 식빵 굽기'},
            {'en':'Boil the kettle.','choices':['주전자 끓여','컵 끓여','병 끓여','상자 끓여'],'ans':0,'hint':('kettle','주전자'),'explain':'kettle = 물 끓이기'},
            {'en':'Use a blender.','choices':['믹서 써','TV 써','컴퓨터 써','전화 써'],'ans':0,'hint':('blender','믹서'),'explain':'blender = 갈기'},
            {'en':'Use a humidifier.','choices':['가습기 써','TV 써','컴퓨터 써','전화 써'],'ans':0,'hint':('humidifier','가습기'),'explain':'humidifier = 습도'},
            {'en':'Dry your hair.','choices':['머리 말려','옷 말려','신발 말려','책 말려'],'ans':0,'hint':('hairdryer','헤어드라이어'),'explain':'hairdryer = 머리'},
            {'en':'Find the remote control.','choices':['리모컨 찾아','책 찾아','음식 찾아','옷 찾아'],'ans':0,'hint':('remote','리모컨'),'explain':'remote = 원격 조작'},
            {'en':'Print a paper.','choices':['종이 출력','종이 자','종이 사','종이 던져'],'ans':0,'hint':('printer','프린터'),'explain':'printer = 인쇄'},
            {'en':'Loud speaker.','choices':['시끄러운 스피커','조용한 스피커','새 스피커','오래된 스피커'],'ans':0,'hint':('speaker','스피커'),'explain':'speaker = 소리'},
            {'en':'Kitchen appliances.','choices':['부엌 가전','부엌 음식','부엌 그릇','부엌 의자'],'ans':0,'hint':('appliance','가전'),'explain':'appliance = 가전 통칭'},
            {'en':'Plug it in.','choices':['꽂아요','자','놀아','먹어'],'ans':0,'hint':('plug','플러그'),'explain':'plug in = 전원 연결'},
            {'en':'Wall outlet.','choices':['벽 콘센트','벽 그림','벽 시계','벽 책'],'ans':0,'hint':('outlet','콘센트'),'explain':'outlet = 플러그 꽂는 곳'},
            {'en':'Long cord.','choices':['긴 전선','긴 머리','긴 옷','긴 신발'],'ans':0,'hint':('cord','전선'),'explain':'cord = 전기 줄'},
            {'en':'Carry a battery pack.','choices':['보조배터리 휴대','TV 휴대','전화 휴대','책 휴대'],'ans':0,'hint':('battery pack','보조배터리'),'explain':'battery pack = 외출용 충전기'},
        ]
    },

    '20260812': {
        'date':'2026-08-12','day_ko':'수','theme':'정원과 식물 가꾸기','theme_emoji':'🌱','description':'정원 영어!',
        'questions':[
            {'en':'A glass greenhouse.','choices':['유리 온실','유리 집','유리 학교','유리 시장'],'ans':0,'hint':('greenhouse','온실'),'explain':'greenhouse = 온실'},
            {'en':'A colorful flowerbed.','choices':['화려한 꽃밭','화려한 옷','화려한 책','화려한 가방'],'ans':0,'hint':('flowerbed','꽃밭'),'explain':'flowerbed = 꽃 모인 곳'},
            {'en':'Use the watering can.','choices':['물뿌리개 사용','컵 사용','책 사용','옷 사용'],'ans':0,'hint':('watering can','물뿌리개'),'explain':'watering can = 물 주기'},
            {'en':'Dig with a shovel.','choices':['삽으로 파','펜으로 써','옷 입어','자기'],'ans':0,'hint':('shovel','삽'),'explain':'shovel = 흙 파기'},
            {'en':'Rake the leaves.','choices':['낙엽 긁어','낙엽 던져','낙엽 자','낙엽 봐'],'ans':0,'hint':('rake','갈퀴'),'explain':'rake = 잎 모으기'},
            {'en':'Garden hose.','choices':['정원 호스','정원 의자','정원 책','정원 옷'],'ans':0,'hint':('hose','호스'),'explain':'hose = 긴 물줄기'},
            {'en':'A wooden planter.','choices':['나무 화분 상자','나무 책상','나무 의자','나무 신발'],'ans':0,'hint':('planter','화분 상자'),'explain':'planter = 식물 통'},
            {'en':'Plant a sapling.','choices':['묘목 심어','책 심어','옷 심어','신발 심어'],'ans':0,'hint':('sapling','묘목'),'explain':'sapling = 어린 나무'},
            {'en':'Pull weeds.','choices':['잡초 뽑아','꽃 따','풀 베','나무 자르'],'ans':0,'hint':('weed','잡초'),'explain':'weed = 필요 없는 풀'},
            {'en':'Add fertilizer.','choices':['비료 줘','물 줘','책 줘','옷 줘'],'ans':0,'hint':('fertilizer','비료'),'explain':'fertilizer = 영양'},
            {'en':'Flowers bloom.','choices':['꽃이 펴','꽃이 자','꽃이 가','꽃이 먹어'],'ans':0,'hint':('bloom','꽃피다'),'explain':'bloom = 꽃 피기'},
            {'en':'New sprouts.','choices':['새싹들','새 옷','새 책','새 사람'],'ans':0,'hint':('sprout','새싹'),'explain':'sprout = 씨앗에서'},
            {'en':'A tomato seedling.','choices':['토마토 모종','토마토 주스','토마토 빵','토마토 잼'],'ans':0,'hint':('seedling','모종'),'explain':'seedling = 어린 식물'},
            {'en':'A pretty orchid.','choices':['예쁜 난초','예쁜 꽃','예쁜 책','예쁜 옷'],'ans':0,'hint':('orchid','난초'),'explain':'orchid = 우아한 꽃'},
            {'en':'White daisy.','choices':['하얀 데이지','하얀 장미','하얀 백합','하얀 튤립'],'ans':0,'hint':('daisy','데이지'),'explain':'daisy = 하얀 들꽃'},
            {'en':'A white lily.','choices':['하얀 백합','하얀 장미','하얀 데이지','하얀 튤립'],'ans':0,'hint':('lily','백합'),'explain':'lily = 우아한 꽃'},
            {'en':'Red poppy.','choices':['빨간 양귀비','빨간 장미','빨간 튤립','빨간 데이지'],'ans':0,'hint':('poppy','양귀비'),'explain':'poppy = 화려한 꽃'},
            {'en':'Spiky cactus.','choices':['가시 선인장','가시 나무','가시 꽃','가시 풀'],'ans':0,'hint':('cactus','선인장'),'explain':'cactus = 사막 식물'},
            {'en':'Grape vine.','choices':['포도 덩굴','포도 나무','포도 잎','포도 꽃'],'ans':0,'hint':('vine','덩굴'),'explain':'vine = 감기는 식물'},
            {'en':'Rose thorns.','choices':['장미 가시','장미 잎','장미 꽃','장미 줄기'],'ans':0,'hint':('thorn','가시'),'explain':'thorn = 날카로움'},
        ]
    },

    '20260813': {
        'date':'2026-08-13','day_ko':'목','theme':'도서관·문구','theme_emoji':'📚','description':'문구 영어!',
        'questions':[
            {'en':'Visit the bookshop.','choices':['서점 방문','학교 방문','집 방문','시장 방문'],'ans':0,'hint':('bookshop','서점'),'explain':'bookshop = 책 파는 곳'},
            {'en':'Use a bookmark.','choices':['책갈피 써','책 던져','책 잊어','책 사'],'ans':0,'hint':('bookmark','책갈피'),'explain':'bookmark = 표시'},
            {'en':'Books on the shelf.','choices':['선반의 책','집의 책','시장의 책','옷장의 책'],'ans':0,'hint':('shelf','선반'),'explain':'shelf = 책 놓는 곳'},
            {'en':'Borrow a book.','choices':['책 빌려','책 사','책 줘','책 던져'],'ans':0,'hint':('borrow','빌리다'),'explain':'borrow = 잠시 받기'},
            {'en':'Return the book.','choices':['책 반납','책 사','책 줘','책 던져'],'ans':0,'hint':('return','반납'),'explain':'return = 돌려주기'},
            {'en':'Meet the deadline.','choices':['기한 맞춰','기한 잊어','자','놀아'],'ans':0,'hint':('deadline','기한'),'explain':'deadline = 끝낼 날'},
            {'en':'In my pencil case.','choices':['필통 속','책가방 속','옷장 속','신발장 속'],'ans':0,'hint':('pencil case','필통'),'explain':'pencil case = 문구 가방'},
            {'en':'A digital archive.','choices':['디지털 기록소','디지털 학교','디지털 집','디지털 가게'],'ans':0,'hint':('archive','기록 보관소'),'explain':'archive = 옛 자료'},
            {'en':'Use correction tape.','choices':['수정테이프 써','연필 써','지우개 써','컴퓨터 써'],'ans':0,'hint':('correction tape','수정테이프'),'explain':'correction tape = 잘못 가리기'},
            {'en':'A blue pen.','choices':['파란 펜','파란 책','파란 옷','파란 가방'],'ans':0,'hint':('pen','펜'),'explain':'pen = 잉크펜'},
            {'en':'Paper clip.','choices':['종이 클립','종이 책','종이 가방','종이 컵'],'ans':0,'hint':('clip','클립'),'explain':'clip = 종이 묶기'},
            {'en':'Use a thumbtack.','choices':['압정 써','연필 써','펜 써','지우개 써'],'ans':0,'hint':('thumbtack','압정'),'explain':'thumbtack = 벽에 꽂기'},
            {'en':'Put in a folder.','choices':['폴더에 넣어','책에 넣어','상자에 넣어','가방에 넣어'],'ans':0,'hint':('folder','폴더'),'explain':'folder = 서류 보관'},
            {'en':'A big binder.','choices':['큰 바인더','큰 책','큰 가방','큰 옷'],'ans':0,'hint':('binder','바인더'),'explain':'binder = 종이 묶음'},
            {'en':'Mark the calendar.','choices':['달력에 표시','책에 표시','옷에 표시','신발에 표시'],'ans':0,'hint':('calendar','달력'),'explain':'calendar = 날짜'},
            {'en':'Yellow sticky note.','choices':['노란 포스트잇','노란 옷','노란 책','노란 신발'],'ans':0,'hint':('sticky note','포스트잇'),'explain':'sticky note = 붙이는 메모'},
            {'en':'Write on the chalkboard.','choices':['칠판에 써','종이에 써','책에 써','옷에 써'],'ans':0,'hint':('chalkboard','칠판'),'explain':'chalkboard = 분필 사용'},
            {'en':'Wipe the whiteboard.','choices':['화이트보드 닦아','책 닦아','옷 닦아','신발 닦아'],'ans':0,'hint':('whiteboard','화이트보드'),'explain':'whiteboard = 마커 사용'},
            {'en':'Check the due date.','choices':['반납일 확인','이름 확인','시간 확인','어디 확인'],'ans':0,'hint':('due date','반납일'),'explain':'due date = 마감'},
            {'en':'Staple the papers.','choices':['서류 스테이플','서류 봐','서류 던져','서류 사'],'ans':0,'hint':('staple','스테이플'),'explain':'staple = 종이 묶기'},
        ]
    },

    '20260814': {
        'date':'2026-08-14','day_ko':'금','theme':'한국 역사 (광복절!)','theme_emoji':'🇰🇷','description':'역사 영어!',
        'questions':[
            {'en':'Korean liberation.','choices':['한국 광복','한국 점령','한국 시작','한국 끝'],'ans':0,'hint':('liberation','광복'),'explain':'liberation = 1945년!'},
            {'en':'Independence Day.','choices':['독립의 날','새해','크리스마스','없음'],'ans':0,'hint':('independence','독립'),'explain':'독립 = 자유!'},
            {'en':'Love freedom.','choices':['자유 사랑','자유 미워','자','놀아'],'ans':0,'hint':('freedom','자유'),'explain':'freedom = 속박 없음'},
            {'en':'A national martyr.','choices':['나라 의사','나라 학생','나라 친구','나라 부모'],'ans':0,'hint':('martyr','순교자'),'explain':'martyr = 안중근·유관순'},
            {'en':'A brave patriot.','choices':['용감한 애국자','용감한 학생','용감한 친구','용감한 친척'],'ans':0,'hint':('patriot','애국자'),'explain':'patriot = 나라 사랑'},
            {'en':'Korean nation.','choices':['한국 국가','한국 학교','한국 도시','한국 집'],'ans':0,'hint':('nation','국가'),'explain':'nation = 한 나라'},
            {'en':'Provincial governor.','choices':['도지사','시장','대통령','없음'],'ans':0,'hint':('governor','도지사'),'explain':'governor = 지방 대표'},
            {'en':'A wise monarch.','choices':['현명한 군주','현명한 학생','현명한 친구','현명한 학자'],'ans':0,'hint':('monarch','군주'),'explain':'monarch = 왕'},
            {'en':'Joseon dynasty.','choices':['조선 왕조','신라 왕조','고려 왕조','고구려 왕조'],'ans':0,'hint':('dynasty','왕조'),'explain':'dynasty = 한 가문 왕'},
            {'en':'A great battle.','choices':['큰 전투','큰 책','큰 학교','큰 집'],'ans':0,'hint':('battle','전투'),'explain':'battle = 싸움'},
            {'en':'Liberation Day is August 15.','choices':['광복절 8/15','광복절 8/16','광복절 3/1','광복절 5/5'],'ans':0,'hint':('liberation day','광복절'),'explain':'8월 15일!'},
            {'en':'Wave the taegukgi.','choices':['태극기 흔들어','옷 흔들어','책 흔들어','없음'],'ans':0,'hint':('taegukgi','태극기'),'explain':'taegukgi = 한국 국기'},
            {'en':'National anthem.','choices':['국가 (애국가)','학교 노래','동요','없음'],'ans':0,'hint':('anthem','국가'),'explain':'anthem = 애국가'},
            {'en':'Hangeul is beautiful.','choices':['한글은 아름다워','한글 어려워','한글 새','한글 옛'],'ans':0,'hint':('hangeul','한글'),'explain':'hangeul = 세종 만듦'},
            {'en':'King Sejong.','choices':['세종대왕','이순신','김유신','이성계'],'ans':0,'hint':('sejong','세종'),'explain':'sejong = 한글 창제'},
            {'en':'Former colony.','choices':['옛 식민지','옛 학교','옛 집','옛 시장'],'ans':0,'hint':('colony','식민지'),'explain':'colony = 지배 받음'},
            {'en':'March on.','choices':['전진','자','놀','먹'],'ans':0,'hint':('march','행진'),'explain':'march = 걸어가기'},
            {'en':'Korean heritage.','choices':['한국 문화유산','한국 음식','한국 옷','한국 책'],'ans':0,'hint':('heritage','유산'),'explain':'heritage = 옛 보물'},
            {'en':'Our ancestors.','choices':['우리 조상','우리 친구','우리 학생','우리 부모'],'ans':0,'hint':('ancestor','조상'),'explain':'ancestor = 옛 어른'},
            {'en':'Korean tradition.','choices':['한국 전통','한국 학교','한국 시장','한국 집'],'ans':0,'hint':('tradition','전통'),'explain':'tradition = 오랜 풍습'},
        ]
    },

    '20260815': {
        'date':'2026-08-15','day_ko':'토','theme':'광복절 특집','theme_emoji':'🎌','description':'광복절 특별!',
        'questions':[
            {'en':'Happy Liberation Day!','choices':['광복절 축하!','새해 축하!','크리스마스!','부활절!'],'ans':0,'hint':('liberation','광복'),'explain':'8월 15일!'},
            {'en':'Korean War ended.','choices':['한국 전쟁 끝','한국 전쟁 시작','없음','다 가능'],'ans':0,'hint':('war','전쟁'),'explain':'전쟁의 끝'},
            {'en':'I am Korean.','choices':['난 한국인이야','난 미국인이야','난 일본인이야','난 중국인이야'],'ans':0,'hint':('Korean','한국인'),'explain':'Korean = 한국인'},
            {'en':'Proud of Korea!','choices':['한국이 자랑스러워!','한국 싫어!','한국 봐!','한국 가!'],'ans':0,'hint':('proud','자랑'),'explain':'proud = 자부심'},
            {'en':'Wave the flag.','choices':['깃발 흔들어','옷 흔들어','책 흔들어','자'],'ans':0,'hint':('flag','깃발'),'explain':'flag = 태극기'},
            {'en':'Sing the anthem.','choices':['국가 불러','동요 불러','자','놀아'],'ans':0,'hint':('anthem','국가'),'explain':'anthem = 애국가'},
            {'en':'Visit the museum.','choices':['박물관 방문','학교 방문','집 방문','시장 방문'],'ans':0,'hint':('museum','박물관'),'explain':'museum = 역사 배움'},
            {'en':'Remember the past.','choices':['과거 기억','과거 잊어','자','놀아'],'ans':0,'hint':('past','과거'),'explain':'past = 옛날'},
            {'en':'Honor the heroes.','choices':['영웅 기리기','영웅 잊기','자','놀기'],'ans':0,'hint':('honor','기리다'),'explain':'honor = 존경'},
            {'en':'A peaceful country.','choices':['평화로운 나라','전쟁 나라','새 나라','오래된 나라'],'ans':0,'hint':('peaceful','평화'),'explain':'peace = 평화'},
            {'en':'Free at last!','choices':['드디어 자유!','드디어 끝!','드디어 시작!','드디어 자!'],'ans':0,'hint':('free','자유'),'explain':'free = 자유'},
            {'en':'Strong country.','choices':['강한 나라','약한 나라','새 나라','오래된 나라'],'ans':0,'hint':('strong','강한'),'explain':'strong = 튼튼'},
            {'en':'Korean people.','choices':['한국 사람들','외국 사람들','학생들','부모들'],'ans':0,'hint':('people','사람들'),'explain':'people = 사람들'},
            {'en':'Brave soldiers.','choices':['용감한 군인','용감한 학생','용감한 친구','용감한 부모'],'ans':0,'hint':('soldiers','군인'),'explain':'soldiers = 군인들'},
            {'en':"Love your country.",'choices':['나라 사랑','나라 미워','자','놀아'],'ans':0,'hint':('country','나라'),'explain':'country = 나라'},
            {'en':'Korean food is the best!','choices':['한식 최고!','외식 최고!','자!','놀아!'],'ans':0,'hint':('food','음식'),'explain':'한국 음식!'},
            {'en':'I love K-pop.','choices':['K팝 좋아','K팝 싫어','자','놀아'],'ans':0,'hint':('K-pop','케이팝'),'explain':'K-pop = 한국 음악'},
            {'en':'Learn hangeul.','choices':['한글 배워','영어 배워','수학 배워','과학 배워'],'ans':0,'hint':('hangeul','한글'),'explain':'hangeul = 한국 글'},
            {'en':'Be proud!','choices':['자랑스러워해!','부끄러워해!','자!','놀아!'],'ans':0,'hint':('proud','자랑스러운'),'explain':'be proud!'},
            {'en':'Happy 8/15!','choices':['8/15 축하!','5/5 축하!','12/25 축하!','1/1 축하!'],'ans':0,'hint':('8/15','광복절'),'explain':'광복절!'},
        ]
    },

    '20260816': {
        'date':'2026-08-16','day_ko':'일','theme':'주말 마무리','theme_emoji':'🌅','description':'한 주 정리 영어!',
        'questions':[
            {'en':'Time to rest.','choices':['쉴 시간','일할 시간','놀 시간','자기 시간'],'ans':0,'hint':('rest','쉬다'),'explain':'rest = 휴식'},
            {'en':'Lazy Sunday.','choices':['느긋한 일요일','바쁜 일요일','피곤한 일요일','짧은 일요일'],'ans':0,'hint':('lazy','느긋'),'explain':'lazy day = 한가'},
            {'en':"It's a beautiful day.",'choices':['아름다운 날','피곤한 날','짧은 날','없는 날'],'ans':0,'hint':('beautiful','아름다운'),'explain':'beautiful = 아름다움'},
            {'en':'Enjoy your time.','choices':['시간 즐기기','시간 잊기','자기','놀기'],'ans':0,'hint':('enjoy','즐기다'),'explain':'enjoy = 즐기기'},
            {'en':'Time flies.','choices':['시간이 빨라','시간이 느려','시간이 멈춰','시간이 없음'],'ans':0,'hint':('flies','날아간다'),'explain':'time flies = 시간 빨라'},
            {'en':"Don't be late.",'choices':['늦지 마','일찍 와','자지 마','놀지 마'],'ans':0,'hint':('late','늦은'),'explain':"don't = 하지 마"},
            {'en':'Try your best.','choices':['최선 다해','대충 해','자','놀아'],'ans':0,'hint':('best','최선'),'explain':'try best = 최선!'},
            {'en':"Keep smiling.",'choices':['계속 웃어','계속 울어','자','놀아'],'ans':0,'hint':('keep','계속'),'explain':'keep smiling = 미소!'},
            {'en':'Believe in yourself.','choices':['자신 믿어','자신 의심','자','놀아'],'ans':0,'hint':('believe','믿다'),'explain':'believe = 믿음'},
            {'en':'A new week starts.','choices':['새 주 시작','옛 주 끝','자','놀아'],'ans':0,'hint':('new','새로운'),'explain':'new week = 새 출발'},
            {'en':'Have a good night.','choices':['좋은 밤','좋은 아침','좋은 점심','좋은 저녁'],'ans':0,'hint':('night','밤'),'explain':'good night = 잘 자!'},
            {'en':'Sweet dreams.','choices':['좋은 꿈','나쁜 꿈','자','놀아'],'ans':0,'hint':('dreams','꿈'),'explain':'sweet dreams = 단꿈'},
            {'en':'See you tomorrow.','choices':['내일 봐','어제 봤어','지금 봐','없음'],'ans':0,'hint':('tomorrow','내일'),'explain':'tomorrow = 내일'},
            {'en':"You're doing great.",'choices':['잘하고 있어','못하고 있어','자','놀아'],'ans':0,'hint':('great','잘'),'explain':"doing great = 잘하고 있음"},
            {'en':"Be kind to others.",'choices':['남에게 친절','남에게 무례','자','놀아'],'ans':0,'hint':('kind','친절'),'explain':'kind = 친절'},
            {'en':'Learn from mistakes.','choices':['실수에서 배워','실수 해서 자','자','놀아'],'ans':0,'hint':('mistake','실수'),'explain':'learn from = 배우기'},
            {'en':'Help your family.','choices':['가족 도와','가족 미워','자','놀아'],'ans':0,'hint':('help','돕다'),'explain':'help family = 가족 돕기'},
            {'en':'Read more books.','choices':['책 더 읽어','책 던져','자','놀아'],'ans':0,'hint':('read','읽다'),'explain':'read more = 더 읽기'},
            {'en':'Stay healthy.','choices':['건강 지키기','아프기','자','놀기'],'ans':0,'hint':('healthy','건강'),'explain':'stay healthy = 건강 유지'},
            {'en':"Let's have a great week!",'choices':['멋진 한 주 보내자!','피곤한 한 주!','자!','놀자!'],'ans':0,'hint':('great','멋진'),'explain':'great week = 멋진 주!'},
        ]
    },

    # ═════════════════════════════════════════════
    # 8/17~8/23 (Week 18) - 가구·음료·미용·상점·빛
    # ═════════════════════════════════════════════
    '20260817': {
        'date':'2026-08-17','day_ko':'월','theme':'가구·인테리어','theme_emoji':'🛋️','description':'가구 영어!',
        'questions':[
            {'en':'Sit on the couch.','choices':['긴 소파에 앉아','책상에 앉아','땅에 앉아','자기'],'ans':0,'hint':('couch','긴소파'),'explain':'couch = 긴 소파'},
            {'en':'A comfy armchair.','choices':['편안한 안락의자','편안한 책','편안한 옷','편안한 신발'],'ans':0,'hint':('armchair','안락의자'),'explain':'armchair = 팔걸이'},
            {'en':'Open the dresser.','choices':['서랍장 열어','문 열어','책 열어','창문 열어'],'ans':0,'hint':('dresser','서랍장'),'explain':'dresser = 옷 보관'},
            {'en':'In the wardrobe.','choices':['옷장 안','책장 안','상자 안','가방 안'],'ans':0,'hint':('wardrobe','옷장'),'explain':'wardrobe = 옷 거는 곳'},
            {'en':'On the nightstand.','choices':['협탁 위','책상 위','땅 위','자 위'],'ans':0,'hint':('nightstand','협탁'),'explain':'nightstand = 침대 옆'},
            {'en':'Soft cushion.','choices':['부드러운 쿠션','부드러운 책','부드러운 옷','부드러운 머리'],'ans':0,'hint':('cushion','쿠션'),'explain':'cushion = 소파에'},
            {'en':'Fluffy pillow.','choices':['폭신한 베개','폭신한 옷','폭신한 책','폭신한 머리'],'ans':0,'hint':('pillow','베개'),'explain':'pillow = 머리 받침'},
            {'en':'Warm blanket.','choices':['따뜻한 담요','따뜻한 옷','따뜻한 음식','따뜻한 차'],'ans':0,'hint':('blanket','담요'),'explain':'blanket = 덮는 천'},
            {'en':'A soft mattress.','choices':['부드러운 매트리스','부드러운 옷','부드러운 책','부드러운 음식'],'ans':0,'hint':('mattress','매트리스'),'explain':'mattress = 침대 깔개'},
            {'en':'A leather recliner.','choices':['가죽 리클라이너','가죽 책','가죽 옷','가죽 신발'],'ans':0,'hint':('recliner','리클라이너'),'explain':'recliner = 눕는 의자'},
            {'en':'A wall tapestry.','choices':['벽 태피스트리','벽 시계','벽 거울','벽 책'],'ans':0,'hint':('tapestry','태피스트리'),'explain':'tapestry = 장식 천'},
            {'en':'A crystal chandelier.','choices':['크리스탈 샹들리에','크리스탈 책','크리스탈 옷','크리스탈 신발'],'ans':0,'hint':('chandelier','샹들리에'),'explain':'chandelier = 화려 등'},
            {'en':'A wall sconce.','choices':['벽 조명','벽 시계','벽 그림','벽 책'],'ans':0,'hint':('sconce','벽 조명'),'explain':'sconce = 벽 등'},
            {'en':'A leather ottoman.','choices':['가죽 오토만','가죽 의자','가죽 책','가죽 옷'],'ans':0,'hint':('ottoman','오토만'),'explain':'ottoman = 발 받침'},
            {'en':'A tall shelf unit.','choices':['키 큰 선반장','키 큰 사람','키 큰 책','키 큰 옷'],'ans':0,'hint':('shelfunit','선반장'),'explain':'shelf unit = 보관'},
            {"en":"Grandma's rocking chair.",'choices':['할머니 흔들의자','할머니 책','할머니 옷','할머니 신발'],'ans':0,'hint':('rocking chair','흔들의자'),'explain':'rocking = 흔들'},
            {'en':'Sleep in the bunk bed.','choices':['이층 침대에서 자','일층에서 자','땅에서 자','책상에서 자'],'ans':0,'hint':('bunk bed','이층 침대'),'explain':'bunk bed = 형제 침대'},
            {'en':'Pretty wallpaper.','choices':['예쁜 벽지','예쁜 종이','예쁜 옷','예쁜 책'],'ans':0,'hint':('wallpaper','벽지'),'explain':'wallpaper = 벽에 붙임'},
            {'en':'Bathroom tile.','choices':['욕실 타일','욕실 비누','욕실 수건','욕실 거울'],'ans':0,'hint':('tile','타일'),'explain':'tile = 바닥·벽'},
            {'en':'Modern interior.','choices':['현대 인테리어','현대 옷','현대 책','현대 음식'],'ans':0,'hint':('interior','인테리어'),'explain':'interior = 실내'},
        ]
    },

    '20260818': {
        'date':'2026-08-18','day_ko':'화','theme':'음료 종류','theme_emoji':'🥤','description':'음료 영어!',
        'questions':[
            {'en':'A cold soda.','choices':['차가운 탄산','뜨거운 물','차가운 우유','차가운 차'],'ans':0,'hint':('soda','탄산음료'),'explain':'soda = 톡 쏘는'},
            {'en':'A can of cola.','choices':['콜라 한 캔','콜라 한 병','콜라 한 잔','콜라 없음'],'ans':0,'hint':('cola','콜라'),'explain':'cola = 검은 탄산'},
            {'en':'Fresh lemonade.','choices':['신선한 레모네이드','신선한 우유','신선한 주스','신선한 차'],'ans':0,'hint':('lemonade','레모네이드'),'explain':'lemonade = 레몬'},
            {'en':'Chocolate milkshake.','choices':['초콜릿 쉐이크','초콜릿 케이크','초콜릿 사탕','초콜릿 우유'],'ans':0,'hint':('milkshake','밀크쉐이크'),'explain':'milkshake = 우유+얼음'},
            {'en':'A creamy latte.','choices':['크리미 라떼','쓴 커피','진한 차','달콤 차'],'ans':0,'hint':('latte','라떼'),'explain':'latte = 우유 커피'},
            {'en':'Strong espresso.','choices':['진한 에스프레소','약한 에스프레소','새 에스프레소','없음'],'ans':0,'hint':('espresso','에스프레소'),'explain':'espresso = 진한 커피'},
            {'en':'Sweet hot chocolate.','choices':['달콤한 핫초콜릿','쓴 커피','짠 우유','신 주스'],'ans':0,'hint':('hot chocolate','핫초콜릿'),'explain':'핫초콜릿 = 겨울 음료'},
            {'en':'Strawberry yogurt drink.','choices':['딸기 요구르트','딸기 케이크','딸기 사탕','딸기 빵'],'ans':0,'hint':('yogurt drink','요구르트'),'explain':'yogurt drink = 마시는 요구르트'},
            {'en':'Cherry slush.','choices':['체리 슬러시','체리 케이크','체리 빵','체리 음료'],'ans':0,'hint':('slush','슬러시'),'explain':'slush = 얼음 음료'},
            {'en':'Green tea.','choices':['녹차','홍차','우유','주스'],'ans':0,'hint':('tea','차'),'explain':'tea = 잎으로 우림'},
            {'en':'Calm herbal tea.','choices':['진정 허브차','진정 음료','진정 우유','진정 케이크'],'ans':0,'hint':('herbal tea','허브차'),'explain':'herbal = 허브'},
            {'en':'Lemon iced tea.','choices':['레몬 아이스티','레몬 케이크','레몬 사탕','레몬 우유'],'ans':0,'hint':('iced tea','아이스티'),'explain':'iced tea = 여름!'},
            {'en':'Taro bubble tea.','choices':['타로 버블티','타로 케이크','타로 우유','타로 빵'],'ans':0,'hint':('bubble tea','버블티'),'explain':'bubble tea = 펄!'},
            {'en':'Fresh coconut water.','choices':['신선한 코코넛 워터','신선한 우유','신선한 빵','신선한 주스'],'ans':0,'hint':('coconut water','코코넛 워터'),'explain':'천연 음료!'},
            {'en':'Refreshing sparkling water.','choices':['상쾌한 탄산수','상쾌한 우유','상쾌한 차','상쾌한 빵'],'ans':0,'hint':('sparkling water','탄산수'),'explain':'sparkling = 버블 물'},
            {'en':'After workout protein shake.','choices':['운동 후 단백질 쉐이크','운동 후 우유','운동 후 차','운동 후 빵'],'ans':0,'hint':('protein shake','단백질'),'explain':'protein = 단백질'},
            {'en':'Warm hot cocoa.','choices':['따뜻한 핫코코아','따뜻한 우유','따뜻한 차','따뜻한 빵'],'ans':0,'hint':('hot cocoa','핫코코아'),'explain':'cocoa = 마시멜로!'},
            {'en':'Korean barley tea.','choices':['한국 보리차','한국 녹차','한국 홍차','한국 커피'],'ans':0,'hint':('barley tea','보리차'),'explain':'barley = 한국 음료'},
            {'en':'Free refreshment.','choices':['무료 음료','무료 책','무료 옷','무료 신발'],'ans':0,'hint':('refreshment','음료'),'explain':'refreshment = 마실 것'},
            {'en':'A fruity mocktail.','choices':['과일 무알코올 칵테일','과일 케이크','과일 사탕','과일 빵'],'ans':0,'hint':('mocktail','무알코올 칵테일'),'explain':'mocktail = 아이용!'},
        ]
    },

    '20260819': {
        'date':'2026-08-19','day_ko':'수','theme':'미용·헤어','theme_emoji':'💇','description':'미용 영어!',
        'questions':[
            {'en':'At the salon.','choices':['미용실에서','학교에서','집에서','시장에서'],'ans':0,'hint':('salon','미용실'),'explain':'salon = 미용 매장'},
            {'en':'Get a haircut.','choices':['머리 잘라요','머리 감아요','머리 빗어요','자기'],'ans':0,'hint':('haircut','머리 자르기'),'explain':'haircut = 자르기'},
            {'en':'Cool hairstyle.','choices':['멋진 헤어스타일','멋진 옷','멋진 신발','멋진 가방'],'ans':0,'hint':('hairstyle','헤어스타일'),'explain':'hairstyle = 머리 모양'},
            {'en':'A high ponytail.','choices':['높은 묶은 머리','낮은 머리','짧은 머리','긴 머리'],'ans':0,'hint':('ponytail','포니테일'),'explain':'ponytail = 말 꼬리'},
            {'en':'A long braid.','choices':['긴 땋은 머리','긴 짧은 머리','긴 묶은 머리','긴 곱슬'],'ans':0,'hint':('braid','땋은 머리'),'explain':'braid = 3가닥'},
            {'en':'Cut my bangs.','choices':['앞머리 잘라','뒷머리 잘라','옆머리 잘라','자기'],'ans':0,'hint':('bangs','앞머리'),'explain':'bangs = 이마 위'},
            {'en':'Use shampoo.','choices':['샴푸 써','컨디셔너 써','비누 써','로션 써'],'ans':0,'hint':('shampoo','샴푸'),'explain':'shampoo = 머리 감기'},
            {'en':'Apply conditioner.','choices':['린스 발라','샴푸 발라','비누 발라','로션 발라'],'ans':0,'hint':('conditioner','린스'),'explain':'conditioner = 부드럽게'},
            {'en':'Use a hairbrush.','choices':['머리빗 써','컴퓨터 써','책 써','옷 써'],'ans':0,'hint':('hairbrush','머리빗'),'explain':'hairbrush = 머리 빗기'},
            {'en':'Comb your hair.','choices':['머리 빗어요','머리 감아요','머리 잘라요','머리 던져요'],'ans':0,'hint':('comb','빗'),'explain':'comb = 가는 빗'},
            {'en':'Pink hair tie.','choices':['분홍 머리끈','분홍 옷','분홍 책','분홍 가방'],'ans':0,'hint':('hair tie','머리끈'),'explain':'hair tie = 묶는 끈'},
            {'en':'Cute hair clip.','choices':['귀여운 머리핀','귀여운 책','귀여운 옷','귀여운 가방'],'ans':0,'hint':('hair clip','머리핀'),'explain':'hair clip = 꽂는 핀'},
            {'en':'A flower headband.','choices':['꽃 머리띠','꽃 시계','꽃 가방','꽃 옷'],'ans':0,'hint':('headband','머리띠'),'explain':'headband = 머리 두름'},
            {'en':'Use a hairpin.','choices':['머리핀 써','연필 써','책 써','옷 써'],'ans':0,'hint':('hairpin','머리핀'),'explain':'hairpin = 가느다란'},
            {'en':'Pretty curls.','choices':['예쁜 컬','예쁜 책','예쁜 옷','예쁜 가방'],'ans':0,'hint':('curl','컬'),'explain':'curl = 꼬불꼬불'},
            {'en':'Get a perm.','choices':['파마해요','자','놀아','먹어'],'ans':0,'hint':('perm','파마'),'explain':'perm = 오래 가는 컬'},
            {'en':'Dye my hair.','choices':['염색해요','자','놀아','먹어'],'ans':0,'hint':('dye','염색'),'explain':'dye = 색 바꾸기'},
            {'en':'Trim the ends.','choices':['끝 다듬어요','끝 자','끝 던져','끝 사'],'ans':0,'hint':('trim','다듬다'),'explain':'trim = 조금 자르기'},
            {'en':'Mom does makeup.','choices':['엄마는 화장해','엄마는 잠 자','엄마는 놀아','엄마는 먹어'],'ans':0,'hint':('makeup','화장'),'explain':'makeup = 얼굴 꾸미기'},
            {'en':'Red lipstick.','choices':['빨간 립스틱','빨간 책','빨간 옷','빨간 가방'],'ans':0,'hint':('lipstick','립스틱'),'explain':'lipstick = 입술'},
        ]
    },

    '20260820': {
        'date':'2026-08-20','day_ko':'목','theme':'가게·상점','theme_emoji':'🏪','description':'쇼핑 영어!',
        'questions':[
            {'en':'At the grocery store.','choices':['식료품점에서','학교에서','집에서','시장에서'],'ans':0,'hint':('grocery store','식료품점'),'explain':'grocery = 음식'},
            {'en':'Big supermarket.','choices':['큰 슈퍼','큰 학교','큰 집','큰 책'],'ans':0,'hint':('supermarket','슈퍼마켓'),'explain':'supermarket = 큰 마트'},
            {'en':'24-hour convenience store.','choices':['24시 편의점','24시 학교','24시 집','24시 시장'],'ans':0,'hint':('convenience','편의'),'explain':'convenience = 24시간'},
            {'en':'Buy meat at the butcher.','choices':['정육점에서 고기','정육점에서 빵','정육점에서 우유','정육점에서 사과'],'ans':0,'hint':('butcher','정육점'),'explain':'butcher = 고기 파는 곳'},
            {'en':'Pretty jewelry store.','choices':['예쁜 보석상','예쁜 옷가게','예쁜 신발 가게','예쁜 책 가게'],'ans':0,'hint':('jewelry store','보석상'),'explain':'jewelry = 보석'},
            {'en':'Fun toy store.','choices':['재밌는 장난감 가게','재밌는 학교','재밌는 집','재밌는 책'],'ans':0,'hint':('toy store','장난감 가게'),'explain':'toy = 장난감'},
            {'en':'Browse the clothing store.','choices':['옷 가게 구경','음식 가게 구경','책 가게 구경','꽃 가게 구경'],'ans':0,'hint':('clothing store','옷가게'),'explain':'clothing = 옷'},
            {'en':'New shoes at the shoe store.','choices':['신발 가게의 새 신발','책 가게의 새 책','옷 가게의 새 옷','학교의 새 친구'],'ans':0,'hint':('shoe store','신발 가게'),'explain':'shoe = 신발'},
            {'en':'Buy a phone at the electronics store.','choices':['전자상가 전화','전자상가 빵','전자상가 옷','전자상가 신발'],'ans':0,'hint':('electronics','전자'),'explain':'electronics = 가전'},
            {'en':'Cute pet store.','choices':['귀여운 애견샵','귀여운 학교','귀여운 집','귀여운 시장'],'ans':0,'hint':('pet store','애견샵'),'explain':'pet = 동물'},
            {'en':'School supplies at the stationery store.','choices':['문구점의 학용품','문구점의 음식','문구점의 옷','문구점의 신발'],'ans':0,'hint':('stationery','문구'),'explain':'stationery = 학용품'},
            {'en':'Tools at the hardware store.','choices':['철물점의 도구','철물점의 음식','철물점의 옷','철물점의 신발'],'ans':0,'hint':('hardware','철물'),'explain':'hardware = 공구'},
            {'en':'Buy medicine at the pharmacy shop.','choices':['약국에서 약','약국에서 빵','약국에서 옷','약국에서 신발'],'ans':0,'hint':('pharmacy','약국'),'explain':'pharmacy = 약'},
            {'en':'Fresh bread at the bakery shop.','choices':['빵집의 빵','빵집의 음식','빵집의 옷','빵집의 책'],'ans':0,'hint':('bakery','빵집'),'explain':'bakery = 빵 굽기'},
            {'en':'Sandwich at the deli.','choices':['델리의 샌드위치','델리의 빵','델리의 우유','델리의 차'],'ans':0,'hint':('deli','델리'),'explain':'deli = 즉석 식품'},
            {'en':'Big warehouse store.','choices':['큰 창고형 매장','큰 학교','큰 집','큰 시장'],'ans':0,'hint':('warehouse','창고'),'explain':'warehouse = 코스트코!'},
            {'en':'Fresh fruit at the outdoor market.','choices':['야외 시장 신선 과일','학교 신선 과일','집 신선 과일','시장 신선 과일'],'ans':0,'hint':('outdoor market','야외 시장'),'explain':'outdoor = 야외'},
            {'en':'Pay at the checkout.','choices':['계산대 결제','학교 결제','집 결제','시장 결제'],'ans':0,'hint':('checkout','계산대'),'explain':'checkout = 돈 내는 곳'},
            {'en':'Push the shopping cart.','choices':['쇼핑카트 밀어','자전거 밀어','자동차 밀어','책 밀어'],'ans':0,'hint':('shopping cart','쇼핑카트'),'explain':'shopping cart = 마트 카트'},
            {'en':'Old antique shop.','choices':['오래된 골동품 가게','오래된 학교','오래된 집','오래된 시장'],'ans':0,'hint':('antique shop','골동품'),'explain':'antique = 옛 물건'},
        ]
    },

    '20260821': {
        'date':'2026-08-21','day_ko':'금','theme':'빛과 그림자','theme_emoji':'🔦','description':'빛 영어!',
        'questions':[
            {'en':'A warm glow.','choices':['따뜻한 빛','따뜻한 옷','따뜻한 음식','따뜻한 차'],'ans':0,'hint':('glow','빛'),'explain':'glow = 부드러운 빛'},
            {'en':'Stars sparkle.','choices':['별이 반짝','별이 자','별이 가','별이 먹어'],'ans':0,'hint':('sparkle','반짝'),'explain':'sparkle = 작은 반짝'},
            {'en':'The sun shines.','choices':['해가 빛나','해가 자','해가 가','해가 먹어'],'ans':0,'hint':('shine','빛나다'),'explain':'shine = 강한 빛'},
            {'en':'Water shimmers.','choices':['물이 가물거려','물이 자','물이 가','물이 먹어'],'ans':0,'hint':('shimmer','가물거리며'),'explain':'shimmer = 잔잔 반짝'},
            {'en':'Candles flicker.','choices':['촛불이 깜박','촛불이 자','촛불이 가','촛불이 먹어'],'ans':0,'hint':('flicker','깜박'),'explain':'flicker = 꺼졌다 켜졌다'},
            {'en':'Lights blink.','choices':['불이 깜빡','불이 자','불이 가','불이 먹어'],'ans':0,'hint':('blink','깜빡'),'explain':'blink = 깜빡임'},
            {'en':'Gold glitter.','choices':['금 반짝이','금 책','금 옷','금 신발'],'ans':0,'hint':('glitter','반짝이'),'explain':'glitter = 가루'},
            {'en':'Sun glare.','choices':['햇빛 눈부심','햇빛 약함','햇빛 자','햇빛 가'],'ans':0,'hint':('glare','눈부심'),'explain':'glare = 너무 밝음'},
            {'en':'A laser beam.','choices':['레이저 광선','레이저 책','레이저 옷','레이저 신발'],'ans':0,'hint':('beam','광선'),'explain':'beam = 빛줄기'},
            {'en':'Sun rays.','choices':['햇살','달빛','별빛','구름빛'],'ans':0,'hint':('ray','빛살'),'explain':'ray = 빛이 뻗음'},
            {'en':'Your reflection.','choices':['네 비친 모습','네 친구','네 책','네 옷'],'ans':0,'hint':('reflection','반사'),'explain':'reflection = 거울 속'},
            {'en':'A shadowy room.','choices':['그늘진 방','밝은 방','새 방','오래된 방'],'ans':0,'hint':('shadowy','그늘진'),'explain':'shadowy = 어두운'},
            {'en':'A dark silhouette.','choices':['어두운 실루엣','어두운 책','어두운 옷','어두운 신발'],'ans':0,'hint':('silhouette','실루엣'),'explain':'silhouette = 윤곽'},
            {'en':'A radiant smile.','choices':['환한 미소','어두운 미소','약한 미소','없음'],'ans':0,'hint':('radiant','환한'),'explain':'radiant = 밝게 빛남'},
            {'en':'Dim light.','choices':['어둑한 빛','밝은 빛','없는 빛','강한 빛'],'ans':0,'hint':('dim','어둑'),'explain':'dim = 약한 빛'},
            {'en':'A gloomy day.','choices':['어두운 날','밝은 날','새 날','오래된 날'],'ans':0,'hint':('gloomy','어두운'),'explain':'gloomy = 침울'},
            {'en':'Wave a glow stick.','choices':['야광봉 흔들기','자기','놀기','먹기'],'ans':0,'hint':('glow stick','야광봉'),'explain':'glow stick = 콘서트'},
            {'en':'Soft firefly light.','choices':['부드러운 반딧불 빛','부드러운 옷','부드러운 책','부드러운 우유'],'ans':0,'hint':('firefly light','반딧불 빛'),'explain':'firefly = 여름 밤'},
            {'en':'A silver moonbeam.','choices':['은빛 달빛','은빛 옷','은빛 책','은빛 신발'],'ans':0,'hint':('moonbeam','달빛 줄기'),'explain':'moonbeam = 달의 광선'},
            {'en':'Warm sunrays.','choices':['따뜻한 햇살','따뜻한 옷','따뜻한 빵','따뜻한 신발'],'ans':0,'hint':('sunray','햇살'),'explain':'sunray = 해의 빛줄기'},
        ]
    },

    '20260822': {
        'date':'2026-08-22','day_ko':'토','theme':'주말 쇼핑','theme_emoji':'🛍️','description':'쇼핑 영어 응용!',
        'questions':[
            {'en':"Let's go to the mall.",'choices':['쇼핑몰 가자','학교 가자','집 가자','시장 가자'],'ans':0,'hint':('mall','쇼핑몰'),'explain':'mall = 큰 쇼핑센터'},
            {'en':'How much is this?','choices':['이거 얼마?','이거 뭐?','이거 어디?','이거 누구?'],'ans':0,'hint':('how much','얼마'),'explain':'how much = 가격'},
            {'en':"It's on sale!",'choices':['할인 중!','새 거!','오래된 거!','없는 거!'],'ans':0,'hint':('sale','할인'),'explain':'on sale = 세일'},
            {'en':"I'll take it.",'choices':['이걸로 할게','싫어요','없어요','자요'],'ans':0,'hint':('take','사다'),'explain':"I'll take = 살게요"},
            {'en':'Cash or card?','choices':['현금? 카드?','이름? 시간?','어디? 뭐?','누구? 왜?'],'ans':0,'hint':('cash','현금'),'explain':'cash or card'},
            {'en':"Here's your receipt.",'choices':['영수증 여기','책 여기','선물 여기','자기 여기'],'ans':0,'hint':('receipt','영수증'),'explain':'receipt = 영수증'},
            {'en':'Try this on.','choices':['이거 입어봐','이거 사','이거 봐','이거 던져'],'ans':0,'hint':('try on','입어보다'),'explain':'try on = 입어보기'},
            {'en':"It's too expensive.",'choices':['너무 비싸','너무 싸','너무 좋아','너무 작아'],'ans':0,'hint':('expensive','비싼'),'explain':'expensive = 비쌈'},
            {'en':"It's cheap.",'choices':['싸요','비싸요','새 거','오래된 거'],'ans':0,'hint':('cheap','싼'),'explain':'cheap = 싼'},
            {'en':'A good deal!','choices':['좋은 가격!','나쁜 가격!','새 거!','오래된 거!'],'ans':0,'hint':('deal','가격'),'explain':'good deal = 좋은 거래'},
            {'en':"Where's the fitting room?",'choices':['탈의실 어디?','학교 어디?','집 어디?','시장 어디?'],'ans':0,'hint':('fitting room','탈의실'),'explain':'fitting = 입어보는 방'},
            {'en':'Different size?','choices':['다른 사이즈?','다른 색?','다른 가격?','다른 사람?'],'ans':0,'hint':('size','사이즈'),'explain':'size = 크기'},
            {'en':'Different color?','choices':['다른 색?','다른 사이즈?','다른 가격?','다른 사람?'],'ans':0,'hint':('color','색'),'explain':'color = 색깔'},
            {'en':'A discount, please.','choices':['할인해 주세요','선물 주세요','자게 해 주세요','보여 주세요'],'ans':0,'hint':('discount','할인'),'explain':'discount = 깎아주기'},
            {'en':"It's sold out.",'choices':['품절','할인','새 상품','다 있음'],'ans':0,'hint':('sold out','품절'),'explain':'sold out = 다 팔림'},
            {'en':'Free delivery!','choices':['배송 무료!','배송 유료!','배송 없음!','배송 늦음!'],'ans':0,'hint':('delivery','배송'),'explain':'delivery = 배달'},
            {'en':'A shopping bag.','choices':['쇼핑백','책가방','옷장','자기'],'ans':0,'hint':('shopping bag','쇼핑백'),'explain':'shopping bag = 쇼핑 가방'},
            {'en':"It looks good.",'choices':['잘 어울려','별로','싫어','이상해'],'ans':0,'hint':('look','보이다'),'explain':'looks good = 잘 어울림'},
            {'en':'Have a nice day!','choices':['좋은 하루!','잘 가요!','다시 와요!','감사!'],'ans':0,'hint':('nice day','좋은 하루'),'explain':'nice day = 좋은 하루!'},
            {'en':"It's a bargain!",'choices':['저렴해!','비싸!','새 거!','오래된 거!'],'ans':0,'hint':('bargain','저렴'),'explain':'bargain = 좋은 가격'},
        ]
    },

    '20260823': {
        'date':'2026-08-23','day_ko':'일','theme':'한 주 마무리','theme_emoji':'🌅','description':'주말 정리 영어!',
        'questions':[
            {'en':'What a week!','choices':['멋진 한 주!','피곤한 한 주!','짧은 한 주!','없는 한 주!'],'ans':0,'hint':('week','한 주'),'explain':'what a week!'},
            {'en':"I'm tired.",'choices':['피곤해','신나','즐거워','졸려'],'ans':0,'hint':('tired','피곤'),'explain':'tired = 피곤'},
            {'en':"Let's relax at home.",'choices':['집에서 쉬자','집에서 일하자','집에서 자자','집에서 먹자'],'ans':0,'hint':('relax','쉬다'),'explain':'relax = 쉬기'},
            {'en':'Watch a movie tonight.','choices':['오늘 밤 영화','오늘 밤 자','오늘 밤 가','오늘 밤 먹어'],'ans':0,'hint':('movie','영화'),'explain':'movie = 영화'},
            {'en':'Order food.','choices':['음식 주문','음식 만들기','자기','놀기'],'ans':0,'hint':('order','주문'),'explain':'order food = 시키기'},
            {'en':'Family time.','choices':['가족 시간','학교 시간','일 시간','자 시간'],'ans':0,'hint':('family','가족'),'explain':'family time = 가족과!'},
            {'en':'Read a book.','choices':['책 읽어','책 던져','책 사','책 자'],'ans':0,'hint':('read','읽다'),'explain':'read = 읽기'},
            {'en':'Play board games.','choices':['보드게임 해','자','놀아','먹어'],'ans':0,'hint':('board games','보드게임'),'explain':'보드게임!'},
            {'en':'Take a nap.','choices':['낮잠 자','일 해','놀아','먹어'],'ans':0,'hint':('nap','낮잠'),'explain':'nap = 짧은 잠'},
            {'en':"It's a peaceful day.",'choices':['평화로운 날','바쁜 날','피곤한 날','없는 날'],'ans':0,'hint':('peaceful','평화'),'explain':'peaceful = 조용'},
            {'en':'Listen to music.','choices':['음악 듣기','음악 끄기','음악 사기','음악 던지기'],'ans':0,'hint':('listen','듣다'),'explain':'listen to = ~ 듣기'},
            {'en':"Cuddle up with a blanket.",'choices':['담요 덮고 안락','담요 던져','담요 사','담요 봐'],'ans':0,'hint':('cuddle','꼭 안기'),'explain':'cuddle = 포근하게'},
            {'en':'Drink hot chocolate.','choices':['핫초콜릿 마셔','우유 마셔','차 마셔','물 마셔'],'ans':0,'hint':('hot chocolate','핫초콜릿'),'explain':'hot chocolate'},
            {'en':'Bake cookies.','choices':['쿠키 굽기','빵 굽기','케이크 굽기','파이 굽기'],'ans':0,'hint':('bake','굽다'),'explain':'bake cookies'},
            {'en':"Tomorrow is a new day.",'choices':['내일은 새로운 날','어제는 새로운 날','오늘은 새로운 날','없음'],'ans':0,'hint':('new day','새 날'),'explain':'tomorrow = 내일'},
            {'en':'Get ready for school.','choices':['학교 준비','집 준비','자기 준비','놀기 준비'],'ans':0,'hint':('ready','준비'),'explain':'get ready = 준비!'},
            {'en':'Pack your bag.','choices':['가방 싸기','옷 싸기','신발 싸기','책 싸기'],'ans':0,'hint':('pack','싸다'),'explain':'pack = 짐 싸기'},
            {'en':'Sleep early.','choices':['일찍 자기','늦게 자기','일찍 일어나','늦게 일어나'],'ans':0,'hint':('early','일찍'),'explain':'sleep early = 일찍 자기'},
            {'en':"It's been a great weekend!",'choices':['멋진 주말이었어!','피곤한 주말!','짧은 주말!','없는 주말!'],'ans':0,'hint':('weekend','주말'),'explain':'great weekend!'},
            {'en':'Goodnight!','choices':['잘 자!','잘 가!','잘 먹어!','잘 와!'],'ans':0,'hint':('goodnight','잘 자'),'explain':'goodnight = 잘 자!'},
        ]
    },

    # ═════════════════════════════════════════════
    # 8/24~8/30 (Week 19) - 새학기·미디어·약속·한국명소·액세서리
    # ═════════════════════════════════════════════
    '20260824': {
        'date':'2026-08-24','day_ko':'월','theme':'새 학기 준비','theme_emoji':'📚','description':'개학 영어!',
        'questions':[
            {'en':'New curriculum.','choices':['새 교과 과정','새 학교','새 친구','없음'],'ans':0,'hint':('curriculum','교과과정'),'explain':'curriculum = 배울 내용'},
            {'en':'Read the syllabus.','choices':['강의계획서 읽어','책 읽어','시 읽어','없음'],'ans':0,'hint':('syllabus','강의계획'),'explain':'syllabus = 학습 안내'},
            {'en':'Class roster.','choices':['반 명단','반 책','반 가게','반 친구'],'ans':0,'hint':('roster','명단'),'explain':'roster = 학생 목록'},
            {'en':'Check the timetable.','choices':['시간표 확인','시계 확인','책 확인','옷 확인'],'ans':0,'hint':('timetable','시간표'),'explain':'timetable = 수업 시간!'},
            {'en':'My cubby.','choices':['내 칸','내 책','내 옷','내 신발'],'ans':0,'hint':('cubby','사물 칸'),'explain':'cubby = 작은 보관함'},
            {'en':'New peer.','choices':['새 또래','새 친척','새 부모님','새 선생님'],'ans':0,'hint':('peer','또래'),'explain':'peer = 같은 나이'},
            {'en':'School orientation.','choices':['학교 오리엔테이션','학교 시험','학교 졸업식','없음'],'ans':0,'hint':('orientation','오리엔테이션'),'explain':'orientation = 첫 소개'},
            {'en':'Enroll in class.','choices':['수업 등록','자기','놀기','먹기'],'ans':0,'hint':('enroll','등록'),'explain':'enroll = 수강신청'},
            {'en':'Register for school.','choices':['학교 등록','학교 그만','없음','자'],'ans':0,'hint':('register','등록'),'explain':'register = 이름 올리기'},
            {'en':'Pay tuition.','choices':['학비 내요','용돈 받기','자','없음'],'ans':0,'hint':('tuition','학비'),'explain':'tuition = 학교 비용'},
            {'en':'School transcript.','choices':['성적증명서','책','옷','신발'],'ans':0,'hint':('transcript','성적증명'),'explain':'transcript = 공식 성적'},
            {'en':'School textbook.','choices':['학교 교과서','학교 옷','학교 음식','학교 시간'],'ans':0,'hint':('textbook','교과서'),'explain':'textbook = 배우는 책'},
            {'en':'Clean workspace.','choices':['깨끗한 공부 공간','더러운 옷','새 학교','오래된 책'],'ans':0,'hint':('workspace','공부 공간'),'explain':'workspace = 내 책상'},
            {'en':'Use a planner.','choices':['플래너 써','연필 써','책 써','옷 써'],'ans':0,'hint':('planner','플래너'),'explain':'planner = 계획 수첩'},
            {'en':'Make a checklist.','choices':['체크리스트 만들어','음식 만들어','옷 만들어','집 만들어'],'ans':0,'hint':('checklist','체크리스트'),'explain':'checklist = 할 일 목록'},
            {'en':"Today's agenda.",'choices':['오늘 안건','오늘 음식','오늘 옷','오늘 시간'],'ans':0,'hint':('agenda','안건'),'explain':'agenda = 오늘 할 일'},
            {'en':'Close the backpack zipper.','choices':['가방 지퍼 닫아','책 지퍼','옷 지퍼','신발 지퍼'],'ans':0,'hint':('backpack zipper','가방 지퍼'),'explain':'backpack zipper = 가방 잠금'},
            {'en':'The deadline approaches.','choices':['마감이 다가와요','시작이 다가와요','자','놀아'],'ans':0,'hint':('deadline approach','마감 임박'),'explain':'deadline = 제출!'},
            {'en':'Back to school sale.','choices':['개학 세일','새해 세일','크리스마스 세일','부활절 세일'],'ans':0,'hint':('backtoschool','개학'),'explain':'back to school = 학교로!'},
            {'en':'A freshman class.','choices':['신입생 반','졸업생 반','선생님 반','없음'],'ans':0,'hint':('freshman','신입생'),'explain':'freshman = 새내기'},
        ]
    },

    '20260825': {
        'date':'2026-08-25','day_ko':'화','theme':'미디어·스트리밍','theme_emoji':'📺','description':'미디어 영어!',
        'questions':[
            {'en':'Broadcast live.','choices':['생중계해요','녹화해요','자','놀아'],'ans':0,'hint':('broadcast live','생중계'),'explain':'broadcast live = 실시간!'},
            {'en':'Live broadcast.','choices':['생방송','녹화방송','지난 방송','없음'],'ans':0,'hint':('broadcast','방송'),'explain':'broadcast = 방송!'},
            {'en':'Subscribe to the channel.','choices':['채널 구독','채널 끊기','채널 사기','채널 봐'],'ans':0,'hint':('subscribe','구독'),'explain':'subscribe = 구독!'},
            {'en':'Unsubscribe button.','choices':['구독 취소 버튼','구독 버튼','구매 버튼','자기 버튼'],'ans':0,'hint':('unsubscribe','구독취소'),'explain':'unsubscribe = 끊기'},
            {'en':'My playlist.','choices':['내 재생목록','내 책','내 옷','내 음식'],'ans':0,'hint':('playlist','재생 목록'),'explain':'playlist = 좋아하는 곡!'},
            {'en':'A livestream show.','choices':['생방송 쇼','녹화 쇼','오래된 쇼','없음'],'ans':0,'hint':('livestream','생방송'),'explain':'livestream = 실시간!'},
            {'en':'Listen to a podcast.','choices':['팟캐스트 들어','책 읽어','TV 봐','자'],'ans':0,'hint':('podcast','팟캐스트'),'explain':'podcast = 오디오!'},
            {'en':'Make a vlog.','choices':['브이로그 찍어','책 만들어','옷 만들어','없음'],'ans':0,'hint':('vlog','브이로그'),'explain':'vlog = 비디오 블로그'},
            {'en':'Movie preview.','choices':['영화 미리보기','영화 끝','영화 시작','없음'],'ans':0,'hint':('preview','미리보기'),'explain':'preview = 살짝 보기!'},
            {'en':'Pretty thumbnail.','choices':['예쁜 썸네일','예쁜 책','예쁜 옷','예쁜 신발'],'ans':0,'hint':('thumbnail','썸네일'),'explain':'thumbnail = 미리보기 이미지'},
            {'en':'Many viewers.','choices':['많은 시청자','많은 친구','많은 학생','많은 책'],'ans':0,'hint':('viewer','시청자'),'explain':'viewer = 보는 사람'},
            {'en':'Million followers.','choices':['100만 팔로워','100만 책','100만 옷','100만 음식'],'ans':0,'hint':('follower','팔로워'),'explain':'follower = SNS 팬'},
            {'en':'Use a streaming service.','choices':['스트리밍 서비스 사용','책 사용','옷 사용','음식 사용'],'ans':0,'hint':('streaming service','스트리밍'),'explain':'streaming = Netflix!'},
            {'en':'Episode 1.','choices':['1화','1편','1책','없음'],'ans':0,'hint':('episode','에피소드'),'explain':'episode = 한 회'},
            {'en':'Season 2.','choices':['시즌 2','계절 2','책 2','없음'],'ans':0,'hint':('season','시즌'),'explain':'season = 한 시즌'},
            {'en':'Binge watch a show.','choices':['드라마 몰아봐요','드라마 끊어요','드라마 봐요','자기'],'ans':0,'hint':('binge','몰아보기'),'explain':'binge watch = 한꺼번에!'},
            {'en':'Upload a video.','choices':['영상 올려요','영상 받아요','영상 봐요','영상 던져요'],'ans':0,'hint':('upload','올리기'),'explain':'upload = 인터넷에!'},
            {'en':'Download a video.','choices':['영상 받아요','영상 올려요','영상 봐요','영상 던져요'],'ans':0,'hint':('download','받기'),'explain':'download = 내 기기에!'},
            {'en':'Viral video.','choices':['화제의 영상','옛 영상','새 영상','없음'],'ans':0,'hint':('viral','화제'),'explain':'viral = 빠르게 퍼짐'},
            {'en':'A new trend.','choices':['새로운 유행','새로운 옷','새로운 음식','새로운 책'],'ans':0,'hint':('trend','유행'),'explain':'trend = 인기 흐름'},
        ]
    },

    '20260826': {
        'date':'2026-08-26','day_ko':'수','theme':'약속과 시간','theme_emoji':'⏰','description':'시간 영어!',
        'questions':[
            {'en':'Doctor appointment.','choices':['의사 약속','학교 약속','친구 약속','부모 약속'],'ans':0,'hint':('appointment','약속'),'explain':'appointment = 정해진 만남'},
            {'en':'Team meeting.','choices':['팀 회의','학교 회의','집 회의','시장 회의'],'ans':0,'hint':('meeting','회의'),'explain':'meeting = 모임'},
            {'en':'Job interview.','choices':['취업 면접','학교 시험','없음','자'],'ans':0,'hint':('interview','면접'),'explain':'interview = 질문 답변'},
            {'en':'Hotel booking.','choices':['호텔 예약','호텔 청소','호텔 자기','호텔 봐'],'ans':0,'hint':('booking','예약'),'explain':'booking = 예약'},
            {'en':'Set a reminder.','choices':['알림 설정','알림 끄기','알림 봐','자기'],'ans':0,'hint':('reminder','알림'),'explain':'reminder = 미리 알림!'},
            {'en':'Morning routine.','choices':['아침 일과','저녁 일과','밤 일과','자기 일과'],'ans':0,'hint':('routine','일과'),'explain':'routine = 매일 같이'},
            {'en':'Weekly report.','choices':['주간 보고서','월간 보고서','일일 보고서','없음'],'ans':0,'hint':('weekly','매주'),'explain':'weekly = 한 주마다'},
            {'en':'Monthly meeting.','choices':['월간 회의','주간 회의','일일 회의','없음'],'ans':0,'hint':('monthly','월간'),'explain':'monthly = 한 달마다'},
            {'en':'Yearly checkup.','choices':['매년 검진','매월 검진','매주 검진','매일 검진'],'ans':0,'hint':('yearly','매년'),'explain':'yearly = 1년에 한 번'},
            {'en':'Arrive on time.','choices':['제 시간 도착','늦게 도착','일찍 도착','자기'],'ans':0,'hint':('on time','제 시간'),'explain':'on time = 안 늦게!'},
            {'en':'Book in advance.','choices':['미리 예약','나중에 예약','자','놀아'],'ans':0,'hint':('in advance','미리'),'explain':'in advance = 앞서서'},
            {'en':'Postpone the meeting.','choices':['회의 연기','회의 시작','회의 끝','없음'],'ans':0,'hint':('postpone','연기'),'explain':'postpone = 미루기'},
            {'en':'Cancel the trip.','choices':['여행 취소','여행 시작','여행 끝','없음'],'ans':0,'hint':('cancel','취소'),'explain':'cancel = 안 하기'},
            {'en':'Reschedule for tomorrow.','choices':['내일로 변경','어제로 변경','오늘 변경','없음'],'ans':0,'hint':('reschedule','일정 변경'),'explain':'reschedule = 날짜 바꿈'},
            {'en':'Confirm the date.','choices':['날짜 확인','날짜 잊어','날짜 바꿔','자'],'ans':0,'hint':('confirm','확인'),'explain':'confirm = 맞다고!'},
            {'en':'Hourly bus.','choices':['매시간 버스','매일 버스','매주 버스','없음'],'ans':0,'hint':('hourly','매시간'),'explain':'hourly = 시간마다'},
            {'en':'Midweek meeting.','choices':['주중 회의','주말 회의','새해 회의','크리스마스 회의'],'ans':0,'hint':('midweek','주중'),'explain':'midweek = 수요일쯤'},
            {'en':'Stay up till midnight.','choices':['자정까지 깨어있어','자정까지 자','자정까지 가','자정까지 먹어'],'ans':0,'hint':('midnight','자정'),'explain':'midnight = 밤 12시'},
            {'en':'Hot midday sun.','choices':['뜨거운 한낮 해','뜨거운 밤','뜨거운 새벽','뜨거운 아침'],'ans':0,'hint':('midday','한낮'),'explain':'midday = 낮 12시'},
            {'en':'Wake up at dawn.','choices':['새벽에 일어나','밤에 일어나','점심에 일어나','저녁에 일어나'],'ans':0,'hint':('dawn','새벽'),'explain':'dawn = 해 뜨기 직전'},
        ]
    },

    '20260827': {
        'date':'2026-08-27','day_ko':'목','theme':'한국 명소','theme_emoji':'🏯','description':'한국 명소 영어!',
        'questions':[
            {'en':'Visit Gyeongbokgung.','choices':['경복궁 방문','학교 방문','집 방문','시장 방문'],'ans':0,'hint':('Gyeongbokgung','경복궁'),'explain':'경복궁 = 조선 왕궁'},
            {'en':'Climb up Namsan Tower.','choices':['남산타워 올라가','남산타워 내려가','남산타워 봐','없음'],'ans':0,'hint':('Namsan Tower','남산타워'),'explain':'Namsan Tower = 서울 상징'},
            {'en':'Walk in Bukchon.','choices':['북촌 걸어요','학교 걸어요','집 걸어요','시장 걸어요'],'ans':0,'hint':('Bukchon','북촌'),'explain':'Bukchon = 한옥마을!'},
            {'en':'Buy souvenirs in Insadong.','choices':['인사동 기념품','인사동 음식','인사동 옷','인사동 책'],'ans':0,'hint':('Insadong','인사동'),'explain':'Insadong = 전통 거리!'},
            {'en':'Shop in Myeongdong.','choices':['명동 쇼핑','명동 자기','명동 놀기','명동 먹기'],'ans':0,'hint':('Myeongdong','명동'),'explain':'Myeongdong = 쇼핑!'},
            {'en':'Night life in Hongdae.','choices':['홍대 야경','홍대 아침','홍대 점심','홍대 자기'],'ans':0,'hint':('Hongdae','홍대'),'explain':'Hongdae = 젊은이!'},
            {'en':'International Itaewon.','choices':['국제적인 이태원','국제적인 학교','국제적인 집','국제적인 시장'],'ans':0,'hint':('Itaewon','이태원'),'explain':'Itaewon = 외국인 많음'},
            {'en':'Fun at Lotte World.','choices':['롯데월드 재미','학교 재미','집 재미','시장 재미'],'ans':0,'hint':('Lotte World','롯데월드'),'explain':'Lotte World = 놀이공원'},
            {'en':'Roller coaster at Everland.','choices':['에버랜드 롤러코스터','학교 롤러코스터','집 롤러코스터','없음'],'ans':0,'hint':('Everland','에버랜드'),'explain':'Everland = 놀이공원!'},
            {'en':'Climb Hallasan.','choices':['한라산 등산','학교 등산','집 등산','시장 등산'],'ans':0,'hint':('Hallasan','한라산'),'explain':'Hallasan = 제주도!'},
            {'en':'Visit Seoraksan.','choices':['설악산 방문','학교 방문','집 방문','시장 방문'],'ans':0,'hint':('Seoraksan','설악산'),'explain':'Seoraksan = 아름다운 산'},
            {'en':'Bike along the Han River.','choices':['한강 자전거','학교 자전거','집 자전거','시장 자전거'],'ans':0,'hint':('Han River','한강'),'explain':'Han River = 서울'},
            {'en':'Fresh fish at Jagalchi Market.','choices':['자갈치 생선','자갈치 옷','자갈치 책','자갈치 신발'],'ans':0,'hint':('Jagalchi','자갈치'),'explain':'Jagalchi = 부산!'},
            {'en':'Visit the DMZ.','choices':['DMZ 방문','학교 방문','집 방문','시장 방문'],'ans':0,'hint':('DMZ','비무장지대'),'explain':'DMZ = 남북 경계'},
            {'en':'Beautiful Jeju.','choices':['아름다운 제주','아름다운 서울','아름다운 부산','아름다운 대구'],'ans':0,'hint':('Jeju','제주'),'explain':'Jeju = 최고 관광지!'},
            {'en':'Ancient Bulguksa.','choices':['고대 불국사','새 학교','새 집','새 시장'],'ans':0,'hint':('Bulguksa','불국사'),'explain':'Bulguksa = 경주 절'},
            {'en':'Visit Seokguram.','choices':['석굴암 방문','학교 방문','집 방문','시장 방문'],'ans':0,'hint':('Seokguram','석굴암'),'explain':'Seokguram = 경주 석굴'},
            {'en':'Walk by Cheonggyecheon.','choices':['청계천 산책','학교 산책','집 산책','시장 산책'],'ans':0,'hint':('Cheonggyecheon','청계천'),'explain':'Cheonggyecheon = 서울!'},
            {'en':'Hike Bukhansan.','choices':['북한산 등산','학교 등산','집 등산','시장 등산'],'ans':0,'hint':('Bukhansan','북한산'),'explain':'Bukhansan = 서울 근교'},
            {'en':'Modern Gangnam.','choices':['현대적 강남','옛 강남','새 강남','오래된 강남'],'ans':0,'hint':('Gangnam','강남'),'explain':'Gangnam = 트렌디!'},
        ]
    },

    '20260828': {
        'date':'2026-08-28','day_ko':'금','theme':'옷 액세서리','theme_emoji':'👒','description':'액세서리 영어!',
        'questions':[
            {'en':'Wear a belt.','choices':['벨트 차요','벨트 빼요','벨트 사요','벨트 봐요'],'ans':0,'hint':('belt','벨트'),'explain':'belt = 바지 고정'},
            {'en':'Cool watch.','choices':['멋진 시계','멋진 책','멋진 옷','멋진 신발'],'ans':0,'hint':('watch','손목시계'),'explain':'watch = 시간 보기'},
            {'en':'Pretty necklace.','choices':['예쁜 목걸이','예쁜 책','예쁜 옷','예쁜 신발'],'ans':0,'hint':('necklace','목걸이'),'explain':'necklace = 목 장식'},
            {'en':'Silver bracelet.','choices':['은 팔찌','은 책','은 옷','은 신발'],'ans':0,'hint':('bracelet','팔찌'),'explain':'bracelet = 손목!'},
            {'en':'Cute earrings.','choices':['귀여운 귀걸이','귀여운 책','귀여운 옷','귀여운 신발'],'ans':0,'hint':('earrings','귀걸이'),'explain':'earrings = 귀 장식'},
            {'en':'A gold ring.','choices':['금반지','금책','금옷','금신발'],'ans':0,'hint':('ring','반지'),'explain':'ring = 손가락'},
            {'en':'Wear a sunhat.','choices':['썬햇 써','책 사','옷 입어','신발 신어'],'ans':0,'hint':('sunhat','썬햇'),'explain':'sunhat = 햇빛 가리기'},
            {'en':'Warm beanie.','choices':['따뜻한 비니','따뜻한 옷','따뜻한 신발','따뜻한 음식'],'ans':0,'hint':('beanie','비니'),'explain':'beanie = 겨울 모자'},
            {'en':'Black beret.','choices':['검정 베레모','검정 옷','검정 신발','검정 책'],'ans':0,'hint':('beret','베레모'),'explain':'beret = 프랑스 모자'},
            {'en':'Wear a bow tie.','choices':['나비 넥타이 매','옷 입어','신발 신어','자기'],'ans':0,'hint':('bow tie','나비 넥타이'),'explain':'bow tie = 정장!'},
            {'en':'Blue necktie.','choices':['파란 넥타이','파란 책','파란 옷','파란 신발'],'ans':0,'hint':('necktie','넥타이'),'explain':'necktie = 정장!'},
            {'en':'A warm shawl.','choices':['따뜻한 숄','따뜻한 책','따뜻한 음식','따뜻한 신발'],'ans':0,'hint':('shawl','숄'),'explain':'shawl = 어깨 두름'},
            {'en':'Leather wallet.','choices':['가죽 지갑','가죽 책','가죽 옷','가죽 신발'],'ans':0,'hint':('wallet','지갑'),'explain':'wallet = 돈·카드'},
            {'en':'Small purse.','choices':['작은 핸드백','작은 책','작은 옷','작은 신발'],'ans':0,'hint':('purse','핸드백'),'explain':'purse = 여성용'},
            {'en':'A leather handbag.','choices':['가죽 핸드백','가죽 책','가죽 옷','가죽 신발'],'ans':0,'hint':('handbag','핸드백'),'explain':'handbag = 손에!'},
            {'en':'Evening clutch.','choices':['이브닝 클러치','이브닝 책','이브닝 옷','이브닝 신발'],'ans':0,'hint':('clutch','클러치'),'explain':'clutch = 작은 손가방'},
            {'en':'Adjust the strap.','choices':['끈 조절','책 조절','옷 조절','신발 조절'],'ans':0,'hint':('strap','끈'),'explain':'strap = 가방끈'},
            {'en':'Designer eyewear.','choices':['디자이너 안경','디자이너 옷','디자이너 신발','디자이너 책'],'ans':0,'hint':('eyewear','안경류'),'explain':'eyewear = 안경 통칭'},
            {'en':'Pink hairband.','choices':['분홍 헤어밴드','분홍 옷','분홍 신발','분홍 책'],'ans':0,'hint':('hairband','헤어밴드'),'explain':'hairband = 머리 두름'},
            {'en':'School badge.','choices':['학교 배지','학교 책','학교 옷','학교 신발'],'ans':0,'hint':('badge','배지'),'explain':'badge = 이름표!'},
        ]
    },

    '20260829': {
        'date':'2026-08-29','day_ko':'토','theme':'주말 외출','theme_emoji':'🚶','description':'외출 영어!',
        'questions':[
            {'en':"Let's go out!",'choices':['외출하자!','자자!','놀자!','먹자!'],'ans':0,'hint':('go out','외출'),'explain':'go out = 나가기'},
            {'en':'A sunny day.','choices':['화창한 날','흐린 날','비 오는 날','눈 오는 날'],'ans':0,'hint':('sunny','화창'),'explain':'sunny = 햇살!'},
            {'en':'Walk in the park.','choices':['공원 산책','학교 산책','집 산책','시장 산책'],'ans':0,'hint':('park','공원'),'explain':'walk in park = 공원!'},
            {'en':'Visit grandma.','choices':['할머니 방문','선생님 방문','친구 방문','부모님 방문'],'ans':0,'hint':('visit','방문'),'explain':'visit = 찾아가기'},
            {'en':'Eat lunch outside.','choices':['밖에서 점심','집에서 점심','학교에서 점심','시장에서 점심'],'ans':0,'hint':('outside','밖'),'explain':'outside = 바깥'},
            {'en':'Take a photo.','choices':['사진 찍어','음식 만들어','책 봐','자'],'ans':0,'hint':('photo','사진'),'explain':'take photo = 찍기'},
            {'en':'Smile for the camera.','choices':['카메라 보고 웃어','TV 보고 웃어','책 보고 웃어','자'],'ans':0,'hint':('camera','카메라'),'explain':'smile for camera = 찍을 때!'},
            {'en':"Let's go shopping.",'choices':['쇼핑 가자','학교 가자','자','놀자'],'ans':0,'hint':('shopping','쇼핑'),'explain':'shopping = 쇼핑'},
            {'en':'Try on clothes.','choices':['옷 입어보기','옷 사기','옷 던지기','옷 자기'],'ans':0,'hint':('try on','입어보기'),'explain':'try on = 입어봐'},
            {'en':'I like this one.','choices':['이게 좋아','싫어','없어','자'],'ans':0,'hint':('like','좋아'),'explain':'like this = 이게 좋아'},
            {'en':'Buy a gift.','choices':['선물 사기','책 사기','음식 사기','자기'],'ans':0,'hint':('gift','선물'),'explain':'buy gift = 선물 사기'},
            {'en':'Wrap the present.','choices':['선물 포장','선물 봐','선물 던져','선물 사'],'ans':0,'hint':('wrap','포장'),'explain':'wrap = 포장하기'},
            {'en':'Catch the bus.','choices':['버스 잡아','버스 던져','버스 사','버스 봐'],'ans':0,'hint':('catch','잡다'),'explain':'catch bus = 버스 타기'},
            {'en':'Wait at the bus stop.','choices':['버스 정거장에서 기다려','집에서 기다려','학교에서 기다려','시장에서 기다려'],'ans':0,'hint':('bus stop','정거장'),'explain':'wait at = ~에서 기다림'},
            {'en':'Cross the street.','choices':['길 건너','길 가','길 봐','길 사'],'ans':0,'hint':('cross','건너다'),'explain':'cross = 건너기'},
            {'en':'Walk slowly.','choices':['천천히 걸어','빨리 걸어','자','놀아'],'ans':0,'hint':('slowly','천천히'),'explain':'walk slowly = 천천히'},
            {'en':'Stop at the corner.','choices':['모퉁이에서 멈춰','학교에서 멈춰','집에서 멈춰','시장에서 멈춰'],'ans':0,'hint':('corner','모퉁이'),'explain':'corner = 꺾이는 곳'},
            {'en':'Look both ways.','choices':['양쪽 봐','한쪽 봐','자','놀아'],'ans':0,'hint':('both ways','양쪽'),'explain':'both ways = 양옆'},
            {'en':'Hold my hand.','choices':['손 잡아줘','손 빼','손 봐','손 던져'],'ans':0,'hint':('hold hand','손잡기'),'explain':'hold = 잡기'},
            {'en':"What a fun day!",'choices':['재밌는 하루!','피곤한 하루!','짧은 하루!','없는 하루!'],'ans':0,'hint':('fun','재밌는'),'explain':'fun day = 재미!'},
        ]
    },

    '20260830': {
        'date':'2026-08-30','day_ko':'일','theme':'개학 전 준비','theme_emoji':'🎒','description':'학교 준비 영어!',
        'questions':[
            {'en':'School starts tomorrow.','choices':['내일 학교 시작','어제 학교 시작','오늘 학교 끝','없음'],'ans':0,'hint':('start','시작'),'explain':'school starts = 학교!'},
            {'en':'Prepare for school.','choices':['학교 준비','학교 끝','학교 자','학교 놀'],'ans':0,'hint':('prepare','준비'),'explain':'prepare = 미리 챙기기'},
            {'en':'Pack your bag.','choices':['가방 싸기','가방 던지기','가방 사기','가방 자기'],'ans':0,'hint':('pack','싸다'),'explain':'pack = 짐 싸기'},
            {'en':'Sharpen the pencils.','choices':['연필 깎기','연필 던지기','연필 사기','연필 자기'],'ans':0,'hint':('sharpen','깎다'),'explain':'sharpen = 날카롭게'},
            {'en':'Lay out clothes.','choices':['옷 미리 꺼내','옷 던져','옷 사','옷 자'],'ans':0,'hint':('lay out','꺼내놓다'),'explain':'lay out = 준비!'},
            {'en':'Set the alarm.','choices':['알람 맞춰','알람 꺼','알람 봐','알람 자'],'ans':0,'hint':('alarm','알람'),'explain':'set alarm = 알람 설정'},
            {'en':'Go to bed early.','choices':['일찍 자','늦게 자','일어나','일하기'],'ans':0,'hint':('bed early','일찍'),'explain':'go to bed early = 일찍 자기'},
            {'en':'Eat a good breakfast.','choices':['좋은 아침 먹어','좋은 점심 먹어','좋은 저녁 먹어','좋은 간식 먹어'],'ans':0,'hint':('breakfast','아침'),'explain':'breakfast = 아침 식사'},
            {'en':'Brush your teeth.','choices':['이 닦아','얼굴 닦아','머리 빗어','발 닦아'],'ans':0,'hint':('brush teeth','이 닦기'),'explain':'brush teeth = 이!'},
            {'en':'Wash your face.','choices':['세수해','자','놀아','먹어'],'ans':0,'hint':('wash face','세수'),'explain':'wash face = 얼굴 씻기'},
            {'en':'Wear your uniform.','choices':['교복 입어','옷 입어','신발 신어','모자 써'],'ans':0,'hint':('uniform','교복'),'explain':'uniform = 학교 옷'},
            {'en':'Tie your shoes.','choices':['신발 끈 묶어','신발 던져','신발 사','신발 봐'],'ans':0,'hint':('tie','묶다'),'explain':'tie shoes = 끈 묶기'},
            {'en':'Check your books.','choices':['책 확인','책 던져','책 사','책 자'],'ans':0,'hint':('check','확인'),'explain':'check books = 책 확인!'},
            {'en':'Bring your homework.','choices':['숙제 가져가','숙제 잊어','숙제 던져','숙제 자'],'ans':0,'hint':('bring','가져오다'),'explain':'bring homework = 가져가'},
            {'en':'Be ready on time.','choices':['제 시간 준비','늦게 준비','자','놀아'],'ans':0,'hint':('ready','준비'),'explain':'ready on time = 제때!'},
            {'en':'Say hi to friends.','choices':['친구에게 인사','친구 미워','친구 자','친구 가'],'ans':0,'hint':('hi','안녕'),'explain':'say hi = 인사하기'},
            {'en':'Pay attention in class.','choices':['수업 집중','수업 자','수업 놀','수업 먹'],'ans':0,'hint':('pay attention','집중'),'explain':'pay attention = 집중!'},
            {'en':'Raise your hand.','choices':['손 들어','손 내려','손 봐','손 자'],'ans':0,'hint':('raise','올리다'),'explain':'raise hand = 손!'},
            {'en':'Listen to the teacher.','choices':['선생님 들어','TV 들어','음악 들어','자'],'ans':0,'hint':('listen','듣다'),'explain':'listen to teacher = 잘 들어'},
            {'en':'Have a great first day!','choices':['멋진 첫날!','피곤한 첫날!','짧은 첫날!','없는 첫날!'],'ans':0,'hint':('first day','첫날'),'explain':'first day = 개학!'},
        ]
    },

    '20260831': {
        'date':'2026-08-31','day_ko':'월','theme':'새 친구 사귀기','theme_emoji':'🤝','description':'친구 사귀기 영어!',
        'questions':[
            {'en':'Nice to meet you.','choices':['만나서 반가워','잘 가','안녕히','자'],'ans':0,'hint':('meet','만나다'),'explain':'meet = 만나기!'},
            {'en':"What's your name?",'choices':['이름이 뭐야?','어디 살아?','몇 살이야?','뭐 해?'],'ans':0,'hint':('name','이름'),'explain':'name = 이름'},
            {'en':"I'm Hyewon.",'choices':['난 혜원이야','난 학생이야','난 가','난 자'],'ans':0,'hint':("I'm",'나는'),'explain':"I'm = 나는!"},
            {'en':'How old are you?','choices':['몇 살이야?','이름이 뭐야?','어디야?','뭐 해?'],'ans':0,'hint':('old','나이'),'explain':'old = 나이!'},
            {'en':"Let's be friends.",'choices':['친구 하자','싸우자','자자','놀자'],'ans':0,'hint':('friends','친구'),'explain':"let's = 하자!"},
            {'en':'Where do you live?','choices':['어디 살아?','뭐 먹어?','뭐 해?','어디 가?'],'ans':0,'hint':('live','살다'),'explain':'live = 살다'},
            {'en':'I live in Seoul.','choices':['서울에 살아','부산 살아','자','놀아'],'ans':0,'hint':('live in','~에 살다'),'explain':'live in = 살다'},
            {'en':"What's your hobby?",'choices':['취미가 뭐야?','이름이 뭐야?','집 어디?','뭐 먹어?'],'ans':0,'hint':('hobby','취미'),'explain':'hobby = 취미!'},
            {'en':'I like drawing.','choices':['그림 좋아','요리 좋아','자','놀아'],'ans':0,'hint':('drawing','그림'),'explain':'drawing = 그림'},
            {'en':"Let's play together.",'choices':['같이 놀자','혼자 자','TV 봐','자'],'ans':0,'hint':('together','같이'),'explain':'together = 함께!'},
            {'en':'Can I sit here?','choices':['여기 앉아도 돼?','여기 자도 돼?','여기 가도 돼?','여기 먹어도 돼?'],'ans':0,'hint':('sit','앉다'),'explain':'sit = 앉기'},
            {'en':'Sure, sit down.','choices':['그래, 앉아','싫어','자','가'],'ans':0,'hint':('sure','그럼'),'explain':'sure = 좋아!'},
            {'en':'You are so kind.','choices':['넌 정말 친절해','넌 정말 나빠','자','놀아'],'ans':0,'hint':('kind','친절'),'explain':'kind = 친절!'},
            {'en':"You're funny.",'choices':['넌 웃겨','넌 슬퍼','자','놀아'],'ans':0,'hint':('funny','웃긴'),'explain':'funny = 재밌!'},
            {'en':'Thank you!','choices':['고마워!','싫어!','자!','가!'],'ans':0,'hint':('thank','고마움'),'explain':'thank = 감사!'},
            {'en':"You're welcome.",'choices':['천만에','싫어','자','가'],'ans':0,'hint':('welcome','환영'),'explain':"you're welcome = 천만!"},
            {'en':"What's up?",'choices':['뭐 해?','어디야?','뭐야?','자'],'ans':0,'hint':('up','어떻게'),'explain':"what's up = 안녕!"},
            {'en':'See you tomorrow.','choices':['내일 봐','어제 봐','자','놀아'],'ans':0,'hint':('tomorrow','내일'),'explain':'see you = 또 봐!'},
            {'en':'Give me a high five!','choices':['하이파이브!','악수해','자','놀아'],'ans':0,'hint':('high five','파이브'),'explain':'high five = 짝!'},
            {'en':"You're my best friend.",'choices':['넌 단짝이야','넌 형이야','자','놀아'],'ans':0,'hint':('best friend','단짝'),'explain':'best friend = 절친!'},
        ]
    },

    '20260901': {
        'date':'2026-09-01','day_ko':'화','theme':'초가을 풍경','theme_emoji':'🍂','description':'가을 영어!',
        'questions':[
            {'en':'Fall is here.','choices':['가을이 왔어','여름이 왔어','겨울이 왔어','봄이 왔어'],'ans':0,'hint':('fall','가을'),'explain':'fall = 가을!'},
            {'en':'The leaves turn red.','choices':['잎이 빨개져','잎이 자라','잎이 떨어져','잎이 푸르러'],'ans':0,'hint':('turn','변하다'),'explain':'turn red = 빨개지다'},
            {'en':'Cool breeze blows.','choices':['시원한 바람 불어','뜨거운 바람','자','놀아'],'ans':0,'hint':('breeze','산들바람'),'explain':'breeze = 산들바람'},
            {'en':'I love autumn.','choices':['가을 좋아해','여름 좋아','자','놀아'],'ans':0,'hint':('autumn','가을'),'explain':'autumn = 가을'},
            {'en':'Look at the sky.','choices':['하늘 봐','땅 봐','자','놀아'],'ans':0,'hint':('sky','하늘'),'explain':'sky = 하늘'},
            {'en':'The sky is so blue.','choices':['하늘이 너무 파래','하늘이 빨개','자','놀아'],'ans':0,'hint':('blue','파란'),'explain':'blue sky = 파란 하늘'},
            {'en':'Eat a chestnut.','choices':['밤 먹어','감 먹어','대추 먹어','배 먹어'],'ans':0,'hint':('chestnut','밤'),'explain':'chestnut = 밤!'},
            {'en':'Pick a persimmon.','choices':['감을 따','배를 따','자','놀아'],'ans':0,'hint':('pick','따다'),'explain':'pick = 따기'},
            {'en':"It's a little chilly.",'choices':['좀 쌀쌀해','좀 더워','자','놀아'],'ans':0,'hint':('chilly','쌀쌀'),'explain':'chilly = 쌀쌀!'},
            {'en':'Wear a jacket.','choices':['재킷 입어','반팔 입어','자','놀아'],'ans':0,'hint':('wear','입다'),'explain':'wear = 입기'},
            {'en':'Leaves are falling.','choices':['잎이 떨어져','잎이 올라','자','놀아'],'ans':0,'hint':('fall','떨어지다'),'explain':'falling = 떨어지는!'},
            {'en':'Walk in the park.','choices':['공원에서 산책','집에서 자','자','놀아'],'ans':0,'hint':('walk','걷다'),'explain':'walk in park = 공원 산책'},
            {'en':'The moon is bright.','choices':['달이 밝아','해가 밝아','자','놀아'],'ans':0,'hint':('moon','달'),'explain':'moon = 달'},
            {'en':'Harvest time!','choices':['수확 시기!','심을 때','자','놀아'],'ans':0,'hint':('harvest','수확'),'explain':'harvest = 거두기!'},
            {'en':'Red apples on the tree.','choices':['나무에 빨간 사과','땅에 사과','자','놀아'],'ans':0,'hint':('apple','사과'),'explain':'on tree = 나무 위'},
            {'en':'Days get shorter.','choices':['낮이 짧아져','낮이 길어져','자','놀아'],'ans':0,'hint':('short','짧은'),'explain':'shorter = 더 짧은'},
            {'en':'Roast some sweet potatoes.','choices':['고구마 구워','떡 구워','자','놀아'],'ans':0,'hint':('roast','굽다'),'explain':'roast = 굽기'},
            {'en':'A dragonfly flies by.','choices':['잠자리가 날아가','벌이 날아','자','놀아'],'ans':0,'hint':('fly','날다'),'explain':'fly = 날다!'},
            {'en':'Wear long sleeves.','choices':['긴팔 입어','반팔 입어','자','놀아'],'ans':0,'hint':('sleeves','소매'),'explain':'long sleeves = 긴팔'},
            {'en':'Autumn is so pretty!','choices':['가을 정말 예뻐!','여름 예뻐','자','놀아'],'ans':0,'hint':('pretty','예쁜'),'explain':'pretty = 예쁜!'},
        ]
    },

    '20260902': {
        'date':'2026-09-02','day_ko':'수','theme':'동아리 활동','theme_emoji':'🎭','description':'동아리 영어!',
        'questions':[
            {'en':'Join the club.','choices':['동아리 가입','동아리 빠져','자','놀아'],'ans':0,'hint':('join','가입'),'explain':'join = 들어가다!'},
            {'en':'I joined art club.','choices':['미술부 들어갔어','미술부 빠졌어','자','놀아'],'ans':0,'hint':('art','미술'),'explain':'art club = 미술부'},
            {'en':"Let's sing together.",'choices':['같이 노래하자','혼자 자','자','가'],'ans':0,'hint':('sing','노래'),'explain':'sing = 노래!'},
            {'en':'Practice every day.','choices':['매일 연습','매일 자','매일 놀','매일 먹'],'ans':0,'hint':('practice','연습'),'explain':'practice = 연습!'},
            {'en':'Show me your dance.','choices':['춤 보여줘','노래 보여','자','놀아'],'ans':0,'hint':('show','보여주다'),'explain':'show = 보여주기'},
            {'en':'Read a book club.','choices':['독서 동아리','수학 동아리','자','놀아'],'ans':0,'hint':('book','책'),'explain':'book club = 독서!'},
            {'en':'I love acting.','choices':['연기 좋아해','요리 좋아해','자','놀아'],'ans':0,'hint':('acting','연기'),'explain':'acting = 연기!'},
            {'en':'Big stage tonight.','choices':['오늘 밤 큰 무대','내일 작은 무대','자','놀아'],'ans':0,'hint':('stage','무대'),'explain':'stage = 무대!'},
            {'en':'Get ready for rehearsal.','choices':['리허설 준비','휴식 준비','자','놀아'],'ans':0,'hint':('rehearsal','연습'),'explain':'rehearsal = 리허설!'},
            {'en':'The show starts soon.','choices':['공연 곧 시작','공연 끝났어','자','놀아'],'ans':0,'hint':('start','시작'),'explain':'show start = 시작!'},
            {'en':'Sing on the stage.','choices':['무대에서 노래','집에서 노래','자','놀아'],'ans':0,'hint':('on stage','무대 위'),'explain':'on stage = 무대 위!'},
            {'en':'I play the piano.','choices':['피아노 쳐','기타 쳐','자','놀아'],'ans':0,'hint':('play','연주'),'explain':'play piano = 피아노!'},
            {'en':'Practice makes perfect.','choices':['연습이 완벽','자면 완벽','자','놀아'],'ans':0,'hint':('perfect','완벽'),'explain':'practice → 완벽!'},
            {'en':'My turn to speak.','choices':['내 차례 말하기','네 차례 자','자','놀아'],'ans':0,'hint':('turn','차례'),'explain':'turn = 차례!'},
            {'en':'Wear costumes.','choices':['의상 입어','반팔 입어','자','놀아'],'ans':0,'hint':('costume','의상'),'explain':'costumes = 무대 옷!'},
            {'en':'Big audience tonight.','choices':['오늘 관객 많아','관객 없어','자','놀아'],'ans':0,'hint':('audience','관객'),'explain':'audience = 관객!'},
            {'en':"Don't be nervous.",'choices':['긴장하지 마','긴장해','자','놀아'],'ans':0,'hint':('nervous','긴장'),'explain':"don't = 하지 마!"},
            {'en':'Take a deep breath.','choices':['숨 크게 쉬어','숨 작게','자','놀아'],'ans':0,'hint':('deep','깊은'),'explain':'deep breath = 심호흡!'},
            {'en':'Good luck!','choices':['행운을 빌어!','싫어!','자!','놀아!'],'ans':0,'hint':('luck','운'),'explain':'good luck = 행운!'},
            {'en':'Amazing performance!','choices':['멋진 공연!','지루한 공연!','자!','놀아!'],'ans':0,'hint':('amazing','멋진'),'explain':'amazing = 굉장!'},
        ]
    },

    '20260903': {
        'date':'2026-09-03','day_ko':'목','theme':'운동회','theme_emoji':'🏃','description':'운동회 영어!',
        'questions':[
            {'en':'Sports day today!','choices':['오늘 운동회!','오늘 시험!','자','놀아'],'ans':0,'hint':('sports day','운동회'),'explain':'sports day = 운동회!'},
            {'en':'Run as fast as you can.','choices':['최대한 빨리 뛰어','천천히 걸어','자','놀아'],'ans':0,'hint':('fast','빠르게'),'explain':'as fast as = 최대한 빨리'},
            {'en':"Don't give up!",'choices':['포기하지 마!','포기해!','자!','놀아!'],'ans':0,'hint':('give up','포기'),'explain':"don't give up = 포기 X!"},
            {'en':"You can do it!",'choices':['넌 할 수 있어!','넌 못해!','자!','놀아!'],'ans':0,'hint':('can','할 수 있다'),'explain':'can do = 할 수 있어!'},
            {'en':'Pass the baton.','choices':['바톤 넘겨','바톤 던져','자','놀아'],'ans':0,'hint':('pass','넘기다'),'explain':'pass = 넘기다!'},
            {'en':'Cross the finish line.','choices':['결승선 통과','출발선','자','놀아'],'ans':0,'hint':('cross','지나다'),'explain':'cross = 가로지르다!'},
            {'en':'Cheer for our team!','choices':['우리 팀 응원!','상대 팀 응원','자','놀아'],'ans':0,'hint':('cheer','응원'),'explain':'cheer = 응원!'},
            {'en':'Win the race!','choices':['경주 이겨!','경주 져!','자','놀아'],'ans':0,'hint':('win','이기다'),'explain':'win = 이기다!'},
            {'en':"It's a tie!",'choices':['무승부!','승리!','패배!','자!'],'ans':0,'hint':('tie','동점'),'explain':'tie = 동점!'},
            {'en':'Pull the rope.','choices':['줄을 당겨','줄을 놔','자','놀아'],'ans':0,'hint':('pull','당기다'),'explain':'pull = 당기다!'},
            {'en':'Jump high!','choices':['높이 뛰어!','낮게 뛰어','자','놀아'],'ans':0,'hint':('jump','뛰다'),'explain':'jump high = 높이 뛰기!'},
            {'en':"That's a great score.",'choices':['멋진 점수','나쁜 점수','자','놀아'],'ans':0,'hint':('score','점수'),'explain':'score = 점수!'},
            {'en':'Take a break.','choices':['쉬어','달려','자','놀아'],'ans':0,'hint':('break','휴식'),'explain':'take a break = 쉬기!'},
            {'en':'Drink some water.','choices':['물 마셔','콜라 마셔','자','놀아'],'ans':0,'hint':('water','물'),'explain':'drink water = 물!'},
            {'en':'Wear your team color.','choices':['팀 색 입어','검정 입어','자','놀아'],'ans':0,'hint':('color','색'),'explain':'team color = 팀 색!'},
            {'en':'Race against time.','choices':['시간과의 싸움','친구와의 싸움','자','놀아'],'ans':0,'hint':('against','대결'),'explain':'against = 맞서!'},
            {'en':'Be a good sport.','choices':['스포츠맨답게','지지 말고','자','놀아'],'ans':0,'hint':('good sport','매너'),'explain':'good sport = 매너 좋게!'},
            {'en':'Congratulations!','choices':['축하해!','싫어!','자!','놀아!'],'ans':0,'hint':('congrats','축하'),'explain':'congrats = 축하!'},
            {'en':'We are number one!','choices':['우리가 1등!','우리가 꼴찌','자!','놀아!'],'ans':0,'hint':('number one','1등'),'explain':'number one = 1등!'},
            {'en':'Great teamwork!','choices':['멋진 팀워크!','나쁜 팀워크','자!','놀아!'],'ans':0,'hint':('teamwork','협동'),'explain':'teamwork = 협동!'},
        ]
    },

    '20260904': {
        'date':'2026-09-04','day_ko':'금','theme':'추석 준비','theme_emoji':'🌕','description':'추석 영어!',
        'questions':[
            {'en':'Chuseok is coming.','choices':['추석이 다가와','설날 다가와','자','놀아'],'ans':0,'hint':('Chuseok','추석'),'explain':'Chuseok = 추석!'},
            {'en':'Make songpyeon together.','choices':['같이 송편 빚어','혼자 자','자','놀아'],'ans':0,'hint':('songpyeon','송편'),'explain':'songpyeon = 송편!'},
            {'en':'Look at the full moon.','choices':['보름달 봐','반달 봐','자','놀아'],'ans':0,'hint':('full moon','보름달'),'explain':'full moon = 보름달!'},
            {'en':'Visit my grandma.','choices':['할머니 댁 가','학교 가','자','놀아'],'ans':0,'hint':('visit','방문'),'explain':'visit = 방문!'},
            {'en':'Wear hanbok.','choices':['한복 입어','한복 빨아','자','놀아'],'ans':0,'hint':('hanbok','한복'),'explain':'hanbok = 한복!'},
            {'en':'Family gathering.','choices':['가족 모임','학교 모임','자','놀아'],'ans':0,'hint':('family','가족'),'explain':'family = 가족!'},
            {'en':'Long holiday.','choices':['긴 연휴','짧은 연휴','자','놀아'],'ans':0,'hint':('long','긴'),'explain':'long holiday = 긴 연휴!'},
            {'en':'Play yutnori.','choices':['윷놀이 해','체스 해','자','놀아'],'ans':0,'hint':('yutnori','윷놀이'),'explain':'yutnori = 윷놀이!'},
            {'en':'Tasty rice cakes.','choices':['맛있는 떡','맛없는 빵','자','놀아'],'ans':0,'hint':('rice cake','떡'),'explain':'rice cake = 떡!'},
            {'en':"Make wishes to the moon.",'choices':['달에게 소원 빌어','해에게 빌어','자','놀아'],'ans':0,'hint':('wish','소원'),'explain':'wish = 소원!'},
            {'en':'Set the table.','choices':['상 차려','상 치워','자','놀아'],'ans':0,'hint':('table','상'),'explain':'set table = 상 차리기!'},
            {'en':'Bow to grandparents.','choices':['조부모께 절','친구에 절','자','놀아'],'ans':0,'hint':('bow','절'),'explain':'bow = 절!'},
            {'en':'Drive to hometown.','choices':['고향 가','학교 가','자','놀아'],'ans':0,'hint':('hometown','고향'),'explain':'hometown = 고향!'},
            {'en':'Traffic is heavy.','choices':['차 막혀','차 시원해','자','놀아'],'ans':0,'hint':('heavy','심한'),'explain':'heavy traffic = 막힘!'},
            {'en':'Eat too much food.','choices':['많이 먹어','조금 먹어','자','놀아'],'ans':0,'hint':('too much','너무 많이'),'explain':'too much = 너무 많이!'},
            {'en':'Help cook the food.','choices':['요리 도와','요리 망쳐','자','놀아'],'ans':0,'hint':('help','돕다'),'explain':'help cook = 요리 돕기!'},
            {'en':'Share with cousins.','choices':['사촌과 나눠','혼자 다 먹어','자','놀아'],'ans':0,'hint':('share','나누다'),'explain':'share = 나누기!'},
            {'en':'Sing folk songs.','choices':['민요 불러','팝 불러','자','놀아'],'ans':0,'hint':('folk','전통'),'explain':'folk song = 민요!'},
            {'en':"Take family photos.",'choices':['가족 사진 찍어','자','놀아','먹어'],'ans':0,'hint':('photo','사진'),'explain':'take photo = 찍기!'},
            {'en':'Happy Chuseok!','choices':['즐거운 추석!','슬픈 추석!','자!','놀아!'],'ans':0,'hint':('happy','즐거운'),'explain':'happy = 즐거운!'},
        ]
    },

    '20260905': {
        'date':'2026-09-05','day_ko':'토','theme':'주말 외출','theme_emoji':'🚶','description':'주말 활동 영어!',
        'questions':[
            {'en':'Go out this weekend.','choices':['이번 주말 외출','평일 외출','자','놀아'],'ans':0,'hint':('go out','나가다'),'explain':'go out = 외출!'},
            {'en':'Walk in the park.','choices':['공원 산책','집에서 자','자','놀아'],'ans':0,'hint':('walk','산책'),'explain':'walk = 걷기/산책!'},
            {'en':'Ride a bike.','choices':['자전거 타','버스 타','자','놀아'],'ans':0,'hint':('bike','자전거'),'explain':'bike = 자전거!'},
            {'en':"Let's go shopping.",'choices':['쇼핑 가자','자자','자','놀아'],'ans':0,'hint':('shopping','쇼핑'),'explain':"let's go = 가자!"},
            {'en':'Visit the museum.','choices':['박물관 방문','학교 방문','자','놀아'],'ans':0,'hint':('museum','박물관'),'explain':'museum = 박물관!'},
            {'en':'Watch a movie.','choices':['영화 봐','TV 봐','자','놀아'],'ans':0,'hint':('movie','영화'),'explain':'watch movie = 영화!'},
            {'en':'Eat at a restaurant.','choices':['식당에서 먹어','집에서 먹어','자','놀아'],'ans':0,'hint':('restaurant','식당'),'explain':'restaurant = 식당!'},
            {'en':"That's delicious.",'choices':['맛있어','맛없어','자','놀아'],'ans':0,'hint':('delicious','맛있는'),'explain':'delicious = 맛있는!'},
            {'en':'Take a selfie.','choices':['셀카 찍어','TV 봐','자','놀아'],'ans':0,'hint':('selfie','셀카'),'explain':'selfie = 셀카!'},
            {'en':"Beautiful weather today.",'choices':['오늘 날씨 좋아','오늘 날씨 나빠','자','놀아'],'ans':0,'hint':('weather','날씨'),'explain':'weather = 날씨!'},
            {'en':'Buy a souvenir.','choices':['기념품 사','책 사','자','놀아'],'ans':0,'hint':('souvenir','기념품'),'explain':'souvenir = 기념품!'},
            {'en':"Let's get ice cream.",'choices':['아이스크림 먹자','국밥 먹자','자','놀아'],'ans':0,'hint':('ice cream','아이스크림'),'explain':'ice cream = 아이스!'},
            {'en':'The line is long.','choices':['줄이 길어','줄이 짧아','자','놀아'],'ans':0,'hint':('line','줄'),'explain':'line = 줄!'},
            {'en':'Wait your turn.','choices':['차례 기다려','새치기 해','자','놀아'],'ans':0,'hint':('wait','기다리다'),'explain':'wait turn = 차례!'},
            {'en':"It's getting late.",'choices':['늦어지고 있어','이르네','자','놀아'],'ans':0,'hint':('late','늦은'),'explain':'late = 늦은!'},
            {'en':'Time to go home.','choices':['집 갈 시간','놀 시간','자','놀아'],'ans':0,'hint':('go home','집 가다'),'explain':'go home = 집 가!'},
            {'en':"Today was fun.",'choices':['오늘 재밌었어','오늘 지루','자','놀아'],'ans':0,'hint':('fun','재미'),'explain':'fun = 재미!'},
            {'en':'I am tired.','choices':['나 피곤해','나 신나','자','놀아'],'ans':0,'hint':('tired','피곤'),'explain':'tired = 피곤!'},
            {'en':'Sleep tight!','choices':['잘 자!','자지 마!','놀아!','먹어!'],'ans':0,'hint':('tight','꿀잠'),'explain':'sleep tight = 잘 자!'},
            {'en':'See you again soon.','choices':['곧 다시 봐','다시 안 봐','자','놀아'],'ans':0,'hint':('again','다시'),'explain':'again = 다시!'},
        ]
    },

    '20260906': {
        'date':'2026-09-06','day_ko':'일','theme':'개학 전 마무리','theme_emoji':'🎒','description':'개학 마무리 영어!',
        'questions':[
            {'en':'New week starts tomorrow.','choices':['내일 새 주 시작','어제 새 주','자','놀아'],'ans':0,'hint':('week','주'),'explain':'new week = 새 주!'},
            {'en':'Check the calendar.','choices':['달력 확인','달 봐','자','놀아'],'ans':0,'hint':('calendar','달력'),'explain':'calendar = 달력!'},
            {'en':'Pack the school bag.','choices':['학교 가방 싸','책 던져','자','놀아'],'ans':0,'hint':('pack','싸다'),'explain':'pack = 싸다!'},
            {'en':"Don't forget your books.",'choices':['책 잊지 마','책 잊어','자','놀아'],'ans':0,'hint':('forget','잊다'),'explain':"don't forget = 잊지 마!"},
            {'en':'Finish the homework.','choices':['숙제 끝내','숙제 미뤄','자','놀아'],'ans':0,'hint':('finish','끝내다'),'explain':'finish = 끝!'},
            {'en':'Set my alarm.','choices':['알람 맞춰','알람 꺼','자','놀아'],'ans':0,'hint':('alarm','알람'),'explain':'set alarm = 알람 설정!'},
            {'en':"Go to bed early.",'choices':['일찍 자','늦게 자','자','놀아'],'ans':0,'hint':('early','일찍'),'explain':'early = 일찍!'},
            {'en':'Brush your teeth.','choices':['이 닦아','얼굴 닦아','자','놀아'],'ans':0,'hint':('brush','닦다'),'explain':'brush teeth = 이 닦기!'},
            {'en':'Wash your face.','choices':['세수해','자','놀아','먹어'],'ans':0,'hint':('wash face','세수'),'explain':'wash face = 세수!'},
            {'en':'Comb my hair.','choices':['머리 빗어','이 닦아','자','놀아'],'ans':0,'hint':('comb','빗다'),'explain':'comb = 빗다!'},
            {'en':'Wear clean clothes.','choices':['깨끗한 옷 입어','더러운 옷','자','놀아'],'ans':0,'hint':('clean','깨끗한'),'explain':'clean = 깨끗한!'},
            {'en':"It's a new start.",'choices':['새로운 시작','마지막','자','놀아'],'ans':0,'hint':('start','시작'),'explain':'new start = 새 시작!'},
            {'en':'Greet your friends.','choices':['친구에게 인사','친구 미워','자','놀아'],'ans':0,'hint':('greet','인사'),'explain':'greet = 인사!'},
            {'en':'Listen in class.','choices':['수업 잘 들어','자','놀','먹'],'ans':0,'hint':('listen','듣다'),'explain':'listen = 듣기!'},
            {'en':'Take good notes.','choices':['필기 잘해','필기 안해','자','놀아'],'ans':0,'hint':('notes','필기'),'explain':'notes = 필기!'},
            {'en':'Ask if you wonder.','choices':['궁금하면 물어','조용히','자','놀아'],'ans':0,'hint':('ask','묻다'),'explain':'ask = 묻기!'},
            {'en':'Try your best.','choices':['최선을 다해','대충해','자','놀아'],'ans':0,'hint':('best','최선'),'explain':'best = 최선!'},
            {'en':'Be kind to everyone.','choices':['모두에 친절','한 명에','자','놀아'],'ans':0,'hint':('kind','친절'),'explain':'kind = 친절!'},
            {'en':'Have a great week!','choices':['멋진 한 주!','피곤한 한 주!','자!','놀아!'],'ans':0,'hint':('great','멋진'),'explain':'great week = 멋진 주!'},
            {'en':'You can do anything.','choices':['뭐든 할 수 있어','아무것도 못해','자','놀아'],'ans':0,'hint':('anything','뭐든'),'explain':'anything = 뭐든지!'},
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

// ═══════ 🔊 발음 시스템 v3 (통일 음성) ═══════
// ═══════ 🔊 통일 발음 엔진 v3 — 모든 브라우저 동일 음성 ═══════
// 구글 음성 파일을 받아 재생 → 어느 기기/브라우저든 같은 목소리·같은 음량
// 음성 파일이 안 되면 브라우저 내장 음성으로 자동 백업
var TTS_VOLUME = 0.7;                 // 0.0 ~ 1.0  모든 기기 공통 음량
var TTS_SILENT = 'data:audio/wav;base64,UklGRrQBAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YZABAACAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA';
var _ttsVoices = [];
var _ttsReady = false;
var _ttsAudio = (typeof Audio !== 'undefined') ? new Audio() : null;

function _ttsLoadVoices() {{
  if (!('speechSynthesis' in window)) return;
  try {{ _ttsVoices = window.speechSynthesis.getVoices() || []; }} catch(e) {{}}
}}
if ('speechSynthesis' in window) {{
  _ttsLoadVoices();
  if (window.speechSynthesis.onvoiceschanged !== undefined) {{
    window.speechSynthesis.onvoiceschanged = _ttsLoadVoices;
  }}
}}

// 첫 터치/클릭 때 오디오 잠금 해제 (모바일 자동재생 정책 대응)
function _ttsPrime() {{
  if (_ttsReady) return;
  _ttsReady = true;
  if (_ttsAudio) {{
    try {{
      _ttsAudio.src = TTS_SILENT;
      _ttsAudio.volume = 0;
      var pr = _ttsAudio.play();
      if (pr && pr.catch) pr.catch(function(){{}});
    }} catch(e) {{}}
  }}
  try {{
    if ('speechSynthesis' in window) {{
      var w = new SpeechSynthesisUtterance(' ');
      w.volume = 0.01;
      window.speechSynthesis.speak(w);
    }}
  }} catch(e) {{}}
}}
document.addEventListener('click', _ttsPrime, {{ capture: true }});
document.addEventListener('touchstart', _ttsPrime, {{ capture: true, passive: true }});

// 브라우저 내장 음성 (백업)
function _ttsFallback(text, onDone) {{
  if (!('speechSynthesis' in window)) {{ if (onDone) onDone(); return; }}
  try {{
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US'; u.rate = 0.85; u.pitch = 1.05; u.volume = TTS_VOLUME;
    if (_ttsVoices.length === 0) _ttsLoadVoices();
    var v = null, i;
    for (i = 0; i < _ttsVoices.length; i++) {{
      if (_ttsVoices[i].lang === 'en-US') {{ v = _ttsVoices[i]; break; }}
    }}
    if (!v) {{
      for (i = 0; i < _ttsVoices.length; i++) {{
        if (_ttsVoices[i].lang && _ttsVoices[i].lang.indexOf('en') === 0) {{ v = _ttsVoices[i]; break; }}
      }}
    }}
    if (v) u.voice = v;
    u.onend = function(){{ if (onDone) onDone(); }};
    u.onerror = function(){{ if (onDone) onDone(); }};
    window.speechSynthesis.speak(u);
    setTimeout(function(){{ try {{ window.speechSynthesis.resume(); }} catch(e){{}} }}, 120);
  }} catch(e) {{ if (onDone) onDone(); }}
}}

// 핵심: 통일 음성 파일 재생 → 실패 시 백업
function playTTS(text, onStart, onDone) {{
  if (!text) {{ if (onDone) onDone(); return; }}
  text = String(text).trim();
  try {{ if (_ttsAudio) _ttsAudio.pause(); }} catch(e) {{}}
  try {{ if ('speechSynthesis' in window) window.speechSynthesis.cancel(); }} catch(e) {{}}

  var settled = false;
  function done() {{ if (settled) return; settled = true; if (onDone) onDone(); }}
  function fallback() {{ if (settled) return; settled = true; _ttsFallback(text, function(){{ if (onDone) onDone(); }}); }}

  if (onStart) onStart();

  if (!_ttsAudio) {{ fallback(); return; }}
  var audio = _ttsAudio;
  audio.onended = function(){{ done(); }};
  audio.onerror = function(){{ fallback(); }};
  try {{
    audio.volume = TTS_VOLUME;
    audio.src = 'https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q=' + encodeURIComponent(text);
    var p = audio.play();
    if (p && p.catch) {{ p.catch(function(){{ fallback(); }}); }}
  }} catch(e) {{ fallback(); }}
}}

function speakSentence(sentence, btn) {{
  playTTS(sentence,
    function(){{ if (btn) btn.classList.add('speaking'); }},
    function(){{ if (btn) btn.classList.remove('speaking'); }});
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
  if (_ttsReady) {{
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
