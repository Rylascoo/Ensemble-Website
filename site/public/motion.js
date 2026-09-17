(() => {
  const order = ['place', 'presence', 'empty1', 'person', 'empty2', 'trace', 'empty3', 'life'];
  const spoken = {
    place: 'Kymaean. Coming Soon.',
    presence: 'The scene has changed.',
    empty1: 'The scene has cleared.',
    person: 'The scene has changed.',
    empty2: 'The scene has cleared.',
    trace: 'The scene has changed.',
    empty3: 'The scene has cleared.',
    life: 'The scene has changed.'
  };

  const stage = document.getElementById('main');
  const live = document.getElementById('state-live');
  if (!stage || !live) return;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0;
  let touchY = null;
  let wheelSum = 0;
  let wheelTimer = 0;
  let wheelLocked = false;
  let lastChange = 0;

  const setState = (next, source = 'api') => {
    const previous = order[index];
    const clamped = Math.max(0, Math.min(order.length - 1, next));
    if (clamped === index && source !== 'load') return order[index];
    const now = performance.now();
    index = clamped;
    const target = order[index];
    const rapidRetarget = previous !== 'place' && lastChange > 0 && (now - lastChange) < 540;

    if (rapidRetarget && !reducedMotion.matches) {
      document.body.classList.add('snap');
      document.body.dataset.state = target;
      void document.body.offsetWidth;
      document.body.classList.remove('snap');
    } else {
      document.body.dataset.state = target;
    }

    document.body.dataset.input = source;
    live.textContent = spoken[target];
    lastChange = now;
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
    }
    else if (event.key === 'End') {
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

  stage.addEventListener('keydown', onKey);
  stage.addEventListener('touchstart', onTouchStart, { passive: true });
  stage.addEventListener('touchend', onTouchEnd, { passive: true });
  stage.addEventListener('pointerdown', () => stage.focus({ preventScroll: true }), { passive: true });
  window.addEventListener('wheel', onWheel, { passive: true });

  window.__KYM_TEMPORAL__ = {
    order,
    get index() { return index; },
    get state() { return order[index]; },
    get reducedMotion() { return reducedMotion.matches; },
    advance: () => step(1, 'api'),
    reverse: () => step(-1, 'api'),
    set: (next) => setState(next, 'api'),
    snapshot: () => ({
      state: order[index],
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
