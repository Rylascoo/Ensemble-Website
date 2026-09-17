(() => {
  const order = ['place', 'presence', 'person', 'trace', 'life'];
  const spoken = {
    place: 'Kymaean. Coming Soon.',
    presence: 'The scene has changed.',
    person: 'The scene has changed.',
    trace: 'The scene has changed.',
    life: 'The scene has changed.'
  };

  const FADE_OUT_MS = 280;
  const EMPTY_HOLD_MS = 300;
  const REVEAL_DELAY_MS = FADE_OUT_MS + EMPTY_HOLD_MS;

  const stage = document.getElementById('main');
  const live = document.getElementById('state-live');
  if (!stage || !live) return;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0;
  let rendered = 'place';
  let transitionTimer = 0;
  let transitionStarted = 0;
  let transitionToken = 0;
  let touchY = null;
  let wheelSum = 0;
  let wheelTimer = 0;
  let wheelLocked = false;

  const cancelReveal = () => {
    window.clearTimeout(transitionTimer);
    transitionTimer = 0;
    transitionToken += 1;
  };

  const render = (target, source, announce = true) => {
    rendered = target;
    document.body.dataset.state = target;
    document.body.dataset.input = source;
    document.body.classList.remove('transitioning');
    transitionStarted = 0;
    if (announce) live.textContent = spoken[target];
    return target;
  };

  const scheduleReveal = (target, source, delay) => {
    const token = ++transitionToken;
    window.clearTimeout(transitionTimer);
    transitionTimer = window.setTimeout(() => {
      if (token !== transitionToken) return;
      transitionTimer = 0;
      render(target, source, true);
    }, delay);
  };

  const setState = (next, source = 'api') => {
    const clamped = Math.max(0, Math.min(order.length - 1, next));
    const target = order[clamped];
    const sameTarget = clamped === index;
    if (sameTarget && source !== 'load' && !transitionTimer) return target;
    index = clamped;
    document.body.dataset.input = source;

    if (source === 'load' || reducedMotion.matches || target === 'place') {
      cancelReveal();
      return render(target, source, true);
    }

    if (rendered === 'place' && !transitionTimer) {
      cancelReveal();
      return render(target, source, true);
    }

    if (rendered !== 'empty') {
      cancelReveal();
      transitionStarted = performance.now();
      rendered = 'empty';
      document.body.classList.add('transitioning');
      document.body.dataset.state = 'empty';
      scheduleReveal(target, source, REVEAL_DELAY_MS);
      return target;
    }

    const elapsed = performance.now() - transitionStarted;
    const remaining = Math.max(80, REVEAL_DELAY_MS - elapsed);
    scheduleReveal(target, source, remaining);
    return target;
  };

  const step = (delta, source) => setState(index + delta, source);

  const onKey = (event) => {
    let delta = 0;
    if (['ArrowDown', 'PageDown', ' ', 'ArrowRight'].includes(event.key)) delta = 1;
    else if (['ArrowUp', 'PageUp', 'ArrowLeft'].includes(event.key)) delta = -1;
    else if (event.key === 'Home') {
      event.preventDefault();
      setState(0, 'keyboard');
      return;
    } else if (event.key === 'End') {
      event.preventDefault();
      setState(order.length - 1, 'keyboard');
      return;
    }

    if (delta) {
      event.preventDefault();
      step(delta, 'keyboard');
    }
  };

  const resetWheelGesture = () => {
    wheelSum = 0;
    wheelLocked = false;
  };

  const onWheel = (event) => {
    window.clearTimeout(wheelTimer);
    wheelTimer = window.setTimeout(resetWheelGesture, 220);
    if (wheelLocked) return;
    if (wheelSum && Math.sign(wheelSum) !== Math.sign(event.deltaY)) wheelSum = 0;
    wheelSum += event.deltaY;

    if (Math.abs(wheelSum) >= 48) {
      step(wheelSum > 0 ? 1 : -1, 'wheel');
      wheelSum = 0;
      wheelLocked = true;
    }
  };

  const onTouchStart = (event) => {
    touchY = event.touches?.[0]?.clientY ?? null;
  };

  const onTouchEnd = (event) => {
    if (touchY == null) return;
    const end = event.changedTouches?.[0]?.clientY ?? touchY;
    const deltaY = touchY - end;
    touchY = null;
    if (Math.abs(deltaY) >= 28) step(deltaY > 0 ? 1 : -1, 'touch');
  };

  const onReducedMotionChange = () => {
    if (!reducedMotion.matches || rendered !== 'empty') return;
    cancelReveal();
    render(order[index], 'reduced-motion', true);
  };

  stage.addEventListener('keydown', onKey);
  stage.addEventListener('touchstart', onTouchStart, { passive: true });
  stage.addEventListener('touchend', onTouchEnd, { passive: true });
  stage.addEventListener('pointerdown', () => stage.focus({ preventScroll: true }), { passive: true });
  window.addEventListener('wheel', onWheel, { passive: true });
  reducedMotion.addEventListener?.('change', onReducedMotionChange);

  window.__KYM_TEMPORAL__ = {
    order,
    get index() { return index; },
    get state() { return order[index]; },
    get renderState() { return rendered; },
    get transitioning() { return rendered === 'empty'; },
    get reducedMotion() { return reducedMotion.matches; },
    get timing() { return { fadeOutMs: FADE_OUT_MS, emptyHoldMs: EMPTY_HOLD_MS, revealDelayMs: REVEAL_DELAY_MS }; },
    advance: () => step(1, 'api'),
    reverse: () => step(-1, 'api'),
    set: (next) => setState(next, 'api'),
    snapshot: () => ({
      state: order[index],
      renderState: rendered,
      transitioning: rendered === 'empty',
      index,
      reducedMotion: reducedMotion.matches,
      activeTag: document.activeElement?.tagName,
      overflowX: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      visible: {
        presence: getComputedStyle(document.querySelector('.presence-carrier')).opacity,
        person: getComputedStyle(document.querySelector('.person-carrier')).opacity,
        trace: getComputedStyle(document.querySelector('.trace-evidence')).opacity,
        life: getComputedStyle(document.querySelector('.life-evidence')).opacity
      }
    })
  };

  setState(0, 'load');
})();
