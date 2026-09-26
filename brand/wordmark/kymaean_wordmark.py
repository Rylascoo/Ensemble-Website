#!/usr/bin/env python3
"""KYMÆAN wordmark generator: the single source of the brand lettering.

Everything is cut, nothing is drawn. Letters are built from skeletons (cap height 100, y down):
each stroke is a chisel cut that widens slightly toward its outer ends; joints keep plain width and
close with a bevel; ends meeting the cap or base line are cut flush; horizontals are lighter so all
strokes read equal. Letters are spaced optically: every pair's mean row-by-row whitespace (open rows
capped at a fixed depth) is solved to the same target.

From the repository root:
  python brand/wordmark/kymaean_wordmark.py            assemble: brand masters + site/public/index.html
                                                        from geometry.json (no dependencies)
  python brand/wordmark/kymaean_wordmark.py --geometry regenerate geometry.json (needs shapely==2.1.2)
  python brand/wordmark/kymaean_wordmark.py --check    regenerate in memory; fail if anything differs
Then run `node tools/site.mjs stamp` and `node tools/site.mjs check`.
"""
import json
import math
import pathlib
import re
import sys

try:  # geometry needs shapely; assembly (the default) does not
    from shapely import affinity
    from shapely.geometry import LineString, Point, Polygon, box
    from shapely.ops import unary_union
except ImportError:  # pragma: no cover
    affinity = None

ROOT = pathlib.Path(__file__).resolve().parents[2]
IVORY, BLACK, INK_2 = "#ddd5c7", "#111111", "#c4bbad"  # INK_2: the release line

# ---------------------------------------------------------------- skeletons
HAND = {  # the wordmark: letter habits of the alphabet that reached Italy through Kyme
    "K": [[(0, 0), (0, 100)], [(57, 0), (3, 48), (60, 100)]],
    "Y": [[(0, 0), (37, 47), (74, 0)], [(37, 47), (37, 100)]],
    "M": [[(0, 100), (14, 0), (46, 58), (78, 0), (92, 100)]],
    "Æ": [[(0, 100), (37, 0)], [(37, 0), (58, 100)], [(38, 0), (92, 0)], [(17, 62), (77, 50)], [(58, 100), (92, 100)]],
    "A": [[(0, 100), (40, 0), (80, 100)], [(18, 65), (62, 56)]],
    "N": [[(0, 100), (8, 0), (70, 100), (80, 0)]],
}

def _arc(cx, cy, r, a0, a1, n=12):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def _spline(pts, n=6):
    """Catmull-Rom through pts."""
    out = []
    P = [pts[0]] + pts + [pts[-1]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n; t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    out.append(pts[-1])
    return out

RW = 9.0  # release-line stroke: heavier, because it is set small
RELEASE = {  # "IN REHEARSAL" in the same hand
    "I": [[(0, 0), (0, 100)]],
    "N": HAND["N"],
    "R": [[(0, 0), (0, 100)], [(0, RW / 2), (30, RW / 2)] + _arc(30, 28.25, 23.75, -90, 90)[1:] + [(0, 52)], [(24, 52), (60, 100)]],
    "E": [[(0, 0), (0, 100)], [(0, 0), (50, 0)], [(0, 52), (42, 47)], [(0, 100), (50, 100)]],
    "H": [[(0, 0), (0, 100)], [(64, 0), (64, 100)], [(0, 54), (64, 47)]],
    "A": HAND["A"],
    "S": [_spline([(54, 16), (44, 6.5), (28, RW / 2), (11, 8), (4, 22), (12, 40), (28, 50), (46, 58),
                   (55, 76), (47, 93), (28, 100 - RW / 2), (10, 92), (1, 82)])],
    "L": [[(0, 0), (0, 100)], [(0, 100), (46, 100)]],
}

# ---------------------------------------------------------------- construction
def segments(polys):
    return [(a, b) for pl in polys for a, b in zip(pl, pl[1:])]

def kind(a, b):
    if abs(b[0] - a[0]) < 0.5: return "v"
    if abs(b[1] - a[1]) < 0.5: return "h"
    return "d"

def on_line(p):
    return p[1] <= 0.5 or p[1] >= 99.5

def free_ends(segs):
    out = {}
    for i, (a, b) in enumerate(segs):
        for p in (a, b):
            out[(i, p)] = not any(LineString(s).distance(Point(p)) < 0.6 for j, s in enumerate(segs) if j != i)
    return out

def waisted(a, b, w, flare, fa, fb, n=10):
    L = math.dist(a, b); ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L; nx, ny = -uy, ux
    left, right = [], []
    for i in range(n + 1):
        t = i / n
        grow = (fa * (1 - 2 * t) ** 2 if t < .5 else 0) + (fb * (2 * t - 1) ** 2 if t >= .5 else 0)
        h = (w + (w * flare - w) * grow) / 2
        px, py = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
        left.append((px + nx * h, py + ny * h)); right.append((px - nx * h, py - ny * h))
    return Polygon(left + right[::-1])

def incised(polys, w=(6.4, 6.0, 5.1), flare=1.26, uniform=None):
    curves = [pl for pl in polys if len(pl) > 5]  # sampled curves: one continuous stroke of plain width
    polys = [pl for pl in polys if len(pl) <= 5]
    cw = uniform or w[1]
    parts = [LineString(pl).buffer(cw / 2, cap_style="flat", join_style="round", quad_segs=4) for pl in curves]
    segs = segments(polys); free = free_ends(segs + [(pl[0], pl[1]) for pl in curves] + [(pl[-2], pl[-1]) for pl in curves])
    wd = {k: (uniform or v) for k, v in zip("vdh", w)}
    for i, (a, b) in enumerate(segs):
        k = kind(a, b); ww = wd[k]
        fa = free[(i, a)] or on_line(a); fb = free[(i, b)] or on_line(b)
        if k == "h" and on_line(a) and on_line(b):  # bars on the cap/base line sit just inside it
            y = ww / 2 if a[1] <= 0.5 else 100 - ww / 2
            a, b = (a[0], y), (b[0], y)
        poly = waisted(a, b, ww, flare, fa, fb)
        L = math.dist(a, b); ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L; nx, ny = -uy, ux; he = ww * flare / 2
        for p, sgn, fl in ((a, -1, fa), (b, 1, fb)):
            if on_line(p) and k != "h" and fl:  # run past the line; the band cut below makes it flush
                q = (p[0] + ux * sgn * 20, p[1] + uy * sgn * 20)
                poly = poly.union(Polygon([(p[0] + nx * he, p[1] + ny * he), (q[0] + nx * he, q[1] + ny * he),
                                           (q[0] - nx * he, q[1] - ny * he), (p[0] - nx * he, p[1] - ny * he)]))
        parts.append(poly)
    for pl in polys:  # bevel every joint inside a polyline
        for p0, v, p1 in zip(pl, pl[1:], pl[2:]):
            pts = [v]
            for a, b in ((p0, v), (v, p1)):
                L = math.dist(a, b); nx, ny = -(b[1] - a[1]) / L, (b[0] - a[0]) / L; h = wd[kind(a, b)] / 2
                pts += [(v[0] + nx * h, v[1] + ny * h), (v[0] - nx * h, v[1] - ny * h)]
            parts.append(Polygon(pts).convex_hull)
    return unary_union(parts).intersection(box(-80, 0, 480, 100))

# ---------------------------------------------------------------- spacing
def _row(g, y):
    r = g.intersection(LineString([(-1e4, y), (1e4, y)]))
    return None if r.is_empty else r.bounds

def layout(glyphs, target, depth=20):
    placed, prev = [], None
    for g in glyphs:
        ox = 0.0
        if prev is not None:
            L, oxl = prev; lb = L.bounds[2] + oxl; rb = g.bounds[0]; diffs = []
            for y in range(2, 99, 2):
                a, b = _row(L, y), _row(g, y)
                l = max((a[2] + oxl) if a else lb - depth, lb - depth)
                r = min(b[0] if b else rb + depth, rb + depth)
                diffs.append(r - l)
            ox = target - sum(diffs) / len(diffs)
        placed.append(affinity.translate(g, ox)); prev = (g, ox)
    return unary_union(placed)

def wordmark():
    return layout([incised(HAND[c]) for c in "KYMÆAN"], target=40)

def release_line():
    kw = dict(uniform=RW, flare=1.18)
    first = layout([incised(RELEASE[c], **kw) for c in "IN"], target=96)
    second = layout([incised(RELEASE[c], **kw) for c in "REHEARSAL"], target=96)
    return unary_union([first, affinity.translate(second, first.bounds[2] + 190 - second.bounds[0])])

# ---------------------------------------------------------------- Threshold K (smooth master geometry)
def threshold_k():
    src = (ROOT / "brand" / "threshold-k-ivory.svg").read_text(encoding="utf-8")
    polys = []
    for d in re.findall(r'd="([^"]+)"', src):
        tok = re.findall(r"[MLCZ]|-?\d+(?:\.\d+)?", d); i = 0; cur = None; pts = []
        while i < len(tok):
            t = tok[i]
            if t in "ML":
                cur = (float(tok[i + 1]), float(tok[i + 2])); pts.append(cur); i += 3
            elif t == "C":
                c1 = (float(tok[i + 1]), float(tok[i + 2])); c2 = (float(tok[i + 3]), float(tok[i + 4]))
                e = (float(tok[i + 5]), float(tok[i + 6]))
                for s in range(1, 17):
                    u = s / 16
                    pts.append(tuple((1 - u) ** 3 * cur[j] + 3 * (1 - u) ** 2 * u * c1[j] + 3 * (1 - u) * u * u * c2[j] + u ** 3 * e[j] for j in (0, 1)))
                cur = e; i += 7
            else:
                i += 1
        polys.append(Polygon(pts))
    k = unary_union(polys); s = 103 / 184
    return affinity.affine_transform(k, [s, 0, 0, s, -18 * s, -18 * s - 1.5])

def stacked_lockup(k_height=2.1, gap=52):
    word = wordmark(); wb = word.bounds
    k = threshold_k(); kb = k.bounds; f = k_height * 100 / (kb[3] - kb[1])
    k = affinity.scale(k, f, f, origin=(0, 0)); kb = k.bounds
    k = affinity.translate(k, (wb[0] + wb[2]) / 2 - (kb[0] + kb[2]) / 2, -gap - kb[3])
    return k, word

# ---------------------------------------------------------------- output
def path_d(g, T=lambda x, y: (x, y), prec=2):
    polys = [g] if isinstance(g, Polygon) else [p for p in getattr(g, "geoms", []) if isinstance(p, Polygon)]
    out = []
    for p in polys:
        for ring in [p.exterior, *p.interiors]:
            c = [T(x, y) for x, y in list(ring.coords)[:-1]]
            f = lambda v: (f"{v:.{prec}f}".rstrip("0").rstrip(".") or "0").replace("-0", "0") if abs(v) >= 0.5 / 10 ** prec else "0"
            out.append("M" + "L".join(f"{f(x)} {f(y)}" for x, y in c) + "Z")
    return "".join(out)

GEOMETRY = pathlib.Path(__file__).with_name("geometry.json")

def geometry():
    """All lettering as path data (1 decimal) with bounds. Needs shapely."""
    word = wordmark(); rel = release_line(); k, _ = stacked_lockup()
    pack = lambda g: {"d": path_d(g.simplify(0.08, preserve_topology=True), prec=1), "bounds": [round(v, 1) for v in g.bounds]}
    k_cut = k.difference(k.buffer(-6.4, join_style="mitre"))  # same silhouette, cut as an outline
    return {"wordmark": pack(word), "release": pack(rel), "lockup_k": pack(k), "lockup_k_cut": pack(k_cut)}

def svg_file(parts, colour, label="Kymaean", pad=4):
    x0 = min(p["bounds"][0] for p in parts); y0 = min(p["bounds"][1] for p in parts)
    x1 = max(p["bounds"][2] for p in parts); y1 = max(p["bounds"][3] for p in parts)
    body = "".join(f'<path fill="{colour}" fill-rule="evenodd" d="{p["d"]}"/>' for p in parts)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0 - pad:.1f} {y0 - pad:.1f} {x1 - x0 + 2 * pad:.1f} '
            f'{y1 - y0 + 2 * pad:.1f}" role="img" aria-label="{label}">{body}</svg>\n')

def replace_between(text, name, content):
    a, b = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    i, j = text.index(a) + len(a), text.index(b)
    return text[:i] + content + text[j:]

def assemble(geo, write=True):
    """Brand masters and the site's lettering from geometry. No dependencies."""
    files = {}
    for colour, tag in ((IVORY, "ivory"), (BLACK, "black")):
        files[f"brand/kymaean-wordmark-{tag}.svg"] = svg_file([geo["wordmark"]], colour)
        files[f"brand/kymaean-lockup-stacked-{tag}.svg"] = svg_file([geo["lockup_k"], geo["wordmark"]], colour)
        files[f"brand/kymaean-lockup-stacked-cut-{tag}.svg"] = svg_file([geo["lockup_k_cut"], geo["wordmark"]], colour)
    x0, _, x1, _ = geo["wordmark"]["bounds"]; s = min(0.86, 650 / (x1 - x0)); tx = (690 - (x1 - x0) * s) / 2 - x0 * s
    wm = f'<path fill="currentColor" transform="translate({tx:.2f} 18) scale({s:.5f})" d="{geo["wordmark"]["d"]}"/>'
    rx0, _, rx1, _ = geo["release"]["bounds"]
    # the release line ships as an image: it is on screen from the first frame, so it is the page's
    # largest-contentful-paint candidate on desktop, where the full-screen stage is not counted
    files["site/public/assets/img/release.svg"] = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{rx0:.1f} 0 {rx1 - rx0:.1f} 100">'
        f'<path fill="{INK_2}" d="{geo["release"]["d"]}"/></svg>\n')
    html = (ROOT / "site/public/index.html").read_text(encoding="utf-8")
    files["site/public/index.html"] = replace_between(html, "wordmark", wm)
    if write:
        for rel_path, text in files.items():
            (ROOT / rel_path).write_text(text, encoding="utf-8", newline="\n")
    return files

if __name__ == "__main__":
    if "--geometry" in sys.argv:
        GEOMETRY.write_text(json.dumps(geometry(), indent=1) + "\n", encoding="utf-8", newline="\n")
        print("wrote", GEOMETRY.relative_to(ROOT))
    elif "--check" in sys.argv:
        fresh = geometry(); saved = json.loads(GEOMETRY.read_text(encoding="utf-8"))
        problems = [k for k in fresh if fresh[k] != saved.get(k)]
        built = assemble(saved, write=False)
        problems += [p for p, t in built.items() if (ROOT / p).read_text(encoding="utf-8") != t]
        if problems:
            sys.exit("FAIL wordmark out of date: " + ", ".join(problems) + " (run --geometry, then assemble)")
        print("PASS wordmark geometry and assembled files are current")
    else:
        assemble(json.loads(GEOMETRY.read_text(encoding="utf-8")))
        print("assembled brand masters and site/public/index.html")
