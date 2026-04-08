export interface DownloadFile {
  name: string;
  description: string;
  size: string;
  format: string;
  url: string;
  field?: string;
}

export interface DownloadSource {
  program: string;
  category: "primary-jwst" | "cross-validation" | "support";
  description: string;
  homepage: string;
  reference: string;
  files: DownloadFile[];
}

export const downloadSources: DownloadSource[] = [
  {
    program: "JADES DR5",
    category: "primary-jwst",
    description: "Largest JWST deep survey. Photometric catalogs with EAZY photo-z, 300K+ sources in GOODS-S and 180K+ in GOODS-N across 35 filters.",
    homepage: "https://jades-survey.github.io/scientists/data.html",
    reference: "Robertson et al. 2026, arXiv:2601.15956",
    files: [
      {
        name: "GOODS-S Photometric Catalog",
        description: "Full photometric catalog: ID, RA/Dec, flags, photometry (27+ bands), EAZY photo-z, Kron photometry, MIRI, morphology",
        size: "5.8 GB",
        format: "FITS",
        url: "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-S/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-s_photometry_v5.0_catalog.fits",
        field: "GOODS-S",
      },
      {
        name: "GOODS-N Photometric Catalog",
        description: "Full photometric catalog: ID, RA/Dec, flags, photometry (27+ bands), EAZY photo-z, Kron photometry, MIRI, morphology",
        size: "2.9 GB",
        format: "FITS",
        url: "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits",
        field: "GOODS-N",
      },
      {
        name: "GOODS-S Growth Curve Catalog",
        description: "Curve-of-growth photometry for aperture corrections",
        size: "~3 GB",
        format: "FITS",
        url: "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-S/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-s_growth_v5.0_catalog.fits",
        field: "GOODS-S",
      },
      {
        name: "GOODS-N Growth Curve Catalog",
        description: "Curve-of-growth photometry for aperture corrections",
        size: "~2 GB",
        format: "FITS",
        url: "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_growth_v5.0_catalog.fits",
        field: "GOODS-N",
      },
    ],
  },
  {
    program: "CEERS",
    category: "primary-jwst",
    description: "Cosmic Evolution Early Release Science survey. 80K+ galaxies in the Extended Groth Strip with 7 NIRCam + 7 HST filters, photo-z, and physical parameters.",
    homepage: "https://ceers.github.io/",
    reference: "Bagley et al. 2023; Cox et al. 2025, arXiv:2510.08743",
    files: [
      {
        name: "Photometric Catalog (Hot+Cold)",
        description: "PSF-matched photometry + LePHARE photo-z + stellar mass + SFR for 80K+ sources",
        size: "~500 MB",
        format: "FITS",
        url: "https://archive.stsci.edu/hlsps/ceers/ceers-full-grizli-v7.2-fix_phot_apcorr.fits",
        field: "EGS",
      },
      {
        name: "CEERS MAST HLSP Page",
        description: "All CEERS data products: mosaics, catalogs, segmentation maps, PSFs",
        size: "Various",
        format: "Multiple",
        url: "https://archive.stsci.edu/hlsp/ceers",
        field: "EGS",
      },
    ],
  },
  {
    program: "UNCOVER DR3",
    category: "primary-jwst",
    description: "Ultra-deep imaging + spectroscopy behind lensing cluster Abell 2744. 74K sources with EAZY photo-z across 27 HST+JWST bands.",
    homepage: "https://jwst-uncover.github.io/DR3.html",
    reference: "Suess et al. 2024, arXiv:2404.13132; Weaver et al. 2024",
    files: [
      {
        name: "SUPER Photometric Catalog",
        description: "Recommended catalog: optimal aperture photometry + EAZY redshifts + lensing magnifications for 74K sources",
        size: "~200 MB",
        format: "FITS",
        url: "https://drive.google.com/file/d/19Jd3Xg5BTrHX5icb81txSn_P0LqxmLsz/view?usp=sharing",
        field: "Abell 2744",
      },
      {
        name: "Zenodo Full Dataset",
        description: "Complete DR3 release including all aperture catalogs, mosaics, and photo-z PDFs",
        size: "~10 GB",
        format: "Multiple",
        url: "https://zenodo.org/records/11059273",
        field: "Abell 2744",
      },
      {
        name: "DR3 Page (All Files)",
        description: "Full listing of all available DR3 data products with README",
        size: "Various",
        format: "Multiple",
        url: "https://jwst-uncover.github.io/DR3.html",
        field: "Abell 2744",
      },
    ],
  },
  {
    program: "COSMOS2025",
    category: "primary-jwst",
    description: "Wide-area COSMOS catalog combining JWST + HST + ground-based data. Photometry, photo-z, stellar mass, morphology for the COSMOS field.",
    homepage: "https://cosmos2025.iap.fr/",
    reference: "Shuntov et al. 2025, A&A 704, A339",
    files: [
      {
        name: "COSMOS2025 Full Catalog",
        description: "Multi-wavelength photometry + photo-z + physical parameters + morphology",
        size: "~5 GB",
        format: "FITS",
        url: "https://cosmos2025.iap.fr/catalog.html",
        field: "COSMOS",
      },
      {
        name: "COSMOS-Web DR0.5 Mosaics",
        description: "NIRCam and MIRI reduced mosaic tiles at 30 and 60 mas pixel scale",
        size: "~50 GB",
        format: "FITS",
        url: "https://exchg.calet.org/cosmosweb-public/DR0.5/",
        field: "COSMOS",
      },
    ],
  },
  {
    program: "GLASS-JWST",
    category: "primary-jwst",
    description: "Deepest ERS observations through Abell 2744. Multi-wavelength photometry from 8 JWST + 8 HST filters, plus NIRSpec spectroscopy.",
    homepage: "https://archive.stsci.edu/hlsp/glass-jwst",
    reference: "Treu et al. 2022; Paris et al. 2023; Mascia et al. 2024",
    files: [
      {
        name: "Release 1: Photometric Catalog",
        description: "Multi-band photometric catalog combining JWST NIRCam (8 bands) + HST (8 bands)",
        size: "~100 MB",
        format: "FITS",
        url: "https://archive.stsci.edu/hlsp/glass-jwst",
        field: "Abell 2744",
      },
      {
        name: "Release 2: NIRSpec Spectroscopy",
        description: "263 spectra of 245 unique sources + emission line catalog",
        size: "~500 MB",
        format: "FITS",
        url: "https://archive.stsci.edu/hlsp/glass-jwst",
        field: "Abell 2744",
      },
      {
        name: "Release 3: NIRISS WFSS",
        description: "Wide-field slitless spectroscopy redshifts + emission line fluxes",
        size: "~200 MB",
        format: "FITS",
        url: "https://archive.stsci.edu/hlsp/glass-jwst",
        field: "Abell 2744",
      },
    ],
  },
  {
    program: "Euclid Q1",
    category: "cross-validation",
    description: "Euclid Quick Release 1: 63 sq. deg with 26 million detections in VIS + NISP imaging, covering Euclid Deep Fields North, Fornax, and South.",
    homepage: "https://easidr.esac.esa.int/",
    reference: "Euclid Collaboration 2025",
    files: [
      {
        name: "MER Final Catalog",
        description: "Main merged catalog with photometric & morphological info for all detected sources",
        size: "~20 GB",
        format: "FITS",
        url: "https://easidr.esac.esa.int/",
        field: "EDF-N, EDF-F, EDF-S",
      },
      {
        name: "NASA/IRSA Mirror",
        description: "Full Euclid Q1 data accessible via IRSA interface",
        size: "Various",
        format: "Multiple",
        url: "https://irsa.ipac.caltech.edu/data/Euclid/Q1/",
        field: "EDF-N, EDF-F, EDF-S",
      },
    ],
  },
  {
    program: "DESI DR1",
    category: "cross-validation",
    description: "Dark Energy Spectroscopic Instrument Data Release 1: 18M+ spectra from 13 months of operations. Spectroscopic redshifts for galaxies, quasars, and stars.",
    homepage: "https://data.desi.lbl.gov/doc/releases/dr1/",
    reference: "DESI Collaboration 2025",
    files: [
      {
        name: "zall-pix-iron.fits (Full Redshift Catalog)",
        description: "All spectroscopic redshifts across all surveys and programs (HEALPix-based)",
        size: "20.8 GB",
        format: "FITS",
        url: "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/",
        field: "All-sky footprint",
      },
      {
        name: "DESI DR1 Data Portal",
        description: "Browse all DR1 data products: spectra, redshifts, value-added catalogs",
        size: "Various",
        format: "Multiple",
        url: "https://data.desi.lbl.gov/doc/releases/dr1/",
        field: "All-sky footprint",
      },
    ],
  },
  {
    program: "Hubble Legacy Fields (HLF)",
    category: "support",
    description: "HST archival mosaics and catalogs in the GOODS/CANDELS fields. Essential for historical comparison with JWST data.",
    homepage: "https://archive.stsci.edu/prepds/hlf/",
    reference: "Illingworth et al. 2016; Whitaker et al. 2019",
    files: [
      {
        name: "HLF Mosaics & Catalogs",
        description: "Deep HST imaging mosaics in ACS + WFC3 bands for GOODS-S, GOODS-N, and other legacy fields",
        size: "~15 GB",
        format: "FITS",
        url: "https://archive.stsci.edu/prepds/hlf/",
        field: "GOODS-S, GOODS-N",
      },
    ],
  },
];
