// QnA 페이지 인터랙션
// 1) 카테고리 필터: 카드 상단 chip 클릭 시 해당 카테고리만 보이기 / 다시 누르면 전체 복귀
// 2) 맨 위로 가기 버튼: PC(>=768px)에서만 노출, 일정 이상 스크롤 시 페이드인
(function () {
  // ----- 카테고리 필터 -----
  var cards = document.querySelectorAll('.qna-report .qna-card');
  cards.forEach(function (card) {
    var bar = card.querySelector('.qna-card__catbar');
    if (!bar) return;
    var buttons = bar.querySelectorAll('[data-filter]');
    var items = card.querySelectorAll('.qna-card__qs > .qna-q');

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = btn.getAttribute('data-filter');
        var isActive = btn.classList.contains('is-active');

        // 다른 active 해제 (한 번에 한 카테고리만)
        buttons.forEach(function (b) { b.classList.remove('is-active'); });

        if (isActive) {
          // 다시 누르면 필터 해제 → 전체 보이기
          items.forEach(function (li) { li.classList.remove('is-hidden'); });
        } else {
          btn.classList.add('is-active');
          items.forEach(function (li) {
            if (li.getAttribute('data-cat') === target) {
              li.classList.remove('is-hidden');
            } else {
              li.classList.add('is-hidden');
            }
          });
        }
      });
    });
  });

  // ----- 맨 위로 가기 (PC만) -----
  // .qna-report 있는 페이지에만 추가 (모든 페이지에 띄우지 말기)
  if (!document.querySelector('.qna-report')) return;

  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'scroll-top';
  btn.setAttribute('aria-label', '맨 위로 가기');
  btn.innerHTML = '↑';
  document.body.appendChild(btn);

  btn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  var visible = false;
  function onScroll() {
    var show = window.scrollY > 200;
    if (show !== visible) {
      visible = show;
      btn.classList.toggle('is-visible', show);
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
