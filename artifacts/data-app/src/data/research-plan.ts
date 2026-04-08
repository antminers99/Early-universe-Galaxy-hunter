export interface JWSTProgram {
  name: string;
  nameAr: string;
  field: string;
  instruments: string;
  status: string;
  catalogSize: string;
  redshiftRange: string;
  url: string;
  description: string;
  descriptionAr: string;
  priority: "start-here" | "primary" | "support";
}

export const jwstPrograms: JWSTProgram[] = [
  {
    name: "JADES DR5",
    nameAr: "JADES DR5",
    field: "GOODS-S, GOODS-N",
    instruments: "NIRCam + NIRSpec + MIRI",
    status: "عام — أحدث وأكبر إصدار",
    catalogSize: "~30 GB كتالوجات + ~2 TB صور",
    redshiftRange: "z > 8 (photo), z > 13 (spec)",
    url: "https://jades-survey.github.io/scientists/data.html",
    description: "Largest JWST deep survey with DR5 including data from 24+ programs. Photometric catalog with z>8 candidates.",
    descriptionAr: "أكبر مسح عميق لـ JWST — الكتالوج الفوتومتري يحوي آلاف المرشحين عند z > 8",
    priority: "start-here"
  },
  {
    name: "CEERS",
    nameAr: "CEERS",
    field: "Extended Groth Strip",
    instruments: "NIRCam + MIRI + NIRSpec",
    status: "عام — DR0.7+",
    catalogSize: "~15 GB كتالوجات + ~500 GB صور",
    redshiftRange: "z ~ 0.5 - 14",
    url: "https://ceers.github.io/dr07.html",
    description: "Cosmic Evolution Early Release Science survey targeting EGS field.",
    descriptionAr: "مسح التطور الكوني — يستهدف حقل EGS بأدوات متعددة",
    priority: "primary"
  },
  {
    name: "UNCOVER",
    nameAr: "UNCOVER",
    field: "Abell 2744 (عنقود عدسي)",
    instruments: "NIRCam + NIRSpec/PRISM",
    status: "عام — DR3",
    catalogSize: "~10 GB كتالوجات",
    redshiftRange: "z ~ 0.2 - 15",
    url: "https://jwst-uncover.github.io/",
    description: "Deep NIRCam imaging + ultradeep spectroscopy behind lensing cluster Abell 2744.",
    descriptionAr: "تصوير عميق + أطياف فائقة العمق خلف العنقود العدسي Abell 2744",
    priority: "primary"
  },
  {
    name: "COSMOS-Web / COSMOS2025",
    nameAr: "COSMOS2025",
    field: "حقل COSMOS",
    instruments: "NIRCam + MIRI",
    status: "عام — كتالوج شامل",
    catalogSize: "~20 GB كتالوج",
    redshiftRange: "z ~ 0.1 - 12+",
    url: "https://cosmos2025.iap.fr/",
    description: "Wide-area JWST+HST+ground catalog with photometry, morphology, redshifts, and physical parameters.",
    descriptionAr: "كتالوج واسع يجمع JWST + هابل + تلسكوبات أرضية مع فوتومتري وتصنيف ومعاملات فيزيائية",
    priority: "primary"
  },
  {
    name: "GLASS-JWST",
    nameAr: "GLASS-JWST",
    field: "Abell 2744",
    instruments: "NIRCam + NIRSpec",
    status: "عام — ERS",
    catalogSize: "~5 GB",
    redshiftRange: "z ~ 6 - 13",
    url: "https://archive.stsci.edu/hlsp/glass-jwst",
    description: "Deepest ERS observations through Abell 2744 lensing cluster.",
    descriptionAr: "أعمق أرصاد برنامج الإطلاق المبكر عبر العنقود العدسي Abell 2744",
    priority: "primary"
  }
];

export interface ResearchStep {
  number: number;
  titleAr: string;
  descriptionAr: string;
  duration: string;
  skills: string[];
  status: "pending" | "in-progress" | "done";
  details: string[];
}

export const researchSteps: ResearchStep[] = [
  {
    number: 1,
    titleAr: "تنزيل الكتالوجات",
    descriptionAr: "تنزيل الكتالوجات الفوتومترية من JADES DR5 و CEERS و UNCOVER و COSMOS2025",
    duration: "يوم واحد",
    skills: ["Download Manager", "Metadata Reader"],
    status: "pending",
    details: [
      "الإحداثيات (RA, Dec)",
      "الانزياح الأحمر الفوتومتري (photo-z) ومجالات الخطأ",
      "الألوان (NIRCam: F090W, F115W, F150W, F200W, F277W, F356W, F444W)",
      "الكتلة النجمية المقدرة (log M*)",
      "الحجم الفعال (R_eff)",
      "معدل تشكل النجوم (SFR)",
      "أعلام الجودة"
    ]
  },
  {
    number: 2,
    titleAr: "تنظيف واختيار العينة",
    descriptionAr: "تنقية البيانات واختيار المجرات عند z > 6 مع استبعاد المصادر غير الموثوقة",
    duration: "يوم واحد",
    skills: ["Data Cleaner"],
    status: "pending",
    details: [
      "اختيار z_phot > 6 فقط",
      "استبعاد مصادر بأعلام جودة سيئة",
      "استبعاد النجوم (star/galaxy classification)",
      "توحيد الأعمدة بين الكتالوجات الأربعة",
      "إزالة المكررات عند تقاطع الحقول",
      "المخرج المتوقع: ~1,000-10,000 مرشح"
    ]
  },
  {
    number: 3,
    titleAr: "صيد الشواذ",
    descriptionAr: "تحديد المجرات ذات الخصائص غير المتوقعة — كتلة عالية، ألوان شاذة، أحجام صغيرة",
    duration: "2-3 أيام",
    skills: ["Outlier Hunter", "Population Analyzer", "Pattern Finder", "Figure Builder"],
    status: "pending",
    details: [
      "رسم توزعات الخصائص الأساسية",
      "مجرات بكتلة > 10^9.5 M\u2609 عند z > 10",
      "مجرات بألوان حمراء غير متوقعة عند z > 8",
      "مجرات صغيرة جدًا بكتلة عالية (compact massive)",
      "أي جرم يقع بعيدًا > 3\u03C3 عن التوزع الرئيسي",
      "إنشاء قائمة قصيرة: 10-50 مرشح"
    ]
  },
  {
    number: 4,
    titleAr: "محاولة القتل",
    descriptionAr: "فحص كل مرشح بحثًا عن تفسيرات بديلة وانحيازات ومشاكل بيانات",
    duration: "3-5 أيام",
    skills: ["Bias Checker", "Alternative Explanation Finder", "Hypothesis Killer", "Paper Finder"],
    status: "pending",
    details: [
      "فحص موثوقية photo-z (مقارنة بين كتالوجات)",
      "استبعاد dusty low-z interlopers",
      "فحص التلوث (نجوم بنية، cosmic rays)",
      "فحص التضخيم العدسي في حقل UNCOVER",
      "مقارنة مع صور NIRCam الخام",
      "بحث في الأدبيات — هل الجرم منشور سابقًا؟"
    ]
  },
  {
    number: 5,
    titleAr: "الفحص الخارجي",
    descriptionAr: "مطابقة المرشحين الناجين مع Euclid Q1 و DESI DR1 كفحص مستقل",
    duration: "2-3 أيام",
    skills: ["Catalog Cross-Matcher", "Result Summarizer", "Report Writer"],
    status: "pending",
    details: [
      "مطابقة مع Euclid Q1 (إذا الحقل مغطى)",
      "مطابقة مع DESI DR1 للأطياف",
      "مقارنة مع كتالوجات Hubble السابقة",
      "كتابة تقرير النتائج النهائي"
    ]
  }
];

export interface AnomalyType {
  nameAr: string;
  descriptionAr: string;
  criterion: string;
  icon: string;
}

export const anomalyTypes: AnomalyType[] = [
  {
    nameAr: "أشد لمعانًا من المتوقع",
    descriptionAr: "المجرة أسطع مما تتوقعه النماذج النظرية لتلك الحقبة",
    criterion: "UV luminosity > expected at given z",
    icon: "sun"
  },
  {
    nameAr: "أكثر احمرارًا من المتوقع",
    descriptionAr: "ألوان NIRCam تشير لكتلة نجمية عالية أو غبار غزير — غريب في كون شاب",
    criterion: "F277W-F444W color excess",
    icon: "palette"
  },
  {
    nameAr: "أصغر/أكثر تماسكًا من المتوقع",
    descriptionAr: "حجم فعال صغير جدًا مقارنة بالكتلة — مجرة مضغوطة بشكل غير عادي",
    criterion: "R_eff << expected for M*",
    icon: "minimize"
  },
  {
    nameAr: "أنضج من عمرها",
    descriptionAr: "كتلة نجمية عالية تتطلب وقتًا أطول مما يسمح به عمر الكون في تلك اللحظة",
    criterion: "log M* > 9.5 at z > 10",
    icon: "clock"
  }
];
