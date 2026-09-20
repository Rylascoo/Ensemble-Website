from pathlib import Path
root = Path(r'C:\Users\Wiryl\Sol Dev\Ensemble-Website-Worktrees\site-v2-2-mascot-placement-study-2026-09-16')
src = root / 'site' / 'public' / 'index.html'
dst = root / 'prototypes' / 'website-v2-2-mascot-placement-study' / 'index.html'
s = src.read_text(encoding='utf-8')
s = s.replace('href="/styles.css"', 'href="../../site/public/styles.css"')
s = s.replace('href="/atmosphere.css"', 'href="../../site/public/atmosphere.css"')
s = s.replace('href="/modes.css"', 'href="../../site/public/modes.css"')
s = s.replace('src="/stage-v2-2.webp?v=2"', 'src="../../site/public/stage-v2-2.webp?v=2"')
s = s.replace('  <link rel="stylesheet" href="../../site/public/modes.css">', '  <link rel="stylesheet" href="../../site/public/modes.css">\n  <link rel="stylesheet" href="./study.css">')
s = s.replace('  <main id="main" class="stage">', '  <img class="bellweather-study" src="./bellweather-derived-cutout.png" alt="" aria-hidden="true">\n\n  <main id="main" class="stage">')
s = s.replace('</body>', '  <script src="./study.js"></script>\n</body>')
dst.write_text(s, encoding='utf-8', newline='\n')
print(dst)
