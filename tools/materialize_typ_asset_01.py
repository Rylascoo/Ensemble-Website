from pathlib import Path
import base64, hashlib, json, sys
repo=Path(__file__).resolve().parents[1]
template=repo/'prototypes/typ-asset-01/final-typeface-app-web.template.html'
sources=repo/'tmp/typ-asset-01/sources'
out=repo/'tmp/typ-asset-01/materialized'; out.mkdir(parents=True,exist_ok=True)
manifest=json.loads((repo/'docs/evidence/TYP_ASSET_01_FINAL_TYPEFACE_SOURCE_MANIFEST_01.json').read_text(encoding='utf-8'))
items=[('C0_SYSTEM_UI','System UI / Segoe UI control',None,'system-ui')]
for c in manifest['candidates']:
 items.append((c['id'],c['family'],sources/c['font_file'],'"TypCandidate"'))
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_file(p): return sha_bytes(Path(p).read_bytes())
records=[]; raw=template.read_text(encoding='utf-8')
for cid,label,font,family in items:
 face=''
 if font:
  data=font.read_bytes(); expected=next(x['font_sha256'] for x in manifest['candidates'] if x['id']==cid)
  if sha_bytes(data)!=expected: raise SystemExit(f'hash mismatch {cid}')
  face='@font-face{font-family:"TypCandidate";src:url(data:font/ttf;base64,'+base64.b64encode(data).decode('ascii')+') format("truetype");font-style:normal;font-weight:200 900;font-display:block}'
 html=raw.replace('__FONT_FACE__',face).replace('__FONT_FAMILY__',family).replace('__CANDIDATE_ID__',cid).replace('__CANDIDATE_LABEL__',label)
 if '__' in html: raise SystemExit(f'unresolved placeholder {cid}')
 p=out/f'{cid}.html'; p.write_text(html,encoding='utf-8')
 records.append({'id':cid,'label':label,'font_sha256':sha_file(font) if font else None,'runtime_sha256':sha_file(p),'runtime_bytes':p.stat().st_size})
(out/'manifest.json').write_text(json.dumps({'template_sha256':sha_file(template),'records':records},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'template_sha256':sha_file(template),'records':records}))
