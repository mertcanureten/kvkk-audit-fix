#!/usr/bin/env python3
"""Validate KVKK report structure and closure evidence, never legal compliance."""
import argparse
import datetime as dt
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data):
    errors = []
    def need(ok, message):
        if not ok:
            errors.append(message)
    def nonempty(v):
        return isinstance(v, str) and bool(v.strip())
    def date(v):
        try:
            dt.date.fromisoformat(v)
            return True
        except (TypeError, ValueError):
            return False
    def source_url(v):
        try:
            return isinstance(v, str) and urlparse(v).scheme == 'https' and bool(urlparse(v).hostname)
        except ValueError:
            return False
    if not isinstance(data, dict):
        return ['root must be an object']
    need(type(data.get('schema_version')) is int and data['schema_version'] == 1, 'schema_version must be 1')
    for key in ('project', 'revision'):
        need(nonempty(data.get(key)), f'{key} is required')
    need(date(data.get('audit_date')), 'audit_date must be an ISO date')
    need(data.get('mode') in ('denetle', 'denetle-duzelt', 'yeniden-dogrula'), 'invalid mode')
    for key in ('scope', 'limitations'):
        v = data.get(key)
        need(isinstance(v, list) and all(nonempty(x) for x in v), f'{key} must be a string list')
    need(bool(data.get('scope')), 'scope cannot be empty')
    findings = data.get('findings')
    if not isinstance(findings, list):
        return errors + ['findings must be a list']
    seen = set()
    for index, f in enumerate(findings):
        prefix = f'findings[{index}]'
        if not isinstance(f, dict):
            errors.append(prefix + ' must be an object')
            continue
        ident = f.get('id')
        need(nonempty(ident), prefix + ': id required')
        if isinstance(ident, str):
            need(ident not in seen, prefix + ': duplicate id')
            seen.add(ident)
        for key in ('title', 'observation', 'impact'):
            need(nonempty(f.get(key)), prefix + ': ' + key + ' required')
        for key, allowed in {
            'severity': ('P0', 'P1', 'P2', 'P3'),
            'confidence': ('yuksek', 'orta', 'dusuk'),
            'classification': ('dogrulanmis-uygunsuzluk', 'olasi-uygunsuzluk', 'belge-eksikligi', 'iyilestirme'),
            'status': ('acik', 'kismi', 'karar-bekliyor', 'duzeltildi-yerel', 'kapandi', 'yanlis-pozitif'),
        }.items():
            need(f.get(key) in allowed, prefix + ': invalid ' + key)
        for key in ('control_ids', 'residual_risks', 'dependencies'):
            v = f.get(key)
            need(isinstance(v, list) and all(nonempty(x) for x in v), prefix + ': invalid ' + key)
        controls = f.get('control_ids')
        need(isinstance(controls, list) and bool(controls) and all(isinstance(x, str) and x in {f'KV-{i:02}' for i in range(1,51)} for x in controls), prefix + ': invalid control ids')
        bases = f.get('legal_basis')
        need(isinstance(bases, list) and bool(bases), prefix + ': legal_basis required')
        bases = bases if isinstance(bases, list) else []
        for b in bases:
            if not isinstance(b, dict):
                errors.append(prefix + ': legal basis must be an object'); continue
            for k in ('source_id', 'provision', 'applicability'):
                need(nonempty(b.get(k)), prefix + ': legal basis ' + k + ' required')
            url = b.get('url')
            need(source_url(url), prefix + ': invalid source URL')
            need(b.get('verification') in ('dogrulandi', 'dogrulanamadi'), prefix + ': invalid legal verification')
            if b.get('verification') == 'dogrulandi':
                need(date(b.get('verified_on')), prefix + ': verified_on required')
        evidence = f.get('evidence')
        need(isinstance(evidence, list) and bool(evidence), prefix + ': evidence required')
        for e in evidence if isinstance(evidence, list) else []:
            need(isinstance(e, dict) and e.get('kind') in ('code', 'runtime', 'document', 'test') and nonempty(e.get('location')) and nonempty(e.get('summary')), prefix + ': invalid evidence')
        rem = f.get('remediation')
        if not isinstance(rem, dict):
            errors.append(prefix + ': remediation required'); rem = {}
        for k in ('summary', 'owner', 'rollback'):
            need(nonempty(rem.get(k)), prefix + ': remediation ' + k + ' required')
        need(isinstance(rem.get('changed_files'), list) and all(nonempty(x) for x in rem.get('changed_files', [])), prefix + ': invalid changed_files')
        need('due_date' in rem and (rem['due_date'] is None or date(rem['due_date'])), prefix + ': invalid due_date')
        v = f.get('verification')
        if not isinstance(v, dict):
            errors.append(prefix + ': verification required'); v = {}
        need(nonempty(v.get('environment')), prefix + ': environment required')
        need(type(v.get('production_verified')) is bool, prefix + ': production_verified must be boolean')
        tests = v.get('tests')
        need(isinstance(tests, list), prefix + ': tests must be list')
        tests = tests if isinstance(tests, list) else []
        for t in tests:
            need(isinstance(t, dict) and nonempty(t.get('name')) and t.get('result') in ('passed', 'failed', 'not_run') and nonempty(t.get('evidence')), prefix + ': invalid test')
        if f.get('classification') == 'dogrulanmis-uygunsuzluk' or f.get('status') == 'kapandi':
            need(bool(bases) and all(isinstance(b, dict) and b.get('verification') == 'dogrulandi' for b in bases), prefix + ': definitive conclusion requires verified legal sources')
        if f.get('status') in ('duzeltildi-yerel', 'kapandi'):
            need(bool(tests) and all(isinstance(t, dict) and t.get('result') == 'passed' for t in tests), prefix + ': resolution requires passing checks')
            need(not f.get('dependencies') and not f.get('residual_risks'), prefix + ': unresolved risk/dependency requires partial status')
        if f.get('status') == 'kapandi':
            need(v.get('production_verified') is True and nonempty(v.get('production_evidence')), prefix + ': closure needs production/process evidence')
        if f.get('status') == 'karar-bekliyor':
            need(nonempty(f.get('decision_needed')), prefix + ': decision_needed required')
        if f.get('status') == 'yanlis-pozitif':
            need(nonempty(f.get('resolution_note')), prefix + ': false positive requires rationale')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    try:
        errors = validate(json.loads(args.report.read_text(encoding='utf-8')))
    except (OSError, ValueError) as exc:
        parser.exit(2, f'Report could not be read: {exc}\n')
    if errors:
        print('\n'.join(errors))
        return 1
    print('Report structure and closure evidence fields are valid; legal accuracy was not assessed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
