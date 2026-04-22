/**
 * 혜원이 영단어 학습 기록 서버 (Google Apps Script)
 * =====================================================
 *
 * 역할: HTML(퀴즈)에서 받은 학습 기록을 Google Sheets에 저장
 *   - 단어장기록 시트: 언제 시작해서 언제 끝났는지, 발음 듣기 횟수
 *   - 퀴즈기록 시트: 시도횟수(1차/2차/3차), 점수, 틀린 단어
 *
 * 카톡 발송은 기존 "매일매일 퀴즈내기" Apps Script가 담당하므로
 * 여기는 오직 Sheets 저장만! (훨씬 간단해졌어요 ✨)
 *
 * 📌 시트 ID는 이미 채워져 있어요. 그냥 복사-붙여넣기만 하면 돼요.
 */

// ============ Google Sheets 설정 ============
// 재님이 만드신 "혜원이 영단어 기록" 스프레드시트 ID (자동 입력됨)
const SHEET_ID = "1wqob-TM5UfWs1eDNDzADeg9tkHjErB1MdghCLg1b1Cg";

// ============ 시트 이름 ============
const VOCAB_SHEET_NAME = "단어장기록";
const QUIZ_SHEET_NAME = "퀴즈기록";

// ============ HTML에서 POST 요청 받기 ============
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const result = { ok: true, actions: [] };

    // 1. 단어장 기록 저장
    if (data.vocab) {
      saveVocabRecord(data.vocab);
      result.actions.push('vocab_saved');
    }

    // 2. 퀴즈 기록 저장
    if (data.quiz) {
      saveQuizRecord(data.quiz);
      result.actions.push('quiz_saved');
    }

    return ContentService.createTextOutput(JSON.stringify(result))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// ============ 단어장 기록 저장 ============
function saveVocabRecord(v) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(VOCAB_SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(VOCAB_SHEET_NAME);
    sheet.appendRow([
      '날짜', '요일', '테마', '시작시간', '종료시간',
      '학습시간(분)', '단어수', '발음듣기횟수', '단어목록'
    ]);
    sheet.getRange(1, 1, 1, 9).setBackground('#c8e6c9').setFontWeight('bold');
    sheet.setFrozenRows(1);
    // 컬럼 너비 조정
    sheet.setColumnWidth(1, 100); // 날짜
    sheet.setColumnWidth(2, 80);  // 요일
    sheet.setColumnWidth(3, 120); // 테마
    sheet.setColumnWidth(4, 150); // 시작시간
    sheet.setColumnWidth(5, 150); // 종료시간
    sheet.setColumnWidth(9, 400); // 단어목록
  }

  sheet.appendRow([
    v.date,
    v.day,
    v.theme || '',
    v.startTime,
    v.endTime,
    v.minutes,
    v.wordsLearned,
    v.listens,
    (v.words || []).join(', ')
  ]);
}

// ============ 퀴즈 기록 저장 ============
function saveQuizRecord(q) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(QUIZ_SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(QUIZ_SHEET_NAME);
    sheet.appendRow([
      '날짜', '요일', '시도횟수', '시작시간', '종료시간',
      '풀이시간(분)', '점수', '총문항', '맞은개수', '틀린개수', '틀린단어'
    ]);
    sheet.getRange(1, 1, 1, 11).setBackground('#ffcdd2').setFontWeight('bold');
    sheet.setFrozenRows(1);
    // 컬럼 너비 조정
    sheet.setColumnWidth(1, 100); // 날짜
    sheet.setColumnWidth(2, 80);  // 요일
    sheet.setColumnWidth(3, 80);  // 시도횟수
    sheet.setColumnWidth(4, 150); // 시작시간
    sheet.setColumnWidth(5, 150); // 종료시간
    sheet.setColumnWidth(11, 400); // 틀린단어
  }

  sheet.appendRow([
    q.date,
    q.day,
    q.attemptNumber + '차',
    q.startTime,
    q.endTime,
    q.minutes,
    q.score,
    q.total,
    q.correctCount,
    q.wrongCount,
    (q.wrongWords || []).join(', ')
  ]);
}

// ============ 브라우저 URL 직접 열 때 표시 ============
function doGet() {
  return ContentService.createTextOutput(
    "혜원이 영단어 서버가 정상 작동 중이에요! 🌟\n" +
    "이 URL은 HTML 퀴즈에서 자동으로 호출돼요."
  );
}

// ============ 테스트 함수 ============
// Apps Script 에디터에서 이 함수를 실행해서 시트 저장이 되는지 확인하세요
function testSheet() {
  saveVocabRecord({
    date: '2026-04-21',
    day: 'Monday',
    theme: '테스트 테마',
    startTime: '2026-04-21 08:00:00',
    endTime: '2026-04-21 08:15:00',
    minutes: 15,
    wordsLearned: 20,
    listens: 100,
    words: ['test1', 'test2', 'test3']
  });
  saveQuizRecord({
    date: '2026-04-21',
    day: 'Monday',
    attemptNumber: 1,
    startTime: '2026-04-21 15:00:00',
    endTime: '2026-04-21 15:05:00',
    minutes: 5,
    score: 18,
    total: 20,
    correctCount: 18,
    wrongCount: 2,
    wrongWords: ['giraffe', 'penguin']
  });
  Logger.log('✅ 테스트 완료! 스프레드시트 탭으로 가서 "단어장기록"과 "퀴즈기록" 시트를 확인하세요.');
}
