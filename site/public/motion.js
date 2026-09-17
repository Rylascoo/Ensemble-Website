(() => {
  const finePointer = window.matchMedia('(pointer: fine)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const root = document.documentElement;

  let frame = 0;
  let nextX = 0;
  let nextY = 0;

  const reset = () => {
    root.style.setProperty('--field-x', '0px');
    root.style.setProperty('--field-y', '0px');
    root.style.setProperty('--light-x', '58%');
    root.style.setProperty('--light-y', '42%');
  };

  const render = () => {
    frame = 0;
    const nx = Math.max(-1, Math.min(1, nextX));
    const ny = Math.max(-1, Math.min(1, nextY));

    root.style.setProperty('--field-x', `${(nx * 2.8).toFixed(2)}px`);
    root.style.setProperty('--field-y', `${(ny * 2.2).toFixed(2)}px`);
    root.style.setProperty('--light-x', `${(58 + nx * 2.2).toFixed(2)}%`);
    root.style.setProperty('--light-y', `${(42 + ny * 1.8).toFixed(2)}%`);
  };

  const onPointerMove = (event) => {
    if (!finePointer.matches || reducedMotion.matches) return;
    nextX = (event.clientX / window.innerWidth - 0.5) * 2;
    nextY = (event.clientY / window.innerHeight - 0.5) * 2;
    if (!frame) frame = requestAnimationFrame(render);
  };

  const syncCapability = () => {
    if (!finePointer.matches || reducedMotion.matches) reset();
  };

  window.addEventListener('pointermove', onPointerMove, { passive: true });
  document.documentElement.addEventListener('mouseleave', reset);
  finePointer.addEventListener?.('change', syncCapability);
  reducedMotion.addEventListener?.('change', syncCapability);
  syncCapability();
})();
