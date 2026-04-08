# JADES DR5 Catalog Schema Report

**Generated:** 2026-04-08 14:24 UTC
**Method:** HTTP range requests (header-only, no full file download)

---

## GOODS-S

**File size:** 6,174,754,560 bytes (6.175 GB)
**URL:** `https://slate.ucsc.edu/~brant/jades-dr5/GOODS-S/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-s_photometry_v5.0_catalog.fits`
**Total extensions:** 13

### Extension Summary

| Ext | Name                 |       Rows |  Cols |    Data Size |
|  ---|----------------------|------------|-------|--------------|
|   0 | PRIMARY              |          0 |     0 |       0.0 MB |
|   1 | FILTERS              |         35 |    12 |       0.0 MB |
|   2 | FLAG                 |    304,366 |   108 |     259.3 MB |
|   3 | SIZE                 |    304,366 |    18 |      42.6 MB |
|   4 | CIRC                 |    304,366 |   570 |     696.4 MB |
|   5 | CIRC_BSUB            |    304,366 |   759 |    1156.6 MB |
|   6 | CIRC_CONV            |    304,366 |   570 |     696.4 MB |
|   7 | CIRC_BSUB_CONV       |    304,366 |   759 |    1156.6 MB |
|   8 | KRON                 |    304,366 |   225 |     546.6 MB |
|   9 | KRON_CONV            |    304,366 |   225 |     546.6 MB |
|  10 | MIRI                 |    304,366 |   465 |     722.0 MB |
|  11 | PHOTOZ               |    304,366 |    34 |     175.3 MB |
|  12 | PHOTOZ_KRON          |    304,366 |    34 |     175.3 MB |

### GOODS-S — FLAG (304,366 rows, 108 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | K            | int64                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | F070W_FLAG                     | D            | float64              | pix        |
|   5 | F070W_WHT                      | D            | float64              | (MJy       |
|   6 | F070W_TEXP                     | D            | float64              | s          |
|   7 | F090W_FLAG                     | D            | float64              | pix        |
|   8 | F090W_WHT                      | D            | float64              | (MJy       |
|   9 | F090W_TEXP                     | D            | float64              | s          |
|  10 | F115W_FLAG                     | D            | float64              | pix        |
|  11 | F115W_WHT                      | D            | float64              | (MJy       |
|  12 | F115W_TEXP                     | D            | float64              | s          |
|  13 | F150W_FLAG                     | D            | float64              | pix        |
|  14 | F150W_WHT                      | D            | float64              | (MJy       |
|  15 | F150W_TEXP                     | D            | float64              | s          |
|  16 | F162M_FLAG                     | D            | float64              | pix        |
|  17 | F162M_WHT                      | D            | float64              | (MJy       |
|  18 | F162M_TEXP                     | D            | float64              | s          |
|  19 | F182M_FLAG                     | D            | float64              | pix        |
|  20 | F182M_WHT                      | D            | float64              | (MJy       |
|  21 | F182M_TEXP                     | D            | float64              | s          |
|  22 | F200W_FLAG                     | D            | float64              | pix        |
|  23 | F200W_WHT                      | D            | float64              | (MJy       |
|  24 | F200W_TEXP                     | D            | float64              | s          |
|  25 | F210M_FLAG                     | D            | float64              | pix        |
|  26 | F210M_WHT                      | D            | float64              | (MJy       |
|  27 | F210M_TEXP                     | D            | float64              | s          |
|  28 | F250M_FLAG                     | D            | float64              | pix        |
|  29 | F250M_WHT                      | D            | float64              | (MJy       |
|  30 | F250M_TEXP                     | D            | float64              | s          |
|  31 | F277W_FLAG                     | D            | float64              | pix        |
|  32 | F277W_WHT                      | D            | float64              | (MJy       |
|  33 | F277W_TEXP                     | D            | float64              | s          |
|  34 | F300M_FLAG                     | D            | float64              | pix        |
|  35 | F300M_WHT                      | D            | float64              | (MJy       |
|  36 | F300M_TEXP                     | D            | float64              | s          |
|  37 | F335M_FLAG                     | D            | float64              | pix        |
|  38 | F335M_WHT                      | D            | float64              | (MJy       |
|  39 | F335M_TEXP                     | D            | float64              | s          |
|  40 | F356W_FLAG                     | D            | float64              | pix        |
|  41 | F356W_WHT                      | D            | float64              | (MJy       |
|  42 | F356W_TEXP                     | D            | float64              | s          |
|  43 | F410M_FLAG                     | D            | float64              | pix        |
|  44 | F410M_WHT                      | D            | float64              | (MJy       |
|  45 | F410M_TEXP                     | D            | float64              | s          |
|  46 | F430M_FLAG                     | D            | float64              | pix        |
|  47 | F430M_WHT                      | D            | float64              | (MJy       |
|  48 | F430M_TEXP                     | D            | float64              | s          |
|  49 | F444W_FLAG                     | D            | float64              | pix        |
|  50 | F444W_WHT                      | D            | float64              | (MJy       |
|  51 | F444W_TEXP                     | D            | float64              | s          |
|  52 | F460M_FLAG                     | D            | float64              | pix        |
|  53 | F460M_WHT                      | D            | float64              | (MJy       |
|  54 | F460M_TEXP                     | D            | float64              | s          |
|  55 | F480M_FLAG                     | D            | float64              | pix        |
|  56 | F480M_WHT                      | D            | float64              | (MJy       |
|  57 | F480M_TEXP                     | D            | float64              | s          |
|  58 | F435W_FLAG                     | D            | float64              | pix        |
|  59 | F435W_WHT                      | D            | float64              | (MJy       |
|  60 | F435W_TEXP                     | D            | float64              | s          |
|  61 | F606W_FLAG                     | D            | float64              | pix        |
|  62 | F606W_WHT                      | D            | float64              | (MJy       |
|  63 | F606W_TEXP                     | D            | float64              | s          |
|  64 | F775W_FLAG                     | D            | float64              | pix        |
|  65 | F775W_WHT                      | D            | float64              | (MJy       |
|  66 | F775W_TEXP                     | D            | float64              | s          |
|  67 | F814W_FLAG                     | D            | float64              | pix        |
|  68 | F814W_WHT                      | D            | float64              | (MJy       |
|  69 | F814W_TEXP                     | D            | float64              | s          |
|  70 | F850LP_FLAG                    | D            | float64              | pix        |
|  71 | F850LP_WHT                     | D            | float64              | (MJy       |
|  72 | F850LP_TEXP                    | D            | float64              | s          |
|  73 | F105W_FLAG                     | D            | float64              | pix        |
|  74 | F105W_WHT                      | D            | float64              | (MJy       |
|  75 | F105W_TEXP                     | D            | float64              | s          |
|  76 | F125W_FLAG                     | D            | float64              | pix        |
|  77 | F125W_WHT                      | D            | float64              | (MJy       |
|  78 | F125W_TEXP                     | D            | float64              | s          |
|  79 | F140W_FLAG                     | D            | float64              | pix        |
|  80 | F140W_WHT                      | D            | float64              | (MJy       |
|  81 | F140W_TEXP                     | D            | float64              | s          |
|  82 | F160W_FLAG                     | D            | float64              | pix        |
|  83 | F160W_WHT                      | D            | float64              | (MJy       |
|  84 | F160W_TEXP                     | D            | float64              | s          |
|  85 | F560W_FLAG                     | D            | float64              | pix        |
|  86 | F560W_WHT                      | D            | float64              | (MJy       |
|  87 | F560W_TEXP                     | D            | float64              | s          |
|  88 | F770W_FLAG                     | D            | float64              | pix        |
|  89 | F770W_WHT                      | D            | float64              | (MJy       |
|  90 | F770W_TEXP                     | D            | float64              | s          |
|  91 | F1280W_FLAG                    | D            | float64              | pix        |
|  92 | F1280W_WHT                     | D            | float64              | (MJy       |
|  93 | F1280W_TEXP                    | D            | float64              | s          |
|  94 | F1500W_FLAG                    | D            | float64              | pix        |
|  95 | F1500W_WHT                     | D            | float64              | (MJy       |
|  96 | F1500W_TEXP                    | D            | float64              | s          |
|  97 | F1800W_FLAG                    | D            | float64              | pix        |
|  98 | F1800W_WHT                     | D            | float64              | (MJy       |
|  99 | F1800W_TEXP                    | D            | float64              | s          |
| 100 | F2100W_FLAG                    | D            | float64              | pix        |
| 101 | F2100W_WHT                     | D            | float64              | (MJy       |
| 102 | F2100W_TEXP                    | D            | float64              | s          |
| 103 | F2550W_FLAG                    | D            | float64              | pix        |
| 104 | F2550W_WHT                     | D            | float64              | (MJy       |
| 105 | F2550W_TEXP                    | D            | float64              | s          |
| 106 | FLAG_BN                        | J            | int32                |            |
| 107 | PARENT_ID                      | J            | int32                |            |
| 108 | PID_HASH                       | J            | int32                |            |

### GOODS-S — SIZE (304,366 rows, 18 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | J            | int32                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | X                              | D            | float64              | pix        |
|   5 | Y                              | D            | float64              | pix        |
|   6 | XC                             | D            | float64              | pix        |
|   7 | YC                             | D            | float64              | pix        |
|   8 | BBOX_XMIN                      | K            | int64                | pix        |
|   9 | BBOX_XMAX                      | K            | int64                | pix        |
|  10 | BBOX_YMIN                      | K            | int64                | pix        |
|  11 | BBOX_YMAX                      | K            | int64                | pix        |
|  12 | NPIX_DET                       | D            | float64              |            |
|  13 | A                              | D            | float64              | arcsec     |
|  14 | B                              | D            | float64              | arcsec     |
|  15 | THETA                          | D            | float64              | deg        |
|  16 | R_KRON_U                       | D            | float64              | nJy        |
|  17 | FWHM                           | D            | float64              | arcsec     |
|  18 | GINI                           | D            | float64              |            |

### GOODS-S — KRON (304,366 rows, 225 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | J            | int32                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | A_KRON                         | D            | float64              | arcsec     |
|   5 | B_KRON                         | D            | float64              | arcsec     |
|   6 | THETA_KRON                     | D            | float64              | deg        |
|   7 | F070W_KRON                     | D            | float64              | nJy        |
|   8 | F070W_KRON_e                   | D            | float64              | nJy        |
|   9 | F070W_KRON_ei                  | D            | float64              | nJy        |
|  10 | F070W_KRON_bkg                 | D            | float64              | nJy        |
|  11 | A_KRON_S                       | D            | float64              | arcsec     |
|  12 | B_KRON_S                       | D            | float64              | arcsec     |
|  13 | THETA_KRON_S                   | D            | float64              | deg        |
|  14 | F070W_KRON_S                   | D            | float64              | nJy        |
|  15 | F070W_KRON_S_e                 | D            | float64              | nJy        |
|  16 | F070W_KRON_S_ei                | D            | float64              | nJy        |
|  17 | F070W_KRON_S_bkg               | D            | float64              | nJy        |
|  18 | F090W_KRON                     | D            | float64              | nJy        |
|  19 | F090W_KRON_e                   | D            | float64              | nJy        |
|  20 | F090W_KRON_ei                  | D            | float64              | nJy        |
|  21 | F090W_KRON_bkg                 | D            | float64              | nJy        |
|  22 | F090W_KRON_S                   | D            | float64              | nJy        |
|  23 | F090W_KRON_S_e                 | D            | float64              | nJy        |
|  24 | F090W_KRON_S_ei                | D            | float64              | nJy        |
|  25 | F090W_KRON_S_bkg               | D            | float64              | nJy        |
|  26 | F105W_KRON                     | D            | float64              | nJy        |
|  27 | F105W_KRON_e                   | D            | float64              | nJy        |
|  28 | F105W_KRON_ei                  | D            | float64              | nJy        |
|  29 | F105W_KRON_bkg                 | D            | float64              | nJy        |
|  30 | F105W_KRON_S                   | D            | float64              | nJy        |
|  31 | F105W_KRON_S_e                 | D            | float64              | nJy        |
|  32 | F105W_KRON_S_ei                | D            | float64              | nJy        |
|  33 | F105W_KRON_S_bkg               | D            | float64              | nJy        |
|  34 | F115W_KRON                     | D            | float64              | nJy        |
|  35 | F115W_KRON_e                   | D            | float64              | nJy        |
|  36 | F115W_KRON_ei                  | D            | float64              | nJy        |
|  37 | F115W_KRON_bkg                 | D            | float64              | nJy        |
|  38 | F115W_KRON_S                   | D            | float64              | nJy        |
|  39 | F115W_KRON_S_e                 | D            | float64              | nJy        |
|  40 | F115W_KRON_S_ei                | D            | float64              | nJy        |
|  41 | F115W_KRON_S_bkg               | D            | float64              | nJy        |
|  42 | F125W_KRON                     | D            | float64              | nJy        |
|  43 | F125W_KRON_e                   | D            | float64              | nJy        |
|  44 | F125W_KRON_ei                  | D            | float64              | nJy        |
|  45 | F125W_KRON_bkg                 | D            | float64              | nJy        |
|  46 | F125W_KRON_S                   | D            | float64              | nJy        |
|  47 | F125W_KRON_S_e                 | D            | float64              | nJy        |
|  48 | F125W_KRON_S_ei                | D            | float64              | nJy        |
|  49 | F125W_KRON_S_bkg               | D            | float64              | nJy        |
|  50 | F140W_KRON                     | D            | float64              | nJy        |
|  51 | F140W_KRON_e                   | D            | float64              | nJy        |
|  52 | F140W_KRON_ei                  | D            | float64              | nJy        |
|  53 | F140W_KRON_bkg                 | D            | float64              | nJy        |
|  54 | F140W_KRON_S                   | D            | float64              | nJy        |
|  55 | F140W_KRON_S_e                 | D            | float64              | nJy        |
|  56 | F140W_KRON_S_ei                | D            | float64              | nJy        |
|  57 | F140W_KRON_S_bkg               | D            | float64              | nJy        |
|  58 | F150W_KRON                     | D            | float64              | nJy        |
|  59 | F150W_KRON_e                   | D            | float64              | nJy        |
|  60 | F150W_KRON_ei                  | D            | float64              | nJy        |
|  61 | F150W_KRON_bkg                 | D            | float64              | nJy        |
|  62 | F150W_KRON_S                   | D            | float64              | nJy        |
|  63 | F150W_KRON_S_e                 | D            | float64              | nJy        |
|  64 | F150W_KRON_S_ei                | D            | float64              | nJy        |
|  65 | F150W_KRON_S_bkg               | D            | float64              | nJy        |
|  66 | F160W_KRON                     | D            | float64              | nJy        |
|  67 | F160W_KRON_e                   | D            | float64              | nJy        |
|  68 | F160W_KRON_ei                  | D            | float64              | nJy        |
|  69 | F160W_KRON_bkg                 | D            | float64              | nJy        |
|  70 | F160W_KRON_S                   | D            | float64              | nJy        |
|  71 | F160W_KRON_S_e                 | D            | float64              | nJy        |
|  72 | F160W_KRON_S_ei                | D            | float64              | nJy        |
|  73 | F160W_KRON_S_bkg               | D            | float64              | nJy        |
|  74 | F162M_KRON                     | D            | float64              | nJy        |
|  75 | F162M_KRON_e                   | D            | float64              | nJy        |
|  76 | F162M_KRON_ei                  | D            | float64              | nJy        |
|  77 | F162M_KRON_bkg                 | D            | float64              | nJy        |
|  78 | F162M_KRON_S                   | D            | float64              | nJy        |
|  79 | F162M_KRON_S_e                 | D            | float64              | nJy        |
|  80 | F162M_KRON_S_ei                | D            | float64              | nJy        |
|  81 | F162M_KRON_S_bkg               | D            | float64              | nJy        |
|  82 | F182M_KRON                     | D            | float64              | nJy        |
|  83 | F182M_KRON_e                   | D            | float64              | nJy        |
|  84 | F182M_KRON_ei                  | D            | float64              | nJy        |
|  85 | F182M_KRON_bkg                 | D            | float64              | nJy        |
|  86 | F182M_KRON_S                   | D            | float64              | nJy        |
|  87 | F182M_KRON_S_e                 | D            | float64              | nJy        |
|  88 | F182M_KRON_S_ei                | D            | float64              | nJy        |
|  89 | F182M_KRON_S_bkg               | D            | float64              | nJy        |
|  90 | F200W_KRON                     | D            | float64              | nJy        |
|  91 | F200W_KRON_e                   | D            | float64              | nJy        |
|  92 | F200W_KRON_ei                  | D            | float64              | nJy        |
|  93 | F200W_KRON_bkg                 | D            | float64              | nJy        |
|  94 | F200W_KRON_S                   | D            | float64              | nJy        |
|  95 | F200W_KRON_S_e                 | D            | float64              | nJy        |
|  96 | F200W_KRON_S_ei                | D            | float64              | nJy        |
|  97 | F200W_KRON_S_bkg               | D            | float64              | nJy        |
|  98 | F210M_KRON                     | D            | float64              | nJy        |
|  99 | F210M_KRON_e                   | D            | float64              | nJy        |
| 100 | F210M_KRON_ei                  | D            | float64              | nJy        |
| 101 | F210M_KRON_bkg                 | D            | float64              | nJy        |
| 102 | F210M_KRON_S                   | D            | float64              | nJy        |
| 103 | F210M_KRON_S_e                 | D            | float64              | nJy        |
| 104 | F210M_KRON_S_ei                | D            | float64              | nJy        |
| 105 | F210M_KRON_S_bkg               | D            | float64              | nJy        |
| 106 | F250M_KRON                     | D            | float64              | nJy        |
| 107 | F250M_KRON_e                   | D            | float64              | nJy        |
| 108 | F250M_KRON_ei                  | D            | float64              | nJy        |
| 109 | F250M_KRON_bkg                 | D            | float64              | nJy        |
| 110 | F250M_KRON_S                   | D            | float64              | nJy        |
| 111 | F250M_KRON_S_e                 | D            | float64              | nJy        |
| 112 | F250M_KRON_S_ei                | D            | float64              | nJy        |
| 113 | F250M_KRON_S_bkg               | D            | float64              | nJy        |
| 114 | F277W_KRON                     | D            | float64              | nJy        |
| 115 | F277W_KRON_e                   | D            | float64              | nJy        |
| 116 | F277W_KRON_ei                  | D            | float64              | nJy        |
| 117 | F277W_KRON_bkg                 | D            | float64              | nJy        |
| 118 | F277W_KRON_S                   | D            | float64              | nJy        |
| 119 | F277W_KRON_S_e                 | D            | float64              | nJy        |
| 120 | F277W_KRON_S_ei                | D            | float64              | nJy        |
| 121 | F277W_KRON_S_bkg               | D            | float64              | nJy        |
| 122 | F300M_KRON                     | D            | float64              | nJy        |
| 123 | F300M_KRON_e                   | D            | float64              | nJy        |
| 124 | F300M_KRON_ei                  | D            | float64              | nJy        |
| 125 | F300M_KRON_bkg                 | D            | float64              | nJy        |
| 126 | F300M_KRON_S                   | D            | float64              | nJy        |
| 127 | F300M_KRON_S_e                 | D            | float64              | nJy        |
| 128 | F300M_KRON_S_ei                | D            | float64              | nJy        |
| 129 | F300M_KRON_S_bkg               | D            | float64              | nJy        |
| 130 | F335M_KRON                     | D            | float64              | nJy        |
| 131 | F335M_KRON_e                   | D            | float64              | nJy        |
| 132 | F335M_KRON_ei                  | D            | float64              | nJy        |
| 133 | F335M_KRON_bkg                 | D            | float64              | nJy        |
| 134 | F335M_KRON_S                   | D            | float64              | nJy        |
| 135 | F335M_KRON_S_e                 | D            | float64              | nJy        |
| 136 | F335M_KRON_S_ei                | D            | float64              | nJy        |
| 137 | F335M_KRON_S_bkg               | D            | float64              | nJy        |
| 138 | F356W_KRON                     | D            | float64              | nJy        |
| 139 | F356W_KRON_e                   | D            | float64              | nJy        |
| 140 | F356W_KRON_ei                  | D            | float64              | nJy        |
| 141 | F356W_KRON_bkg                 | D            | float64              | nJy        |
| 142 | F356W_KRON_S                   | D            | float64              | nJy        |
| 143 | F356W_KRON_S_e                 | D            | float64              | nJy        |
| 144 | F356W_KRON_S_ei                | D            | float64              | nJy        |
| 145 | F356W_KRON_S_bkg               | D            | float64              | nJy        |
| 146 | F410M_KRON                     | D            | float64              | nJy        |
| 147 | F410M_KRON_e                   | D            | float64              | nJy        |
| 148 | F410M_KRON_ei                  | D            | float64              | nJy        |
| 149 | F410M_KRON_bkg                 | D            | float64              | nJy        |
| 150 | F410M_KRON_S                   | D            | float64              | nJy        |
| 151 | F410M_KRON_S_e                 | D            | float64              | nJy        |
| 152 | F410M_KRON_S_ei                | D            | float64              | nJy        |
| 153 | F410M_KRON_S_bkg               | D            | float64              | nJy        |
| 154 | F430M_KRON                     | D            | float64              | nJy        |
| 155 | F430M_KRON_e                   | D            | float64              | nJy        |
| 156 | F430M_KRON_ei                  | D            | float64              | nJy        |
| 157 | F430M_KRON_bkg                 | D            | float64              | nJy        |
| 158 | F430M_KRON_S                   | D            | float64              | nJy        |
| 159 | F430M_KRON_S_e                 | D            | float64              | nJy        |
| 160 | F430M_KRON_S_ei                | D            | float64              | nJy        |
| 161 | F430M_KRON_S_bkg               | D            | float64              | nJy        |
| 162 | F435W_KRON                     | D            | float64              | nJy        |
| 163 | F435W_KRON_e                   | D            | float64              | nJy        |
| 164 | F435W_KRON_ei                  | D            | float64              | nJy        |
| 165 | F435W_KRON_bkg                 | D            | float64              | nJy        |
| 166 | F435W_KRON_S                   | D            | float64              | nJy        |
| 167 | F435W_KRON_S_e                 | D            | float64              | nJy        |
| 168 | F435W_KRON_S_ei                | D            | float64              | nJy        |
| 169 | F435W_KRON_S_bkg               | D            | float64              | nJy        |
| 170 | F444W_KRON                     | D            | float64              | nJy        |
| 171 | F444W_KRON_e                   | D            | float64              | nJy        |
| 172 | F444W_KRON_ei                  | D            | float64              | nJy        |
| 173 | F444W_KRON_bkg                 | D            | float64              | nJy        |
| 174 | F444W_KRON_S                   | D            | float64              | nJy        |
| 175 | F444W_KRON_S_e                 | D            | float64              | nJy        |
| 176 | F444W_KRON_S_ei                | D            | float64              | nJy        |
| 177 | F444W_KRON_S_bkg               | D            | float64              | nJy        |
| 178 | F460M_KRON                     | D            | float64              | nJy        |
| 179 | F460M_KRON_e                   | D            | float64              | nJy        |
| 180 | F460M_KRON_ei                  | D            | float64              | nJy        |
| 181 | F460M_KRON_bkg                 | D            | float64              | nJy        |
| 182 | F460M_KRON_S                   | D            | float64              | nJy        |
| 183 | F460M_KRON_S_e                 | D            | float64              | nJy        |
| 184 | F460M_KRON_S_ei                | D            | float64              | nJy        |
| 185 | F460M_KRON_S_bkg               | D            | float64              | nJy        |
| 186 | F480M_KRON                     | D            | float64              | nJy        |
| 187 | F480M_KRON_e                   | D            | float64              | nJy        |
| 188 | F480M_KRON_ei                  | D            | float64              | nJy        |
| 189 | F480M_KRON_bkg                 | D            | float64              | nJy        |
| 190 | F480M_KRON_S                   | D            | float64              | nJy        |
| 191 | F480M_KRON_S_e                 | D            | float64              | nJy        |
| 192 | F480M_KRON_S_ei                | D            | float64              | nJy        |
| 193 | F480M_KRON_S_bkg               | D            | float64              | nJy        |
| 194 | F606W_KRON                     | D            | float64              | nJy        |
| 195 | F606W_KRON_e                   | D            | float64              | nJy        |
| 196 | F606W_KRON_ei                  | D            | float64              | nJy        |
| 197 | F606W_KRON_bkg                 | D            | float64              | nJy        |
| 198 | F606W_KRON_S                   | D            | float64              | nJy        |
| 199 | F606W_KRON_S_e                 | D            | float64              | nJy        |
| 200 | F606W_KRON_S_ei                | D            | float64              | nJy        |
| 201 | F606W_KRON_S_bkg               | D            | float64              | nJy        |
| 202 | F775W_KRON                     | D            | float64              | nJy        |
| 203 | F775W_KRON_e                   | D            | float64              | nJy        |
| 204 | F775W_KRON_ei                  | D            | float64              | nJy        |
| 205 | F775W_KRON_bkg                 | D            | float64              | nJy        |
| 206 | F775W_KRON_S                   | D            | float64              | nJy        |
| 207 | F775W_KRON_S_e                 | D            | float64              | nJy        |
| 208 | F775W_KRON_S_ei                | D            | float64              | nJy        |
| 209 | F775W_KRON_S_bkg               | D            | float64              | nJy        |
| 210 | F814W_KRON                     | D            | float64              | nJy        |
| 211 | F814W_KRON_e                   | D            | float64              | nJy        |
| 212 | F814W_KRON_ei                  | D            | float64              | nJy        |
| 213 | F814W_KRON_bkg                 | D            | float64              | nJy        |
| 214 | F814W_KRON_S                   | D            | float64              | nJy        |
| 215 | F814W_KRON_S_e                 | D            | float64              | nJy        |
| 216 | F814W_KRON_S_ei                | D            | float64              | nJy        |
| 217 | F814W_KRON_S_bkg               | D            | float64              | nJy        |
| 218 | F850LP_KRON                    | D            | float64              | nJy        |
| 219 | F850LP_KRON_e                  | D            | float64              | nJy        |
| 220 | F850LP_KRON_ei                 | D            | float64              | nJy        |
| 221 | F850LP_KRON_bkg                | D            | float64              | nJy        |
| 222 | F850LP_KRON_S                  | D            | float64              | nJy        |
| 223 | F850LP_KRON_S_e                | D            | float64              | nJy        |
| 224 | F850LP_KRON_S_ei               | D            | float64              | nJy        |
| 225 | F850LP_KRON_S_bkg              | D            | float64              | nJy        |

### GOODS-S — KRON_CONV (304,366 rows, 225 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | J            | int32                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | A_KRON                         | D            | float64              | arcsec     |
|   5 | B_KRON                         | D            | float64              | arcsec     |
|   6 | THETA_KRON                     | D            | float64              | deg        |
|   7 | F070W_KRON                     | D            | float64              | nJy        |
|   8 | F070W_KRON_e                   | D            | float64              | nJy        |
|   9 | F070W_KRON_ei                  | D            | float64              | nJy        |
|  10 | F070W_KRON_bkg                 | D            | float64              | nJy        |
|  11 | A_KRON_S                       | D            | float64              | arcsec     |
|  12 | B_KRON_S                       | D            | float64              | arcsec     |
|  13 | THETA_KRON_S                   | D            | float64              | deg        |
|  14 | F070W_KRON_S                   | D            | float64              | nJy        |
|  15 | F070W_KRON_S_e                 | D            | float64              | nJy        |
|  16 | F070W_KRON_S_ei                | D            | float64              | nJy        |
|  17 | F070W_KRON_S_bkg               | D            | float64              | nJy        |
|  18 | F090W_KRON                     | D            | float64              | nJy        |
|  19 | F090W_KRON_e                   | D            | float64              | nJy        |
|  20 | F090W_KRON_ei                  | D            | float64              | nJy        |
|  21 | F090W_KRON_bkg                 | D            | float64              | nJy        |
|  22 | F090W_KRON_S                   | D            | float64              | nJy        |
|  23 | F090W_KRON_S_e                 | D            | float64              | nJy        |
|  24 | F090W_KRON_S_ei                | D            | float64              | nJy        |
|  25 | F090W_KRON_S_bkg               | D            | float64              | nJy        |
|  26 | F105W_KRON                     | D            | float64              | nJy        |
|  27 | F105W_KRON_e                   | D            | float64              | nJy        |
|  28 | F105W_KRON_ei                  | D            | float64              | nJy        |
|  29 | F105W_KRON_bkg                 | D            | float64              | nJy        |
|  30 | F105W_KRON_S                   | D            | float64              | nJy        |
|  31 | F105W_KRON_S_e                 | D            | float64              | nJy        |
|  32 | F105W_KRON_S_ei                | D            | float64              | nJy        |
|  33 | F105W_KRON_S_bkg               | D            | float64              | nJy        |
|  34 | F115W_KRON                     | D            | float64              | nJy        |
|  35 | F115W_KRON_e                   | D            | float64              | nJy        |
|  36 | F115W_KRON_ei                  | D            | float64              | nJy        |
|  37 | F115W_KRON_bkg                 | D            | float64              | nJy        |
|  38 | F115W_KRON_S                   | D            | float64              | nJy        |
|  39 | F115W_KRON_S_e                 | D            | float64              | nJy        |
|  40 | F115W_KRON_S_ei                | D            | float64              | nJy        |
|  41 | F115W_KRON_S_bkg               | D            | float64              | nJy        |
|  42 | F125W_KRON                     | D            | float64              | nJy        |
|  43 | F125W_KRON_e                   | D            | float64              | nJy        |
|  44 | F125W_KRON_ei                  | D            | float64              | nJy        |
|  45 | F125W_KRON_bkg                 | D            | float64              | nJy        |
|  46 | F125W_KRON_S                   | D            | float64              | nJy        |
|  47 | F125W_KRON_S_e                 | D            | float64              | nJy        |
|  48 | F125W_KRON_S_ei                | D            | float64              | nJy        |
|  49 | F125W_KRON_S_bkg               | D            | float64              | nJy        |
|  50 | F140W_KRON                     | D            | float64              | nJy        |
|  51 | F140W_KRON_e                   | D            | float64              | nJy        |
|  52 | F140W_KRON_ei                  | D            | float64              | nJy        |
|  53 | F140W_KRON_bkg                 | D            | float64              | nJy        |
|  54 | F140W_KRON_S                   | D            | float64              | nJy        |
|  55 | F140W_KRON_S_e                 | D            | float64              | nJy        |
|  56 | F140W_KRON_S_ei                | D            | float64              | nJy        |
|  57 | F140W_KRON_S_bkg               | D            | float64              | nJy        |
|  58 | F150W_KRON                     | D            | float64              | nJy        |
|  59 | F150W_KRON_e                   | D            | float64              | nJy        |
|  60 | F150W_KRON_ei                  | D            | float64              | nJy        |
|  61 | F150W_KRON_bkg                 | D            | float64              | nJy        |
|  62 | F150W_KRON_S                   | D            | float64              | nJy        |
|  63 | F150W_KRON_S_e                 | D            | float64              | nJy        |
|  64 | F150W_KRON_S_ei                | D            | float64              | nJy        |
|  65 | F150W_KRON_S_bkg               | D            | float64              | nJy        |
|  66 | F160W_KRON                     | D            | float64              | nJy        |
|  67 | F160W_KRON_e                   | D            | float64              | nJy        |
|  68 | F160W_KRON_ei                  | D            | float64              | nJy        |
|  69 | F160W_KRON_bkg                 | D            | float64              | nJy        |
|  70 | F160W_KRON_S                   | D            | float64              | nJy        |
|  71 | F160W_KRON_S_e                 | D            | float64              | nJy        |
|  72 | F160W_KRON_S_ei                | D            | float64              | nJy        |
|  73 | F160W_KRON_S_bkg               | D            | float64              | nJy        |
|  74 | F162M_KRON                     | D            | float64              | nJy        |
|  75 | F162M_KRON_e                   | D            | float64              | nJy        |
|  76 | F162M_KRON_ei                  | D            | float64              | nJy        |
|  77 | F162M_KRON_bkg                 | D            | float64              | nJy        |
|  78 | F162M_KRON_S                   | D            | float64              | nJy        |
|  79 | F162M_KRON_S_e                 | D            | float64              | nJy        |
|  80 | F162M_KRON_S_ei                | D            | float64              | nJy        |
|  81 | F162M_KRON_S_bkg               | D            | float64              | nJy        |
|  82 | F182M_KRON                     | D            | float64              | nJy        |
|  83 | F182M_KRON_e                   | D            | float64              | nJy        |
|  84 | F182M_KRON_ei                  | D            | float64              | nJy        |
|  85 | F182M_KRON_bkg                 | D            | float64              | nJy        |
|  86 | F182M_KRON_S                   | D            | float64              | nJy        |
|  87 | F182M_KRON_S_e                 | D            | float64              | nJy        |
|  88 | F182M_KRON_S_ei                | D            | float64              | nJy        |
|  89 | F182M_KRON_S_bkg               | D            | float64              | nJy        |
|  90 | F200W_KRON                     | D            | float64              | nJy        |
|  91 | F200W_KRON_e                   | D            | float64              | nJy        |
|  92 | F200W_KRON_ei                  | D            | float64              | nJy        |
|  93 | F200W_KRON_bkg                 | D            | float64              | nJy        |
|  94 | F200W_KRON_S                   | D            | float64              | nJy        |
|  95 | F200W_KRON_S_e                 | D            | float64              | nJy        |
|  96 | F200W_KRON_S_ei                | D            | float64              | nJy        |
|  97 | F200W_KRON_S_bkg               | D            | float64              | nJy        |
|  98 | F210M_KRON                     | D            | float64              | nJy        |
|  99 | F210M_KRON_e                   | D            | float64              | nJy        |
| 100 | F210M_KRON_ei                  | D            | float64              | nJy        |
| 101 | F210M_KRON_bkg                 | D            | float64              | nJy        |
| 102 | F210M_KRON_S                   | D            | float64              | nJy        |
| 103 | F210M_KRON_S_e                 | D            | float64              | nJy        |
| 104 | F210M_KRON_S_ei                | D            | float64              | nJy        |
| 105 | F210M_KRON_S_bkg               | D            | float64              | nJy        |
| 106 | F250M_KRON                     | D            | float64              | nJy        |
| 107 | F250M_KRON_e                   | D            | float64              | nJy        |
| 108 | F250M_KRON_ei                  | D            | float64              | nJy        |
| 109 | F250M_KRON_bkg                 | D            | float64              | nJy        |
| 110 | F250M_KRON_S                   | D            | float64              | nJy        |
| 111 | F250M_KRON_S_e                 | D            | float64              | nJy        |
| 112 | F250M_KRON_S_ei                | D            | float64              | nJy        |
| 113 | F250M_KRON_S_bkg               | D            | float64              | nJy        |
| 114 | F277W_KRON                     | D            | float64              | nJy        |
| 115 | F277W_KRON_e                   | D            | float64              | nJy        |
| 116 | F277W_KRON_ei                  | D            | float64              | nJy        |
| 117 | F277W_KRON_bkg                 | D            | float64              | nJy        |
| 118 | F277W_KRON_S                   | D            | float64              | nJy        |
| 119 | F277W_KRON_S_e                 | D            | float64              | nJy        |
| 120 | F277W_KRON_S_ei                | D            | float64              | nJy        |
| 121 | F277W_KRON_S_bkg               | D            | float64              | nJy        |
| 122 | F300M_KRON                     | D            | float64              | nJy        |
| 123 | F300M_KRON_e                   | D            | float64              | nJy        |
| 124 | F300M_KRON_ei                  | D            | float64              | nJy        |
| 125 | F300M_KRON_bkg                 | D            | float64              | nJy        |
| 126 | F300M_KRON_S                   | D            | float64              | nJy        |
| 127 | F300M_KRON_S_e                 | D            | float64              | nJy        |
| 128 | F300M_KRON_S_ei                | D            | float64              | nJy        |
| 129 | F300M_KRON_S_bkg               | D            | float64              | nJy        |
| 130 | F335M_KRON                     | D            | float64              | nJy        |
| 131 | F335M_KRON_e                   | D            | float64              | nJy        |
| 132 | F335M_KRON_ei                  | D            | float64              | nJy        |
| 133 | F335M_KRON_bkg                 | D            | float64              | nJy        |
| 134 | F335M_KRON_S                   | D            | float64              | nJy        |
| 135 | F335M_KRON_S_e                 | D            | float64              | nJy        |
| 136 | F335M_KRON_S_ei                | D            | float64              | nJy        |
| 137 | F335M_KRON_S_bkg               | D            | float64              | nJy        |
| 138 | F356W_KRON                     | D            | float64              | nJy        |
| 139 | F356W_KRON_e                   | D            | float64              | nJy        |
| 140 | F356W_KRON_ei                  | D            | float64              | nJy        |
| 141 | F356W_KRON_bkg                 | D            | float64              | nJy        |
| 142 | F356W_KRON_S                   | D            | float64              | nJy        |
| 143 | F356W_KRON_S_e                 | D            | float64              | nJy        |
| 144 | F356W_KRON_S_ei                | D            | float64              | nJy        |
| 145 | F356W_KRON_S_bkg               | D            | float64              | nJy        |
| 146 | F410M_KRON                     | D            | float64              | nJy        |
| 147 | F410M_KRON_e                   | D            | float64              | nJy        |
| 148 | F410M_KRON_ei                  | D            | float64              | nJy        |
| 149 | F410M_KRON_bkg                 | D            | float64              | nJy        |
| 150 | F410M_KRON_S                   | D            | float64              | nJy        |
| 151 | F410M_KRON_S_e                 | D            | float64              | nJy        |
| 152 | F410M_KRON_S_ei                | D            | float64              | nJy        |
| 153 | F410M_KRON_S_bkg               | D            | float64              | nJy        |
| 154 | F430M_KRON                     | D            | float64              | nJy        |
| 155 | F430M_KRON_e                   | D            | float64              | nJy        |
| 156 | F430M_KRON_ei                  | D            | float64              | nJy        |
| 157 | F430M_KRON_bkg                 | D            | float64              | nJy        |
| 158 | F430M_KRON_S                   | D            | float64              | nJy        |
| 159 | F430M_KRON_S_e                 | D            | float64              | nJy        |
| 160 | F430M_KRON_S_ei                | D            | float64              | nJy        |
| 161 | F430M_KRON_S_bkg               | D            | float64              | nJy        |
| 162 | F435W_KRON                     | D            | float64              | nJy        |
| 163 | F435W_KRON_e                   | D            | float64              | nJy        |
| 164 | F435W_KRON_ei                  | D            | float64              | nJy        |
| 165 | F435W_KRON_bkg                 | D            | float64              | nJy        |
| 166 | F435W_KRON_S                   | D            | float64              | nJy        |
| 167 | F435W_KRON_S_e                 | D            | float64              | nJy        |
| 168 | F435W_KRON_S_ei                | D            | float64              | nJy        |
| 169 | F435W_KRON_S_bkg               | D            | float64              | nJy        |
| 170 | F444W_KRON                     | D            | float64              | nJy        |
| 171 | F444W_KRON_e                   | D            | float64              | nJy        |
| 172 | F444W_KRON_ei                  | D            | float64              | nJy        |
| 173 | F444W_KRON_bkg                 | D            | float64              | nJy        |
| 174 | F444W_KRON_S                   | D            | float64              | nJy        |
| 175 | F444W_KRON_S_e                 | D            | float64              | nJy        |
| 176 | F444W_KRON_S_ei                | D            | float64              | nJy        |
| 177 | F444W_KRON_S_bkg               | D            | float64              | nJy        |
| 178 | F460M_KRON                     | D            | float64              | nJy        |
| 179 | F460M_KRON_e                   | D            | float64              | nJy        |
| 180 | F460M_KRON_ei                  | D            | float64              | nJy        |
| 181 | F460M_KRON_bkg                 | D            | float64              | nJy        |
| 182 | F460M_KRON_S                   | D            | float64              | nJy        |
| 183 | F460M_KRON_S_e                 | D            | float64              | nJy        |
| 184 | F460M_KRON_S_ei                | D            | float64              | nJy        |
| 185 | F460M_KRON_S_bkg               | D            | float64              | nJy        |
| 186 | F480M_KRON                     | D            | float64              | nJy        |
| 187 | F480M_KRON_e                   | D            | float64              | nJy        |
| 188 | F480M_KRON_ei                  | D            | float64              | nJy        |
| 189 | F480M_KRON_bkg                 | D            | float64              | nJy        |
| 190 | F480M_KRON_S                   | D            | float64              | nJy        |
| 191 | F480M_KRON_S_e                 | D            | float64              | nJy        |
| 192 | F480M_KRON_S_ei                | D            | float64              | nJy        |
| 193 | F480M_KRON_S_bkg               | D            | float64              | nJy        |
| 194 | F606W_KRON                     | D            | float64              | nJy        |
| 195 | F606W_KRON_e                   | D            | float64              | nJy        |
| 196 | F606W_KRON_ei                  | D            | float64              | nJy        |
| 197 | F606W_KRON_bkg                 | D            | float64              | nJy        |
| 198 | F606W_KRON_S                   | D            | float64              | nJy        |
| 199 | F606W_KRON_S_e                 | D            | float64              | nJy        |
| 200 | F606W_KRON_S_ei                | D            | float64              | nJy        |
| 201 | F606W_KRON_S_bkg               | D            | float64              | nJy        |
| 202 | F775W_KRON                     | D            | float64              | nJy        |
| 203 | F775W_KRON_e                   | D            | float64              | nJy        |
| 204 | F775W_KRON_ei                  | D            | float64              | nJy        |
| 205 | F775W_KRON_bkg                 | D            | float64              | nJy        |
| 206 | F775W_KRON_S                   | D            | float64              | nJy        |
| 207 | F775W_KRON_S_e                 | D            | float64              | nJy        |
| 208 | F775W_KRON_S_ei                | D            | float64              | nJy        |
| 209 | F775W_KRON_S_bkg               | D            | float64              | nJy        |
| 210 | F814W_KRON                     | D            | float64              | nJy        |
| 211 | F814W_KRON_e                   | D            | float64              | nJy        |
| 212 | F814W_KRON_ei                  | D            | float64              | nJy        |
| 213 | F814W_KRON_bkg                 | D            | float64              | nJy        |
| 214 | F814W_KRON_S                   | D            | float64              | nJy        |
| 215 | F814W_KRON_S_e                 | D            | float64              | nJy        |
| 216 | F814W_KRON_S_ei                | D            | float64              | nJy        |
| 217 | F814W_KRON_S_bkg               | D            | float64              | nJy        |
| 218 | F850LP_KRON                    | D            | float64              | nJy        |
| 219 | F850LP_KRON_e                  | D            | float64              | nJy        |
| 220 | F850LP_KRON_ei                 | D            | float64              | nJy        |
| 221 | F850LP_KRON_bkg                | D            | float64              | nJy        |
| 222 | F850LP_KRON_S                  | D            | float64              | nJy        |
| 223 | F850LP_KRON_S_e                | D            | float64              | nJy        |
| 224 | F850LP_KRON_S_ei               | D            | float64              | nJy        |
| 225 | F850LP_KRON_S_bkg              | D            | float64              | nJy        |

### GOODS-S — MIRI (304,366 rows, 465 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | J            | int32                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | F560W_CIRC0                    | E            | float32              | nJy        |
|   5 | F560W_CIRC0_e                  | E            | float32              | nJy        |
|   6 | F560W_CIRC0_ei                 | E            | float32              | nJy        |
|   7 | F560W_CIRC1                    | E            | float32              | nJy        |
|   8 | F560W_CIRC1_e                  | E            | float32              | nJy        |
|   9 | F560W_CIRC1_ei                 | E            | float32              | nJy        |
|  10 | F560W_CIRC2                    | E            | float32              | nJy        |
|  11 | F560W_CIRC2_e                  | E            | float32              | nJy        |
|  12 | F560W_CIRC2_ei                 | E            | float32              | nJy        |
|  13 | F560W_CIRC3                    | E            | float32              | nJy        |
|  14 | F560W_CIRC3_e                  | E            | float32              | nJy        |
|  15 | F560W_CIRC3_ei                 | E            | float32              | nJy        |
|  16 | F560W_CIRC4                    | E            | float32              | nJy        |
|  17 | F560W_CIRC4_e                  | E            | float32              | nJy        |
|  18 | F560W_CIRC4_ei                 | E            | float32              | nJy        |
|  19 | F560W_CIRC5                    | E            | float32              | nJy        |
|  20 | F560W_CIRC5_e                  | E            | float32              | nJy        |
|  21 | F560W_CIRC5_ei                 | E            | float32              | nJy        |
|  22 | F560W_CIRC6                    | E            | float32              | nJy        |
|  23 | F560W_CIRC6_e                  | E            | float32              | nJy        |
|  24 | F560W_CIRC6_ei                 | E            | float32              | nJy        |
|  25 | F770W_CIRC0                    | E            | float32              | nJy        |
|  26 | F770W_CIRC0_e                  | E            | float32              | nJy        |
|  27 | F770W_CIRC0_ei                 | E            | float32              | nJy        |
|  28 | F770W_CIRC1                    | E            | float32              | nJy        |
|  29 | F770W_CIRC1_e                  | E            | float32              | nJy        |
|  30 | F770W_CIRC1_ei                 | E            | float32              | nJy        |
|  31 | F770W_CIRC2                    | E            | float32              | nJy        |
|  32 | F770W_CIRC2_e                  | E            | float32              | nJy        |
|  33 | F770W_CIRC2_ei                 | E            | float32              | nJy        |
|  34 | F770W_CIRC3                    | E            | float32              | nJy        |
|  35 | F770W_CIRC3_e                  | E            | float32              | nJy        |
|  36 | F770W_CIRC3_ei                 | E            | float32              | nJy        |
|  37 | F770W_CIRC4                    | E            | float32              | nJy        |
|  38 | F770W_CIRC4_e                  | E            | float32              | nJy        |
|  39 | F770W_CIRC4_ei                 | E            | float32              | nJy        |
|  40 | F770W_CIRC5                    | E            | float32              | nJy        |
|  41 | F770W_CIRC5_e                  | E            | float32              | nJy        |
|  42 | F770W_CIRC5_ei                 | E            | float32              | nJy        |
|  43 | F770W_CIRC6                    | E            | float32              | nJy        |
|  44 | F770W_CIRC6_e                  | E            | float32              | nJy        |
|  45 | F770W_CIRC6_ei                 | E            | float32              | nJy        |
|  46 | F1000W_CIRC0                   | E            | float32              | nJy        |
|  47 | F1000W_CIRC0_e                 | E            | float32              | nJy        |
|  48 | F1000W_CIRC0_ei                | E            | float32              | nJy        |
|  49 | F1000W_CIRC1                   | E            | float32              | nJy        |
|  50 | F1000W_CIRC1_e                 | E            | float32              | nJy        |
|  51 | F1000W_CIRC1_ei                | E            | float32              | nJy        |
|  52 | F1000W_CIRC2                   | E            | float32              | nJy        |
|  53 | F1000W_CIRC2_e                 | E            | float32              | nJy        |
|  54 | F1000W_CIRC2_ei                | E            | float32              | nJy        |
|  55 | F1000W_CIRC3                   | E            | float32              | nJy        |
|  56 | F1000W_CIRC3_e                 | E            | float32              | nJy        |
|  57 | F1000W_CIRC3_ei                | E            | float32              | nJy        |
|  58 | F1000W_CIRC4                   | E            | float32              | nJy        |
|  59 | F1000W_CIRC4_e                 | E            | float32              | nJy        |
|  60 | F1000W_CIRC4_ei                | E            | float32              | nJy        |
|  61 | F1000W_CIRC5                   | E            | float32              | nJy        |
|  62 | F1000W_CIRC5_e                 | E            | float32              | nJy        |
|  63 | F1000W_CIRC5_ei                | E            | float32              | nJy        |
|  64 | F1000W_CIRC6                   | E            | float32              | nJy        |
|  65 | F1000W_CIRC6_e                 | E            | float32              | nJy        |
|  66 | F1000W_CIRC6_ei                | E            | float32              | nJy        |
|  67 | F1280W_CIRC0                   | E            | float32              | nJy        |
|  68 | F1280W_CIRC0_e                 | E            | float32              | nJy        |
|  69 | F1280W_CIRC0_ei                | E            | float32              | nJy        |
|  70 | F1280W_CIRC1                   | E            | float32              | nJy        |
|  71 | F1280W_CIRC1_e                 | E            | float32              | nJy        |
|  72 | F1280W_CIRC1_ei                | E            | float32              | nJy        |
|  73 | F1280W_CIRC2                   | E            | float32              | nJy        |
|  74 | F1280W_CIRC2_e                 | E            | float32              | nJy        |
|  75 | F1280W_CIRC2_ei                | E            | float32              | nJy        |
|  76 | F1280W_CIRC3                   | E            | float32              | nJy        |
|  77 | F1280W_CIRC3_e                 | E            | float32              | nJy        |
|  78 | F1280W_CIRC3_ei                | E            | float32              | nJy        |
|  79 | F1280W_CIRC4                   | E            | float32              | nJy        |
|  80 | F1280W_CIRC4_e                 | E            | float32              | nJy        |
|  81 | F1280W_CIRC4_ei                | E            | float32              | nJy        |
|  82 | F1280W_CIRC5                   | E            | float32              | nJy        |
|  83 | F1280W_CIRC5_e                 | E            | float32              | nJy        |
|  84 | F1280W_CIRC5_ei                | E            | float32              | nJy        |
|  85 | F1280W_CIRC6                   | E            | float32              | nJy        |
|  86 | F1280W_CIRC6_e                 | E            | float32              | nJy        |
|  87 | F1280W_CIRC6_ei                | E            | float32              | nJy        |
|  88 | F1500W_CIRC0                   | E            | float32              | nJy        |
|  89 | F1500W_CIRC0_e                 | E            | float32              | nJy        |
|  90 | F1500W_CIRC0_ei                | E            | float32              | nJy        |
|  91 | F1500W_CIRC1                   | E            | float32              | nJy        |
|  92 | F1500W_CIRC1_e                 | E            | float32              | nJy        |
|  93 | F1500W_CIRC1_ei                | E            | float32              | nJy        |
|  94 | F1500W_CIRC2                   | E            | float32              | nJy        |
|  95 | F1500W_CIRC2_e                 | E            | float32              | nJy        |
|  96 | F1500W_CIRC2_ei                | E            | float32              | nJy        |
|  97 | F1500W_CIRC3                   | E            | float32              | nJy        |
|  98 | F1500W_CIRC3_e                 | E            | float32              | nJy        |
|  99 | F1500W_CIRC3_ei                | E            | float32              | nJy        |
| 100 | F1500W_CIRC4                   | E            | float32              | nJy        |
| 101 | F1500W_CIRC4_e                 | E            | float32              | nJy        |
| 102 | F1500W_CIRC4_ei                | E            | float32              | nJy        |
| 103 | F1500W_CIRC5                   | E            | float32              | nJy        |
| 104 | F1500W_CIRC5_e                 | E            | float32              | nJy        |
| 105 | F1500W_CIRC5_ei                | E            | float32              | nJy        |
| 106 | F1500W_CIRC6                   | E            | float32              | nJy        |
| 107 | F1500W_CIRC6_e                 | E            | float32              | nJy        |
| 108 | F1500W_CIRC6_ei                | E            | float32              | nJy        |
| 109 | F1800W_CIRC0                   | E            | float32              | nJy        |
| 110 | F1800W_CIRC0_e                 | E            | float32              | nJy        |
| 111 | F1800W_CIRC0_ei                | E            | float32              | nJy        |
| 112 | F1800W_CIRC1                   | E            | float32              | nJy        |
| 113 | F1800W_CIRC1_e                 | E            | float32              | nJy        |
| 114 | F1800W_CIRC1_ei                | E            | float32              | nJy        |
| 115 | F1800W_CIRC2                   | E            | float32              | nJy        |
| 116 | F1800W_CIRC2_e                 | E            | float32              | nJy        |
| 117 | F1800W_CIRC2_ei                | E            | float32              | nJy        |
| 118 | F1800W_CIRC3                   | E            | float32              | nJy        |
| 119 | F1800W_CIRC3_e                 | E            | float32              | nJy        |
| 120 | F1800W_CIRC3_ei                | E            | float32              | nJy        |
| 121 | F1800W_CIRC4                   | E            | float32              | nJy        |
| 122 | F1800W_CIRC4_e                 | E            | float32              | nJy        |
| 123 | F1800W_CIRC4_ei                | E            | float32              | nJy        |
| 124 | F1800W_CIRC5                   | E            | float32              | nJy        |
| 125 | F1800W_CIRC5_e                 | E            | float32              | nJy        |
| 126 | F1800W_CIRC5_ei                | E            | float32              | nJy        |
| 127 | F1800W_CIRC6                   | E            | float32              | nJy        |
| 128 | F1800W_CIRC6_e                 | E            | float32              | nJy        |
| 129 | F1800W_CIRC6_ei                | E            | float32              | nJy        |
| 130 | F2100W_CIRC0                   | E            | float32              | nJy        |
| 131 | F2100W_CIRC0_e                 | E            | float32              | nJy        |
| 132 | F2100W_CIRC0_ei                | E            | float32              | nJy        |
| 133 | F2100W_CIRC1                   | E            | float32              | nJy        |
| 134 | F2100W_CIRC1_e                 | E            | float32              | nJy        |
| 135 | F2100W_CIRC1_ei                | E            | float32              | nJy        |
| 136 | F2100W_CIRC2                   | E            | float32              | nJy        |
| 137 | F2100W_CIRC2_e                 | E            | float32              | nJy        |
| 138 | F2100W_CIRC2_ei                | E            | float32              | nJy        |
| 139 | F2100W_CIRC3                   | E            | float32              | nJy        |
| 140 | F2100W_CIRC3_e                 | E            | float32              | nJy        |
| 141 | F2100W_CIRC3_ei                | E            | float32              | nJy        |
| 142 | F2100W_CIRC4                   | E            | float32              | nJy        |
| 143 | F2100W_CIRC4_e                 | E            | float32              | nJy        |
| 144 | F2100W_CIRC4_ei                | E            | float32              | nJy        |
| 145 | F2100W_CIRC5                   | E            | float32              | nJy        |
| 146 | F2100W_CIRC5_e                 | E            | float32              | nJy        |
| 147 | F2100W_CIRC5_ei                | E            | float32              | nJy        |
| 148 | F2100W_CIRC6                   | E            | float32              | nJy        |
| 149 | F2100W_CIRC6_e                 | E            | float32              | nJy        |
| 150 | F2100W_CIRC6_ei                | E            | float32              | nJy        |
| 151 | F2550W_CIRC0                   | E            | float32              | nJy        |
| 152 | F2550W_CIRC0_e                 | E            | float32              | nJy        |
| 153 | F2550W_CIRC0_ei                | E            | float32              | nJy        |
| 154 | F2550W_CIRC1                   | E            | float32              | nJy        |
| 155 | F2550W_CIRC1_e                 | E            | float32              | nJy        |
| 156 | F2550W_CIRC1_ei                | E            | float32              | nJy        |
| 157 | F2550W_CIRC2                   | E            | float32              | nJy        |
| 158 | F2550W_CIRC2_e                 | E            | float32              | nJy        |
| 159 | F2550W_CIRC2_ei                | E            | float32              | nJy        |
| 160 | F2550W_CIRC3                   | E            | float32              | nJy        |
| 161 | F2550W_CIRC3_e                 | E            | float32              | nJy        |
| 162 | F2550W_CIRC3_ei                | E            | float32              | nJy        |
| 163 | F2550W_CIRC4                   | E            | float32              | nJy        |
| 164 | F2550W_CIRC4_e                 | E            | float32              | nJy        |
| 165 | F2550W_CIRC4_ei                | E            | float32              | nJy        |
| 166 | F2550W_CIRC5                   | E            | float32              | nJy        |
| 167 | F2550W_CIRC5_e                 | E            | float32              | nJy        |
| 168 | F2550W_CIRC5_ei                | E            | float32              | nJy        |
| 169 | F2550W_CIRC6                   | E            | float32              | nJy        |
| 170 | F2550W_CIRC6_e                 | E            | float32              | nJy        |
| 171 | F2550W_CIRC6_ei                | E            | float32              | nJy        |
| 172 | F560W_CIRC0_BSUB               | E            | float32              | nJy        |
| 173 | F560W_CIRC0_bkg_BSUB           | D            | float64              | nJy        |
| 174 | F560W_CIRC0_e_BSUB             | E            | float32              | nJy        |
| 175 | F560W_CIRC0_ei_BSUB            | E            | float32              | nJy        |
| 176 | F560W_CIRC1_BSUB               | E            | float32              | nJy        |
| 177 | F560W_CIRC1_bkg_BSUB           | D            | float64              | nJy        |
| 178 | F560W_CIRC1_e_BSUB             | E            | float32              | nJy        |
| 179 | F560W_CIRC1_ei_BSUB            | E            | float32              | nJy        |
| 180 | F560W_CIRC2_BSUB               | E            | float32              | nJy        |
| 181 | F560W_CIRC2_bkg_BSUB           | D            | float64              | nJy        |
| 182 | F560W_CIRC2_e_BSUB             | E            | float32              | nJy        |
| 183 | F560W_CIRC2_ei_BSUB            | E            | float32              | nJy        |
| 184 | F560W_CIRC3_BSUB               | E            | float32              | nJy        |
| 185 | F560W_CIRC3_bkg_BSUB           | D            | float64              | nJy        |
| 186 | F560W_CIRC3_e_BSUB             | E            | float32              | nJy        |
| 187 | F560W_CIRC3_ei_BSUB            | E            | float32              | nJy        |
| 188 | F560W_CIRC4_BSUB               | E            | float32              | nJy        |
| 189 | F560W_CIRC4_bkg_BSUB           | D            | float64              | nJy        |
| 190 | F560W_CIRC4_e_BSUB             | E            | float32              | nJy        |
| 191 | F560W_CIRC4_ei_BSUB            | E            | float32              | nJy        |
| 192 | F560W_CIRC5_BSUB               | E            | float32              | nJy        |
| 193 | F560W_CIRC5_bkg_BSUB           | D            | float64              | nJy        |
| 194 | F560W_CIRC5_e_BSUB             | E            | float32              | nJy        |
| 195 | F560W_CIRC5_ei_BSUB            | E            | float32              | nJy        |
| 196 | F560W_CIRC6_BSUB               | E            | float32              | nJy        |
| 197 | F560W_CIRC6_bkg_BSUB           | D            | float64              | nJy        |
| 198 | F560W_CIRC6_e_BSUB             | E            | float32              | nJy        |
| 199 | F560W_CIRC6_ei_BSUB            | E            | float32              | nJy        |
| 200 | F770W_CIRC0_BSUB               | E            | float32              | nJy        |
| 201 | F770W_CIRC0_bkg_BSUB           | D            | float64              | nJy        |
| 202 | F770W_CIRC0_e_BSUB             | E            | float32              | nJy        |
| 203 | F770W_CIRC0_ei_BSUB            | E            | float32              | nJy        |
| 204 | F770W_CIRC1_BSUB               | E            | float32              | nJy        |
| 205 | F770W_CIRC1_bkg_BSUB           | D            | float64              | nJy        |
| 206 | F770W_CIRC1_e_BSUB             | E            | float32              | nJy        |
| 207 | F770W_CIRC1_ei_BSUB            | E            | float32              | nJy        |
| 208 | F770W_CIRC2_BSUB               | E            | float32              | nJy        |
| 209 | F770W_CIRC2_bkg_BSUB           | D            | float64              | nJy        |
| 210 | F770W_CIRC2_e_BSUB             | E            | float32              | nJy        |
| 211 | F770W_CIRC2_ei_BSUB            | E            | float32              | nJy        |
| 212 | F770W_CIRC3_BSUB               | E            | float32              | nJy        |
| 213 | F770W_CIRC3_bkg_BSUB           | D            | float64              | nJy        |
| 214 | F770W_CIRC3_e_BSUB             | E            | float32              | nJy        |
| 215 | F770W_CIRC3_ei_BSUB            | E            | float32              | nJy        |
| 216 | F770W_CIRC4_BSUB               | E            | float32              | nJy        |
| 217 | F770W_CIRC4_bkg_BSUB           | D            | float64              | nJy        |
| 218 | F770W_CIRC4_e_BSUB             | E            | float32              | nJy        |
| 219 | F770W_CIRC4_ei_BSUB            | E            | float32              | nJy        |
| 220 | F770W_CIRC5_BSUB               | E            | float32              | nJy        |
| 221 | F770W_CIRC5_bkg_BSUB           | D            | float64              | nJy        |
| 222 | F770W_CIRC5_e_BSUB             | E            | float32              | nJy        |
| 223 | F770W_CIRC5_ei_BSUB            | E            | float32              | nJy        |
| 224 | F770W_CIRC6_BSUB               | E            | float32              | nJy        |
| 225 | F770W_CIRC6_bkg_BSUB           | D            | float64              | nJy        |
| 226 | F770W_CIRC6_e_BSUB             | E            | float32              | nJy        |
| 227 | F770W_CIRC6_ei_BSUB            | E            | float32              | nJy        |
| 228 | F1000W_CIRC0_BSUB              | E            | float32              | nJy        |
| 229 | F1000W_CIRC0_bkg_BSUB          | D            | float64              | nJy        |
| 230 | F1000W_CIRC0_e_BSUB            | E            | float32              | nJy        |
| 231 | F1000W_CIRC0_ei_BSUB           | E            | float32              | nJy        |
| 232 | F1000W_CIRC1_BSUB              | E            | float32              | nJy        |
| 233 | F1000W_CIRC1_bkg_BSUB          | D            | float64              | nJy        |
| 234 | F1000W_CIRC1_e_BSUB            | E            | float32              | nJy        |
| 235 | F1000W_CIRC1_ei_BSUB           | E            | float32              | nJy        |
| 236 | F1000W_CIRC2_BSUB              | E            | float32              | nJy        |
| 237 | F1000W_CIRC2_bkg_BSUB          | D            | float64              | nJy        |
| 238 | F1000W_CIRC2_e_BSUB            | E            | float32              | nJy        |
| 239 | F1000W_CIRC2_ei_BSUB           | E            | float32              | nJy        |
| 240 | F1000W_CIRC3_BSUB              | E            | float32              | nJy        |
| 241 | F1000W_CIRC3_bkg_BSUB          | D            | float64              | nJy        |
| 242 | F1000W_CIRC3_e_BSUB            | E            | float32              | nJy        |
| 243 | F1000W_CIRC3_ei_BSUB           | E            | float32              | nJy        |
| 244 | F1000W_CIRC4_BSUB              | E            | float32              | nJy        |
| 245 | F1000W_CIRC4_bkg_BSUB          | D            | float64              | nJy        |
| 246 | F1000W_CIRC4_e_BSUB            | E            | float32              | nJy        |
| 247 | F1000W_CIRC4_ei_BSUB           | E            | float32              | nJy        |
| 248 | F1000W_CIRC5_BSUB              | E            | float32              | nJy        |
| 249 | F1000W_CIRC5_bkg_BSUB          | D            | float64              | nJy        |
| 250 | F1000W_CIRC5_e_BSUB            | E            | float32              | nJy        |
| 251 | F1000W_CIRC5_ei_BSUB           | E            | float32              | nJy        |
| 252 | F1000W_CIRC6_BSUB              | E            | float32              | nJy        |
| 253 | F1000W_CIRC6_bkg_BSUB          | D            | float64              | nJy        |
| 254 | F1000W_CIRC6_e_BSUB            | E            | float32              | nJy        |
| 255 | F1000W_CIRC6_ei_BSUB           | E            | float32              | nJy        |
| 256 | F1280W_CIRC0_BSUB              | E            | float32              | nJy        |
| 257 | F1280W_CIRC0_bkg_BSUB          | D            | float64              | nJy        |
| 258 | F1280W_CIRC0_e_BSUB            | E            | float32              | nJy        |
| 259 | F1280W_CIRC0_ei_BSUB           | E            | float32              | nJy        |
| 260 | F1280W_CIRC1_BSUB              | E            | float32              | nJy        |
| 261 | F1280W_CIRC1_bkg_BSUB          | D            | float64              | nJy        |
| 262 | F1280W_CIRC1_e_BSUB            | E            | float32              | nJy        |
| 263 | F1280W_CIRC1_ei_BSUB           | E            | float32              | nJy        |
| 264 | F1280W_CIRC2_BSUB              | E            | float32              | nJy        |
| 265 | F1280W_CIRC2_bkg_BSUB          | D            | float64              | nJy        |
| 266 | F1280W_CIRC2_e_BSUB            | E            | float32              | nJy        |
| 267 | F1280W_CIRC2_ei_BSUB           | E            | float32              | nJy        |
| 268 | F1280W_CIRC3_BSUB              | E            | float32              | nJy        |
| 269 | F1280W_CIRC3_bkg_BSUB          | D            | float64              | nJy        |
| 270 | F1280W_CIRC3_e_BSUB            | E            | float32              | nJy        |
| 271 | F1280W_CIRC3_ei_BSUB           | E            | float32              | nJy        |
| 272 | F1280W_CIRC4_BSUB              | E            | float32              | nJy        |
| 273 | F1280W_CIRC4_bkg_BSUB          | D            | float64              | nJy        |
| 274 | F1280W_CIRC4_e_BSUB            | E            | float32              | nJy        |
| 275 | F1280W_CIRC4_ei_BSUB           | E            | float32              | nJy        |
| 276 | F1280W_CIRC5_BSUB              | E            | float32              | nJy        |
| 277 | F1280W_CIRC5_bkg_BSUB          | D            | float64              | nJy        |
| 278 | F1280W_CIRC5_e_BSUB            | E            | float32              | nJy        |
| 279 | F1280W_CIRC5_ei_BSUB           | E            | float32              | nJy        |
| 280 | F1280W_CIRC6_BSUB              | E            | float32              | nJy        |
| 281 | F1280W_CIRC6_bkg_BSUB          | D            | float64              | nJy        |
| 282 | F1280W_CIRC6_e_BSUB            | E            | float32              | nJy        |
| 283 | F1280W_CIRC6_ei_BSUB           | E            | float32              | nJy        |
| 284 | F1500W_CIRC0_BSUB              | E            | float32              | nJy        |
| 285 | F1500W_CIRC0_bkg_BSUB          | D            | float64              | nJy        |
| 286 | F1500W_CIRC0_e_BSUB            | E            | float32              | nJy        |
| 287 | F1500W_CIRC0_ei_BSUB           | E            | float32              | nJy        |
| 288 | F1500W_CIRC1_BSUB              | E            | float32              | nJy        |
| 289 | F1500W_CIRC1_bkg_BSUB          | D            | float64              | nJy        |
| 290 | F1500W_CIRC1_e_BSUB            | E            | float32              | nJy        |
| 291 | F1500W_CIRC1_ei_BSUB           | E            | float32              | nJy        |
| 292 | F1500W_CIRC2_BSUB              | E            | float32              | nJy        |
| 293 | F1500W_CIRC2_bkg_BSUB          | D            | float64              | nJy        |
| 294 | F1500W_CIRC2_e_BSUB            | E            | float32              | nJy        |
| 295 | F1500W_CIRC2_ei_BSUB           | E            | float32              | nJy        |
| 296 | F1500W_CIRC3_BSUB              | E            | float32              | nJy        |
| 297 | F1500W_CIRC3_bkg_BSUB          | D            | float64              | nJy        |
| 298 | F1500W_CIRC3_e_BSUB            | E            | float32              | nJy        |
| 299 | F1500W_CIRC3_ei_BSUB           | E            | float32              | nJy        |
| 300 | F1500W_CIRC4_BSUB              | E            | float32              | nJy        |
| 301 | F1500W_CIRC4_bkg_BSUB          | D            | float64              | nJy        |
| 302 | F1500W_CIRC4_e_BSUB            | E            | float32              | nJy        |
| 303 | F1500W_CIRC4_ei_BSUB           | E            | float32              | nJy        |
| 304 | F1500W_CIRC5_BSUB              | E            | float32              | nJy        |
| 305 | F1500W_CIRC5_bkg_BSUB          | D            | float64              | nJy        |
| 306 | F1500W_CIRC5_e_BSUB            | E            | float32              | nJy        |
| 307 | F1500W_CIRC5_ei_BSUB           | E            | float32              | nJy        |
| 308 | F1500W_CIRC6_BSUB              | E            | float32              | nJy        |
| 309 | F1500W_CIRC6_bkg_BSUB          | D            | float64              | nJy        |
| 310 | F1500W_CIRC6_e_BSUB            | E            | float32              | nJy        |
| 311 | F1500W_CIRC6_ei_BSUB           | E            | float32              | nJy        |
| 312 | F1800W_CIRC0_BSUB              | E            | float32              | nJy        |
| 313 | F1800W_CIRC0_bkg_BSUB          | D            | float64              | nJy        |
| 314 | F1800W_CIRC0_e_BSUB            | E            | float32              | nJy        |
| 315 | F1800W_CIRC0_ei_BSUB           | E            | float32              | nJy        |
| 316 | F1800W_CIRC1_BSUB              | E            | float32              | nJy        |
| 317 | F1800W_CIRC1_bkg_BSUB          | D            | float64              | nJy        |
| 318 | F1800W_CIRC1_e_BSUB            | E            | float32              | nJy        |
| 319 | F1800W_CIRC1_ei_BSUB           | E            | float32              | nJy        |
| 320 | F1800W_CIRC2_BSUB              | E            | float32              | nJy        |
| 321 | F1800W_CIRC2_bkg_BSUB          | D            | float64              | nJy        |
| 322 | F1800W_CIRC2_e_BSUB            | E            | float32              | nJy        |
| 323 | F1800W_CIRC2_ei_BSUB           | E            | float32              | nJy        |
| 324 | F1800W_CIRC3_BSUB              | E            | float32              | nJy        |
| 325 | F1800W_CIRC3_bkg_BSUB          | D            | float64              | nJy        |
| 326 | F1800W_CIRC3_e_BSUB            | E            | float32              | nJy        |
| 327 | F1800W_CIRC3_ei_BSUB           | E            | float32              | nJy        |
| 328 | F1800W_CIRC4_BSUB              | E            | float32              | nJy        |
| 329 | F1800W_CIRC4_bkg_BSUB          | D            | float64              | nJy        |
| 330 | F1800W_CIRC4_e_BSUB            | E            | float32              | nJy        |
| 331 | F1800W_CIRC4_ei_BSUB           | E            | float32              | nJy        |
| 332 | F1800W_CIRC5_BSUB              | E            | float32              | nJy        |
| 333 | F1800W_CIRC5_bkg_BSUB          | D            | float64              | nJy        |
| 334 | F1800W_CIRC5_e_BSUB            | E            | float32              | nJy        |
| 335 | F1800W_CIRC5_ei_BSUB           | E            | float32              | nJy        |
| 336 | F1800W_CIRC6_BSUB              | E            | float32              | nJy        |
| 337 | F1800W_CIRC6_bkg_BSUB          | D            | float64              | nJy        |
| 338 | F1800W_CIRC6_e_BSUB            | E            | float32              | nJy        |
| 339 | F1800W_CIRC6_ei_BSUB           | E            | float32              | nJy        |
| 340 | F2100W_CIRC0_BSUB              | E            | float32              | nJy        |
| 341 | F2100W_CIRC0_bkg_BSUB          | D            | float64              | nJy        |
| 342 | F2100W_CIRC0_e_BSUB            | E            | float32              | nJy        |
| 343 | F2100W_CIRC0_ei_BSUB           | E            | float32              | nJy        |
| 344 | F2100W_CIRC1_BSUB              | E            | float32              | nJy        |
| 345 | F2100W_CIRC1_bkg_BSUB          | D            | float64              | nJy        |
| 346 | F2100W_CIRC1_e_BSUB            | E            | float32              | nJy        |
| 347 | F2100W_CIRC1_ei_BSUB           | E            | float32              | nJy        |
| 348 | F2100W_CIRC2_BSUB              | E            | float32              | nJy        |
| 349 | F2100W_CIRC2_bkg_BSUB          | D            | float64              | nJy        |
| 350 | F2100W_CIRC2_e_BSUB            | E            | float32              | nJy        |
| 351 | F2100W_CIRC2_ei_BSUB           | E            | float32              | nJy        |
| 352 | F2100W_CIRC3_BSUB              | E            | float32              | nJy        |
| 353 | F2100W_CIRC3_bkg_BSUB          | D            | float64              | nJy        |
| 354 | F2100W_CIRC3_e_BSUB            | E            | float32              | nJy        |
| 355 | F2100W_CIRC3_ei_BSUB           | E            | float32              | nJy        |
| 356 | F2100W_CIRC4_BSUB              | E            | float32              | nJy        |
| 357 | F2100W_CIRC4_bkg_BSUB          | D            | float64              | nJy        |
| 358 | F2100W_CIRC4_e_BSUB            | E            | float32              | nJy        |
| 359 | F2100W_CIRC4_ei_BSUB           | E            | float32              | nJy        |
| 360 | F2100W_CIRC5_BSUB              | E            | float32              | nJy        |
| 361 | F2100W_CIRC5_bkg_BSUB          | D            | float64              | nJy        |
| 362 | F2100W_CIRC5_e_BSUB            | E            | float32              | nJy        |
| 363 | F2100W_CIRC5_ei_BSUB           | E            | float32              | nJy        |
| 364 | F2100W_CIRC6_BSUB              | E            | float32              | nJy        |
| 365 | F2100W_CIRC6_bkg_BSUB          | D            | float64              | nJy        |
| 366 | F2100W_CIRC6_e_BSUB            | E            | float32              | nJy        |
| 367 | F2100W_CIRC6_ei_BSUB           | E            | float32              | nJy        |
| 368 | F2550W_CIRC0_BSUB              | E            | float32              | nJy        |
| 369 | F2550W_CIRC0_bkg_BSUB          | D            | float64              | nJy        |
| 370 | F2550W_CIRC0_e_BSUB            | E            | float32              | nJy        |
| 371 | F2550W_CIRC0_ei_BSUB           | E            | float32              | nJy        |
| 372 | F2550W_CIRC1_BSUB              | E            | float32              | nJy        |
| 373 | F2550W_CIRC1_bkg_BSUB          | D            | float64              | nJy        |
| 374 | F2550W_CIRC1_e_BSUB            | E            | float32              | nJy        |
| 375 | F2550W_CIRC1_ei_BSUB           | E            | float32              | nJy        |
| 376 | F2550W_CIRC2_BSUB              | E            | float32              | nJy        |
| 377 | F2550W_CIRC2_bkg_BSUB          | D            | float64              | nJy        |
| 378 | F2550W_CIRC2_e_BSUB            | E            | float32              | nJy        |
| 379 | F2550W_CIRC2_ei_BSUB           | E            | float32              | nJy        |
| 380 | F2550W_CIRC3_BSUB              | E            | float32              | nJy        |
| 381 | F2550W_CIRC3_bkg_BSUB          | D            | float64              | nJy        |
| 382 | F2550W_CIRC3_e_BSUB            | E            | float32              | nJy        |
| 383 | F2550W_CIRC3_ei_BSUB           | E            | float32              | nJy        |
| 384 | F2550W_CIRC4_BSUB              | E            | float32              | nJy        |
| 385 | F2550W_CIRC4_bkg_BSUB          | D            | float64              | nJy        |
| 386 | F2550W_CIRC4_e_BSUB            | E            | float32              | nJy        |
| 387 | F2550W_CIRC4_ei_BSUB           | E            | float32              | nJy        |
| 388 | F2550W_CIRC5_BSUB              | E            | float32              | nJy        |
| 389 | F2550W_CIRC5_bkg_BSUB          | D            | float64              | nJy        |
| 390 | F2550W_CIRC5_e_BSUB            | E            | float32              | nJy        |
| 391 | F2550W_CIRC5_ei_BSUB           | E            | float32              | nJy        |
| 392 | F2550W_CIRC6_BSUB              | E            | float32              | nJy        |
| 393 | F2550W_CIRC6_bkg_BSUB          | D            | float64              | nJy        |
| 394 | F2550W_CIRC6_e_BSUB            | E            | float32              | nJy        |
| 395 | F2550W_CIRC6_ei_BSUB           | E            | float32              | nJy        |
| 396 | A_KRON                         | D            | float64              | arcsec     |
| 397 | B_KRON                         | D            | float64              | arcsec     |
| 398 | THETA_KRON                     | D            | float64              | deg        |
| 399 | F560W_KRON                     | D            | float64              | nJy        |
| 400 | F560W_KRON_e                   | D            | float64              | nJy        |
| 401 | F560W_KRON_ei                  | D            | float64              | nJy        |
| 402 | F560W_KRON_bkg                 | D            | float64              | nJy        |
| 403 | F770W_KRON                     | D            | float64              | nJy        |
| 404 | F770W_KRON_e                   | D            | float64              | nJy        |
| 405 | F770W_KRON_ei                  | D            | float64              | nJy        |
| 406 | F770W_KRON_bkg                 | D            | float64              | nJy        |
| 407 | F1000W_KRON                    | D            | float64              | nJy        |
| 408 | F1000W_KRON_e                  | D            | float64              | nJy        |
| 409 | F1000W_KRON_ei                 | D            | float64              | nJy        |
| 410 | F1000W_KRON_bkg                | D            | float64              | nJy        |
| 411 | F1280W_KRON                    | D            | float64              | nJy        |
| 412 | F1280W_KRON_e                  | D            | float64              | nJy        |
| 413 | F1280W_KRON_ei                 | D            | float64              | nJy        |
| 414 | F1280W_KRON_bkg                | D            | float64              | nJy        |
| 415 | F1500W_KRON                    | D            | float64              | nJy        |
| 416 | F1500W_KRON_e                  | D            | float64              | nJy        |
| 417 | F1500W_KRON_ei                 | D            | float64              | nJy        |
| 418 | F1500W_KRON_bkg                | D            | float64              | nJy        |
| 419 | F1800W_KRON                    | D            | float64              | nJy        |
| 420 | F1800W_KRON_e                  | D            | float64              | nJy        |
| 421 | F1800W_KRON_ei                 | D            | float64              | nJy        |
| 422 | F1800W_KRON_bkg                | D            | float64              | nJy        |
| 423 | F2100W_KRON                    | D            | float64              | nJy        |
| 424 | F2100W_KRON_e                  | D            | float64              | nJy        |
| 425 | F2100W_KRON_ei                 | D            | float64              | nJy        |
| 426 | F2100W_KRON_bkg                | D            | float64              | nJy        |
| 427 | F2550W_KRON                    | D            | float64              | nJy        |
| 428 | F2550W_KRON_e                  | D            | float64              | nJy        |
| 429 | F2550W_KRON_ei                 | D            | float64              | nJy        |
| 430 | F2550W_KRON_bkg                | D            | float64              | nJy        |
| 431 | A_KRON_S                       | D            | float64              | arcsec     |
| 432 | B_KRON_S                       | D            | float64              | arcsec     |
| 433 | THETA_KRON_S                   | D            | float64              | deg        |
| 434 | F560W_KRON_S                   | D            | float64              | nJy        |
| 435 | F560W_KRON_S_e                 | D            | float64              | nJy        |
| 436 | F560W_KRON_S_ei                | D            | float64              | nJy        |
| 437 | F560W_KRON_S_bkg               | D            | float64              | nJy        |
| 438 | F770W_KRON_S                   | D            | float64              | nJy        |
| 439 | F770W_KRON_S_e                 | D            | float64              | nJy        |
| 440 | F770W_KRON_S_ei                | D            | float64              | nJy        |
| 441 | F770W_KRON_S_bkg               | D            | float64              | nJy        |
| 442 | F1000W_KRON_S                  | D            | float64              | nJy        |
| 443 | F1000W_KRON_S_e                | D            | float64              | nJy        |
| 444 | F1000W_KRON_S_ei               | D            | float64              | nJy        |
| 445 | F1000W_KRON_S_bkg              | D            | float64              | nJy        |
| 446 | F1280W_KRON_S                  | D            | float64              | nJy        |
| 447 | F1280W_KRON_S_e                | D            | float64              | nJy        |
| 448 | F1280W_KRON_S_ei               | D            | float64              | nJy        |
| 449 | F1280W_KRON_S_bkg              | D            | float64              | nJy        |
| 450 | F1500W_KRON_S                  | D            | float64              | nJy        |
| 451 | F1500W_KRON_S_e                | D            | float64              | nJy        |
| 452 | F1500W_KRON_S_ei               | D            | float64              | nJy        |
| 453 | F1500W_KRON_S_bkg              | D            | float64              | nJy        |
| 454 | F1800W_KRON_S                  | D            | float64              | nJy        |
| 455 | F1800W_KRON_S_e                | D            | float64              | nJy        |
| 456 | F1800W_KRON_S_ei               | D            | float64              | nJy        |
| 457 | F1800W_KRON_S_bkg              | D            | float64              | nJy        |
| 458 | F2100W_KRON_S                  | D            | float64              | nJy        |
| 459 | F2100W_KRON_S_e                | D            | float64              | nJy        |
| 460 | F2100W_KRON_S_ei               | D            | float64              | nJy        |
| 461 | F2100W_KRON_S_bkg              | D            | float64              | nJy        |
| 462 | F2550W_KRON_S                  | D            | float64              | nJy        |
| 463 | F2550W_KRON_S_e                | D            | float64              | nJy        |
| 464 | F2550W_KRON_S_ei               | D            | float64              | nJy        |
| 465 | F2550W_KRON_S_bkg              | D            | float64              | nJy        |

### GOODS-S — PHOTOZ (304,366 rows, 34 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | K            | int64                |            |
|   2 | z_spec                         | D            | float64              |            |
|   3 | z_a                            | E            | float32              |            |
|   4 | z_ml                           | E            | float32              |            |
|   5 | chi_a                          | E            | float32              |            |
|   6 | l68                            | D            | float64              |            |
|   7 | u68                            | D            | float64              |            |
|   8 | l95                            | D            | float64              |            |
|   9 | u95                            | D            | float64              |            |
|  10 | l99                            | D            | float64              |            |
|  11 | u99                            | D            | float64              |            |
|  12 | nfilt                          | K            | int64                |            |
|  13 | z_peak                         | D            | float64              |            |
|  14 | chi_peak                       | D            | float64              |            |
|  15 | z025                           | E            | float32              |            |
|  16 | z160                           | E            | float32              |            |
|  17 | z500                           | E            | float32              |            |
|  18 | z840                           | E            | float32              |            |
|  19 | z975                           | E            | float32              |            |
|  20 | Prob_gt_5                      | D            | float64              |            |
|  21 | Prob_gt_6                      | D            | float64              |            |
|  22 | Prob_gt_7                      | D            | float64              |            |
|  23 | Prob_gt_8                      | D            | float64              |            |
|  24 | Prob_gt_9                      | D            | float64              |            |
|  25 | chisq_z_lt_7                   | D            | float64              |            |
|  26 | z_chisq_z_lt_7                 | D            | float64              |            |
|  27 | chisq_z_lt_6                   | D            | float64              |            |
|  28 | z_chisq_z_lt_6                 | D            | float64              |            |
|  29 | chisq_z_lt_5                   | D            | float64              |            |
|  30 | z_chisq_z_lt_5                 | D            | float64              |            |
|  31 | chisq_z_lt_4                   | D            | float64              |            |
|  32 | z_chisq_z_lt_4                 | D            | float64              |            |
|  33 | z_bins                         | 22D          | float64[22]          |            |
|  34 | Prob_z_bins                    | 22D          | float64[22]          |            |

### GOODS-S — PHOTOZ_KRON (304,366 rows, 34 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | K            | int64                |            |
|   2 | z_spec                         | D            | float64              |            |
|   3 | z_a                            | E            | float32              |            |
|   4 | z_ml                           | E            | float32              |            |
|   5 | chi_a                          | E            | float32              |            |
|   6 | l68                            | D            | float64              |            |
|   7 | u68                            | D            | float64              |            |
|   8 | l95                            | D            | float64              |            |
|   9 | u95                            | D            | float64              |            |
|  10 | l99                            | D            | float64              |            |
|  11 | u99                            | D            | float64              |            |
|  12 | nfilt                          | K            | int64                |            |
|  13 | z_peak                         | D            | float64              |            |
|  14 | chi_peak                       | D            | float64              |            |
|  15 | z025                           | E            | float32              |            |
|  16 | z160                           | E            | float32              |            |
|  17 | z500                           | E            | float32              |            |
|  18 | z840                           | E            | float32              |            |
|  19 | z975                           | E            | float32              |            |
|  20 | Prob_gt_5                      | D            | float64              |            |
|  21 | Prob_gt_6                      | D            | float64              |            |
|  22 | Prob_gt_7                      | D            | float64              |            |
|  23 | Prob_gt_8                      | D            | float64              |            |
|  24 | Prob_gt_9                      | D            | float64              |            |
|  25 | chisq_z_lt_7                   | D            | float64              |            |
|  26 | z_chisq_z_lt_7                 | D            | float64              |            |
|  27 | chisq_z_lt_6                   | D            | float64              |            |
|  28 | z_chisq_z_lt_6                 | D            | float64              |            |
|  29 | chisq_z_lt_5                   | D            | float64              |            |
|  30 | z_chisq_z_lt_5                 | D            | float64              |            |
|  31 | chisq_z_lt_4                   | D            | float64              |            |
|  32 | z_chisq_z_lt_4                 | D            | float64              |            |
|  33 | z_bins                         | 22D          | float64[22]          |            |
|  34 | Prob_z_bins                    | 22D          | float64[22]          |            |

### GOODS-S — Research Column Availability

| Needed For Research | Found? |
|---------------------|--------|
| photo-z (EAZY) | YES |
| spectroscopic z | YES |
| RA/Dec coordinates | YES |
| quality flags | YES |
| NIRCam photometry (F090W-F444W) | YES |
| effective radius (R_eff) | YES |
| Kron photometry | YES |
| MIRI photometry | YES |
| stellar mass (log M*) | NO |
| star formation rate (SFR) | NO |
| photo-z probability (Prob_gt_z) | YES |

---

## GOODS-N

**File size:** 3,116,517,120 bytes (3.117 GB)
**URL:** `https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits`
**Total extensions:** 13

### Extension Summary

| Ext | Name                 |       Rows |  Cols |    Data Size |
|  ---|----------------------|------------|-------|--------------|
|   0 | PRIMARY              |          0 |     0 |       0.0 MB |
|   1 | FILTERS              |         27 |    12 |       0.0 MB |
|   2 | FLAG                 |    181,144 |    90 |     128.2 MB |
|   3 | SIZE                 |    181,144 |    18 |      25.4 MB |
|   4 | CIRC                 |    181,144 |   528 |     384.0 MB |
|   5 | CIRC_BSUB            |    181,144 |   703 |     637.6 MB |
|   6 | CIRC_CONV            |    181,144 |   528 |     384.0 MB |
|   7 | CIRC_BSUB_CONV       |    181,144 |   691 |     626.8 MB |
|   8 | KRON                 |    181,144 |   209 |     302.1 MB |
|   9 | KRON_CONV            |    181,144 |   209 |     302.1 MB |
|  10 | MIRI                 |    181,144 |   123 |     116.7 MB |
|  11 | PHOTOZ               |    181,144 |    34 |     104.3 MB |
|  12 | PHOTOZ_KRON          |    181,144 |    34 |     104.3 MB |

### GOODS-N — FLAG (181,144 rows, 90 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | K            | int64                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | F070W_FLAG                     | D            | float64              | pix        |
|   5 | F070W_WHT                      | D            | float64              | (MJy       |
|   6 | F070W_TEXP                     | D            | float64              | s          |
|   7 | F090W_FLAG                     | D            | float64              | pix        |
|   8 | F090W_WHT                      | D            | float64              | (MJy       |
|   9 | F090W_TEXP                     | D            | float64              | s          |
|  10 | F115W_FLAG                     | D            | float64              | pix        |
|  11 | F115W_WHT                      | D            | float64              | (MJy       |
|  12 | F115W_TEXP                     | D            | float64              | s          |
|  13 | F150W_FLAG                     | D            | float64              | pix        |
|  14 | F150W_WHT                      | D            | float64              | (MJy       |
|  15 | F150W_TEXP                     | D            | float64              | s          |
|  16 | F162M_FLAG                     | D            | float64              | pix        |
|  17 | F162M_WHT                      | D            | float64              | (MJy       |
|  18 | F162M_TEXP                     | D            | float64              | s          |
|  19 | F182M_FLAG                     | D            | float64              | pix        |
|  20 | F182M_WHT                      | D            | float64              | (MJy       |
|  21 | F182M_TEXP                     | D            | float64              | s          |
|  22 | F187N_FLAG                     | D            | float64              | pix        |
|  23 | F187N_WHT                      | D            | float64              | (MJy       |
|  24 | F187N_TEXP                     | D            | float64              | s          |
|  25 | F200W_FLAG                     | D            | float64              | pix        |
|  26 | F200W_WHT                      | D            | float64              | (MJy       |
|  27 | F200W_TEXP                     | D            | float64              | s          |
|  28 | F210M_FLAG                     | D            | float64              | pix        |
|  29 | F210M_WHT                      | D            | float64              | (MJy       |
|  30 | F210M_TEXP                     | D            | float64              | s          |
|  31 | F277W_FLAG                     | D            | float64              | pix        |
|  32 | F277W_WHT                      | D            | float64              | (MJy       |
|  33 | F277W_TEXP                     | D            | float64              | s          |
|  34 | F300M_FLAG                     | D            | float64              | pix        |
|  35 | F300M_WHT                      | D            | float64              | (MJy       |
|  36 | F300M_TEXP                     | D            | float64              | s          |
|  37 | F335M_FLAG                     | D            | float64              | pix        |
|  38 | F335M_WHT                      | D            | float64              | (MJy       |
|  39 | F335M_TEXP                     | D            | float64              | s          |
|  40 | F356W_FLAG                     | D            | float64              | pix        |
|  41 | F356W_WHT                      | D            | float64              | (MJy       |
|  42 | F356W_TEXP                     | D            | float64              | s          |
|  43 | F410M_FLAG                     | D            | float64              | pix        |
|  44 | F410M_WHT                      | D            | float64              | (MJy       |
|  45 | F410M_TEXP                     | D            | float64              | s          |
|  46 | F430M_FLAG                     | D            | float64              | pix        |
|  47 | F430M_WHT                      | D            | float64              | (MJy       |
|  48 | F430M_TEXP                     | D            | float64              | s          |
|  49 | F444W_FLAG                     | D            | float64              | pix        |
|  50 | F444W_WHT                      | D            | float64              | (MJy       |
|  51 | F444W_TEXP                     | D            | float64              | s          |
|  52 | F460M_FLAG                     | D            | float64              | pix        |
|  53 | F460M_WHT                      | D            | float64              | (MJy       |
|  54 | F460M_TEXP                     | D            | float64              | s          |
|  55 | F435W_FLAG                     | D            | float64              | pix        |
|  56 | F435W_WHT                      | D            | float64              | (MJy       |
|  57 | F435W_TEXP                     | D            | float64              | s          |
|  58 | F606W_FLAG                     | D            | float64              | pix        |
|  59 | F606W_WHT                      | D            | float64              | (MJy       |
|  60 | F606W_TEXP                     | D            | float64              | s          |
|  61 | F775W_FLAG                     | D            | float64              | pix        |
|  62 | F775W_WHT                      | D            | float64              | (MJy       |
|  63 | F775W_TEXP                     | D            | float64              | s          |
|  64 | F814W_FLAG                     | D            | float64              | pix        |
|  65 | F814W_WHT                      | D            | float64              | (MJy       |
|  66 | F814W_TEXP                     | D            | float64              | s          |
|  67 | F850LP_FLAG                    | D            | float64              | pix        |
|  68 | F850LP_WHT                     | D            | float64              | (MJy       |
|  69 | F850LP_TEXP                    | D            | float64              | s          |
|  70 | F105W_FLAG                     | D            | float64              | pix        |
|  71 | F105W_WHT                      | D            | float64              | (MJy       |
|  72 | F105W_TEXP                     | D            | float64              | s          |
|  73 | F125W_FLAG                     | D            | float64              | pix        |
|  74 | F125W_WHT                      | D            | float64              | (MJy       |
|  75 | F125W_TEXP                     | D            | float64              | s          |
|  76 | F140W_FLAG                     | D            | float64              | pix        |
|  77 | F140W_WHT                      | D            | float64              | (MJy       |
|  78 | F140W_TEXP                     | D            | float64              | s          |
|  79 | F160W_FLAG                     | D            | float64              | pix        |
|  80 | F160W_WHT                      | D            | float64              | (MJy       |
|  81 | F160W_TEXP                     | D            | float64              | s          |
|  82 | F770W_FLAG                     | D            | float64              | pix        |
|  83 | F770W_WHT                      | D            | float64              | (MJy       |
|  84 | F770W_TEXP                     | D            | float64              | s          |
|  85 | F1280W_FLAG                    | D            | float64              | pix        |
|  86 | F1280W_WHT                     | D            | float64              | (MJy       |
|  87 | F1280W_TEXP                    | D            | float64              | s          |
|  88 | FLAG_BN                        | J            | int32                |            |
|  89 | PARENT_ID                      | J            | int32                |            |
|  90 | PID_HASH                       | J            | int32                |            |

### GOODS-N — SIZE (181,144 rows, 18 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | J            | int32                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | X                              | D            | float64              | pix        |
|   5 | Y                              | D            | float64              | pix        |
|   6 | XC                             | D            | float64              | pix        |
|   7 | YC                             | D            | float64              | pix        |
|   8 | BBOX_XMIN                      | K            | int64                | pix        |
|   9 | BBOX_XMAX                      | K            | int64                | pix        |
|  10 | BBOX_YMIN                      | K            | int64                | pix        |
|  11 | BBOX_YMAX                      | K            | int64                | pix        |
|  12 | NPIX_DET                       | D            | float64              |            |
|  13 | A                              | D            | float64              | arcsec     |
|  14 | B                              | D            | float64              | arcsec     |
|  15 | THETA                          | D            | float64              | deg        |
|  16 | R_KRON_U                       | D            | float64              | nJy        |
|  17 | FWHM                           | D            | float64              | arcsec     |
|  18 | GINI                           | D            | float64              |            |

### GOODS-N — KRON (181,144 rows, 209 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | J            | int32                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | A_KRON                         | D            | float64              | arcsec     |
|   5 | B_KRON                         | D            | float64              | arcsec     |
|   6 | THETA_KRON                     | D            | float64              | deg        |
|   7 | F070W_KRON                     | D            | float64              | nJy        |
|   8 | F070W_KRON_e                   | D            | float64              | nJy        |
|   9 | F070W_KRON_ei                  | D            | float64              | nJy        |
|  10 | F070W_KRON_bkg                 | D            | float64              | nJy        |
|  11 | A_KRON_S                       | D            | float64              | arcsec     |
|  12 | B_KRON_S                       | D            | float64              | arcsec     |
|  13 | THETA_KRON_S                   | D            | float64              | deg        |
|  14 | F070W_KRON_S                   | D            | float64              | nJy        |
|  15 | F070W_KRON_S_e                 | D            | float64              | nJy        |
|  16 | F070W_KRON_S_ei                | D            | float64              | nJy        |
|  17 | F070W_KRON_S_bkg               | D            | float64              | nJy        |
|  18 | F090W_KRON                     | D            | float64              | nJy        |
|  19 | F090W_KRON_e                   | D            | float64              | nJy        |
|  20 | F090W_KRON_ei                  | D            | float64              | nJy        |
|  21 | F090W_KRON_bkg                 | D            | float64              | nJy        |
|  22 | F090W_KRON_S                   | D            | float64              | nJy        |
|  23 | F090W_KRON_S_e                 | D            | float64              | nJy        |
|  24 | F090W_KRON_S_ei                | D            | float64              | nJy        |
|  25 | F090W_KRON_S_bkg               | D            | float64              | nJy        |
|  26 | F105W_KRON                     | D            | float64              | nJy        |
|  27 | F105W_KRON_e                   | D            | float64              | nJy        |
|  28 | F105W_KRON_ei                  | D            | float64              | nJy        |
|  29 | F105W_KRON_bkg                 | D            | float64              | nJy        |
|  30 | F105W_KRON_S                   | D            | float64              | nJy        |
|  31 | F105W_KRON_S_e                 | D            | float64              | nJy        |
|  32 | F105W_KRON_S_ei                | D            | float64              | nJy        |
|  33 | F105W_KRON_S_bkg               | D            | float64              | nJy        |
|  34 | F115W_KRON                     | D            | float64              | nJy        |
|  35 | F115W_KRON_e                   | D            | float64              | nJy        |
|  36 | F115W_KRON_ei                  | D            | float64              | nJy        |
|  37 | F115W_KRON_bkg                 | D            | float64              | nJy        |
|  38 | F115W_KRON_S                   | D            | float64              | nJy        |
|  39 | F115W_KRON_S_e                 | D            | float64              | nJy        |
|  40 | F115W_KRON_S_ei                | D            | float64              | nJy        |
|  41 | F115W_KRON_S_bkg               | D            | float64              | nJy        |
|  42 | F125W_KRON                     | D            | float64              | nJy        |
|  43 | F125W_KRON_e                   | D            | float64              | nJy        |
|  44 | F125W_KRON_ei                  | D            | float64              | nJy        |
|  45 | F125W_KRON_bkg                 | D            | float64              | nJy        |
|  46 | F125W_KRON_S                   | D            | float64              | nJy        |
|  47 | F125W_KRON_S_e                 | D            | float64              | nJy        |
|  48 | F125W_KRON_S_ei                | D            | float64              | nJy        |
|  49 | F125W_KRON_S_bkg               | D            | float64              | nJy        |
|  50 | F140W_KRON                     | D            | float64              | nJy        |
|  51 | F140W_KRON_e                   | D            | float64              | nJy        |
|  52 | F140W_KRON_ei                  | D            | float64              | nJy        |
|  53 | F140W_KRON_bkg                 | D            | float64              | nJy        |
|  54 | F140W_KRON_S                   | D            | float64              | nJy        |
|  55 | F140W_KRON_S_e                 | D            | float64              | nJy        |
|  56 | F140W_KRON_S_ei                | D            | float64              | nJy        |
|  57 | F140W_KRON_S_bkg               | D            | float64              | nJy        |
|  58 | F150W_KRON                     | D            | float64              | nJy        |
|  59 | F150W_KRON_e                   | D            | float64              | nJy        |
|  60 | F150W_KRON_ei                  | D            | float64              | nJy        |
|  61 | F150W_KRON_bkg                 | D            | float64              | nJy        |
|  62 | F150W_KRON_S                   | D            | float64              | nJy        |
|  63 | F150W_KRON_S_e                 | D            | float64              | nJy        |
|  64 | F150W_KRON_S_ei                | D            | float64              | nJy        |
|  65 | F150W_KRON_S_bkg               | D            | float64              | nJy        |
|  66 | F160W_KRON                     | D            | float64              | nJy        |
|  67 | F160W_KRON_e                   | D            | float64              | nJy        |
|  68 | F160W_KRON_ei                  | D            | float64              | nJy        |
|  69 | F160W_KRON_bkg                 | D            | float64              | nJy        |
|  70 | F160W_KRON_S                   | D            | float64              | nJy        |
|  71 | F160W_KRON_S_e                 | D            | float64              | nJy        |
|  72 | F160W_KRON_S_ei                | D            | float64              | nJy        |
|  73 | F160W_KRON_S_bkg               | D            | float64              | nJy        |
|  74 | F162M_KRON                     | D            | float64              | nJy        |
|  75 | F162M_KRON_e                   | D            | float64              | nJy        |
|  76 | F162M_KRON_ei                  | D            | float64              | nJy        |
|  77 | F162M_KRON_bkg                 | D            | float64              | nJy        |
|  78 | F162M_KRON_S                   | D            | float64              | nJy        |
|  79 | F162M_KRON_S_e                 | D            | float64              | nJy        |
|  80 | F162M_KRON_S_ei                | D            | float64              | nJy        |
|  81 | F162M_KRON_S_bkg               | D            | float64              | nJy        |
|  82 | F182M_KRON                     | D            | float64              | nJy        |
|  83 | F182M_KRON_e                   | D            | float64              | nJy        |
|  84 | F182M_KRON_ei                  | D            | float64              | nJy        |
|  85 | F182M_KRON_bkg                 | D            | float64              | nJy        |
|  86 | F182M_KRON_S                   | D            | float64              | nJy        |
|  87 | F182M_KRON_S_e                 | D            | float64              | nJy        |
|  88 | F182M_KRON_S_ei                | D            | float64              | nJy        |
|  89 | F182M_KRON_S_bkg               | D            | float64              | nJy        |
|  90 | F200W_KRON                     | D            | float64              | nJy        |
|  91 | F200W_KRON_e                   | D            | float64              | nJy        |
|  92 | F200W_KRON_ei                  | D            | float64              | nJy        |
|  93 | F200W_KRON_bkg                 | D            | float64              | nJy        |
|  94 | F200W_KRON_S                   | D            | float64              | nJy        |
|  95 | F200W_KRON_S_e                 | D            | float64              | nJy        |
|  96 | F200W_KRON_S_ei                | D            | float64              | nJy        |
|  97 | F200W_KRON_S_bkg               | D            | float64              | nJy        |
|  98 | F210M_KRON                     | D            | float64              | nJy        |
|  99 | F210M_KRON_e                   | D            | float64              | nJy        |
| 100 | F210M_KRON_ei                  | D            | float64              | nJy        |
| 101 | F210M_KRON_bkg                 | D            | float64              | nJy        |
| 102 | F210M_KRON_S                   | D            | float64              | nJy        |
| 103 | F210M_KRON_S_e                 | D            | float64              | nJy        |
| 104 | F210M_KRON_S_ei                | D            | float64              | nJy        |
| 105 | F210M_KRON_S_bkg               | D            | float64              | nJy        |
| 106 | F277W_KRON                     | D            | float64              | nJy        |
| 107 | F277W_KRON_e                   | D            | float64              | nJy        |
| 108 | F277W_KRON_ei                  | D            | float64              | nJy        |
| 109 | F277W_KRON_bkg                 | D            | float64              | nJy        |
| 110 | F277W_KRON_S                   | D            | float64              | nJy        |
| 111 | F277W_KRON_S_e                 | D            | float64              | nJy        |
| 112 | F277W_KRON_S_ei                | D            | float64              | nJy        |
| 113 | F277W_KRON_S_bkg               | D            | float64              | nJy        |
| 114 | F300M_KRON                     | D            | float64              | nJy        |
| 115 | F300M_KRON_e                   | D            | float64              | nJy        |
| 116 | F300M_KRON_ei                  | D            | float64              | nJy        |
| 117 | F300M_KRON_bkg                 | D            | float64              | nJy        |
| 118 | F300M_KRON_S                   | D            | float64              | nJy        |
| 119 | F300M_KRON_S_e                 | D            | float64              | nJy        |
| 120 | F300M_KRON_S_ei                | D            | float64              | nJy        |
| 121 | F300M_KRON_S_bkg               | D            | float64              | nJy        |
| 122 | F335M_KRON                     | D            | float64              | nJy        |
| 123 | F335M_KRON_e                   | D            | float64              | nJy        |
| 124 | F335M_KRON_ei                  | D            | float64              | nJy        |
| 125 | F335M_KRON_bkg                 | D            | float64              | nJy        |
| 126 | F335M_KRON_S                   | D            | float64              | nJy        |
| 127 | F335M_KRON_S_e                 | D            | float64              | nJy        |
| 128 | F335M_KRON_S_ei                | D            | float64              | nJy        |
| 129 | F335M_KRON_S_bkg               | D            | float64              | nJy        |
| 130 | F356W_KRON                     | D            | float64              | nJy        |
| 131 | F356W_KRON_e                   | D            | float64              | nJy        |
| 132 | F356W_KRON_ei                  | D            | float64              | nJy        |
| 133 | F356W_KRON_bkg                 | D            | float64              | nJy        |
| 134 | F356W_KRON_S                   | D            | float64              | nJy        |
| 135 | F356W_KRON_S_e                 | D            | float64              | nJy        |
| 136 | F356W_KRON_S_ei                | D            | float64              | nJy        |
| 137 | F356W_KRON_S_bkg               | D            | float64              | nJy        |
| 138 | F410M_KRON                     | D            | float64              | nJy        |
| 139 | F410M_KRON_e                   | D            | float64              | nJy        |
| 140 | F410M_KRON_ei                  | D            | float64              | nJy        |
| 141 | F410M_KRON_bkg                 | D            | float64              | nJy        |
| 142 | F410M_KRON_S                   | D            | float64              | nJy        |
| 143 | F410M_KRON_S_e                 | D            | float64              | nJy        |
| 144 | F410M_KRON_S_ei                | D            | float64              | nJy        |
| 145 | F410M_KRON_S_bkg               | D            | float64              | nJy        |
| 146 | F430M_KRON                     | D            | float64              | nJy        |
| 147 | F430M_KRON_e                   | D            | float64              | nJy        |
| 148 | F430M_KRON_ei                  | D            | float64              | nJy        |
| 149 | F430M_KRON_bkg                 | D            | float64              | nJy        |
| 150 | F430M_KRON_S                   | D            | float64              | nJy        |
| 151 | F430M_KRON_S_e                 | D            | float64              | nJy        |
| 152 | F430M_KRON_S_ei                | D            | float64              | nJy        |
| 153 | F430M_KRON_S_bkg               | D            | float64              | nJy        |
| 154 | F435W_KRON                     | D            | float64              | nJy        |
| 155 | F435W_KRON_e                   | D            | float64              | nJy        |
| 156 | F435W_KRON_ei                  | D            | float64              | nJy        |
| 157 | F435W_KRON_bkg                 | D            | float64              | nJy        |
| 158 | F435W_KRON_S                   | D            | float64              | nJy        |
| 159 | F435W_KRON_S_e                 | D            | float64              | nJy        |
| 160 | F435W_KRON_S_ei                | D            | float64              | nJy        |
| 161 | F435W_KRON_S_bkg               | D            | float64              | nJy        |
| 162 | F444W_KRON                     | D            | float64              | nJy        |
| 163 | F444W_KRON_e                   | D            | float64              | nJy        |
| 164 | F444W_KRON_ei                  | D            | float64              | nJy        |
| 165 | F444W_KRON_bkg                 | D            | float64              | nJy        |
| 166 | F444W_KRON_S                   | D            | float64              | nJy        |
| 167 | F444W_KRON_S_e                 | D            | float64              | nJy        |
| 168 | F444W_KRON_S_ei                | D            | float64              | nJy        |
| 169 | F444W_KRON_S_bkg               | D            | float64              | nJy        |
| 170 | F460M_KRON                     | D            | float64              | nJy        |
| 171 | F460M_KRON_e                   | D            | float64              | nJy        |
| 172 | F460M_KRON_ei                  | D            | float64              | nJy        |
| 173 | F460M_KRON_bkg                 | D            | float64              | nJy        |
| 174 | F460M_KRON_S                   | D            | float64              | nJy        |
| 175 | F460M_KRON_S_e                 | D            | float64              | nJy        |
| 176 | F460M_KRON_S_ei                | D            | float64              | nJy        |
| 177 | F460M_KRON_S_bkg               | D            | float64              | nJy        |
| 178 | F606W_KRON                     | D            | float64              | nJy        |
| 179 | F606W_KRON_e                   | D            | float64              | nJy        |
| 180 | F606W_KRON_ei                  | D            | float64              | nJy        |
| 181 | F606W_KRON_bkg                 | D            | float64              | nJy        |
| 182 | F606W_KRON_S                   | D            | float64              | nJy        |
| 183 | F606W_KRON_S_e                 | D            | float64              | nJy        |
| 184 | F606W_KRON_S_ei                | D            | float64              | nJy        |
| 185 | F606W_KRON_S_bkg               | D            | float64              | nJy        |
| 186 | F775W_KRON                     | D            | float64              | nJy        |
| 187 | F775W_KRON_e                   | D            | float64              | nJy        |
| 188 | F775W_KRON_ei                  | D            | float64              | nJy        |
| 189 | F775W_KRON_bkg                 | D            | float64              | nJy        |
| 190 | F775W_KRON_S                   | D            | float64              | nJy        |
| 191 | F775W_KRON_S_e                 | D            | float64              | nJy        |
| 192 | F775W_KRON_S_ei                | D            | float64              | nJy        |
| 193 | F775W_KRON_S_bkg               | D            | float64              | nJy        |
| 194 | F814W_KRON                     | D            | float64              | nJy        |
| 195 | F814W_KRON_e                   | D            | float64              | nJy        |
| 196 | F814W_KRON_ei                  | D            | float64              | nJy        |
| 197 | F814W_KRON_bkg                 | D            | float64              | nJy        |
| 198 | F814W_KRON_S                   | D            | float64              | nJy        |
| 199 | F814W_KRON_S_e                 | D            | float64              | nJy        |
| 200 | F814W_KRON_S_ei                | D            | float64              | nJy        |
| 201 | F814W_KRON_S_bkg               | D            | float64              | nJy        |
| 202 | F850LP_KRON                    | D            | float64              | nJy        |
| 203 | F850LP_KRON_e                  | D            | float64              | nJy        |
| 204 | F850LP_KRON_ei                 | D            | float64              | nJy        |
| 205 | F850LP_KRON_bkg                | D            | float64              | nJy        |
| 206 | F850LP_KRON_S                  | D            | float64              | nJy        |
| 207 | F850LP_KRON_S_e                | D            | float64              | nJy        |
| 208 | F850LP_KRON_S_ei               | D            | float64              | nJy        |
| 209 | F850LP_KRON_S_bkg              | D            | float64              | nJy        |

### GOODS-N — KRON_CONV (181,144 rows, 209 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | J            | int32                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | A_KRON                         | D            | float64              | arcsec     |
|   5 | B_KRON                         | D            | float64              | arcsec     |
|   6 | THETA_KRON                     | D            | float64              | deg        |
|   7 | F070W_KRON                     | D            | float64              | nJy        |
|   8 | F070W_KRON_e                   | D            | float64              | nJy        |
|   9 | F070W_KRON_ei                  | D            | float64              | nJy        |
|  10 | F070W_KRON_bkg                 | D            | float64              | nJy        |
|  11 | A_KRON_S                       | D            | float64              | arcsec     |
|  12 | B_KRON_S                       | D            | float64              | arcsec     |
|  13 | THETA_KRON_S                   | D            | float64              | deg        |
|  14 | F070W_KRON_S                   | D            | float64              | nJy        |
|  15 | F070W_KRON_S_e                 | D            | float64              | nJy        |
|  16 | F070W_KRON_S_ei                | D            | float64              | nJy        |
|  17 | F070W_KRON_S_bkg               | D            | float64              | nJy        |
|  18 | F090W_KRON                     | D            | float64              | nJy        |
|  19 | F090W_KRON_e                   | D            | float64              | nJy        |
|  20 | F090W_KRON_ei                  | D            | float64              | nJy        |
|  21 | F090W_KRON_bkg                 | D            | float64              | nJy        |
|  22 | F090W_KRON_S                   | D            | float64              | nJy        |
|  23 | F090W_KRON_S_e                 | D            | float64              | nJy        |
|  24 | F090W_KRON_S_ei                | D            | float64              | nJy        |
|  25 | F090W_KRON_S_bkg               | D            | float64              | nJy        |
|  26 | F105W_KRON                     | D            | float64              | nJy        |
|  27 | F105W_KRON_e                   | D            | float64              | nJy        |
|  28 | F105W_KRON_ei                  | D            | float64              | nJy        |
|  29 | F105W_KRON_bkg                 | D            | float64              | nJy        |
|  30 | F105W_KRON_S                   | D            | float64              | nJy        |
|  31 | F105W_KRON_S_e                 | D            | float64              | nJy        |
|  32 | F105W_KRON_S_ei                | D            | float64              | nJy        |
|  33 | F105W_KRON_S_bkg               | D            | float64              | nJy        |
|  34 | F115W_KRON                     | D            | float64              | nJy        |
|  35 | F115W_KRON_e                   | D            | float64              | nJy        |
|  36 | F115W_KRON_ei                  | D            | float64              | nJy        |
|  37 | F115W_KRON_bkg                 | D            | float64              | nJy        |
|  38 | F115W_KRON_S                   | D            | float64              | nJy        |
|  39 | F115W_KRON_S_e                 | D            | float64              | nJy        |
|  40 | F115W_KRON_S_ei                | D            | float64              | nJy        |
|  41 | F115W_KRON_S_bkg               | D            | float64              | nJy        |
|  42 | F125W_KRON                     | D            | float64              | nJy        |
|  43 | F125W_KRON_e                   | D            | float64              | nJy        |
|  44 | F125W_KRON_ei                  | D            | float64              | nJy        |
|  45 | F125W_KRON_bkg                 | D            | float64              | nJy        |
|  46 | F125W_KRON_S                   | D            | float64              | nJy        |
|  47 | F125W_KRON_S_e                 | D            | float64              | nJy        |
|  48 | F125W_KRON_S_ei                | D            | float64              | nJy        |
|  49 | F125W_KRON_S_bkg               | D            | float64              | nJy        |
|  50 | F140W_KRON                     | D            | float64              | nJy        |
|  51 | F140W_KRON_e                   | D            | float64              | nJy        |
|  52 | F140W_KRON_ei                  | D            | float64              | nJy        |
|  53 | F140W_KRON_bkg                 | D            | float64              | nJy        |
|  54 | F140W_KRON_S                   | D            | float64              | nJy        |
|  55 | F140W_KRON_S_e                 | D            | float64              | nJy        |
|  56 | F140W_KRON_S_ei                | D            | float64              | nJy        |
|  57 | F140W_KRON_S_bkg               | D            | float64              | nJy        |
|  58 | F150W_KRON                     | D            | float64              | nJy        |
|  59 | F150W_KRON_e                   | D            | float64              | nJy        |
|  60 | F150W_KRON_ei                  | D            | float64              | nJy        |
|  61 | F150W_KRON_bkg                 | D            | float64              | nJy        |
|  62 | F150W_KRON_S                   | D            | float64              | nJy        |
|  63 | F150W_KRON_S_e                 | D            | float64              | nJy        |
|  64 | F150W_KRON_S_ei                | D            | float64              | nJy        |
|  65 | F150W_KRON_S_bkg               | D            | float64              | nJy        |
|  66 | F160W_KRON                     | D            | float64              | nJy        |
|  67 | F160W_KRON_e                   | D            | float64              | nJy        |
|  68 | F160W_KRON_ei                  | D            | float64              | nJy        |
|  69 | F160W_KRON_bkg                 | D            | float64              | nJy        |
|  70 | F160W_KRON_S                   | D            | float64              | nJy        |
|  71 | F160W_KRON_S_e                 | D            | float64              | nJy        |
|  72 | F160W_KRON_S_ei                | D            | float64              | nJy        |
|  73 | F160W_KRON_S_bkg               | D            | float64              | nJy        |
|  74 | F162M_KRON                     | D            | float64              | nJy        |
|  75 | F162M_KRON_e                   | D            | float64              | nJy        |
|  76 | F162M_KRON_ei                  | D            | float64              | nJy        |
|  77 | F162M_KRON_bkg                 | D            | float64              | nJy        |
|  78 | F162M_KRON_S                   | D            | float64              | nJy        |
|  79 | F162M_KRON_S_e                 | D            | float64              | nJy        |
|  80 | F162M_KRON_S_ei                | D            | float64              | nJy        |
|  81 | F162M_KRON_S_bkg               | D            | float64              | nJy        |
|  82 | F182M_KRON                     | D            | float64              | nJy        |
|  83 | F182M_KRON_e                   | D            | float64              | nJy        |
|  84 | F182M_KRON_ei                  | D            | float64              | nJy        |
|  85 | F182M_KRON_bkg                 | D            | float64              | nJy        |
|  86 | F182M_KRON_S                   | D            | float64              | nJy        |
|  87 | F182M_KRON_S_e                 | D            | float64              | nJy        |
|  88 | F182M_KRON_S_ei                | D            | float64              | nJy        |
|  89 | F182M_KRON_S_bkg               | D            | float64              | nJy        |
|  90 | F200W_KRON                     | D            | float64              | nJy        |
|  91 | F200W_KRON_e                   | D            | float64              | nJy        |
|  92 | F200W_KRON_ei                  | D            | float64              | nJy        |
|  93 | F200W_KRON_bkg                 | D            | float64              | nJy        |
|  94 | F200W_KRON_S                   | D            | float64              | nJy        |
|  95 | F200W_KRON_S_e                 | D            | float64              | nJy        |
|  96 | F200W_KRON_S_ei                | D            | float64              | nJy        |
|  97 | F200W_KRON_S_bkg               | D            | float64              | nJy        |
|  98 | F210M_KRON                     | D            | float64              | nJy        |
|  99 | F210M_KRON_e                   | D            | float64              | nJy        |
| 100 | F210M_KRON_ei                  | D            | float64              | nJy        |
| 101 | F210M_KRON_bkg                 | D            | float64              | nJy        |
| 102 | F210M_KRON_S                   | D            | float64              | nJy        |
| 103 | F210M_KRON_S_e                 | D            | float64              | nJy        |
| 104 | F210M_KRON_S_ei                | D            | float64              | nJy        |
| 105 | F210M_KRON_S_bkg               | D            | float64              | nJy        |
| 106 | F277W_KRON                     | D            | float64              | nJy        |
| 107 | F277W_KRON_e                   | D            | float64              | nJy        |
| 108 | F277W_KRON_ei                  | D            | float64              | nJy        |
| 109 | F277W_KRON_bkg                 | D            | float64              | nJy        |
| 110 | F277W_KRON_S                   | D            | float64              | nJy        |
| 111 | F277W_KRON_S_e                 | D            | float64              | nJy        |
| 112 | F277W_KRON_S_ei                | D            | float64              | nJy        |
| 113 | F277W_KRON_S_bkg               | D            | float64              | nJy        |
| 114 | F300M_KRON                     | D            | float64              | nJy        |
| 115 | F300M_KRON_e                   | D            | float64              | nJy        |
| 116 | F300M_KRON_ei                  | D            | float64              | nJy        |
| 117 | F300M_KRON_bkg                 | D            | float64              | nJy        |
| 118 | F300M_KRON_S                   | D            | float64              | nJy        |
| 119 | F300M_KRON_S_e                 | D            | float64              | nJy        |
| 120 | F300M_KRON_S_ei                | D            | float64              | nJy        |
| 121 | F300M_KRON_S_bkg               | D            | float64              | nJy        |
| 122 | F335M_KRON                     | D            | float64              | nJy        |
| 123 | F335M_KRON_e                   | D            | float64              | nJy        |
| 124 | F335M_KRON_ei                  | D            | float64              | nJy        |
| 125 | F335M_KRON_bkg                 | D            | float64              | nJy        |
| 126 | F335M_KRON_S                   | D            | float64              | nJy        |
| 127 | F335M_KRON_S_e                 | D            | float64              | nJy        |
| 128 | F335M_KRON_S_ei                | D            | float64              | nJy        |
| 129 | F335M_KRON_S_bkg               | D            | float64              | nJy        |
| 130 | F356W_KRON                     | D            | float64              | nJy        |
| 131 | F356W_KRON_e                   | D            | float64              | nJy        |
| 132 | F356W_KRON_ei                  | D            | float64              | nJy        |
| 133 | F356W_KRON_bkg                 | D            | float64              | nJy        |
| 134 | F356W_KRON_S                   | D            | float64              | nJy        |
| 135 | F356W_KRON_S_e                 | D            | float64              | nJy        |
| 136 | F356W_KRON_S_ei                | D            | float64              | nJy        |
| 137 | F356W_KRON_S_bkg               | D            | float64              | nJy        |
| 138 | F410M_KRON                     | D            | float64              | nJy        |
| 139 | F410M_KRON_e                   | D            | float64              | nJy        |
| 140 | F410M_KRON_ei                  | D            | float64              | nJy        |
| 141 | F410M_KRON_bkg                 | D            | float64              | nJy        |
| 142 | F410M_KRON_S                   | D            | float64              | nJy        |
| 143 | F410M_KRON_S_e                 | D            | float64              | nJy        |
| 144 | F410M_KRON_S_ei                | D            | float64              | nJy        |
| 145 | F410M_KRON_S_bkg               | D            | float64              | nJy        |
| 146 | F430M_KRON                     | D            | float64              | nJy        |
| 147 | F430M_KRON_e                   | D            | float64              | nJy        |
| 148 | F430M_KRON_ei                  | D            | float64              | nJy        |
| 149 | F430M_KRON_bkg                 | D            | float64              | nJy        |
| 150 | F430M_KRON_S                   | D            | float64              | nJy        |
| 151 | F430M_KRON_S_e                 | D            | float64              | nJy        |
| 152 | F430M_KRON_S_ei                | D            | float64              | nJy        |
| 153 | F430M_KRON_S_bkg               | D            | float64              | nJy        |
| 154 | F435W_KRON                     | D            | float64              | nJy        |
| 155 | F435W_KRON_e                   | D            | float64              | nJy        |
| 156 | F435W_KRON_ei                  | D            | float64              | nJy        |
| 157 | F435W_KRON_bkg                 | D            | float64              | nJy        |
| 158 | F435W_KRON_S                   | D            | float64              | nJy        |
| 159 | F435W_KRON_S_e                 | D            | float64              | nJy        |
| 160 | F435W_KRON_S_ei                | D            | float64              | nJy        |
| 161 | F435W_KRON_S_bkg               | D            | float64              | nJy        |
| 162 | F444W_KRON                     | D            | float64              | nJy        |
| 163 | F444W_KRON_e                   | D            | float64              | nJy        |
| 164 | F444W_KRON_ei                  | D            | float64              | nJy        |
| 165 | F444W_KRON_bkg                 | D            | float64              | nJy        |
| 166 | F444W_KRON_S                   | D            | float64              | nJy        |
| 167 | F444W_KRON_S_e                 | D            | float64              | nJy        |
| 168 | F444W_KRON_S_ei                | D            | float64              | nJy        |
| 169 | F444W_KRON_S_bkg               | D            | float64              | nJy        |
| 170 | F460M_KRON                     | D            | float64              | nJy        |
| 171 | F460M_KRON_e                   | D            | float64              | nJy        |
| 172 | F460M_KRON_ei                  | D            | float64              | nJy        |
| 173 | F460M_KRON_bkg                 | D            | float64              | nJy        |
| 174 | F460M_KRON_S                   | D            | float64              | nJy        |
| 175 | F460M_KRON_S_e                 | D            | float64              | nJy        |
| 176 | F460M_KRON_S_ei                | D            | float64              | nJy        |
| 177 | F460M_KRON_S_bkg               | D            | float64              | nJy        |
| 178 | F606W_KRON                     | D            | float64              | nJy        |
| 179 | F606W_KRON_e                   | D            | float64              | nJy        |
| 180 | F606W_KRON_ei                  | D            | float64              | nJy        |
| 181 | F606W_KRON_bkg                 | D            | float64              | nJy        |
| 182 | F606W_KRON_S                   | D            | float64              | nJy        |
| 183 | F606W_KRON_S_e                 | D            | float64              | nJy        |
| 184 | F606W_KRON_S_ei                | D            | float64              | nJy        |
| 185 | F606W_KRON_S_bkg               | D            | float64              | nJy        |
| 186 | F775W_KRON                     | D            | float64              | nJy        |
| 187 | F775W_KRON_e                   | D            | float64              | nJy        |
| 188 | F775W_KRON_ei                  | D            | float64              | nJy        |
| 189 | F775W_KRON_bkg                 | D            | float64              | nJy        |
| 190 | F775W_KRON_S                   | D            | float64              | nJy        |
| 191 | F775W_KRON_S_e                 | D            | float64              | nJy        |
| 192 | F775W_KRON_S_ei                | D            | float64              | nJy        |
| 193 | F775W_KRON_S_bkg               | D            | float64              | nJy        |
| 194 | F814W_KRON                     | D            | float64              | nJy        |
| 195 | F814W_KRON_e                   | D            | float64              | nJy        |
| 196 | F814W_KRON_ei                  | D            | float64              | nJy        |
| 197 | F814W_KRON_bkg                 | D            | float64              | nJy        |
| 198 | F814W_KRON_S                   | D            | float64              | nJy        |
| 199 | F814W_KRON_S_e                 | D            | float64              | nJy        |
| 200 | F814W_KRON_S_ei                | D            | float64              | nJy        |
| 201 | F814W_KRON_S_bkg               | D            | float64              | nJy        |
| 202 | F850LP_KRON                    | D            | float64              | nJy        |
| 203 | F850LP_KRON_e                  | D            | float64              | nJy        |
| 204 | F850LP_KRON_ei                 | D            | float64              | nJy        |
| 205 | F850LP_KRON_bkg                | D            | float64              | nJy        |
| 206 | F850LP_KRON_S                  | D            | float64              | nJy        |
| 207 | F850LP_KRON_S_e                | D            | float64              | nJy        |
| 208 | F850LP_KRON_S_ei               | D            | float64              | nJy        |
| 209 | F850LP_KRON_S_bkg              | D            | float64              | nJy        |

### GOODS-N — MIRI (181,144 rows, 123 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | J            | int32                |            |
|   2 | RA                             | D            | float64              | deg        |
|   3 | DEC                            | D            | float64              | deg        |
|   4 | F770W_CIRC0                    | E            | float32              | nJy        |
|   5 | F770W_CIRC0_e                  | E            | float32              | nJy        |
|   6 | F770W_CIRC0_ei                 | E            | float32              | nJy        |
|   7 | F770W_CIRC1                    | E            | float32              | nJy        |
|   8 | F770W_CIRC1_e                  | E            | float32              | nJy        |
|   9 | F770W_CIRC1_ei                 | E            | float32              | nJy        |
|  10 | F770W_CIRC2                    | E            | float32              | nJy        |
|  11 | F770W_CIRC2_e                  | E            | float32              | nJy        |
|  12 | F770W_CIRC2_ei                 | E            | float32              | nJy        |
|  13 | F770W_CIRC3                    | E            | float32              | nJy        |
|  14 | F770W_CIRC3_e                  | E            | float32              | nJy        |
|  15 | F770W_CIRC3_ei                 | E            | float32              | nJy        |
|  16 | F770W_CIRC4                    | E            | float32              | nJy        |
|  17 | F770W_CIRC4_e                  | E            | float32              | nJy        |
|  18 | F770W_CIRC4_ei                 | E            | float32              | nJy        |
|  19 | F770W_CIRC5                    | E            | float32              | nJy        |
|  20 | F770W_CIRC5_e                  | E            | float32              | nJy        |
|  21 | F770W_CIRC5_ei                 | E            | float32              | nJy        |
|  22 | F770W_CIRC6                    | E            | float32              | nJy        |
|  23 | F770W_CIRC6_e                  | E            | float32              | nJy        |
|  24 | F770W_CIRC6_ei                 | E            | float32              | nJy        |
|  25 | F1280W_CIRC0                   | E            | float32              | nJy        |
|  26 | F1280W_CIRC0_e                 | E            | float32              | nJy        |
|  27 | F1280W_CIRC0_ei                | E            | float32              | nJy        |
|  28 | F1280W_CIRC1                   | E            | float32              | nJy        |
|  29 | F1280W_CIRC1_e                 | E            | float32              | nJy        |
|  30 | F1280W_CIRC1_ei                | E            | float32              | nJy        |
|  31 | F1280W_CIRC2                   | E            | float32              | nJy        |
|  32 | F1280W_CIRC2_e                 | E            | float32              | nJy        |
|  33 | F1280W_CIRC2_ei                | E            | float32              | nJy        |
|  34 | F1280W_CIRC3                   | E            | float32              | nJy        |
|  35 | F1280W_CIRC3_e                 | E            | float32              | nJy        |
|  36 | F1280W_CIRC3_ei                | E            | float32              | nJy        |
|  37 | F1280W_CIRC4                   | E            | float32              | nJy        |
|  38 | F1280W_CIRC4_e                 | E            | float32              | nJy        |
|  39 | F1280W_CIRC4_ei                | E            | float32              | nJy        |
|  40 | F1280W_CIRC5                   | E            | float32              | nJy        |
|  41 | F1280W_CIRC5_e                 | E            | float32              | nJy        |
|  42 | F1280W_CIRC5_ei                | E            | float32              | nJy        |
|  43 | F1280W_CIRC6                   | E            | float32              | nJy        |
|  44 | F1280W_CIRC6_e                 | E            | float32              | nJy        |
|  45 | F1280W_CIRC6_ei                | E            | float32              | nJy        |
|  46 | F770W_CIRC0_BSUB               | E            | float32              | nJy        |
|  47 | F770W_CIRC0_bkg_BSUB           | D            | float64              | nJy        |
|  48 | F770W_CIRC0_e_BSUB             | E            | float32              | nJy        |
|  49 | F770W_CIRC0_ei_BSUB            | E            | float32              | nJy        |
|  50 | F770W_CIRC1_BSUB               | E            | float32              | nJy        |
|  51 | F770W_CIRC1_bkg_BSUB           | D            | float64              | nJy        |
|  52 | F770W_CIRC1_e_BSUB             | E            | float32              | nJy        |
|  53 | F770W_CIRC1_ei_BSUB            | E            | float32              | nJy        |
|  54 | F770W_CIRC2_BSUB               | E            | float32              | nJy        |
|  55 | F770W_CIRC2_bkg_BSUB           | D            | float64              | nJy        |
|  56 | F770W_CIRC2_e_BSUB             | E            | float32              | nJy        |
|  57 | F770W_CIRC2_ei_BSUB            | E            | float32              | nJy        |
|  58 | F770W_CIRC3_BSUB               | E            | float32              | nJy        |
|  59 | F770W_CIRC3_bkg_BSUB           | D            | float64              | nJy        |
|  60 | F770W_CIRC3_e_BSUB             | E            | float32              | nJy        |
|  61 | F770W_CIRC3_ei_BSUB            | E            | float32              | nJy        |
|  62 | F770W_CIRC4_BSUB               | E            | float32              | nJy        |
|  63 | F770W_CIRC4_bkg_BSUB           | D            | float64              | nJy        |
|  64 | F770W_CIRC4_e_BSUB             | E            | float32              | nJy        |
|  65 | F770W_CIRC4_ei_BSUB            | E            | float32              | nJy        |
|  66 | F770W_CIRC5_BSUB               | E            | float32              | nJy        |
|  67 | F770W_CIRC5_bkg_BSUB           | D            | float64              | nJy        |
|  68 | F770W_CIRC5_e_BSUB             | E            | float32              | nJy        |
|  69 | F770W_CIRC5_ei_BSUB            | E            | float32              | nJy        |
|  70 | F770W_CIRC6_BSUB               | E            | float32              | nJy        |
|  71 | F770W_CIRC6_bkg_BSUB           | D            | float64              | nJy        |
|  72 | F770W_CIRC6_e_BSUB             | E            | float32              | nJy        |
|  73 | F770W_CIRC6_ei_BSUB            | E            | float32              | nJy        |
|  74 | F1280W_CIRC0_BSUB              | E            | float32              | nJy        |
|  75 | F1280W_CIRC0_bkg_BSUB          | D            | float64              | nJy        |
|  76 | F1280W_CIRC0_e_BSUB            | E            | float32              | nJy        |
|  77 | F1280W_CIRC0_ei_BSUB           | E            | float32              | nJy        |
|  78 | F1280W_CIRC1_BSUB              | E            | float32              | nJy        |
|  79 | F1280W_CIRC1_bkg_BSUB          | D            | float64              | nJy        |
|  80 | F1280W_CIRC1_e_BSUB            | E            | float32              | nJy        |
|  81 | F1280W_CIRC1_ei_BSUB           | E            | float32              | nJy        |
|  82 | F1280W_CIRC2_BSUB              | E            | float32              | nJy        |
|  83 | F1280W_CIRC2_bkg_BSUB          | D            | float64              | nJy        |
|  84 | F1280W_CIRC2_e_BSUB            | E            | float32              | nJy        |
|  85 | F1280W_CIRC2_ei_BSUB           | E            | float32              | nJy        |
|  86 | F1280W_CIRC3_BSUB              | E            | float32              | nJy        |
|  87 | F1280W_CIRC3_bkg_BSUB          | D            | float64              | nJy        |
|  88 | F1280W_CIRC3_e_BSUB            | E            | float32              | nJy        |
|  89 | F1280W_CIRC3_ei_BSUB           | E            | float32              | nJy        |
|  90 | F1280W_CIRC4_BSUB              | E            | float32              | nJy        |
|  91 | F1280W_CIRC4_bkg_BSUB          | D            | float64              | nJy        |
|  92 | F1280W_CIRC4_e_BSUB            | E            | float32              | nJy        |
|  93 | F1280W_CIRC4_ei_BSUB           | E            | float32              | nJy        |
|  94 | F1280W_CIRC5_BSUB              | E            | float32              | nJy        |
|  95 | F1280W_CIRC5_bkg_BSUB          | D            | float64              | nJy        |
|  96 | F1280W_CIRC5_e_BSUB            | E            | float32              | nJy        |
|  97 | F1280W_CIRC5_ei_BSUB           | E            | float32              | nJy        |
|  98 | F1280W_CIRC6_BSUB              | E            | float32              | nJy        |
|  99 | F1280W_CIRC6_bkg_BSUB          | D            | float64              | nJy        |
| 100 | F1280W_CIRC6_e_BSUB            | E            | float32              | nJy        |
| 101 | F1280W_CIRC6_ei_BSUB           | E            | float32              | nJy        |
| 102 | A_KRON                         | D            | float64              | arcsec     |
| 103 | B_KRON                         | D            | float64              | arcsec     |
| 104 | THETA_KRON                     | D            | float64              | deg        |
| 105 | F770W_KRON                     | D            | float64              | nJy        |
| 106 | F770W_KRON_e                   | D            | float64              | nJy        |
| 107 | F770W_KRON_ei                  | D            | float64              | nJy        |
| 108 | F770W_KRON_bkg                 | D            | float64              | nJy        |
| 109 | A_KRON_S                       | D            | float64              | arcsec     |
| 110 | B_KRON_S                       | D            | float64              | arcsec     |
| 111 | THETA_KRON_S                   | D            | float64              | deg        |
| 112 | F770W_KRON_S                   | D            | float64              | nJy        |
| 113 | F770W_KRON_S_e                 | D            | float64              | nJy        |
| 114 | F770W_KRON_S_ei                | D            | float64              | nJy        |
| 115 | F770W_KRON_S_bkg               | D            | float64              | nJy        |
| 116 | F1280W_KRON                    | D            | float64              | nJy        |
| 117 | F1280W_KRON_e                  | D            | float64              | nJy        |
| 118 | F1280W_KRON_ei                 | D            | float64              | nJy        |
| 119 | F1280W_KRON_bkg                | D            | float64              | nJy        |
| 120 | F1280W_KRON_S                  | D            | float64              | nJy        |
| 121 | F1280W_KRON_S_e                | D            | float64              | nJy        |
| 122 | F1280W_KRON_S_ei               | D            | float64              | nJy        |
| 123 | F1280W_KRON_S_bkg              | D            | float64              | nJy        |

### GOODS-N — PHOTOZ (181,144 rows, 34 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | K            | int64                |            |
|   2 | z_spec                         | D            | float64              |            |
|   3 | z_a                            | E            | float32              |            |
|   4 | z_ml                           | E            | float32              |            |
|   5 | chi_a                          | E            | float32              |            |
|   6 | l68                            | D            | float64              |            |
|   7 | u68                            | D            | float64              |            |
|   8 | l95                            | D            | float64              |            |
|   9 | u95                            | D            | float64              |            |
|  10 | l99                            | D            | float64              |            |
|  11 | u99                            | D            | float64              |            |
|  12 | nfilt                          | K            | int64                |            |
|  13 | z_peak                         | D            | float64              |            |
|  14 | chi_peak                       | D            | float64              |            |
|  15 | z025                           | E            | float32              |            |
|  16 | z160                           | E            | float32              |            |
|  17 | z500                           | E            | float32              |            |
|  18 | z840                           | E            | float32              |            |
|  19 | z975                           | E            | float32              |            |
|  20 | Prob_gt_5                      | D            | float64              |            |
|  21 | Prob_gt_6                      | D            | float64              |            |
|  22 | Prob_gt_7                      | D            | float64              |            |
|  23 | Prob_gt_8                      | D            | float64              |            |
|  24 | Prob_gt_9                      | D            | float64              |            |
|  25 | chisq_z_lt_7                   | D            | float64              |            |
|  26 | z_chisq_z_lt_7                 | D            | float64              |            |
|  27 | chisq_z_lt_6                   | D            | float64              |            |
|  28 | z_chisq_z_lt_6                 | D            | float64              |            |
|  29 | chisq_z_lt_5                   | D            | float64              |            |
|  30 | z_chisq_z_lt_5                 | D            | float64              |            |
|  31 | chisq_z_lt_4                   | D            | float64              |            |
|  32 | z_chisq_z_lt_4                 | D            | float64              |            |
|  33 | z_bins                         | 22D          | float64[22]          |            |
|  34 | Prob_z_bins                    | 22D          | float64[22]          |            |

### GOODS-N — PHOTOZ_KRON (181,144 rows, 34 columns)

|   # | Column Name                    | Format       | Type                 | Unit       |
|  ---|--------------------------------|--------------|----------------------|------------|
|   1 | ID                             | K            | int64                |            |
|   2 | z_spec                         | D            | float64              |            |
|   3 | z_a                            | E            | float32              |            |
|   4 | z_ml                           | E            | float32              |            |
|   5 | chi_a                          | E            | float32              |            |
|   6 | l68                            | D            | float64              |            |
|   7 | u68                            | D            | float64              |            |
|   8 | l95                            | D            | float64              |            |
|   9 | u95                            | D            | float64              |            |
|  10 | l99                            | D            | float64              |            |
|  11 | u99                            | D            | float64              |            |
|  12 | nfilt                          | K            | int64                |            |
|  13 | z_peak                         | D            | float64              |            |
|  14 | chi_peak                       | D            | float64              |            |
|  15 | z025                           | E            | float32              |            |
|  16 | z160                           | E            | float32              |            |
|  17 | z500                           | E            | float32              |            |
|  18 | z840                           | E            | float32              |            |
|  19 | z975                           | E            | float32              |            |
|  20 | Prob_gt_5                      | D            | float64              |            |
|  21 | Prob_gt_6                      | D            | float64              |            |
|  22 | Prob_gt_7                      | D            | float64              |            |
|  23 | Prob_gt_8                      | D            | float64              |            |
|  24 | Prob_gt_9                      | D            | float64              |            |
|  25 | chisq_z_lt_7                   | D            | float64              |            |
|  26 | z_chisq_z_lt_7                 | D            | float64              |            |
|  27 | chisq_z_lt_6                   | D            | float64              |            |
|  28 | z_chisq_z_lt_6                 | D            | float64              |            |
|  29 | chisq_z_lt_5                   | D            | float64              |            |
|  30 | z_chisq_z_lt_5                 | D            | float64              |            |
|  31 | chisq_z_lt_4                   | D            | float64              |            |
|  32 | z_chisq_z_lt_4                 | D            | float64              |            |
|  33 | z_bins                         | 22D          | float64[22]          |            |
|  34 | Prob_z_bins                    | 22D          | float64[22]          |            |

### GOODS-N — Research Column Availability

| Needed For Research | Found? |
|---------------------|--------|
| photo-z (EAZY) | YES |
| spectroscopic z | YES |
| RA/Dec coordinates | YES |
| quality flags | YES |
| NIRCam photometry (F090W-F444W) | YES |
| effective radius (R_eff) | YES |
| Kron photometry | YES |
| MIRI photometry | YES |
| stellar mass (log M*) | NO |
| star formation rate (SFR) | NO |
| photo-z probability (Prob_gt_z) | YES |

---

## Summary & Conclusions

**Most required columns are present, but some are absent from this catalog:**

#### Present in catalog

- photo-z (EAZY): GOODS-S: YES, GOODS-N: YES
- spectroscopic z: GOODS-S: YES, GOODS-N: YES
- RA/Dec coordinates: GOODS-S: YES, GOODS-N: YES
- quality flags: GOODS-S: YES, GOODS-N: YES
- NIRCam photometry (F090W-F444W): GOODS-S: YES, GOODS-N: YES
- effective radius (R_eff): GOODS-S: YES, GOODS-N: YES
- Kron photometry: GOODS-S: YES, GOODS-N: YES
- MIRI photometry: GOODS-S: YES, GOODS-N: YES
- photo-z probability (Prob_gt_z): GOODS-S: YES, GOODS-N: YES

#### NOT present in this catalog

- **stellar mass (log M*)**: GOODS-S: NO, GOODS-N: NO
- **star formation rate (SFR)**: GOODS-S: NO, GOODS-N: NO

> **Note:** JADES DR5 is a **photometric catalog** (flux measurements + EAZY photo-z fitting).
> Stellar mass (log M*) and SFR require **SED fitting** (e.g., Prospector, BAGPIPES, CIGALE),
> which is a separate analysis step not included in this catalog release.
> These physical parameters must be derived from the photometry during our analysis (Step 3),
> or obtained from a separate value-added catalog if one is published for DR5.

### Key Extensions for the Anomaly Search

1. **FLAG** — Source ID, RA, Dec, per-band quality flags and weights
2. **PHOTOZ** — EAZY photo-z from small-aperture photometry (z_peak, z_a, z_ml, z_spec, chi-squared comparisons at z<4/5/6/7)
3. **PHOTOZ_KRON** — EAZY photo-z from Kron photometry (same columns as PHOTOZ)
4. **SIZE** — Morphological parameters (R_kron, semi-major/minor axes, position angle)
5. **KRON / KRON_CONV** — Kron aperture photometry in all NIRCam bands
6. **MIRI** — MIRI photometry (F770W, F1000W, F1280W, etc.)
7. **CIRC / CIRC_BSUB / CIRC_CONV / CIRC_BSUB_CONV** — Circular aperture photometry (multiple aperture sizes)

### Recommended Query Strategy

To build the z > 6 sample without downloading the full files:
1. Download only the FLAG + PHOTOZ extensions (~230 MB for GOODS-N, ~360 MB for GOODS-S)
2. Filter on z_peak > 6 or z_a > 6
3. For surviving candidates, fetch KRON + SIZE data
4. Only download CIRC/MIRI extensions if needed for specific analysis
