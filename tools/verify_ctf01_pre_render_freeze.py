from pathlib import Path
import json, hashlib, sys
root=Path(__file__).resolve().parents[1]
m=json.loads((root/"docs/evidence/CTF_01_FROZEN_INPUT_MANIFEST_01.json").read_text(encoding="utf-8"))
errs=[]
for rec in m["bindings"]:
 p=root/rec["path"]
 if not p.is_file(): errs.append(f"missing:{rec['path']}"); continue
 b=p.read_bytes(); h=hashlib.sha256(b).hexdigest()
 if h!=rec["sha256"]: errs.append(f"hash:{rec['path']}")
 if len(b)!=rec["bytes"]: errs.append(f"bytes:{rec['path']}")
packets=[r for r in m["bindings"] if "/renderer/CTF_01_" in r["path"]]
if len(packets)!=6: errs.append(f"packet_count:{len(packets)}")
if len(m["bindings"])!=19: errs.append(f"binding_count:{len(m["bindings"])}")
if m["eligible_premises"]!=["R1","R2","R3"] or m["rejected_premises"]!=["R4"]: errs.append("eligibility")
if m["image_budget"]["consumed"]!=0: errs.append("budget")
for rec in packets:
 text=(root/rec["path"]).read_text(encoding="utf-8").lower()
 for forbidden in ["kymaean","ensemble","vfd-01","ctf-01","threshold k","quiet stage","mineral theater","design sol"]:
  if forbidden in text: errs.append(f"forbidden:{forbidden}:{rec['path']}")
if errs:
 print("CTF01_FREEZE=FAIL",*errs,sep="\n"); sys.exit(1)
print(f"CTF01_FREEZE=PASS bindings={len(m['bindings'])} packets={len(packets)} images=0 effective_max={m['image_budget']['effective_total_max']}")
