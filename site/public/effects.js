(() => {
  const root = document.documentElement;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const finePointer = window.matchMedia('(pointer: fine)');

  if (reducedMotion.matches || !finePointer.matches) return;

  let frame = 0;
  let nextX = 0;
  let nextY = 0;

  const paint = () => {
    frame = 0;
    root.style.setProperty('--shift-x', `${nextX.toFixed(2)}px`);
    root.style.setProperty('--shift-y', `${nextY.toFixed(2)}px`);
  };

  window.addEventListener('pointermove', (event) => {
    const nx = (event.clientX / window.innerWidth - 0.5) * 2;
    const ny = (event.clientY / window.innerHeight - 0.5) * 2;
    nextX = nx * 8;
    nextY = ny * 5;
    if (!frame) frame = requestAnimationFrame(paint);
  }, { passive: true });

  document.documentElement.addEventListener('mouseleave', () => {
    nextX = 0;
    nextY = 0;
    if (!frame) frame = requestAnimationFrame(paint);
  });
})();
