export interface Dataset {
  name: string;
  nameAr: string;
  description: string;
  descriptionAr: string;
  url: string;
  size: string;
  format: string;
  priority: "essential" | "important" | "supplementary";
}

export interface Category {
  id: string;
  title: string;
  titleAr: string;
  description: string;
  descriptionAr: string;
  icon: string;
  color: string;
  datasets: Dataset[];
}

export const categories: Category[] = [
  {
    id: "jwst",
    title: "James Webb Space Telescope (JWST)",
    titleAr: "تلسكوب جيمس ويب الفضائي",
    description: "The primary gateway to early universe observations - first galaxies and early light",
    descriptionAr: "البوابة الأساسية لرصد الكون المبكر - أول المجرات والضوء المبكر",
    icon: "telescope",
    color: "from-amber-500/20 to-orange-500/20 dark:from-amber-500/10 dark:to-orange-500/10",
    datasets: [
      {
        name: "MAST Portal",
        nameAr: "بوابة MAST",
        description: "Direct search, download, and preview of all JWST data",
        descriptionAr: "البحث المباشر في داتا JWST والتنزيل والمعاينة",
        url: "https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html",
        size: "~270 TB",
        format: "FITS, ASDF",
        priority: "essential"
      },
      {
        name: "JWST Mission Page on MAST",
        nameAr: "صفحة مهمة JWST على MAST",
        description: "Mission-level data and basic information collection",
        descriptionAr: "بيانات المهمة نفسها ومعلوماتها الأساسية",
        url: "https://archive.stsci.edu/missions-and-data/jwst",
        size: "~270 TB (shared with MAST)",
        format: "FITS, ASDF",
        priority: "essential"
      },
      {
        name: "JWST Data Access Guide",
        nameAr: "دليل الوصول لداتا JWST",
        description: "Official guide for correct data download procedures",
        descriptionAr: "أهم دليل رسمي لتنزيل الداتا بشكل صحيح",
        url: "https://jwst-docs.stsci.edu/jwst-data-access",
        size: "Documentation",
        format: "Web",
        priority: "essential"
      },
      {
        name: "JWST Web Access",
        nameAr: "الوصول عبر الويب لداتا JWST",
        description: "Browser-based data access interface",
        descriptionAr: "الوصول من خلال المتصفح فقط",
        url: "https://jwst-docs.stsci.edu/jwst-data-access/jwst-data-access-overview",
        size: "Web interface",
        format: "Web",
        priority: "important"
      },
      {
        name: "JWST Programmatic/API Access",
        nameAr: "الوصول البرمجي/API لداتا JWST",
        description: "Essential for AI/Python automation and programmatic workflows",
        descriptionAr: "مهم للذكاء الصناعي مع بايثون أو الأتمتة",
        url: "https://jwst-docs.stsci.edu/jwst-data-access/jwst-programmatic-data-access",
        size: "API access",
        format: "REST API, astroquery",
        priority: "essential"
      },
      {
        name: "High Level Science Products (HLSP)",
        nameAr: "منتجات علمية عالية المستوى",
        description: "Pre-processed, cleaner data products from various projects",
        descriptionAr: "منتجات جاهزة أنظف وأسهل من الخام",
        url: "https://archive.stsci.edu/hlsp/",
        size: "~50 TB",
        format: "FITS, CSV, ECSV",
        priority: "important"
      },
      {
        name: "JWST Early Release Observations (ERO)",
        nameAr: "أرصاد الإطلاق المبكر",
        description: "Excellent for quick start and initial understanding",
        descriptionAr: "ممتاز للبداية السريعة والفهم الأولي",
        url: "https://archive.stsci.edu/hlsp/ero",
        size: "~2 TB",
        format: "FITS",
        priority: "important"
      }
    ]
  },
  {
    id: "cmb",
    title: "Cosmic Microwave Background (CMB)",
    titleAr: "الخلفية الكونية الميكروية",
    description: "The universe at age ~380,000 years - closest to the 'baby universe'",
    descriptionAr: "صورة الكون بعمر 380 ألف سنة - أقرب ما يكون للكون الطفل",
    icon: "waves",
    color: "from-blue-500/20 to-cyan-500/20 dark:from-blue-500/10 dark:to-cyan-500/10",
    datasets: [
      {
        name: "Planck Legacy Archive (PLA)",
        nameAr: "أرشيف بلانك",
        description: "One of the most important archives for the early universe",
        descriptionAr: "من أهم أرشيفات الكون المبكر على الإطلاق",
        url: "https://pla.esac.esa.int/",
        size: "~30 TB",
        format: "FITS, HEALPix",
        priority: "essential"
      },
      {
        name: "Planck Archive Documentation",
        nameAr: "شرح أرشيف بلانك من ESA",
        description: "Understanding archive contents before downloading",
        descriptionAr: "لمعرفة ماذا يوجد داخله قبل تنزيل أي شيء",
        url: "https://www.cosmos.esa.int/web/planck/planck-legacy-archive",
        size: "Documentation",
        format: "Web",
        priority: "important"
      },
      {
        name: "NASA LAMBDA",
        nameAr: "ناسا LAMBDA",
        description: "NASA's primary center for CMB data, tools, and links",
        descriptionAr: "مركز ناسا الأساسي لداتا الخلفية الكونية وأدواتها",
        url: "https://lambda.gsfc.nasa.gov/",
        size: "~15 TB (all hosted data)",
        format: "FITS, HEALPix, Text",
        priority: "essential"
      },
      {
        name: "LAMBDA Hosted Data",
        nameAr: "كل الداتا المستضافة على LAMBDA",
        description: "All experiments and public products in one place",
        descriptionAr: "التجارب والمنتجات العامة كلها تقريبا",
        url: "https://lambda.gsfc.nasa.gov/product/",
        size: "~15 TB",
        format: "FITS, HEALPix",
        priority: "important"
      },
      {
        name: "LAMBDA CMB Experiments",
        nameAr: "كل تجارب CMB على LAMBDA",
        description: "All CMB sources from a single access point",
        descriptionAr: "كل المصادر من مكان واحد",
        url: "https://lambda.gsfc.nasa.gov/product/expt/",
        size: "Varies by experiment",
        format: "FITS, HEALPix",
        priority: "important"
      },
      {
        name: "BICEP/Keck Data Products",
        nameAr: "بيانات BICEP/Keck",
        description: "Important for searching primordial signals like gravitational waves",
        descriptionAr: "مهم للبحث عن آثار أقدم مثل موجات بدئية محتملة",
        url: "https://lambda.gsfc.nasa.gov/product/bicepkeck/",
        size: "~5 GB",
        format: "FITS, HEALPix",
        priority: "important"
      },
      {
        name: "ACT DR6 Data Products",
        nameAr: "بيانات ACT DR6",
        description: "Modern, powerful CMB data release",
        descriptionAr: "داتا حديثة وقوية جدا في CMB",
        url: "https://lambda.gsfc.nasa.gov/product/act/actpol_prod_table.html",
        size: "~500 GB",
        format: "FITS, HEALPix",
        priority: "important"
      }
    ]
  },
  {
    id: "early-galaxies",
    title: "First Galaxies & Early Universe",
    titleAr: "أول المجرات والكون المبكر",
    description: "Completing JWST with complementary observations of early cosmic structures",
    descriptionAr: "تكملة JWST - أرصاد مكملة للبنى الكونية المبكرة",
    icon: "sparkles",
    color: "from-purple-500/20 to-violet-500/20 dark:from-purple-500/10 dark:to-violet-500/10",
    datasets: [
      {
        name: "MAST Home (Hubble + more)",
        nameAr: "بوابة MAST الرئيسية",
        description: "Not just JWST - also Hubble and many related datasets",
        descriptionAr: "ليس فقط JWST، بل هابل وبيانات كثيرة مرتبطة",
        url: "https://mast.stsci.edu/",
        size: "~500 TB (all missions)",
        format: "FITS, ASDF, CSV",
        priority: "essential"
      },
      {
        name: "Webb Early Universe Science",
        nameAr: "صفحة علوم الكون المبكر لويب",
        description: "Key reference for understanding what we're searching for in early stages",
        descriptionAr: "أهم صفحة لمعرفة ما الذي نبحث عنه في المراحل الأولى",
        url: "https://jwst-docs.stsci.edu/methods-and-roadmaps/jwst-early-universe",
        size: "Documentation",
        format: "Web",
        priority: "important"
      },
      {
        name: "ALMA Science Archive",
        nameAr: "أرشيف ALMA العلمي",
        description: "Critical for dust, gas, and early galaxies - complements Webb",
        descriptionAr: "مهم جدا للغبار والغاز والمجرات المبكرة ويكمل Webb",
        url: "https://almascience.nrao.edu/aq/",
        size: "~1.5 PB",
        format: "FITS, MS (Measurement Sets)",
        priority: "essential"
      }
    ]
  },
  {
    id: "surveys",
    title: "Large-Scale Surveys",
    titleAr: "المسوحات الكبيرة",
    description: "Connecting primordial seeds to observed cosmic structure evolution",
    descriptionAr: "ربط البذور الأولى بتطور البنية الكونية التي نراها",
    icon: "grid",
    color: "from-emerald-500/20 to-teal-500/20 dark:from-emerald-500/10 dark:to-teal-500/10",
    datasets: [
      {
        name: "Euclid Q1 Data Access",
        nameAr: "بيانات Euclid Q1",
        description: "Recent and very important public data release",
        descriptionAr: "داتا عامة حديثة ومهمة جدا",
        url: "https://www.cosmos.esa.int/web/euclid/euclid-early-release-observations",
        size: "~260 TB",
        format: "FITS, VOTable",
        priority: "essential"
      },
      {
        name: "Euclid Q1 Documentation",
        nameAr: "توثيق Euclid Q1",
        description: "Important to read before downloading",
        descriptionAr: "مهم قراءته قبل التنزيل",
        url: "https://www.cosmos.esa.int/web/euclid/documentation",
        size: "Documentation",
        format: "Web",
        priority: "important"
      },
      {
        name: "Euclid Q1 Papers",
        nameAr: "أوراق Euclid Q1",
        description: "First papers built on the same data",
        descriptionAr: "قائمة الأوراق الأولى المبنية على الداتا نفسها",
        url: "https://www.cosmos.esa.int/web/euclid/euclid-q1-papers",
        size: "Papers",
        format: "PDF",
        priority: "supplementary"
      },
      {
        name: "DESI DR1",
        nameAr: "بيانات DESI DR1",
        description: "Galaxy and quasar distribution, large-scale structure. DR1 has 18M+ unique target spectra",
        descriptionAr: "توزع المجرات والكويزرات والبنية الكبيرة. أكثر من 18 مليون هدف فريد",
        url: "https://data.desi.lbl.gov/doc/releases/",
        size: "~1.2 TB",
        format: "FITS, HDF5, CSV",
        priority: "essential"
      },
      {
        name: "DESI Papers",
        nameAr: "أوراق DESI الأساسية",
        description: "Foundation papers to avoid starting from scratch",
        descriptionAr: "حتى لا نبدأ من الصفر",
        url: "https://data.desi.lbl.gov/doc/papers/",
        size: "Papers",
        format: "PDF",
        priority: "supplementary"
      },
      {
        name: "DESI Database Access",
        nameAr: "قواعد بيانات DESI",
        description: "Very useful for structured, filterable work",
        descriptionAr: "مفيد جدا للشغل المنظم والقابل للفلترة",
        url: "https://data.desi.lbl.gov/doc/access/",
        size: "API access",
        format: "SQL, REST API",
        priority: "important"
      },
      {
        name: "SDSS DR19 Data Access",
        nameAr: "بيانات SDSS DR19",
        description: "Massive treasure of spectra, quasars, connecting early universe to later distribution",
        descriptionAr: "كنز كبير للأطياف والكويزرات وربط الكون المبكر بالتوزع اللاحق",
        url: "https://www.sdss.org/dr19/data_access/",
        size: "~70 TB",
        format: "FITS, CSV, CASJobs",
        priority: "essential"
      },
      {
        name: "SDSS DR19 Bulk Downloads",
        nameAr: "تنزيل SDSS DR19 بالجملة",
        description: "For actual downloading instead of just browsing",
        descriptionAr: "للتنزيل الفعلي بدل التصفح فقط",
        url: "https://www.sdss.org/dr19/data_access/bulk/",
        size: "~70 TB",
        format: "FITS, CSV",
        priority: "important"
      },
      {
        name: "SDSS API / Valis",
        nameAr: "واجهة SDSS البرمجية",
        description: "Important for programmatic workflows",
        descriptionAr: "مهم للشغل البرمجي",
        url: "https://www.sdss.org/dr19/data_access/api/",
        size: "API access",
        format: "REST API",
        priority: "important"
      }
    ]
  },
  {
    id: "reionization",
    title: "Epoch of Reionization",
    titleAr: "عصر إعادة التأين",
    description: "Approaching 'cosmic darkness' - earlier than first galaxies",
    descriptionAr: "الاقتراب من الظلام الكوني - مراحل أسبق من أول المجرات",
    icon: "radio",
    color: "from-rose-500/20 to-pink-500/20 dark:from-rose-500/10 dark:to-pink-500/10",
    datasets: [
      {
        name: "HERA Public Data Release 1",
        nameAr: "بيانات HERA العامة",
        description: "One of the most important current datasets in this field",
        descriptionAr: "من أهم ما عندنا حاليا في هذا الباب",
        url: "https://reionization.org/science/public-data-release-1/",
        size: "~200 GB",
        format: "HDF5, uvh5",
        priority: "essential"
      },
      {
        name: "HERA Main Site",
        nameAr: "موقع HERA الرئيسي",
        description: "Access to papers, memos, and updates",
        descriptionAr: "الأوراق والميموز والتحديثات",
        url: "https://reionization.org/",
        size: "Documentation",
        format: "Web",
        priority: "important"
      },
      {
        name: "HERA Papers",
        nameAr: "أوراق HERA",
        description: "Understanding what was examined and what remains open",
        descriptionAr: "لفهم ماذا فحصوا وماذا بقي مفتوحا",
        url: "https://reionization.org/science/papers/",
        size: "Papers",
        format: "PDF",
        priority: "supplementary"
      },
      {
        name: "MWA Data Access",
        nameAr: "بيانات MWA",
        description: "Important radio data for similar research questions",
        descriptionAr: "داتا راديوية مهمة لنفس النوع من الأسئلة تقريبا",
        url: "https://www.mwatelescope.org/data",
        size: "~30 PB (raw), ~5 TB (processed)",
        format: "FITS, MS",
        priority: "important"
      }
    ]
  },
  {
    id: "gravitational-waves",
    title: "Gravitational Waves",
    titleAr: "موجات الجاذبية",
    description: "An additional, harder path - useful for reaching even deeper",
    descriptionAr: "باب إضافي أصعب - مفيد للوصول أبعد لاحقا",
    icon: "activity",
    color: "from-slate-500/20 to-gray-500/20 dark:from-slate-500/10 dark:to-gray-500/10",
    datasets: [
      {
        name: "GWOSC",
        nameAr: "مركز بيانات موجات الجاذبية المفتوحة",
        description: "Open gravitational wave data - useful for harder, deeper exploration later",
        descriptionAr: "ليس الخيار الأول للمراحل الأولى لكنه مفيد لاحقا",
        url: "https://gwosc.org/",
        size: "~40 TB",
        format: "HDF5, GWF",
        priority: "supplementary"
      }
    ]
  }
];

export const quickStartOrder = [
  { name: "JWST / MAST Portal", url: "https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html", step: 1 },
  { name: "JWST Access Docs", url: "https://jwst-docs.stsci.edu/jwst-data-access", step: 2 },
  { name: "Planck Archive", url: "https://pla.esac.esa.int/", step: 3 },
  { name: "NASA LAMBDA", url: "https://lambda.gsfc.nasa.gov/", step: 4 },
  { name: "Euclid Q1 Data", url: "https://www.cosmos.esa.int/web/euclid/euclid-early-release-observations", step: 5 },
  { name: "DESI DR1", url: "https://data.desi.lbl.gov/doc/releases/", step: 6 },
  { name: "SDSS DR19", url: "https://www.sdss.org/dr19/data_access/", step: 7 },
  { name: "HERA DR1", url: "https://reionization.org/science/public-data-release-1/", step: 8 },
];

export function getTotalSize(): string {
  return "~1.2+ PB";
}

export function getDatasetCount(): number {
  return categories.reduce((sum, cat) => sum + cat.datasets.length, 0);
}

export function getCategoryCount(): number {
  return categories.length;
}

export function getEssentialCount(): number {
  return categories.reduce(
    (sum, cat) => sum + cat.datasets.filter(d => d.priority === "essential").length,
    0
  );
}
