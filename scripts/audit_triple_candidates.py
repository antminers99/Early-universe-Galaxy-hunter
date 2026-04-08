#!/usr/bin/env python3
"""
Phase 5: Kill audit of 35 triple-overlap z>10 candidates.
Numerical checks substituting for visual inspection where image data is unavailable.
"""
import csv
import math
import numpy as np
from datetime import datetime, timezone

NIRCAM_PSF_FWHM_ARCSEC = {
    'F090W': 0.034, 'F115W': 0.040, 'F150W': 0.050, 'F200W': 0.066,
    'F277W': 0.087, 'F356W': 0.115, 'F444W': 0.145,
}
PIXEL_SCALE = 0.03

TARGET_BANDS = ['F090W', 'F115W', 'F150W', 'F200W', 'F277W', 'F356W', 'F444W']

LYMAN_BREAK_UM = 0.0912
BAND_PIVOT_UM = {
    'F090W': 0.902, 'F115W': 1.154, 'F150W': 1.501, 'F200W': 1.990,
    'F277W': 2.762, 'F356W': 3.568, 'F444W': 4.421,
}


def to_float(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (ValueError, TypeError):
        return None


def load_csv(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def expected_dropout_bands(z_peak):
    lyman_obs = LYMAN_BREAK_UM * (1 + z_peak)
    dropouts = []
    for band, pivot in sorted(BAND_PIVOT_UM.items(), key=lambda x: x[1]):
        if pivot < lyman_obs * 0.9:
            dropouts.append(band)
    return dropouts


def expected_detection_bands(z_peak):
    lyman_obs = LYMAN_BREAK_UM * (1 + z_peak)
    detections = []
    for band, pivot in sorted(BAND_PIVOT_UM.items(), key=lambda x: x[1]):
        if pivot > lyman_obs * 1.1:
            detections.append(band)
    return detections


def check_dropout_consistency(row, z_peak):
    dropout_bands = expected_dropout_bands(z_peak)
    detection_bands = expected_detection_bands(z_peak)

    issues = []
    flags = {'dropout_ok': True, 'detection_ok': True}

    for band in dropout_bands:
        flux = to_float(row.get(f'{band}_flux'))
        err = to_float(row.get(f'{band}_err'))
        if flux is not None and err is not None and err > 0:
            snr = flux / err
            if snr > 3:
                issues.append(f"{band} detected at SNR={snr:.1f} (should be dropout at z={z_peak:.1f})")
                flags['dropout_ok'] = False

    n_detected = 0
    n_expected = len(detection_bands)
    for band in detection_bands:
        flux = to_float(row.get(f'{band}_flux'))
        err = to_float(row.get(f'{band}_err'))
        if flux is not None and err is not None and err > 0:
            snr = flux / err
            if snr > 2:
                n_detected += 1

    if n_expected > 0 and n_detected < n_expected * 0.5:
        issues.append(f"Only {n_detected}/{n_expected} expected detection bands have SNR>2")
        flags['detection_ok'] = False

    return issues, flags


def check_size_vs_psf(row):
    fwhm_pix = to_float(row.get('FWHM_pix'))
    issues = []
    if fwhm_pix is None or fwhm_pix <= 0:
        issues.append("FWHM invalid or zero")
        return issues, {'size_ok': False}

    fwhm_arcsec = fwhm_pix * PIXEL_SCALE
    psf_f444w = NIRCAM_PSF_FWHM_ARCSEC['F444W']

    if fwhm_arcsec < psf_f444w * 0.5:
        issues.append(f"FWHM={fwhm_arcsec:.4f}\" < 0.5x PSF ({psf_f444w:.4f}\") — likely point source or artifact")
        return issues, {'size_ok': False}

    if fwhm_arcsec < psf_f444w * 0.8:
        issues.append(f"FWHM={fwhm_arcsec:.4f}\" < 0.8x PSF — marginally resolved, treat with caution")
        return issues, {'size_ok': True}

    return issues, {'size_ok': True}


def check_error_quality(row):
    issues = []
    flags = {'errors_ok': True}

    for band in ['F356W', 'F444W']:
        flux = to_float(row.get(f'{band}_flux'))
        err = to_float(row.get(f'{band}_err'))
        if flux is None or err is None:
            issues.append(f"{band} flux or error missing")
            flags['errors_ok'] = False
            continue
        if err <= 0:
            issues.append(f"{band} error <= 0")
            flags['errors_ok'] = False
            continue
        snr = flux / err
        if snr < 2:
            issues.append(f"{band} SNR={snr:.1f} too low for reliable measurement")
            flags['errors_ok'] = False

    f356_flux = to_float(row.get('F356W_flux'))
    f444_flux = to_float(row.get('F444W_flux'))
    if f356_flux and f444_flux and f356_flux > 0 and f444_flux > 0:
        ratio = f444_flux / f356_flux
        if ratio > 50 or ratio < 0.02:
            issues.append(f"F444W/F356W ratio = {ratio:.1f} — extreme, possible artifact")
            flags['errors_ok'] = False

    return issues, flags


def check_flux_center_consistency(row):
    issues = []
    f356 = to_float(row.get('F356W_flux'))
    f444 = to_float(row.get('F444W_flux'))
    e356 = to_float(row.get('F356W_err'))
    e444 = to_float(row.get('F444W_err'))

    if not all([f356, f444, e356, e444]) or e356 <= 0 or e444 <= 0:
        return issues, {'center_ok': False}

    snr356 = f356 / e356
    snr444 = f444 / e444

    if snr444 > 3 and snr356 < 1:
        issues.append(f"F444W detected (SNR={snr444:.1f}) but F356W not (SNR={snr356:.1f}) — suspicious for z~11-13")
        return issues, {'center_ok': False}

    return issues, {'center_ok': True}


def find_nearest_neighbors(candidates, all_sources):
    results = {}
    for c in candidates:
        cid = c['ID']
        cra = to_float(c['RA'])
        cdec = to_float(c['DEC'])
        cfield = c['field']
        if cra is None or cdec is None:
            results[cid] = {'nn_dist': None, 'nn_id': None, 'nn_count_1as': 0}
            continue

        min_dist = 999
        min_id = None
        count_1as = 0

        for s in all_sources:
            if s['ID'] == cid and s['field'] == cfield:
                continue
            if s['field'] != cfield:
                continue
            sra = to_float(s['RA'])
            sdec = to_float(s['DEC'])
            if sra is None or sdec is None:
                continue

            dra = (sra - cra) * math.cos(math.radians(cdec)) * 3600
            ddec = (sdec - cdec) * 3600
            dist = math.sqrt(dra**2 + ddec**2)

            if dist < min_dist:
                min_dist = dist
                min_id = s['ID']
            if dist < 1.0:
                count_1as += 1

        results[cid] = {'nn_dist': min_dist, 'nn_id': min_id, 'nn_count_1as': count_1as}

    return results


def check_single_band_dominance(row):
    issues = []
    fluxes = {}
    snrs = {}
    for band in TARGET_BANDS:
        f = to_float(row.get(f'{band}_flux'))
        e = to_float(row.get(f'{band}_err'))
        if f is not None and e is not None and e > 0:
            fluxes[band] = f
            snrs[band] = f / e

    good_bands = [b for b, s in snrs.items() if s > 3]
    if len(good_bands) <= 1:
        issues.append(f"Only {len(good_bands)} band(s) with SNR>3 — measurement based on too few bands")
        return issues, {'multi_band_ok': False}

    return issues, {'multi_band_ok': True}


def assign_verdict(all_issues, all_flags):
    critical_fails = 0
    warnings = 0

    if not all_flags.get('dropout_ok', True):
        critical_fails += 1
    if not all_flags.get('errors_ok', True):
        critical_fails += 1
    if not all_flags.get('size_ok', True):
        warnings += 1
    if not all_flags.get('center_ok', True):
        warnings += 1
    if not all_flags.get('multi_band_ok', True):
        critical_fails += 1

    nn_dist = all_flags.get('nn_dist')
    if nn_dist is not None and nn_dist < 0.3:
        warnings += 1

    if critical_fails >= 2:
        return 'FAIL'
    elif critical_fails == 1 or warnings >= 2:
        return 'MAYBE'
    else:
        return 'PASS'


def main():
    print("="*70)
    print("  Phase 5: Kill Audit of 35 Triple-Overlap z>10 Candidates")
    print(f"  {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("="*70)

    overlap = load_csv('data/research/overlap_candidates_v1.csv')
    triple = [r for r in overlap if int(r['num_hunts']) == 3]
    print(f"\n  Triple-overlap candidates: {len(triple)}")

    features = load_csv('data/research/sample_b_features_v1.csv')
    feat_map = {}
    for r in features:
        feat_map[(r['field'], r['ID'])] = r

    all_sources = load_csv('data/research/sample_b_killed_v1.csv')
    print(f"  All sources for neighbor check: {len(all_sources):,}")

    candidates = []
    for t in triple:
        key = (t['field'], t['ID'])
        feat = feat_map.get(key, {})
        merged = {**feat, **t}
        candidates.append(merged)

    nn_results = find_nearest_neighbors(candidates, all_sources)

    audit_rows = []

    for c in candidates:
        z_peak = to_float(c.get('z_peak', 0)) or 0
        cid = c['ID']

        all_issues = []
        all_flags = {}

        issues, flags = check_dropout_consistency(c, z_peak)
        all_issues.extend(issues)
        all_flags.update(flags)

        issues, flags = check_size_vs_psf(c)
        all_issues.extend(issues)
        all_flags.update(flags)

        issues, flags = check_error_quality(c)
        all_issues.extend(issues)
        all_flags.update(flags)

        issues, flags = check_flux_center_consistency(c)
        all_issues.extend(issues)
        all_flags.update(flags)

        issues, flags = check_single_band_dominance(c)
        all_issues.extend(issues)
        all_flags.update(flags)

        nn = nn_results.get(cid, {})
        nn_dist = nn.get('nn_dist')
        nn_count = nn.get('nn_count_1as', 0)
        all_flags['nn_dist'] = nn_dist

        if nn_dist is not None and nn_dist < 0.3:
            all_issues.append(f"Nearest neighbor at {nn_dist:.3f}\" — possible blending")
        if nn_count >= 3:
            all_issues.append(f"{nn_count} sources within 1\" — crowded region")

        verdict = assign_verdict(all_issues, all_flags)

        dropout_bands = expected_dropout_bands(z_peak)
        detection_bands = expected_detection_bands(z_peak)

        snr_profile = {}
        for band in TARGET_BANDS:
            f = to_float(c.get(f'{band}_flux'))
            e = to_float(c.get(f'{band}_err'))
            if f is not None and e is not None and e > 0:
                snr_profile[band] = f"{f/e:.1f}"
            else:
                snr_profile[band] = "N/A"

        audit_rows.append({
            'field': c['field'],
            'ID': cid,
            'z_peak': f"{z_peak:.2f}",
            'Prob_gt_6': c.get('Prob_gt_6', ''),
            'verdict': verdict,
            'n_issues': len(all_issues),
            'issues': '; '.join(all_issues) if all_issues else 'None',
            'dropout_ok': 'Y' if all_flags.get('dropout_ok', False) else 'N',
            'detection_ok': 'Y' if all_flags.get('detection_ok', False) else 'N',
            'size_ok': 'Y' if all_flags.get('size_ok', False) else 'N',
            'errors_ok': 'Y' if all_flags.get('errors_ok', False) else 'N',
            'center_ok': 'Y' if all_flags.get('center_ok', False) else 'N',
            'multi_band_ok': 'Y' if all_flags.get('multi_band_ok', False) else 'N',
            'FWHM_arcsec': f"{(to_float(c.get('FWHM_pix', 0)) or 0) * PIXEL_SCALE:.4f}",
            'nn_dist_arcsec': f"{nn_dist:.3f}" if nn_dist else 'N/A',
            'nn_count_1as': nn_count,
            'expected_dropouts': ','.join(dropout_bands),
            'expected_detections': ','.join(detection_bands),
            'SNR_F090W': snr_profile.get('F090W', ''),
            'SNR_F115W': snr_profile.get('F115W', ''),
            'SNR_F150W': snr_profile.get('F150W', ''),
            'SNR_F200W': snr_profile.get('F200W', ''),
            'SNR_F277W': snr_profile.get('F277W', ''),
            'SNR_F356W': snr_profile.get('F356W', ''),
            'SNR_F444W': snr_profile.get('F444W', ''),
            'F444W_flux': c.get('F444W_flux', ''),
            'FWHM_pix': c.get('FWHM_pix', ''),
            'A_pix': c.get('A_pix', ''),
        })

    import os
    os.makedirs('data/research', exist_ok=True)
    keys = list(audit_rows[0].keys())
    with open('data/research/audit_triple_candidates_v1.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(audit_rows)

    pass_count = sum(1 for r in audit_rows if r['verdict'] == 'PASS')
    maybe_count = sum(1 for r in audit_rows if r['verdict'] == 'MAYBE')
    fail_count = sum(1 for r in audit_rows if r['verdict'] == 'FAIL')

    survivors = [r for r in audit_rows if r['verdict'] in ('PASS', 'MAYBE')]
    survivors_pass = [r for r in audit_rows if r['verdict'] == 'PASS']

    with open('data/research/top_candidates_survivors_v1.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(survivors)

    print(f"\n{'='*70}")
    print(f"  AUDIT RESULTS")
    print(f"{'='*70}")

    print(f"\n  Verdicts:")
    print(f"    PASS:  {pass_count}")
    print(f"    MAYBE: {maybe_count}")
    print(f"    FAIL:  {fail_count}")
    print(f"    Total: {len(audit_rows)}")

    print(f"\n  Survivors (PASS + MAYBE): {len(survivors)}")
    print(f"  Clean PASS only: {pass_count}")

    print(f"\n  --- Detailed per-candidate audit ---")
    for r in audit_rows:
        marker = {'PASS': 'P', 'MAYBE': '?', 'FAIL': 'X'}[r['verdict']]
        issues_short = r['issues'][:80] if r['issues'] != 'None' else ''
        print(f"    [{marker}] {r['field']:7s} ID={r['ID']:>8s} z={r['z_peak']:>5s} | drop={r['dropout_ok']} det={r['detection_ok']} sz={r['size_ok']} err={r['errors_ok']} ctr={r['center_ok']} mb={r['multi_band_ok']} nn={r['nn_dist_arcsec']:>6s} | {issues_short}")

    print(f"\n  --- Top 10 survivors ---")
    for i, r in enumerate(survivors[:10], 1):
        print(f"    {i:>2}. [{r['verdict']:5s}] {r['field']:7s} ID={r['ID']:>8s} z={r['z_peak']:>5s} P6={r['Prob_gt_6'][:5]} FWHM={r['FWHM_arcsec']}\" nn={r['nn_dist_arcsec']}\" issues={r['n_issues']}")

    print(f"\n  --- GOODS-S vs GOODS-N comparison (among 35 candidates) ---")
    for field_label in ['GOODS-S', 'GOODS-N']:
        field_rows = [r for r in audit_rows if r['field'] == field_label]
        if not field_rows:
            continue
        n = len(field_rows)
        n_pass = sum(1 for r in field_rows if r['verdict'] == 'PASS')
        n_maybe = sum(1 for r in field_rows if r['verdict'] == 'MAYBE')
        n_fail = sum(1 for r in field_rows if r['verdict'] == 'FAIL')

        f444_vals = [to_float(r['F444W_flux']) for r in field_rows if to_float(r['F444W_flux'])]
        fwhm_vals = [to_float(r['FWHM_pix']) for r in field_rows if to_float(r['FWHM_pix'])]
        nn_vals = [to_float(r['nn_dist_arcsec']) for r in field_rows if to_float(r['nn_dist_arcsec'])]

        print(f"\n    {field_label}: {n} candidates")
        print(f"      PASS={n_pass}, MAYBE={n_maybe}, FAIL={n_fail}")
        if f444_vals:
            print(f"      median F444W flux: {np.median(f444_vals):.1f} nJy")
        if fwhm_vals:
            print(f"      median FWHM: {np.median(fwhm_vals)*PIXEL_SCALE:.4f}\"")
        if nn_vals:
            print(f"      median nearest neighbor: {np.median(nn_vals):.3f}\"")

    issue_counter = {}
    for r in audit_rows:
        if r['issues'] == 'None':
            continue
        for issue in r['issues'].split('; '):
            key = issue.split('—')[0].split('=')[0].strip()[:50]
            issue_counter[key] = issue_counter.get(key, 0) + 1

    print(f"\n  --- Most common issues ---")
    for issue, count in sorted(issue_counter.items(), key=lambda x: -x[1])[:10]:
        print(f"    {count:>3}x  {issue}")

    print(f"\n  Files saved:")
    print(f"    data/research/audit_triple_candidates_v1.csv")
    print(f"    data/research/top_candidates_survivors_v1.csv")

    print(f"\n  Phase 5 complete.")


if __name__ == '__main__':
    main()
