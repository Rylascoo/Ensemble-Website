#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
P={
 'AUD':R/'docs/evidence/PHASE_C_POST_APPICON_01_REENTRY_AUDIT_09.json',
 'METHOD':R/'docs/evidence/CHARART_01_EXPRESSIVE_CHARACTER_ARTWORK_MASTER_METHOD_01.json',
 'RENDER':R/'docs/evidence/CHARART_01_ISOLATED_RENDERER_PACKET_01.json',
 'REG':R/'docs/evidence/DESIGN_PACKET_REGISTRY_01.json',
 'CUR':R/'CURRENT_STATE.md','LED':R/'docs/evidence/DESIGN_LEDGER.md',
 'HAND':R/'docs/HANDOFF_CHARART_01_EXPRESSIVE_CHARACTER_ARTWORK_MASTER_2026_09_14.md',
 'PIV':R/'docs/evidence/APP_UI_DIRECTOR_ITERATIVE_DESIGN_PIVOT_2026_09_14.json',
 'NEW_HAND':R/'docs/HANDOFF_APPUI_01_WINDOWS11_ARM64_WORKING_APP_DESIGN_2026_09_14.md',
 'ATTR':R/'.gitattributes'}
H={'AUD':'fe16dba8eb40664533de5af833f94f1fefc1ba5ef94b4c9bdee9e98524808ab0','METHOD':'83743369365323eae9635c7eadb729e553eda4bda8a1c948c25058ba5d9bd161','RENDER':'29008eb467d450e0b6ce420c34311a61e3b18394636524e6ede4fff747df6afb','PIV':'4b21d11345aed8a049f95ae1b40115a3b9650fef32a554d7789765d61a34b9c3'}
DRIVE='16mixyRAIXVjLbY7vQVfaew_9Kim628vy'
def b(p): return p.read_bytes().replace(b'\r\n',b'\n')
def sha(p): return hashlib.sha256(b(p)).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def fail(x): raise AssertionError(x)
def main():
 for k in ['AUD','METHOD','RENDER','PIV']:
  if not P[k].exists(): fail(f'missing {P[k].relative_to(R)}')
  got=sha(P[k])
  if got!=H[k]: fail(f'{k} hash mismatch {got}')
 aud,method,render,reg,piv=[load(P[k]) for k in ['AUD','METHOD','RENDER','REG','PIV']]
 if piv.get('status')!='DIRECTOR_SEQUENCING_CORRECTION_ACTIVE': fail('pivot status')
 pt=piv.get('platform_target',{})
 if pt.get('os')!='Microsoft Windows 11' or pt.get('architecture')!='ARM64' or pt.get('distribution_intent')!='Microsoft Store': fail('pivot platform')
 cd=piv.get('charart_disposition',{})
 if cd.get('status')!='DIRECTOR_TERMINATED_AFTER_VALID_FIRST_OUTPUT_NO_MASTER_ADOPTED' or cd.get('attempt_consumed') is not True or cd.get('master_authority_created') is not False: fail('pivot CHARART disposition')
 aw=piv.get('active_work',{})
 if aw.get('id')!='APPUI-01' or aw.get('mode')!='ITERATIVE_SCREEN_FIRST' or aw.get('human_artwork_dependency') is not False: fail('pivot APPUI state')
 if aud.get('status')!='COMPLETE_CHARART_01_ACTIVATED': fail('audit status')
 sel=aud.get('selected_program',{})
 if sel.get('id')!='CHARART-01' or 'SINGLE_MASTER' not in sel.get('type',''): fail('selected program')
 if aud.get('baseline',{}).get('drive_charart01_folder_id')!=DRIVE: fail('audit Drive root')
 ra=aud.get('recursive_audit',{})
 for k in ['img01_history_preserved','cps_b_authority_preserved','f2_result_aware_rescue_prevented','f3_revival_prevented','director_taste_gate_preserved']:
  if ra.get(k) is not True: fail(f'audit recursion {k}')
 if method.get('status')!='FROZEN_PRE_RENDER_SINGLE_MASTER': fail('method status')
 if method.get('activation_audit_sha256')!=H['AUD']: fail('method audit linkage')
 if method.get('authority',{}).get('drive_charart01_folder_id')!=DRIVE: fail('method Drive root')
 al=method.get('attempt_law',{})
 if al.get('valid_render_budget')!=1 or al.get('technical_no_output_retry_budget')!=1: fail('attempt budget')
 for k in ['same_gate_reroll','prompt_repair_after_exposure','image_edit_after_exposure','inpaint_outpaint_upscale_before_scoring']:
  if al.get(k) is not False: fail(f'attempt law {k}')
 crops=method.get('fixed_crop_windows',{})
 expected={'ENSEMBLE_FULL':[0.0,0.0,1.0,1.0],'PAIR_AB':[0.04,0.04,0.72,0.96],'FOCUSED_B':[0.33,0.06,0.7,0.94],'FRAGMENT_A':[0.0,0.18,0.3,0.88],'APP_CARD_BC':[0.44,0.1,0.97,0.92]}
 if crops!=expected: fail('fixed crops')
 dg=method.get('director_gate',{})
 if dg.get('required_if_design_sol_survivor') is not True or dg.get('director_may_request_same_gate_prompt_tuning') is not False: fail('Director gate')
 if render.get('status')!='FROZEN_EXTERNAL_ISOLATED_EXECUTION_READY_NO_RENDER_RESULT': fail('renderer status')
 if render.get('method_sha256')!=H['METHOD'] or render.get('drive_destination_folder_id')!=DRIVE: fail('renderer linkage')
 if render.get('valid_render_budget')!=1 or render.get('technical_no_output_retry_budget')!=1: fail('renderer budget')
 prompt=render.get('renderer_visible_prompt','').lower()
 forbidden=['kymaean','ensemble','cps-b','img-f1','img-f2','img-f3','stage-core','director','threshold k']
 bad=[x for x in forbidden if x in prompt]
 if bad: fail(f'forbidden renderer context {bad}')
 iso=method.get('renderer_isolation',{})
 for k in ['historical_images_visible','img_f1_raw_visible','director_prior_visible','stage_image_visible','project_or_brand_name_visible','competing_prompt_visible','renderer_critique_requested']:
  if iso.get(k) is not False: fail(f'isolation {k}')
 if 'fresh regular non-project image-generation chat' not in iso.get('execution_context',''): fail('execution isolation context')
 sp=reg.get('synthesis_policy',{})
 checks={'latest_reentry_audit_sha256':H['AUD'],'active_charart_program':'CHARART-01','active_charart_status':'DIRECTOR_TERMINATED_AFTER_VALID_OUTPUT_NO_MASTER_ADOPTED','active_charart_method_sha256':H['METHOD'],'active_charart_renderer_packet_sha256':H['RENDER'],'active_charart_drive_folder_id':DRIVE,'active_charart_director_gate':'CLOSED_NO_MASTER','active_charart_output_sha256':'4b793a5bf265d932e581d5b34fd05fa9ed132c3b6d0b2623a26a3c7b3363d6ba','latest_director_sequencing_correction_sha256':H['PIV'],'active_app_ui_program':'APPUI-01','active_app_ui_status':'ITERATIVE_WINDOWS11_ARM64_SCREEN_FIRST'}
 for k,w in checks.items():
  if sp.get(k)!=w: fail(f'registry {k}')
 cur=P['CUR'].read_text(encoding='utf-8'); led=P['LED'].read_text(encoding='utf-8'); hand=P['HAND'].read_text(encoding='utf-8')
 for token in ['APPUI-01 - Windows 11 ARM64 Working App Visual Prototype','Microsoft Windows 11 desktop on ARM64','DIRECTOR-TERMINATED / NO MASTER ADOPTED / NO SCORING',H['PIV']]:
  if token not in cur: fail(f'CURRENT_STATE missing {token}')
 if len(P['CUR'].read_bytes())>3072: fail('CURRENT_STATE exceeds 3 KiB')
 for token in ['## L-166 - Post-APPICON reentry activates CHARART-01',H['AUD'],H['METHOD'],H['RENDER'],DRIVE,'## L-169 - Director pivots Phase C from human-art gating to iterative Windows app-screen design',H['PIV'],'APPUI-01']:
  if token not in led: fail(f'ledger missing {token}')
 new_hand=P['NEW_HAND'].read_text(encoding='utf-8')
 for token in ['D-R1-STATUS: SUPERSEDED','Superseded by `docs/HANDOFF_APPUI_01_WINDOWS11_ARM64_WORKING_APP_DESIGN_2026_09_14.md`',H['AUD'],H['METHOD'],H['RENDER']]:
  if token not in hand: fail(f'old handoff missing {token}')
 for token in ['APPUI-01 Fresh-Chat Handoff','Microsoft Windows 11 desktop app on ARM64 intended for the Microsoft Store',H['PIV'],'CHARART-01 is Director-terminated']:
  if token not in new_hand: fail(f'new handoff missing {token}')
 attrs=P['ATTR'].read_text(encoding='utf-8')
 for rel in ['docs/evidence/PHASE_C_POST_APPICON_01_REENTRY_AUDIT_09.json','docs/evidence/CHARART_01_EXPRESSIVE_CHARACTER_ARTWORK_MASTER_METHOD_01.json','docs/evidence/CHARART_01_ISOLATED_RENDERER_PACKET_01.json','docs/evidence/APP_UI_DIRECTOR_ITERATIVE_DESIGN_PIVOT_2026_09_14.json']:
  if f'{rel} text eol=lf' not in attrs: fail(f'LF policy missing {rel}')
 for p in P.values():
  if not p.exists(): fail(f'missing {p.relative_to(R)}')
  if p.suffix.lower() in {'.json','.md','.py'} or p.name=='.gitattributes':
   txt=p.read_text(encoding='utf-8')
   if '\ufffd' in txt: fail(f'Unicode replacement in {p.relative_to(R)}')
   bad=[ord(c) for c in txt if ord(c)<32 and c not in '\n\r\t']
   if bad: fail(f'control chars in {p.relative_to(R)}')
 print('CHARART_01_CHECKPOINT=PASS')
 print('STATE=DIRECTOR_TERMINATED_NO_MASTER ATTEMPT_CONSUMED=TRUE')
 print('APPUI_01=ACTIVE WINDOWS11_ARM64 SCREEN_FIRST HUMAN_ARTWORK_DEPENDENCY=FALSE')
 return 0
if __name__=='__main__':
 try: sys.exit(main())
 except Exception as e:
  print(f'CHARART_01_FAIL: {e}',file=sys.stderr); sys.exit(1)
