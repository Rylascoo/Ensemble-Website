from PIL import Image, ImageDraw, ImageFilter, ImageChops
from pathlib import Path
import hashlib, json

here = Path(__file__).resolve().parent
repo = here.parents[1]
src = repo / 'site' / 'public' / 'stage-v2-2.webp'
out = here / 'exact-stage-translation-study-03.png'

source = Image.open(src).convert('RGB')
base = source.convert('RGBA')
W, H = source.size

clip = Image.new('L', (W, H), 0)
cd = ImageDraw.Draw(clip)
left, right = 690, 1030
top, shoulder, bottom = 120, 300, 720
cx = (left + right) // 2
radius = (right - left) // 2
cd.rectangle([left, shoulder, right, bottom], fill=255)
cd.pieslice([cx-radius, top, cx+radius, top+2*radius], 180, 360, fill=255)

def clipped(layer):
    global base
    tmp = Image.new('RGBA', (W, H), (0,0,0,0))
    tmp.paste(layer, (0,0), clip)
    base = Image.alpha_composite(base, tmp)

# Preserve source texture while establishing a practical backstage volume.
rear = Image.new('RGBA', (W,H), (0,0,0,0))
d = ImageDraw.Draw(rear)
d.rectangle([left, top, right, bottom], fill=(2,3,4,146))
# Perspective-separated planes: subtle, not scenic additions.
d.polygon([(713,304),(784,260),(806,720),(697,720)], fill=(8,9,10,76))
d.polygon([(796,258),(860,240),(865,720),(819,720)], fill=(13,13,15,58))
d.polygon([(869,242),(941,252),(935,720),(872,720)], fill=(5,6,7,84))
d.polygon([(950,260),(1015,300),(1028,720),(940,720)], fill=(10,11,12,64))
# Narrow floor-depth hints, kept nearly black.
d.polygon([(780,646),(858,620),(932,646),(919,663),(844,640),(791,663)], fill=(18,17,18,28))
clipped(rear)

# Latent Character-light: slightly more legible than Study 02, still only spill/reflection.
spill = Image.new('RGBA', (W,H), (0,0,0,0))
s = ImageDraw.Draw(spill)
s.ellipse([742,432,858,710], fill=(101,70,111,42))
s.ellipse([724,650,882,735], fill=(106,73,116,22))
s.ellipse([919,468,1019,710], fill=(61,108,104,39))
s.ellipse([895,658,1033,735], fill=(66,113,109,20))
spill = spill.filter(ImageFilter.GaussianBlur(36))
clipped(spill)

# Rear working blacks: uneven spacing and depth.
mask = Image.new('RGBA', (W,H), (0,0,0,0))
m = ImageDraw.Draw(mask)
m.polygon([(694,264),(757,222),(785,720),(690,720)], fill=(5,5,7,238))
m.polygon([(743,222),(823,194),(835,720),(779,720)], fill=(8,8,10,244))
m.polygon([(780,207),(799,201),(808,720),(797,720)], fill=(16,16,18,118))
m.polygon([(1027,274),(981,233),(959,720),(1030,720)], fill=(5,6,7,232))
m.polygon([(996,239),(962,219),(944,720),(977,720)], fill=(10,10,12,213))
# More irregular teaser profile, still a practical horizontal masking piece.
m.polygon([(720,184),(1004,170),(987,222),(747,232)], fill=(6,6,8,223))
# Edge reflections only.
m.polygon([(817,266),(822,264),(829,689),(824,690)], fill=(88,66,95,28))
m.polygon([(953,290),(958,292),(951,685),(946,685)], fill=(57,94,92,25))
mask = mask.filter(ImageFilter.GaussianBlur(0.45))
clipped(mask)

# Bellweather carrier: quieter, more natural stride, intentionally non-detailed.
fig = Image.new('RGBA', (W,H), (0,0,0,0))
f = ImageDraw.Draw(fig)
fx, ground = 956, 724
tone = (34,31,31,150)
f.ellipse([fx-9,ground-184,fx+13,ground-162], fill=tone)
f.polygon([(fx-3,ground-164),(fx+8,ground-163),(fx+9,ground-149),(fx-5,ground-149)], fill=tone)
# torso with slight forward lean
f.polygon([(fx-10,ground-151),(fx+16,ground-148),(fx+25,ground-87),(fx-3,ground-82),(fx-20,ground-104)], fill=tone)
# arms: one receding, one partly hidden by masking later
f.polygon([(fx-12,ground-138),(fx-23,ground-129),(fx-43,ground-96),(fx-36,ground-90),(fx-7,ground-115)], fill=tone)
f.polygon([(fx+12,ground-136),(fx+21,ground-126),(fx+42,ground-107),(fx+36,ground-100),(fx+7,ground-115)], fill=tone)
# legs, narrower stride than Study 02
f.polygon([(fx+1,ground-85),(fx+13,ground-82),(fx+31,ground-15),(fx+19,ground-12),(fx-1,ground-67)], fill=tone)
f.polygon([(fx-5,ground-84),(fx+5,ground-82),(fx-17,ground-17),(fx-31,ground-14),(fx-16,ground-75)], fill=tone)
f.ellipse([fx+17,ground-18,fx+43,ground-7], fill=(25,24,24,146))
f.ellipse([fx-40,ground-20,fx-15,ground-8], fill=(25,24,24,146))
fig = fig.filter(ImageFilter.GaussianBlur(0.7))
shadow = Image.new('RGBA',(W,H),(0,0,0,0))
sh = ImageDraw.Draw(shadow)
sh.ellipse([fx-47,ground-8,fx+50,ground+11], fill=(0,0,0,38))
shadow = shadow.filter(ImageFilter.GaussianBlur(15))
clipped(shadow)
clipped(fig)

# Mid-plane leg crosses the figure, so Bellweather is genuinely encountered through layers.
mid = Image.new('RGBA',(W,H),(0,0,0,0))
q = ImageDraw.Draw(mid)
q.polygon([(921,248),(903,242),(898,720),(918,720)], fill=(9,9,11,229))
q.polygon([(907,246),(902,244),(902,720),(908,720)], fill=(18,18,20,95))
mid = mid.filter(ImageFilter.GaussianBlur(0.35))
clipped(mid)

# Foreground right leg further breaks the silhouette and prevents icon/poster read.
front = Image.new('RGBA',(W,H),(0,0,0,0))
r = ImageDraw.Draw(front)
r.polygon([(1011,247),(983,230),(971,720),(1028,720)], fill=(6,6,8,242))
r.polygon([(990,236),(981,232),(977,720),(986,720)], fill=(15,15,17,112))
front = front.filter(ImageFilter.GaussianBlur(0.4))
clipped(front)

base_rgb = base.convert('RGB')
base_rgb.save(out, quality=96)

diff = ImageChops.difference(source, base_rgb)
bbox = diff.getbbox()
outside = Image.new('L',(W,H),255)
outside.paste(0,(0,0),clip)
outside_diff = ImageChops.multiply(diff.convert('L'), outside)
outside_changed = outside_diff.getbbox() is not None

source_sha = hashlib.sha256(src.read_bytes()).hexdigest()
output_sha = hashlib.sha256(out.read_bytes()).hexdigest()
manifest = {
  'study':'Exact Stage Translation Study 03',
  'status':'NON_PRODUCTION_STATIC_CONVERGENCE',
  'source_file':src.name,
  'source_sha256':source_sha,
  'source_size':[W,H],
  'output_file':out.name,
  'outside_doorway_pixel_changes':bool(outside_changed),
  'changes':[
    'stronger black-on-black perspective hierarchy without new scenery',
    'working-black overlaps made more irregular and spatial',
    'latent plum-violet and mineral-teal spill raised slightly from Study 02 while remaining indirect',
    'Bellweather quieter and more naturally mid-stride',
    'Bellweather partially occluded by both mid-plane and foreground masking'
  ],
  'explicitly_unchanged':[
    'camera/crop','outer Stage architecture',
    'all decoded source pixels outside inset doorway clip',
    'existing amber/blue Stage lighting outside intervention',
    'floor and surrounding scene'
  ],
  'prohibited_or_absent':[
    'marketing copy','furniture','props','decorative set additions',
    'formal tied-back curtains','portal geometry','visible light cones',
    'particles','magical activation','motion prototype',
    'production implementation'
  ]
}
(here/'exact-stage-translation-study-03.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(out)
print('source_sha256='+source_sha)
print('output_sha256='+output_sha)
print('output_bytes='+str(out.stat().st_size))
print('diff_bbox='+str(bbox))
print('outside_doorway_pixel_changes='+str(outside_changed))

