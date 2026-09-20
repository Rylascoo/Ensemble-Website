from pathlib import Path
p = Path(r'C:\Users\Wiryl\Sol Dev\Ensemble-Website-Worktrees\site-v2-2-mascot-placement-study-2026-09-16\prototypes\website-v2-2-mascot-placement-study\study.css')
s = p.read_text(encoding='utf-8-sig')
s = s.replace('body[data-variant="a4"] .bellweather-study {\n  right: 10vw;\n  bottom: 5svh;\n  height: 29svh;\n  animation:', 'body[data-variant="a4"] .bellweather-study {\n  right: 14vw;\n  bottom: 4svh;\n  height: 34svh;\n  -webkit-mask-image: linear-gradient(to right, transparent 0 18%, #000 38% 100%);\n  mask-image: linear-gradient(to right, transparent 0 18%, #000 38% 100%);\n  animation:')
s = s.replace('  body[data-variant="a1"] .bellweather-study,\n  body[data-variant="a4"] .bellweather-study {', '  body[data-variant="a1"] .bellweather-study {')
s = s.replace('  body[data-variant="a3"] .bellweather-study {\n    right: 1vw;\n    bottom: 3svh;\n    height: 27svh;\n  }', '  body[data-variant="a3"] .bellweather-study,\n  body[data-variant="a4"] .bellweather-study {\n    right: 1vw;\n    bottom: 3svh;\n    height: 27svh;\n  }')
p.write_text(s, encoding='utf-8', newline='\n')
print('A4 now uses A3 placement with delayed reveal')
