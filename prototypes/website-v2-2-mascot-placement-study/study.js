(() => {
  const allowed = new Set(['control', 'a1', 'a2', 'a3', 'a4']);
  const requested = (new URLSearchParams(window.location.search).get('variant') || 'control').toLowerCase();
  const variant = allowed.has(requested) ? requested : 'control';
  document.body.dataset.variant = variant;
  document.documentElement.dataset.study = 'website-v2-2-mascot-placement';
})();
