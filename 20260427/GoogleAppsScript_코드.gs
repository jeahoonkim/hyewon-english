/**
 * 혜원이 영단어 학습 기록 서버 (Google Apps Script)
 * =====================================================
 *
 * 기능 1: HTML(퀴즈)에서 받은 학습 기록을 Google Sheets에 저장
 * 기능 2: 매일 아침 7시 재님 카톡으로 학습 리마인더 발송 (NEW!)
 *
 * 시트:
 *   - 단어장기록 시트: 언제 시작해서 언제 끝났는지, 발음 듣기 횟수
 *   - 퀴즈기록 시트: 시도횟수(1차/2차/3차), 점수, 틀린 단어
 *
 * 카톡 발송은 기존 "매일매일 퀴즈내기" Apps Script가 담당
 */

// ============ Google Sheets 설정 ============
const SHEET_ID = "1wqob-TM5UfWs1eDNDzADeg9tkHjErB1MdghCLg1b1Cg";

// ============ 시트 이름 ============
const VOCAB_SHEET_NAME = "단어장기록";
const QUIZ_SHEET_NAME = "퀴즈기록";

// ============ 기존 카톡 발송 Apps Script URL (재님이 만든 것) ============
const LEGACY_APPS_URL = "https://script.google.com/macros/s/AKfycbzBGQgFRhsSdQimr8UwIbFXF1pubMLSuMFXketQ_XJGvsA5fNh3oo_JQ9cviWQSKbAPyg/exec";

// ============ 혜원이 홈페이지 ============
const HOMEPAGE_URL = "https://hyewon-english.pages.dev/";


// =====================================================
// [1] HTML에서 POST 요청 받기 → 시트에 기록 저장
// =====================================================
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const result = { ok: true, actions: [] };

    if (data.vocab) {
      saveVocabRecord(data.vocab);
      result.actions.push('vocab_saved');
    }
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


// =====================================================
// [2] 단어장 기록 저장
// =====================================================
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
    sheet.setColumnWidth(1, 100);
    sheet.setColumnWidth(2, 80);
    sheet.setColumnWidth(3, 120);
    sheet.setColumnWidth(4, 150);
    sheet.setColumnWidth(5, 150);
    sheet.setColumnWidth(9, 400);
  }

  sheet.appendRow([
    v.date, v.day, v.theme || '',
    v.startTime, v.endTime,
    v.minutes, v.wordsLearned, v.listens,
    (v.words || []).join(', ')
  ]);
}


// =====================================================
// [3] 퀴즈 기록 저장
// =====================================================
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
    sheet.setColumnWidth(1, 100);
    sheet.setColumnWidth(2, 80);
    sheet.setColumnWidth(3, 80);
    sheet.setColumnWidth(4, 150);
    sheet.setColumnWidth(5, 150);
    sheet.setColumnWidth(11, 400);
  }

  sheet.appendRow([
    q.date, q.day, q.attemptNumber + '차',
    q.startTime, q.endTime,
    q.minutes, q.score, q.total,
    q.correctCount, q.wrongCount,
    (q.wrongWords || []).join(', ')
  ]);
}


// =====================================================
// [4] 브라우저 URL 직접 열 때 표시
// =====================================================
function doGet() {
  return ContentService.createTextOutput(
    "혜원이 영단어 서버가 정상 작동 중이에요! 🌟\n" +
    "이 URL은 HTML 퀴즈에서 자동으로 호출돼요."
  );
}


// =====================================================
// [5] 🔔 아침 리마인더 (Time Trigger로 매일 아침 7시 자동 실행)
// =====================================================
function morningReminder() {
  const today = new Date();
  const dayIdx = today.getDay(); // 0=일, 1=월, ..., 6=토
  const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const dayKoNames = ['일', '월', '화', '수', '목', '금', '토'];
  const dayEn = dayNames[dayIdx];
  const dayKo = dayKoNames[dayIdx];

  // 오늘 날짜 포맷 (예: 4월 27일)
  const month = today.getMonth() + 1;
  const date = today.getDate();
  const dateStr = `${month}월 ${date}일 (${dayKo})`;

  let msg = '';

  // 일요일 - 복습의 날
  if (dayEn === 'Sunday') {
    msg = '🌻 일요일은 복습의 날!\n\n' +
          `📅 ${dateStr}\n\n` +
          '지난주 틀린 단어를 같이 복습해봐요 💪\n\n' +
          `👉 ${HOMEPAGE_URL}\n\n` +
          '혜원이한테 링크 전달해주세요!';
  }
  // 토요일 - 종합시험
  else if (dayEn === 'Saturday') {
    msg = '📝 토요일 종합시험 Day!\n\n' +
          `📅 ${dateStr}\n\n` +
          '이번주 배운 단어 100개 한방에 테스트 🎯\n\n' +
          `👉 ${HOMEPAGE_URL}\n\n' +
          '혜원이 파이팅! 🐱';
  }
  // 평일 (월~금) - 일반 학습
  else {
    msg = `🌅 혜원이 오늘 영단어 시간!\n\n` +
          `📅 ${dateStr}\n\n` +
          `📚 아침 7시: 단어장 (20개 단어)\n` +
          `📝 오후 3시: 퀴즈 도전\n\n` +
          `👉 ${HOMEPAGE_URL}\n\n` +
          `혜원이한테 링크 전달해주세요 😊`;
  }

  sendKakaoSelf(msg);
}


// =====================================================
// [6] 📱 카톡으로 재님에게 메시지 전송 (기존 Apps Script 활용)
// =====================================================
function sendKakaoSelf(subject) {
  const url = LEGACY_APPS_URL + '?subject=' + encodeURIComponent(subject);
  try {
    UrlFetchApp.fetch(url, {
      method: 'get',
      muteHttpExceptions: true
    });
    Logger.log('✅ 카톡 발송 성공: ' + subject.substring(0, 30) + '...');
  } catch (err) {
    Logger.log('❌ 카톡 발송 실패: ' + err.toString());
  }
}


// =====================================================
// [7] 🧪 테스트 함수 (수동 실행해서 리마인더 카톡 오는지 확인)
// =====================================================
function testReminder() {
  Logger.log('📢 리마인더 테스트 발송 중...');
  morningReminder();
  Logger.log('✅ 완료! 재님 카톡을 확인해보세요.');
}


// =====================================================
// [8] 🧪 시트 저장 테스트 함수 (초기 설정 확인용)
// =====================================================
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
    score: 18, total: 20,
    correctCount: 18, wrongCount: 2,
    wrongWords: ['giraffe', 'penguin']
  });
  Logger.log('✅ 테스트 완료! 스프레드시트 탭으로 가서 확인하세요.');
}
