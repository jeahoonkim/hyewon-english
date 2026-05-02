/**
 * 혜원이 영단어 학습 기록 서버 (Google Apps Script)
 * =====================================================
 *
 * 기능:
 *   [1] HTML에서 받은 학습 기록을 Google Sheets에 저장
 *   [2] Google 캘린더에 주간 학습 일정 자동 등록 (NEW! 🆕)
 *   [3] 매일 아침 카톡 리마인더 (선택 사항)
 */

// ============ Google Sheets 설정 ============
const SHEET_ID = "1wqob-TM5UfWs1eDNDzADeg9tkHjErB1MdghCLg1b1Cg";
const VOCAB_SHEET_NAME = "단어장기록";
const QUIZ_SHEET_NAME = "퀴즈기록";
const ACTIVITY_SHEET_NAME = "활동기록";   // 🆕 모든 활동 시간순
const STATUS_SHEET_NAME = "현재상태";     // 🆕 요약 대시보드
const COUPONS_SHEET_NAME = "쿠폰목록";    // 🆕 모든 기기 동기화용
const SYNC_SHEET_NAME = "동기화상태";     // 🆕 포인트/지갑/스트릭 마스터

// ============ 카톡 발송 URL (기존 재님 Apps Script) ============
const LEGACY_APPS_URL = "https://script.google.com/macros/s/AKfycbzBGQgFRhsSdQimr8UwIbFXF1pubMLSuMFXketQ_XJGvsA5fNh3oo_JQ9cviWQSKbAPyg/exec";

// ============ 홈페이지 ============
const HOMEPAGE_URL = "https://hyewon-english.pages.dev/";


// =====================================================
// [1] HTML에서 POST 요청 받기 → 시트에 기록 저장
// =====================================================
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const result = { ok: true, actions: [] };
    if (data.vocab)        { saveVocabRecord(data.vocab); result.actions.push('vocab_saved'); }
    if (data.quiz)         { saveQuizRecord(data.quiz);   result.actions.push('quiz_saved'); }
    if (data.activity)     { saveActivity(data.activity); result.actions.push('activity_saved'); }
    if (data.status)       { updateStatus(data.status);   result.actions.push('status_updated'); }
    // 🌐 다중 기기 동기화 액션들
    if (data.sync_state)   { syncSetState(data.sync_state); result.actions.push('state_synced'); }
    if (data.coupon_add)   { syncCouponAdd(data.coupon_add); result.actions.push('coupon_added'); }
    if (data.coupon_use)   { syncCouponUse(data.coupon_use); result.actions.push('coupon_used'); }
    return ContentService.createTextOutput(JSON.stringify(result))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}


// =====================================================
// 🆕 [활동기록] 모든 활동 시간순 기록
// =====================================================
function saveActivity(act) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(ACTIVITY_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(ACTIVITY_SHEET_NAME);
    sheet.appendRow([
      '날짜', '시간', '종류', '내용',
      '변동(P)', '포인트잔액', '쿠폰수', '지갑(원)'
    ]);
    sheet.getRange(1, 1, 1, 8).setBackground('#fff3bf').setFontWeight('bold');
    sheet.setFrozenRows(1);
    sheet.setColumnWidth(1, 100);
    sheet.setColumnWidth(2, 70);
    sheet.setColumnWidth(3, 110);
    sheet.setColumnWidth(4, 200);
    sheet.setColumnWidth(5, 80);
    sheet.setColumnWidth(6, 100);
    sheet.setColumnWidth(7, 70);
    sheet.setColumnWidth(8, 90);
  }
  sheet.appendRow([
    act.date || '',
    act.time || '',
    act.type || '',
    act.detail || '',
    act.delta || 0,
    act.points || 0,
    act.coupons || 0,
    act.wallet || 0
  ]);
}


// =====================================================
// 🆕 [현재상태] 요약 대시보드 (한 줄씩 덮어쓰기)
// =====================================================
function updateStatus(status) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(STATUS_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(STATUS_SHEET_NAME);
    sheet.setColumnWidth(1, 220);
    sheet.setColumnWidth(2, 200);
  }
  // 모두 클리어 후 다시 쓰기
  sheet.clearContents();
  sheet.appendRow(['🐱 혜원이 학습 현재 상태', '']);
  sheet.getRange(1, 1, 1, 2).setBackground('#ff8fb5').setFontWeight('bold').setFontColor('white');

  const rows = [
    ['🕐 마지막 업데이트', status.timestamp || ''],
    ['', ''],
    ['💎 현재 포인트', (status.points || 0) + ' P'],
    ['🎫 쿠폰 (사용가능 / 전체)', (status.unusedCoupons || 0) + ' / ' + (status.totalCoupons || 0)],
    ['💰 지갑 잔액', (status.wallet || 0) + ' 원'],
    ['', ''],
    ['🔥 연속 학습', (status.streak || 0) + ' 일'],
    ['📅 마지막 학습일', status.lastDate || '없음'],
    ['📚 누적 학습일', (status.totalDays || 0) + ' 일'],
    ['🎯 누적 단어 수', (status.totalWords || 0) + ' 개'],
    ['', ''],
    ['🏆 누적 퀴즈 점수', (status.totalScore || 0) + ' / ' + (status.maxScore || 0) + ' 점']
  ];

  rows.forEach(r => sheet.appendRow(r));
  // 강조
  sheet.getRange(3, 1, 1, 2).setBackground('#fff3bf').setFontWeight('bold');
  sheet.getRange(7, 1, 1, 2).setBackground('#ffd4e5').setFontWeight('bold');
}

function saveVocabRecord(v) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(VOCAB_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(VOCAB_SHEET_NAME);
    sheet.appendRow(['날짜', '요일', '테마', '시작시간', '종료시간',
      '학습시간(분)', '단어수', '발음듣기횟수', '단어목록']);
    sheet.getRange(1, 1, 1, 9).setBackground('#c8e6c9').setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  sheet.appendRow([
    v.date, v.day, v.theme || '', v.startTime, v.endTime,
    v.minutes, v.wordsLearned, v.listens, (v.words || []).join(', ')
  ]);

  // ⭐ 활동기록 시트에도 자동 추가 (단어장 완료 = +100P)
  try {
    const tm = v.endTime ? String(v.endTime).split(' ')[1] || '' : '';
    saveActivity({
      date: v.date,
      time: tm.substring(0, 5),
      type: '📚 단어장 완료',
      detail: (v.theme || '') + ' · ' + (v.minutes || 0) + '분 · ' + (v.wordsLearned || 0) + '단어 (발음 ' + (v.listens || 0) + '회)',
      delta: 100,
      points: 0, coupons: 0, wallet: 0
    });
  } catch(e) { Logger.log('활동기록 추가 실패(단어장): ' + e); }
}

function saveQuizRecord(q) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(QUIZ_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(QUIZ_SHEET_NAME);
    sheet.appendRow(['날짜', '요일', '시도횟수', '시작시간', '종료시간',
      '풀이시간(분)', '점수', '총문항', '맞은개수', '틀린개수', '틀린단어']);
    sheet.getRange(1, 1, 1, 11).setBackground('#ffcdd2').setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  sheet.appendRow([
    q.date, q.day, q.attemptNumber + '차', q.startTime, q.endTime,
    q.minutes, q.score, q.total, q.correctCount, q.wrongCount,
    (q.wrongWords || []).join(', ')
  ]);

  // ⭐ 활동기록 시트에도 자동 추가 (퀴즈 정답마다 +10P + 콤보 보너스)
  try {
    const tm = q.endTime ? String(q.endTime).split(' ')[1] || '' : '';
    // pointsEarned가 HTML에서 보내졌으면 사용, 없으면 추정 (정답 1개당 평균 약 13P)
    const earned = (typeof q.pointsEarned === 'number') ? q.pointsEarned : ((q.correctCount || 0) * 13);
    const comboInfo = q.maxCombo ? ' · 최고콤보 ' + q.maxCombo : '';
    saveActivity({
      date: q.date,
      time: tm.substring(0, 5),
      type: '📝 퀴즈 완료',
      detail: (q.attemptNumber || 1) + '차 · ' + q.score + '/' + q.total +
              ' · 정답 ' + q.correctCount + '개' + comboInfo,
      delta: earned,
      points: 0, coupons: 0, wallet: 0
    });
  } catch(e) { Logger.log('활동기록 추가 실패(퀴즈): ' + e); }
}

function doGet(e) {
  if (e && e.parameter) {
    const action = e.parameter.action;
    let result = null;

    if (action === 'check_bonus') {
      const lastRow = parseInt(e.parameter.last_row || '1');
      result = getNewBonuses(lastRow);
    } else if (action === 'get_state') {
      // 🌐 다중 기기 동기화: 현재 상태 + 쿠폰 목록 가져오기
      result = getFullState();
    }

    if (result !== null) {
      const json = JSON.stringify(result);
      if (e.parameter.callback) {
        return ContentService.createTextOutput(
          e.parameter.callback + '(' + json + ');'
        ).setMimeType(ContentService.MimeType.JAVASCRIPT);
      }
      return ContentService.createTextOutput(json)
        .setMimeType(ContentService.MimeType.JSON);
    }
  }
  return ContentService.createTextOutput("혜원이 영단어 서버 정상 작동 중 🌟");
}


// =====================================================
// 🌐 [동기화] 모든 기기에서 동일한 데이터 사용
// =====================================================

// 마스터 상태 시트 (동기화용 - 포인트/지갑/스트릭/마지막업데이트)
function _getSyncSheet() {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(SYNC_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SYNC_SHEET_NAME);
    sheet.appendRow(['항목', '값', '마지막 업데이트']);
    sheet.getRange(1, 1, 1, 3).setBackground('#c8e6c9').setFontWeight('bold');
    sheet.appendRow(['points', 0, '']);
    sheet.appendRow(['wallet', 0, '']);
    sheet.appendRow(['streak', 0, '']);
    sheet.appendRow(['lucky_received_date', '', '']);
    sheet.appendRow(['last_streak_reward', 0, '']);
    sheet.setColumnWidth(1, 200);
    sheet.setColumnWidth(2, 120);
    sheet.setColumnWidth(3, 180);
  }
  return sheet;
}

function _getSyncValue(key) {
  const sheet = _getSyncSheet();
  const data = sheet.getRange(2, 1, sheet.getLastRow() - 1, 2).getValues();
  for (let i = 0; i < data.length; i++) {
    if (data[i][0] === key) return data[i][1];
  }
  return null;
}

function _setSyncValue(key, value) {
  const sheet = _getSyncSheet();
  const data = sheet.getRange(2, 1, sheet.getLastRow() - 1, 1).getValues();
  const now = Utilities.formatDate(new Date(), 'Asia/Seoul', 'yyyy-MM-dd HH:mm:ss');
  for (let i = 0; i < data.length; i++) {
    if (data[i][0] === key) {
      sheet.getRange(i + 2, 2).setValue(value);
      sheet.getRange(i + 2, 3).setValue(now);
      return;
    }
  }
  // 없으면 추가
  sheet.appendRow([key, value, now]);
}

// 쿠폰 시트
function _getCouponsSheet() {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(COUPONS_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(COUPONS_SHEET_NAME);
    sheet.appendRow(['ID', '종류', '이름', '이모지', '가격(P)', '발급일', '사용여부', '사용일']);
    sheet.getRange(1, 1, 1, 8).setBackground('#fce7f3').setFontWeight('bold');
    sheet.setFrozenRows(1);
    sheet.setColumnWidth(1, 160);
    sheet.setColumnWidth(2, 100);
    sheet.setColumnWidth(3, 180);
    sheet.setColumnWidth(4, 60);
    sheet.setColumnWidth(5, 80);
    sheet.setColumnWidth(6, 110);
    sheet.setColumnWidth(7, 80);
    sheet.setColumnWidth(8, 110);
  }
  return sheet;
}

// 🌐 모든 기기에서 가져오는 풀 상태
function getFullState() {
  const points = parseInt(_getSyncValue('points') || '0');
  const wallet = parseInt(_getSyncValue('wallet') || '0');
  const streak = parseInt(_getSyncValue('streak') || '0');
  const lucky = String(_getSyncValue('lucky_received_date') || '');
  const lastStreakReward = parseInt(_getSyncValue('last_streak_reward') || '0');

  // 쿠폰 목록 (사용 안 한 것 + 사용한 것 모두)
  const sheet = _getCouponsSheet();
  const lastRow = sheet.getLastRow();
  const coupons = [];
  if (lastRow > 1) {
    const rows = sheet.getRange(2, 1, lastRow - 1, 8).getValues();
    rows.forEach(function(r) {
      if (r[0]) {  // ID 있는 것만
        coupons.push({
          id: r[0],
          type: r[1],
          name: r[2],
          emoji: r[3],
          cost: parseInt(r[4]) || 0,
          date: r[5] ? Utilities.formatDate(new Date(r[5]), 'Asia/Seoul', 'yyyy-MM-dd') : '',
          used: !!r[6],
          usedDate: r[7] ? Utilities.formatDate(new Date(r[7]), 'Asia/Seoul', 'yyyy-MM-dd') : null
        });
      }
    });
  }

  return {
    points: points,
    wallet: wallet,
    streak: streak,
    lucky_received_date: lucky,
    last_streak_reward: lastStreakReward,
    coupons: coupons,
    server_time: Utilities.formatDate(new Date(), 'Asia/Seoul', 'yyyy-MM-dd HH:mm:ss')
  };
}

// 폰에서 쿠폰 발급/사용 시 호출 (doPost에서 처리)
function syncCouponAdd(coupon) {
  const sheet = _getCouponsSheet();
  // 이미 있는 ID인지 체크
  const lastRow = sheet.getLastRow();
  if (lastRow > 1) {
    const ids = sheet.getRange(2, 1, lastRow - 1, 1).getValues().map(r => r[0]);
    if (ids.indexOf(coupon.id) !== -1) return;  // 중복 방지
  }
  sheet.appendRow([
    coupon.id,
    coupon.type || '',
    coupon.name || '',
    coupon.emoji || '',
    coupon.cost || 0,
    coupon.date || Utilities.formatDate(new Date(), 'Asia/Seoul', 'yyyy-MM-dd'),
    coupon.used ? 'YES' : '',
    coupon.usedDate || ''
  ]);
}

function syncCouponUse(couponId) {
  const sheet = _getCouponsSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow <= 1) return;
  const ids = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
  for (let i = 0; i < ids.length; i++) {
    if (ids[i][0] === couponId) {
      const rowNum = i + 2;
      sheet.getRange(rowNum, 7).setValue('YES');
      sheet.getRange(rowNum, 8).setValue(Utilities.formatDate(new Date(), 'Asia/Seoul', 'yyyy-MM-dd'));
      return;
    }
  }
}

function syncSetState(state) {
  if (state.points !== undefined) _setSyncValue('points', state.points);
  if (state.wallet !== undefined) _setSyncValue('wallet', state.wallet);
  if (state.streak !== undefined) _setSyncValue('streak', state.streak);
  if (state.lucky_received_date !== undefined) _setSyncValue('lucky_received_date', state.lucky_received_date);
  if (state.last_streak_reward !== undefined) _setSyncValue('last_streak_reward', state.last_streak_reward);
}


// =====================================================
// 🎁 [관리자_보너스] 시트에서 새 보너스 가져오기
// =====================================================
const BONUS_SHEET_NAME = "관리자_보너스";

function getNewBonuses(lastSeenRow) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(BONUS_SHEET_NAME);

  // 시트 없으면 자동 생성 (헤더 + 안내)
  if (!sheet) {
    sheet = ss.insertSheet(BONUS_SHEET_NAME);
    sheet.appendRow(['날짜', '포인트', '메시지', '지급 완료?']);
    sheet.getRange(1, 1, 1, 4).setBackground('#fff3bf').setFontWeight('bold');
    sheet.setFrozenRows(1);
    sheet.setColumnWidth(1, 110);
    sheet.setColumnWidth(2, 90);
    sheet.setColumnWidth(3, 250);
    sheet.setColumnWidth(4, 130);
    sheet.appendRow(['(여기 아래에 입력)', '', '', '']);
    sheet.getRange('A2:D2').setFontStyle('italic').setFontColor('#999');
    return { bonuses: [], lastRow: 2 };
  }

  const lastSheetRow = sheet.getLastRow();
  if (lastSheetRow < 3) return { bonuses: [], lastRow: lastSheetRow };

  // 데이터 행은 3행부터 (1=헤더, 2=안내)
  const startRow = Math.max(3, lastSeenRow + 1);
  if (startRow > lastSheetRow) return { bonuses: [], lastRow: lastSheetRow };

  const range = sheet.getRange(startRow, 1, lastSheetRow - startRow + 1, 4);
  const data = range.getValues();
  const bonuses = [];

  data.forEach((row, idx) => {
    const rowNum = startRow + idx;
    const points = parseInt(row[1]);
    const completed = String(row[3] || '').trim();

    // 포인트가 숫자이고 아직 처리 안 된 줄만
    if (!isNaN(points) && points !== 0 && !completed) {
      bonuses.push({
        rowNum: rowNum,
        date: row[0] ? Utilities.formatDate(new Date(row[0]), 'Asia/Seoul', 'yyyy-MM-dd') : '',
        points: points,
        message: row[2] || ''
      });
      // "지급 완료" 표시 (중복 방지)
      sheet.getRange(rowNum, 4).setValue('✅ ' + Utilities.formatDate(new Date(), 'Asia/Seoul', 'MM-dd HH:mm'));
    }
  });

  return { bonuses: bonuses, lastRow: lastSheetRow };
}


// =====================================================
// [2] 🗓️ 구글 캘린더 자동 등록 (NEW!)
// =====================================================

/**
 * 학습 스케줄 (SCHEDULE 배열)
 * ──────────────────────────────────────
 * 매주 주말에 이 배열에 다음 주 정보 추가 후 setupCalendarForHyewon() 실행
 * ──────────────────────────────────────
 */
const LEARNING_SCHEDULE = [
  // ───── 이번 주 (4/21~4/25) ─────
  { date: "2026-04-21", theme: "동물과 자연 2탄", emoji: "🌊",
    folder: "20260421",
    vocab: "혜원이_영단어_화요일_동물과자연2.html",
    quiz:  "혜원이_영단어_화요일_퀴즈.html" },
  { date: "2026-04-22", theme: "학교", emoji: "🏫",
    folder: "20260422",
    vocab: "혜원이_영단어_수요일_학교.html",
    quiz:  "혜원이_영단어_수요일_퀴즈.html" },
  { date: "2026-04-23", theme: "가족", emoji: "👨‍👩‍👧",
    folder: "20260423",
    vocab: "혜원이_영단어_목요일_가족.html",
    quiz:  "혜원이_영단어_목요일_퀴즈.html" },
  { date: "2026-04-24", theme: "음식", emoji: "🍔",
    folder: "20260424",
    vocab: "혜원이_영단어_금요일_음식.html",
    quiz:  "혜원이_영단어_금요일_퀴즈.html" },
  { date: "2026-04-25", theme: "주간 종합시험", emoji: "🏆",
    folder: "20260425",
    vocab: "혜원이_영단어_토요일_종합시험.html",
    quiz:  "혜원이_영단어_토요일_종합시험.html",
    isExam: true },

  // ───── 다음 주 (4/27~5/1) ─────
  { date: "2026-04-27", theme: "동물과 자연 1탄", emoji: "🌳",
    folder: "20260427",
    vocab: "혜원이_영단어_월요일_동물과자연.html",
    quiz:  "혜원이_영단어_월요일_퀴즈.html" },
  { date: "2026-04-28", theme: "색깔", emoji: "🎨",
    folder: "20260428",
    vocab: "혜원이_영단어_화요일_색깔.html",
    quiz:  "혜원이_영단어_화요일_퀴즈.html" },
  { date: "2026-04-29", theme: "숫자와 시간", emoji: "🔢",
    folder: "20260429",
    vocab: "혜원이_영단어_수요일_숫자와시간.html",
    quiz:  "혜원이_영단어_수요일_퀴즈.html" },
  { date: "2026-04-30", theme: "집과 방", emoji: "🏠",
    folder: "20260430",
    vocab: "혜원이_영단어_목요일_집과방.html",
    quiz:  "혜원이_영단어_목요일_퀴즈.html" },
  { date: "2026-05-01", theme: "옷과 몸", emoji: "🎽",
    folder: "20260501",
    vocab: "혜원이_영단어_금요일_옷과몸.html",
    quiz:  "혜원이_영단어_금요일_퀴즈.html" }
];


/**
 * 👨‍🏫 캘린더에 이번 주 + 다음 주 학습 일정 한방에 등록
 *    → Apps Script 편집기에서 이 함수 선택 → 실행
 */
function setupCalendarForHyewon() {
  const calendar = CalendarApp.getDefaultCalendar();
  let created = 0;
  let skipped = 0;

  LEARNING_SCHEDULE.forEach(item => {
    // 이미 있으면 건너뛰기
    const day = new Date(item.date + 'T00:00:00+09:00');
    const existing = calendar.getEventsForDay(day, {
      search: '혜원이 영단어'
    });
    if (existing.length > 0) {
      Logger.log(`⏭️  이미 이벤트 존재: ${item.date} (${item.theme})`);
      skipped++;
      return;
    }

    // 종합시험(토요일)은 특별 처리
    if (item.isExam) {
      createExamEvent(calendar, item);
    } else {
      createDailyEvent(calendar, item);
    }
    created++;
  });

  Logger.log(`\n✅ 완료! 새로 ${created}개 생성 / ${skipped}개 건너뜀`);
  Logger.log(`📅 구글 캘린더에서 ${LEARNING_SCHEDULE[0].date}부터 확인하세요.`);
}


/**
 * 평일 학습 이벤트
 *   - 오후 3시: 단어장 (학교 끝나고)
 *   - 오후 8시: 퀴즈 (저녁에 복습)
 *
 *   ⏰ 시간대 안내:
 *     기준이 한국 시간(KST = UTC+9)이에요.
 *     불가리아에서는 여름=오전 9시/오후 2시, 겨울=오전 8시/오후 1시로 자동 환산돼요.
 */
function createDailyEvent(calendar, item) {
  // 한국 시간 기준 (+09:00 = KST)
  const vocabStart = new Date(item.date + 'T15:00:00+09:00'); // 오후 3시 (단어장)
  const vocabEnd   = new Date(item.date + 'T15:30:00+09:00');
  const quizStart  = new Date(item.date + 'T20:00:00+09:00'); // 오후 8시 (퀴즈)
  const quizEnd    = new Date(item.date + 'T20:30:00+09:00');

  const vocabUrl = `${HOMEPAGE_URL}${item.folder}/${encodeURIComponent(item.vocab)}`;
  const quizUrl  = `${HOMEPAGE_URL}${item.folder}/${encodeURIComponent(item.quiz)}`;

  // ①  오후 3시 - 단어장 (분홍색)
  const vocabDesc =
    `📚 단어장 학습 시간!\n\n` +
    `🌸 오늘 테마: ${item.theme} ${item.emoji}\n\n` +
    `👉 단어장 링크: ${vocabUrl}\n\n` +
    `🏠 홈페이지: ${HOMEPAGE_URL}`;

  const vocabEvent = calendar.createEvent(
    `🌸 혜원이 영단어 (${item.theme}) ${item.emoji}`,
    vocabStart, vocabEnd,
    { description: vocabDesc }
  );
  vocabEvent.setColor(CalendarApp.EventColor.PALE_RED); // 연분홍
  vocabEvent.addPopupReminder(0); // 정각 알림

  // ②  오후 8시 - 퀴즈 (파랑색)
  const quizDesc =
    `📝 퀴즈 시간! 배운 단어 복습!\n\n` +
    `🎯 오늘의 20문제: ${item.theme} ${item.emoji}\n\n` +
    `👉 퀴즈 링크: ${quizUrl}\n\n` +
    `🏠 홈페이지: ${HOMEPAGE_URL}`;

  const quizEvent = calendar.createEvent(
    `📝 혜원이 영단어 퀴즈 (${item.theme})`,
    quizStart, quizEnd,
    { description: quizDesc }
  );
  quizEvent.setColor(CalendarApp.EventColor.PALE_BLUE); // 연파랑
  quizEvent.addPopupReminder(0);

  Logger.log(`✅ ${item.date} 생성: ${item.theme} (오후3시 단어장 + 오후8시 퀴즈)`);
}


/**
 * 토요일 종합시험 이벤트
 */
function createExamEvent(calendar, item) {
  const start = new Date(item.date + 'T10:00:00+09:00');
  const end   = new Date(item.date + 'T11:00:00+09:00');

  const url = `${HOMEPAGE_URL}${item.folder}/${encodeURIComponent(item.quiz)}`;
  const desc =
    `🏆 주간 종합시험 Day!\n\n` +
    `🎯 이번 주 배운 단어 80개 한방에 테스트\n\n` +
    `👉 시험 링크: ${url}\n\n` +
    `📊 혜원이 파이팅! 이번 주 고생했어요 💪`;

  const event = calendar.createEvent(
    `🏆 혜원이 영단어 주간 종합시험`,
    start, end,
    { description: desc }
  );
  event.setColor(CalendarApp.EventColor.YELLOW); // 축제 노랑
  event.addPopupReminder(15);
  event.addPopupReminder(0);

  Logger.log(`✅ ${item.date} 생성: 주간 종합시험 🏆`);
}


/**
 * 🧹 혜원이 영단어 이벤트 모두 삭제 (다시 생성하고 싶을 때)
 *    ⚠️ 주의: 이 함수 실행하면 모든 '혜원이 영단어' 이벤트가 삭제돼요!
 */
function deleteAllHyewonEvents() {
  const calendar = CalendarApp.getDefaultCalendar();
  const startDate = new Date('2026-04-01');
  const endDate = new Date('2026-06-30');
  const events = calendar.getEvents(startDate, endDate, { search: '혜원이 영단어' });

  Logger.log(`🧹 삭제 대상: ${events.length}개 이벤트`);
  events.forEach(e => {
    Logger.log(`  삭제: ${e.getTitle()} (${e.getStartTime().toLocaleDateString()})`);
    e.deleteEvent();
  });
  Logger.log(`✅ 삭제 완료!`);
}


// =====================================================
// [3] 📱 카톡 리마인더 (선택 사항 — 캘린더만 쓰면 안 써도 됨)
// =====================================================
function morningReminder() {
  const today = new Date();
  const dayKo = ['일', '월', '화', '수', '목', '금', '토'][today.getDay()];
  const dateStr = `${today.getMonth()+1}월 ${today.getDate()}일 (${dayKo})`;

  const msg = `🌅 혜원이 오늘 영단어 시간!\n\n` +
              `📅 ${dateStr}\n\n` +
              `👉 ${HOMEPAGE_URL}\n\n` +
              `혜원이한테 링크 전달해주세요 😊`;
  sendKakaoSelf(msg);
}

function sendKakaoSelf(subject) {
  const url = LEGACY_APPS_URL + '?subject=' + encodeURIComponent(subject);
  UrlFetchApp.fetch(url, { method: 'get', muteHttpExceptions: true });
}


// =====================================================
// [4] 🧪 테스트 함수
// =====================================================
function testSheet() {
  saveVocabRecord({
    date: '2026-04-21', day: 'Monday', theme: '테스트',
    startTime: '2026-04-21 08:00:00', endTime: '2026-04-21 08:15:00',
    minutes: 15, wordsLearned: 20, listens: 100, words: ['test1']
  });
  Logger.log('✅ 시트 저장 테스트 완료!');
}

function testReminder() {
  morningReminder();
  Logger.log('✅ 카톡 리마인더 테스트 발송!');
}

/**
 * 🧪 캘린더 단일 이벤트 테스트
 */
function testCalendar() {
  const calendar = CalendarApp.getDefaultCalendar();
  const tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  tomorrow.setHours(7, 0, 0, 0);
  const tomorrowEnd = new Date(tomorrow);
  tomorrowEnd.setHours(7, 30);

  const event = calendar.createEvent(
    '🧪 혜원이 영단어 테스트',
    tomorrow, tomorrowEnd,
    { description: '테스트 이벤트입니다. 확인 후 삭제하세요.' }
  );
  event.setColor(CalendarApp.EventColor.PALE_RED);
  event.addPopupReminder(0);

  Logger.log(`✅ 내일(${tomorrow.toLocaleDateString()}) 오전 7시 테스트 이벤트 생성!`);
  Logger.log(`   구글 캘린더에서 확인해보세요.`);
}
