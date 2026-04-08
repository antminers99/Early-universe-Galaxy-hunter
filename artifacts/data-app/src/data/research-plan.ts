export interface JWSTProgram {
  name: string;
  field: string;
  instruments: string;
  status: string;
  catalogSize: string;
  redshiftRange: string;
  url: string;
  description: string;
  priority: "start-here" | "primary" | "support";
}

export const jwstPrograms: JWSTProgram[] = [
  {
    name: "JADES DR5",
    field: "GOODS-S, GOODS-N",
    instruments: "NIRCam + NIRSpec + MIRI",
    status: "Public — latest and largest release",
    catalogSize: "~30 GB catalogs + ~2 TB images",
    redshiftRange: "z > 8 (photo), z > 13 (spec)",
    url: "https://jades-survey.github.io/scientists/data.html",
    description: "Largest JWST deep survey with DR5 including data from 24+ programs. Photometric catalog with z>8 candidates.",
    priority: "start-here"
  },
  {
    name: "CEERS",
    field: "Extended Groth Strip",
    instruments: "NIRCam + MIRI + NIRSpec",
    status: "Public — DR0.7+",
    catalogSize: "~15 GB catalogs + ~500 GB images",
    redshiftRange: "z ~ 0.5 - 14",
    url: "https://ceers.github.io/dr07.html",
    description: "Cosmic Evolution Early Release Science survey targeting the EGS field with multiple instruments.",
    priority: "primary"
  },
  {
    name: "UNCOVER",
    field: "Abell 2744 (lensing cluster)",
    instruments: "NIRCam + NIRSpec/PRISM",
    status: "Public — DR3",
    catalogSize: "~10 GB catalogs",
    redshiftRange: "z ~ 0.2 - 15",
    url: "https://jwst-uncover.github.io/",
    description: "Deep NIRCam imaging + ultradeep spectroscopy behind lensing cluster Abell 2744.",
    priority: "primary"
  },
  {
    name: "COSMOS-Web / COSMOS2025",
    field: "COSMOS field",
    instruments: "NIRCam + MIRI",
    status: "Public — comprehensive catalog",
    catalogSize: "~20 GB catalog",
    redshiftRange: "z ~ 0.1 - 12+",
    url: "https://cosmos2025.iap.fr/",
    description: "Wide-area JWST+HST+ground catalog with photometry, morphology, redshifts, and physical parameters.",
    priority: "primary"
  },
  {
    name: "GLASS-JWST",
    field: "Abell 2744",
    instruments: "NIRCam + NIRSpec",
    status: "Public — ERS",
    catalogSize: "~5 GB",
    redshiftRange: "z ~ 6 - 13",
    url: "https://archive.stsci.edu/hlsp/glass-jwst",
    description: "Deepest Early Release Science observations through the Abell 2744 lensing cluster.",
    priority: "primary"
  }
];

export interface ResearchStep {
  number: number;
  title: string;
  description: string;
  duration: string;
  skills: string[];
  status: "pending" | "in-progress" | "done";
  details: string[];
}

export const researchSteps: ResearchStep[] = [
  {
    number: 1,
    title: "Download Catalogs",
    description: "Download photometric catalogs from JADES DR5, CEERS, UNCOVER, and COSMOS2025.",
    duration: "1 day",
    skills: ["Download Manager", "Metadata Reader"],
    status: "pending",
    details: [
      "Coordinates (RA, Dec)",
      "Photometric redshift (photo-z) and error ranges",
      "Colors (NIRCam: F090W, F115W, F150W, F200W, F277W, F356W, F444W)",
      "Estimated stellar mass (log M*)",
      "Effective radius (R_eff)",
      "Star formation rate (SFR)",
      "Quality flags"
    ]
  },
  {
    number: 2,
    title: "Clean & Select Sample",
    description: "Clean data and select galaxies at z > 6, excluding unreliable sources.",
    duration: "1 day",
    skills: ["Data Cleaner"],
    status: "pending",
    details: [
      "Select z_phot > 6 only",
      "Exclude sources with bad quality flags",
      "Exclude stars (star/galaxy classification)",
      "Unify columns across all four catalogs",
      "Remove duplicates at field overlaps",
      "Expected output: ~1,000-10,000 candidates"
    ]
  },
  {
    number: 3,
    title: "Hunt Outliers",
    description: "Identify galaxies with unexpected properties — high mass, anomalous colors, compact sizes.",
    duration: "2-3 days",
    skills: ["Outlier Hunter", "Population Analyzer", "Pattern Finder", "Figure Builder"],
    status: "pending",
    details: [
      "Plot distributions of key properties",
      "Galaxies with mass > 10^9.5 M\u2609 at z > 10",
      "Galaxies with unexpectedly red colors at z > 8",
      "Very compact galaxies with high mass (compact massive)",
      "Any object > 3\u03C3 from the main distribution",
      "Build shortlist: 10-50 candidates"
    ]
  },
  {
    number: 4,
    title: "Kill the Hypothesis",
    description: "Examine each candidate for alternative explanations, biases, and data issues.",
    duration: "3-5 days",
    skills: ["Bias Checker", "Alternative Explanation Finder", "Hypothesis Killer", "Paper Finder"],
    status: "pending",
    details: [
      "Check photo-z reliability (cross-catalog comparison)",
      "Exclude dusty low-z interlopers",
      "Check for contamination (brown dwarfs, cosmic rays)",
      "Check lensing magnification in UNCOVER field",
      "Compare with raw NIRCam images",
      "Literature search — is this object previously published?"
    ]
  },
  {
    number: 5,
    title: "External Validation",
    description: "Cross-match surviving candidates with Euclid Q1 and DESI DR1 for independent verification.",
    duration: "2-3 days",
    skills: ["Catalog Cross-Matcher", "Result Summarizer", "Report Writer"],
    status: "pending",
    details: [
      "Match with Euclid Q1 (if field is covered)",
      "Match with DESI DR1 for spectroscopy",
      "Compare with previous Hubble catalogs",
      "Write final results report"
    ]
  }
];

export interface AnomalyType {
  name: string;
  description: string;
  criterion: string;
  icon: string;
}

export const anomalyTypes: AnomalyType[] = [
  {
    name: "Brighter Than Expected",
    description: "The galaxy is more luminous than theoretical models predict for that epoch.",
    criterion: "UV luminosity > expected at given z",
    icon: "sun"
  },
  {
    name: "Redder Than Expected",
    description: "NIRCam colors suggest high stellar mass or abundant dust — unusual in a young universe.",
    criterion: "F277W-F444W color excess",
    icon: "palette"
  },
  {
    name: "Smaller / More Compact Than Expected",
    description: "Very small effective radius compared to stellar mass — an unusually compressed galaxy.",
    criterion: "R_eff << expected for M*",
    icon: "minimize"
  },
  {
    name: "More Mature Than Its Age",
    description: "High stellar mass requiring more time to assemble than the age of the universe at that moment allows.",
    criterion: "log M* > 9.5 at z > 10",
    icon: "clock"
  }
];
