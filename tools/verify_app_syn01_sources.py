#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'docs/evidence/APP_SYN_01_EXECUTION_DEFAULTS_AND_SOURCE_MANIFEST_02.json'
STAGE_PACKET=ROOT/'docs/evidence/packets/PKT_STAGE_CORE_02.json'

def lf_sha(path:Path)->str:
 data=path.read_text(encoding='utf-8').replace('\r\n','\n').replace('\r','\n').encode('utf-8')
 return hashlib.sha256(data).hexdigest()

def main()->int:
 m=json.loads(MANIFEST.read_text(encoding='utf-8'));stage=json.loads(STAGE_PACKET.read_text(encoding='utf-8'))['visual_master']
 assert m['schema']=='kymaean.app-syn-01.execution-defaults-source-manifest.v2'
 assert m['status']=='FROZEN_BROWSER_LAUNCHER_REPAIR_NO_DESIGN_RESULT'
 assert m['predecessor_manifest']['lf_sha256']=='af5e8c2a05bb368344c4538a616dfbfcd4594ec10377dca28d7f2c236f37dceb'
 repair=m['browser_launcher_repair'];assert repair['classification']=='EDGE_LAUNCHER_DETACHED_CHILD_CDP_HANDSHAKE_DEFECT_NO_PAGE_LOAD_NO_DESIGN_RESULT' and repair['visual_evidence_consumed_before_repair'] is False
 transport=m['browser_transport'];assert transport['cdp_port_default']==9229 and transport['shutdown']=='Browser.close CDP command'
 assert m['recursive_audit']['new_visual_synthesis_evidence_consumed'] is False
 for _,rec in m['packet_sources'].items(): assert lf_sha(ROOT/rec['path'])==rec['lf_sha256'],rec['path']
 for path,expected in m['materialization_sources'].items(): assert lf_sha(ROOT/path)==expected,path
 d=m['drive_stage_input'];assert d['drive_file_id']==stage['drive_file_id'] and d['sha256_raw']==stage['sha256'] and d['size_bytes']==stage['uploaded_size_bytes'] and d['dimensions']==[1672,941]
 assert len(m['browser_modes'])==10 and len(m['ablation_matrix'])==11
 template=(ROOT/m['review_surface']['template']).read_text(encoding='utf-8')
 for token in ('__STAGE_DATA_URI__','__C0_SVG__','__O3_SVG__'): assert token in template,token
 for token in ('460ms','70ms','140ms','280ms','translateY(28px)','#F4F3F7','#006F73','#F7F5F2','#9A4D2E'): assert token in template,token
 assert 'http://' not in template and 'https://' not in template
 assert set(m['clr_contextual_probes']['families'])=={'F1','F2'} and m['clr_contextual_probes']['variants']==['FULL','NO_MAT','NO_O3','NO_MOT']
 assert m['director_review_surface']['primary_aesthetic'].startswith('normal-wide')
 assert m['recursive_audit']=={'status':'CLEAN_PRE_EXPOSURE_AFTER_MECHANICAL_LAUNCHER_REPAIR','new_visual_synthesis_evidence_consumed':False,'material_defects_remaining':False}
 print('APP_SYN_01_SOURCES=PASS')
 print('PACKETS='+str(len(m['packet_sources'])))
 print('MATERIALIZATION_SOURCES='+str(len(m['materialization_sources'])))
 return 0

if __name__=='__main__':
 raise SystemExit(main())
