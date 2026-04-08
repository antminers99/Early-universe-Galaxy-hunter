import { Link } from "wouter";
import {
  jwstPrograms,
  researchSteps,
  anomalyTypes,
} from "@/data/research-plan";
import {
  ExternalLink,
  Target,
  Telescope,
  FlaskConical,
  Skull,
  Search,
  FileCheck,
  Sun,
  Palette,
  Minimize2,
  Clock,
  AlertTriangle,
  CheckCircle2,
  Circle,
  ArrowRight,
  Sparkles,
  Shield,
  Brain,
} from "lucide-react";

const anomalyIcons: Record<string, React.ElementType> = {
  sun: Sun,
  palette: Palette,
  minimize: Minimize2,
  clock: Clock,
};

const stepIcons: Record<number, React.ElementType> = {
  1: Target,
  2: FlaskConical,
  3: Search,
  4: Skull,
  5: FileCheck,
};

const priorityLabels: Record<string, { text: string; bg: string; fg: string }> = {
  "start-here": { text: "ابدأ هنا", bg: "bg-emerald-100 dark:bg-emerald-900/30", fg: "text-emerald-700 dark:text-emerald-400" },
  primary: { text: "أساسي", bg: "bg-blue-100 dark:bg-blue-900/30", fg: "text-blue-700 dark:text-blue-400" },
  support: { text: "داعم", bg: "bg-gray-100 dark:bg-gray-800/50", fg: "text-gray-600 dark:text-gray-400" },
};

const statusIcons: Record<string, React.ElementType> = {
  pending: Circle,
  "in-progress": ArrowRight,
  done: CheckCircle2,
};

const statusLabels: Record<string, { text: string; color: string }> = {
  pending: { text: "لم يبدأ", color: "text-muted-foreground" },
  "in-progress": { text: "جاري العمل", color: "text-amber-600 dark:text-amber-400" },
  done: { text: "مكتمل", color: "text-emerald-600 dark:text-emerald-400" },
};

export default function ResearchPlan() {
  return (
    <div className="min-h-screen bg-background" dir="rtl">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 py-8">
        <nav className="flex items-center gap-1 mb-6 p-1 rounded-lg bg-muted/50 w-fit">
          <Link href="/"
            className="px-4 py-2 rounded-md text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">
            فهرس البيانات
          </Link>
          <Link href="/research"
            className="px-4 py-2 rounded-md text-sm font-medium bg-card text-foreground shadow-sm">
            خطة البحث
          </Link>
        </nav>

        <div className="mb-8">
          <div className="flex items-center gap-3 mb-3">
            <div className="p-2.5 rounded-xl bg-gradient-to-br from-violet-500/20 to-purple-500/20">
              <Telescope className="w-6 h-6 text-foreground" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-foreground">
                الهدف الأول: مجرات مبكرة غريبة
              </h1>
              <p className="text-sm text-muted-foreground">JWST Early Universe Anomaly Search</p>
            </div>
          </div>
          <p className="text-muted-foreground leading-relaxed max-w-3xl">
            نبحث في داتا جيمس ويب العامة عن مجرات مبكرة جدًا (z {">"} 6) تبدو "غريبة" أكثر من المتوقع،
            ثم نحاول قتل الفكرة قبل تصديقها. هذه إشارات أولية — لا ادعاءات.
          </p>
        </div>

        <div className="rounded-xl border border-border bg-card p-6 mb-6">
          <div className="flex items-center gap-2 mb-3">
            <Sparkles className="w-5 h-5 text-violet-500" />
            <h2 className="text-lg font-semibold text-foreground">السؤال البحثي</h2>
          </div>
          <blockquote className="border-r-4 border-primary/40 pr-4 py-2 text-foreground leading-relaxed">
            "هل توجد في كتالوجات JWST العامة (JADES DR5, CEERS, UNCOVER, COSMOS-Web)
            مجموعة من المجرات عند z {">"} 6 تظهر خصائص فوتومترية أو مورفولوجية شاذة
            مقارنة بالتوقعات النظرية لتلك الحقبة؟"
          </blockquote>
        </div>

        <div className="rounded-xl border border-border bg-card p-6 mb-6">
          <h2 className="text-lg font-semibold text-foreground mb-4">ماذا نعني بـ "غريبة"؟</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {anomalyTypes.map((anomaly) => {
              const Icon = anomalyIcons[anomaly.icon] || AlertTriangle;
              return (
                <div key={anomaly.icon} className="flex items-start gap-3 p-3 rounded-lg border border-border/50">
                  <div className="p-2 rounded-lg bg-amber-100 dark:bg-amber-900/20 shrink-0">
                    <Icon className="w-4 h-4 text-amber-700 dark:text-amber-400" />
                  </div>
                  <div>
                    <div className="font-medium text-sm text-foreground">{anomaly.nameAr}</div>
                    <div className="text-xs text-muted-foreground mt-0.5">{anomaly.descriptionAr}</div>
                    <div className="text-xs text-muted-foreground/70 mt-1 font-mono" dir="ltr">{anomaly.criterion}</div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        <div className="rounded-xl border border-border bg-card p-6 mb-6">
          <h2 className="text-lg font-semibold text-foreground mb-4">برامج JWST المستهدفة</h2>
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-border">
                  <th className="text-right p-3 font-medium text-muted-foreground">البرنامج</th>
                  <th className="text-right p-3 font-medium text-muted-foreground">الحقل</th>
                  <th className="text-right p-3 font-medium text-muted-foreground">الأدوات</th>
                  <th className="text-right p-3 font-medium text-muted-foreground">مدى z</th>
                  <th className="text-right p-3 font-medium text-muted-foreground">الحجم</th>
                  <th className="text-right p-3 font-medium text-muted-foreground">الأولوية</th>
                  <th className="text-right p-3 font-medium text-muted-foreground"></th>
                </tr>
              </thead>
              <tbody>
                {jwstPrograms.map((program) => {
                  const priority = priorityLabels[program.priority];
                  return (
                    <tr key={program.name} className="border-b border-border/50 hover:bg-muted/30">
                      <td className="p-3 font-medium text-foreground">{program.nameAr}</td>
                      <td className="p-3 text-muted-foreground">{program.field}</td>
                      <td className="p-3 text-muted-foreground text-xs" dir="ltr">{program.instruments}</td>
                      <td className="p-3 text-muted-foreground text-xs" dir="ltr">{program.redshiftRange}</td>
                      <td className="p-3 text-muted-foreground text-xs">{program.catalogSize}</td>
                      <td className="p-3">
                        <span className={`inline-flex px-2 py-0.5 rounded-full text-xs font-medium ${priority.bg} ${priority.fg}`}>
                          {priority.text}
                        </span>
                      </td>
                      <td className="p-3">
                        <a href={program.url} target="_blank" rel="noopener noreferrer"
                           className="text-primary hover:text-primary/80">
                          <ExternalLink className="w-4 h-4" />
                        </a>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>

        <div className="mb-6">
          <h2 className="text-lg font-semibold text-foreground mb-4">خطة العمل — 5 خطوات</h2>
          <div className="space-y-3">
            {researchSteps.map((step) => {
              const StepIcon = stepIcons[step.number] || Circle;
              const StatusIcon = statusIcons[step.status];
              const statusLabel = statusLabels[step.status];

              return (
                <div key={step.number} className="rounded-xl border border-border bg-card p-5">
                  <div className="flex items-start gap-4">
                    <div className="flex items-center justify-center w-10 h-10 rounded-xl bg-primary/10 text-primary font-bold shrink-0">
                      <StepIcon className="w-5 h-5" />
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-3 flex-wrap mb-1">
                        <h3 className="font-semibold text-foreground">
                          الخطوة {step.number}: {step.titleAr}
                        </h3>
                        <div className={`flex items-center gap-1 text-xs ${statusLabel.color}`}>
                          <StatusIcon className="w-3.5 h-3.5" />
                          {statusLabel.text}
                        </div>
                        <span className="text-xs text-muted-foreground bg-muted px-2 py-0.5 rounded">
                          {step.duration}
                        </span>
                      </div>
                      <p className="text-sm text-muted-foreground mb-3">{step.descriptionAr}</p>
                      <div className="flex flex-wrap gap-1.5 mb-3">
                        {step.skills.map((skill) => (
                          <span key={skill} className="text-xs px-2 py-0.5 rounded bg-violet-100 dark:bg-violet-900/20 text-violet-700 dark:text-violet-400">
                            {skill}
                          </span>
                        ))}
                      </div>
                      <ul className="space-y-1">
                        {step.details.map((detail, i) => (
                          <li key={i} className="text-xs text-muted-foreground flex items-start gap-2">
                            <span className="text-primary mt-0.5">-</span>
                            {detail}
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
          <div className="rounded-xl border border-border bg-card p-5">
            <div className="flex items-center gap-2 mb-3">
              <Brain className="w-5 h-5 text-emerald-500" />
              <h3 className="font-semibold text-foreground">أين يدخل الذكاء الاصطناعي بقوة</h3>
            </div>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" /> تنزيل وترتيب الكتالوجات</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" /> كتابة كود التنظيف والفلترة</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" /> رسم التوزعات والمخططات</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" /> اكتشاف الشواذ إحصائيًا</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" /> مطابقة الكتالوجات</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" /> البحث في الأدبيات</li>
            </ul>
          </div>

          <div className="rounded-xl border border-border bg-card p-5">
            <div className="flex items-center gap-2 mb-3">
              <Shield className="w-5 h-5 text-amber-500" />
              <h3 className="font-semibold text-foreground">أين نحتاج حذر بشري</h3>
            </div>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li className="flex items-center gap-2"><AlertTriangle className="w-4 h-4 text-amber-500 shrink-0" /> تفسير photo-z عند z {">"} 10</li>
              <li className="flex items-center gap-2"><AlertTriangle className="w-4 h-4 text-amber-500 shrink-0" /> تأكيد أن الشاذ حقيقي وليس قطعة أثرية</li>
              <li className="flex items-center gap-2"><AlertTriangle className="w-4 h-4 text-amber-500 shrink-0" /> أي ادعاء بأن الجرم "جديد" أو "غير مفسر"</li>
              <li className="flex items-center gap-2"><AlertTriangle className="w-4 h-4 text-amber-500 shrink-0" /> تقييم جودة البيانات في حافة المكشاف</li>
            </ul>
          </div>
        </div>

        <div className="rounded-xl border border-amber-200 dark:border-amber-800/50 bg-amber-50/50 dark:bg-amber-900/10 p-5 mb-6">
          <p className="text-sm text-amber-800 dark:text-amber-300 font-medium mb-1">مستوى الادعاء المتوقع</p>
          <p className="text-sm text-amber-700 dark:text-amber-400/80 leading-relaxed">
            في نهاية هذا الهدف، أقصى ما يمكن أن نقوله هو:
            <strong className="block mt-1">
              "إشارة أولية — نلاحظ مجموعة من المرشحين عند z {">"} X يظهرون خصائص غير عادية تستحق مزيدًا من التحقق الطيفي"
            </strong>
          </p>
          <p className="text-xs text-amber-600 dark:text-amber-500/80 mt-2">
            لا نقول "اكتشاف". لا نقول "إثبات". نقول "ملاحظة تستحق المتابعة".
          </p>
        </div>

        <footer className="pt-6 border-t border-border text-center text-xs text-muted-foreground">
          خطة بحثية أولية — تُعدَّل مع تقدم العمل
        </footer>
      </div>
    </div>
  );
}
