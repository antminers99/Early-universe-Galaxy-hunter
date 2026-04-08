#!/usr/bin/env python3
"""
Phase 4: First anomaly hunt across 3 dimensions (brightness, redness, compactness).
Works within redshift bins. Outputs candidate lists + overlap analysis.
"""
import csv
import os
import math
import numpy as np
from datetime import datetime, timezone


def load_features():
    with open('data/research/sample_b_features_v1.csv') as f:
        return list(csv.DictReader(f))


def to_float(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (ValueError, TypeError):
        return None


def build_hunt_ready(rows):
    ready = []
    for r in rows:
        cb = int(r['clean_phot_bands'])
        snr444 = to_float(r['F444W_SNR'])
        if cb >= 5 and snr444 is not None and snr444 >= 3:
            ready.append(r)
    return ready


def save_csv(records, filepath):
    if not records:
        return
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    keys = list(records[0].keys())
    with open(filepath, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(records)
    print(f"  Saved {len(records):,} rows -> {filepath}")


def hunt_brightness(ready, bin_label):
    bin_rows = [r for r in ready if r['bin_z'] == bin_label]
    if not bin_rows:
        return []

    for r in bin_rows:
        r['_f444w'] = to_float(r['F444W_flux']) or 0

    bin_rows.sort(key=lambda r: r['_f444w'], reverse=True)

    n = len(bin_rows)
    top_1pct = max(1, n // 100)
    top_n = max(top_1pct, min(30, n))

    results = []
    for rank, r in enumerate(bin_rows[:top_n], 1):
        results.append({
            'field': r['field'],
            'ID': r['ID'],
            'z_peak': r['z_peak'],
            'Prob_gt_6': r['Prob_gt_6'],
            'bin_z': bin_label,
            'F444W_flux': r['F444W_flux'],
            'F444W_err': r['F444W_err'],
            'F444W_SNR': r['F444W_SNR'],
            'F356W_flux': r['F356W_flux'],
            'F356W_err': r['F356W_err'],
            'A_arcsec': r['A_arcsec'],
            'FWHM_arcsec': r['FWHM_arcsec'],
            'rank_in_bin': rank,
            'bin_size': n,
            'hunt_type': 'brightness',
        })

    return results


def hunt_redness(ready, bin_label):
    bin_rows = [r for r in ready if r['bin_z'] == bin_label]
    if not bin_rows:
        return []

    candidates_red1 = []
    candidates_red2 = []

    for r in bin_rows:
        f444 = to_float(r['F444W_flux'])
        f200 = to_float(r['F200W_flux'])
        f356 = to_float(r['F356W_flux'])
        f150 = to_float(r['F150W_flux'])
        e444 = to_float(r['F444W_err'])
        e200 = to_float(r['F200W_err'])
        e356 = to_float(r['F356W_err'])
        e150 = to_float(r['F150W_err'])

        red1 = None
        if (f444 and f200 and e444 and e200 and
            f444 > 0 and f200 > 0 and e444 > 0 and e200 > 0 and
            f444/e444 >= 2 and f200/e200 >= 2):
            red1 = math.log10(f444 / f200)

        red2 = None
        if (f356 and f150 and e356 and e150 and
            f356 > 0 and f150 > 0 and e356 > 0 and e150 > 0 and
            f356/e356 >= 2 and f150/e150 >= 2):
            red2 = math.log10(f356 / f150)

        r['_red1'] = red1
        r['_red2'] = red2

        if red1 is not None:
            candidates_red1.append(r)
        if red2 is not None:
            candidates_red2.append(r)

    candidates_red1.sort(key=lambda r: r['_red1'], reverse=True)
    candidates_red2.sort(key=lambda r: r['_red2'], reverse=True)

    results = []
    seen_ids = set()

    for src_list, color_name in [(candidates_red1, 'red_1'), (candidates_red2, 'red_2')]:
        n = len(src_list)
        top_1pct = max(1, n // 100)
        top_n = max(top_1pct, min(30, n))

        for rank, r in enumerate(src_list[:top_n], 1):
            key = (r['field'], r['ID'], color_name)
            if key in seen_ids:
                continue
            seen_ids.add(key)
            results.append({
                'field': r['field'],
                'ID': r['ID'],
                'z_peak': r['z_peak'],
                'Prob_gt_6': r['Prob_gt_6'],
                'bin_z': bin_label,
                'F444W_flux': r['F444W_flux'],
                'F200W_flux': r['F200W_flux'],
                'F356W_flux': r['F356W_flux'],
                'F150W_flux': r['F150W_flux'],
                'red_1': f"{r['_red1']:.4f}" if r['_red1'] is not None else '',
                'red_2': f"{r['_red2']:.4f}" if r['_red2'] is not None else '',
                'A_arcsec': r['A_arcsec'],
                'FWHM_arcsec': r['FWHM_arcsec'],
                'rank_in_bin': rank,
                'color_index': color_name,
                'bin_size': n,
                'hunt_type': 'redness',
            })

    return results


def hunt_compactness(ready, bin_label):
    bin_rows = [r for r in ready if r['bin_z'] == bin_label]
    if not bin_rows:
        return []

    fwhm_candidates = []
    proxy_candidates = []

    for r in bin_rows:
        fwhm = to_float(r['FWHM_arcsec'])
        f444 = to_float(r['F444W_flux'])

        if fwhm and fwhm > 0:
            r['_fwhm'] = fwhm
            fwhm_candidates.append(r)

            if f444 and f444 > 0:
                r['_compact_proxy'] = math.log10(f444) - 2 * math.log10(fwhm)
                proxy_candidates.append(r)

    fwhm_candidates.sort(key=lambda r: r['_fwhm'])
    proxy_candidates.sort(key=lambda r: r.get('_compact_proxy', -999), reverse=True)

    results = []
    seen_ids = set()

    for src_list, metric_name, top_limit in [
        (fwhm_candidates, 'smallest_fwhm', 30),
        (proxy_candidates, 'highest_compact_proxy', 30)
    ]:
        for rank, r in enumerate(src_list[:top_limit], 1):
            key = (r['field'], r['ID'], metric_name)
            if key in seen_ids:
                continue
            seen_ids.add(key)
            results.append({
                'field': r['field'],
                'ID': r['ID'],
                'z_peak': r['z_peak'],
                'Prob_gt_6': r['Prob_gt_6'],
                'bin_z': bin_label,
                'F444W_flux': r['F444W_flux'],
                'F444W_SNR': r['F444W_SNR'],
                'FWHM_arcsec': r['FWHM_arcsec'],
                'A_arcsec': r['A_arcsec'],
                'B_arcsec': r['B_arcsec'],
                'compact_proxy': f"{r.get('_compact_proxy', 0):.4f}" if '_compact_proxy' in r else '',
                'rank_in_bin': rank,
                'metric': metric_name,
                'bin_size': len(src_list),
                'hunt_type': 'compactness',
            })

    return results


def build_overlap(bright, red, compact):
    all_candidates = {}

    for lst, hunt_type in [(bright, 'brightness'), (red, 'redness'), (compact, 'compactness')]:
        for r in lst:
            key = (r['field'], r['ID'])
            if key not in all_candidates:
                all_candidates[key] = {
                    'field': r['field'],
                    'ID': r['ID'],
                    'z_peak': r['z_peak'],
                    'Prob_gt_6': r['Prob_gt_6'],
                    'bin_z': r['bin_z'],
                    'hunts': set(),
                    'data': {},
                }
            all_candidates[key]['hunts'].add(hunt_type)
            all_candidates[key]['data'][hunt_type] = r

    overlap = []
    for key, info in all_candidates.items():
        if len(info['hunts']) >= 2:
            hunt_list = sorted(info['hunts'])
            row = {
                'field': info['field'],
                'ID': info['ID'],
                'z_peak': info['z_peak'],
                'Prob_gt_6': info['Prob_gt_6'],
                'bin_z': info['bin_z'],
                'num_hunts': len(info['hunts']),
                'hunt_types': '+'.join(hunt_list),
                'in_brightness': 1 if 'brightness' in info['hunts'] else 0,
                'in_redness': 1 if 'redness' in info['hunts'] else 0,
                'in_compactness': 1 if 'compactness' in info['hunts'] else 0,
            }

            bd = info['data']
            if 'brightness' in bd:
                row['F444W_flux'] = bd['brightness'].get('F444W_flux', '')
                row['F444W_SNR'] = bd['brightness'].get('F444W_SNR', '')
                row['bright_rank'] = bd['brightness'].get('rank_in_bin', '')
            else:
                row['F444W_flux'] = ''
                row['F444W_SNR'] = ''
                row['bright_rank'] = ''

            if 'redness' in bd:
                row['red_1'] = bd['redness'].get('red_1', '')
                row['red_2'] = bd['redness'].get('red_2', '')
                row['red_rank'] = bd['redness'].get('rank_in_bin', '')
            else:
                row['red_1'] = ''
                row['red_2'] = ''
                row['red_rank'] = ''

            if 'compactness' in bd:
                row['FWHM_arcsec'] = bd['compactness'].get('FWHM_arcsec', '')
                row['compact_proxy'] = bd['compactness'].get('compact_proxy', '')
                row['compact_rank'] = bd['compactness'].get('rank_in_bin', '')
            else:
                row['FWHM_arcsec'] = ''
                row['compact_proxy'] = ''
                row['compact_rank'] = ''

            overlap.append(row)

    overlap.sort(key=lambda r: (-r['num_hunts'], r['bin_z'], r['z_peak']))
    return overlap


def print_top10(candidates, hunt_name):
    print(f"\n  === Top 10 {hunt_name} candidates ===")
    seen = set()
    count = 0
    for r in candidates:
        key = (r['field'], r['ID'])
        if key in seen:
            continue
        seen.add(key)
        count += 1
        if count > 10:
            break

        extras = []
        if hunt_name == 'brightness':
            extras = [f"F444W={r['F444W_flux']}", f"SNR={r['F444W_SNR']}"]
        elif hunt_name == 'redness':
            if r.get('red_1'):
                extras.append(f"red_1={r['red_1']}")
            if r.get('red_2'):
                extras.append(f"red_2={r['red_2']}")
        elif hunt_name == 'compactness':
            extras = [f"FWHM={r['FWHM_arcsec']}\"", f"proxy={r.get('compact_proxy','')}"]

        extra_str = ', '.join(extras)
        print(f"    {count:>2}. {r['field']} ID={r['ID']:>8} z={r['z_peak']:>6} bin={r['bin_z']} P6={r['Prob_gt_6'][:5]} | {extra_str}")


def main():
    print("="*60)
    print("  Phase 4: First Anomaly Hunt")
    print(f"  {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("="*60)

    features = load_features()
    ready = build_hunt_ready(features)
    save_csv(ready, 'data/research/sample_hunt_ready_v1.csv')

    print(f"\n  Hunt-ready sources: {len(ready):,} / {len(features):,}")
    bins = ['6-8', '8-10', '10-15']
    for bz in bins:
        n = sum(1 for r in ready if r['bin_z'] == bz)
        print(f"    bin {bz}: {n:,}")

    all_bright = []
    all_red = []
    all_compact = []

    for bz in bins:
        print(f"\n  --- Hunting in bin {bz} ---")

        bright = hunt_brightness(ready, bz)
        print(f"    Brightness: {len(bright):,} candidates")
        all_bright.extend(bright)

        red = hunt_redness(ready, bz)
        print(f"    Redness: {len(red):,} candidates")
        all_red.extend(red)

        compact = hunt_compactness(ready, bz)
        print(f"    Compactness: {len(compact):,} candidates")
        all_compact.extend(compact)

    save_csv(all_bright, 'data/research/bright_outliers_v1.csv')
    save_csv(all_red, 'data/research/red_outliers_v1.csv')
    save_csv(all_compact, 'data/research/compact_outliers_v1.csv')

    overlap = build_overlap(all_bright, all_red, all_compact)
    save_csv(overlap, 'data/research/overlap_candidates_v1.csv')

    print(f"\n{'='*60}")
    print(f"  PHASE 4 RESULTS")
    print(f"{'='*60}")

    print(f"\n  Candidate counts:")
    print(f"    Brightness outliers: {len(all_bright):,}")
    print(f"    Redness outliers:    {len(all_red):,}")
    print(f"    Compactness outliers: {len(all_compact):,}")
    print(f"    Overlap (2+ hunts):  {len(overlap):,}")

    if overlap:
        triple = [r for r in overlap if r['num_hunts'] == 3]
        double = [r for r in overlap if r['num_hunts'] == 2]
        print(f"      Triple overlap (all 3): {len(triple):,}")
        print(f"      Double overlap (2 of 3): {len(double):,}")

        print(f"\n  Overlap by bin:")
        for bz in bins:
            n = sum(1 for r in overlap if r['bin_z'] == bz)
            nt = sum(1 for r in overlap if r['bin_z'] == bz and r['num_hunts'] == 3)
            print(f"    bin {bz}: {n:,} overlap ({nt} triple)")

    print_top10(all_bright, 'brightness')
    print_top10(all_red, 'redness')
    print_top10(all_compact, 'compactness')

    if overlap:
        print(f"\n  === Top overlap candidates (2+ hunts) ===")
        for i, r in enumerate(overlap[:15], 1):
            print(f"    {i:>2}. {r['field']} ID={r['ID']:>8} z={r['z_peak']:>6} bin={r['bin_z']} | {r['hunt_types']} ({r['num_hunts']} hunts)")

    print(f"\n  Field distribution of overlap candidates:")
    if overlap:
        gs = sum(1 for r in overlap if r['field'] == 'GOODS-S')
        gn = sum(1 for r in overlap if r['field'] == 'GOODS-N')
        print(f"    GOODS-S: {gs:,}")
        print(f"    GOODS-N: {gn:,}")
        if gs > 0 and gn > 0:
            ratio = gs / gn
            expected_ratio = 5258 / 2696
            print(f"    Ratio S/N: {ratio:.2f} (expected from sample size: {expected_ratio:.2f})")
            if abs(ratio - expected_ratio) / expected_ratio > 0.3:
                print(f"    >>> NOTE: Distribution differs from expected — may need investigation")
            else:
                print(f"    >>> Distribution roughly proportional to sample size — no clustering signal")

    print(f"\n  Phase 4 complete.")
    print(f"  REMINDER: These are CANDIDATES only. No claims of anomaly until:")
    print(f"    - Image inspection")
    print(f"    - Error analysis")
    print(f"    - Detection limit check")
    print(f"    - Artifact exclusion")


if __name__ == '__main__':
    main()
