import { useState } from "react";
import {
  categories,
  quickStartOrder,
  getDatasetCount,
  getCategoryCount,
  getEssentialCount,
  type Dataset,
  type Category,
} from "@/data/cosmic-datasets";
import {
  Telescope,
  Waves,
  Sparkles,
  Grid3X3,
  Radio,
  Activity,
  ExternalLink,
  ChevronDown,
  ChevronUp,
  Zap,
  Database,
  FolderOpen,
  Star,
  ArrowRight,
  Search,
  Filter,
} from "lucide-react";

const iconMap: Record<string, React.ElementType> = {
  telescope: Telescope,
  waves: Waves,
  sparkles: Sparkles,
  grid: Grid3X3,
  radio: Radio,
  activity: Activity,
};

const priorityStyles: Record<string, { bg: string; text: string; label: string; labelAr: string }> = {
  essential: {
    bg: "bg-emerald-100 dark:bg-emerald-900/30",
    text: "text-emerald-700 dark:text-emerald-400",
    label: "Essential",
    labelAr: "أساسي",
  },
  important: {
    bg: "bg-blue-100 dark:bg-blue-900/30",
    text: "text-blue-700 dark:text-blue-400",
    label: "Important",
    labelAr: "مهم",
  },
  supplementary: {
    bg: "bg-gray-100 dark:bg-gray-800/50",
    text: "text-gray-600 dark:text-gray-400",
    label: "Supplementary",
    labelAr: "تكميلي",
  },
};

function PriorityBadge({ priority }: { priority: Dataset["priority"] }) {
  const style = priorityStyles[priority];
  return (
    <span className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium ${style.bg} ${style.text}`}>
      {priority === "essential" && <Star className="w-3 h-3" />}
      {style.labelAr}
    </span>
  );
}

function DatasetRow({ dataset }: { dataset: Dataset }) {
  return (
    <div className="group flex items-start gap-4 p-4 rounded-lg border border-transparent hover:border-border hover:bg-muted/50 transition-all duration-200">
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 flex-wrap mb-1">
          <a
            href={dataset.url}
            target="_blank"
            rel="noopener noreferrer"
            className="font-medium text-foreground hover:text-primary transition-colors flex items-center gap-1.5"
          >
            {dataset.nameAr}
            <ExternalLink className="w-3.5 h-3.5 opacity-0 group-hover:opacity-100 transition-opacity" />
          </a>
          <PriorityBadge priority={dataset.priority} />
        </div>
        <p className="text-sm text-muted-foreground leading-relaxed mb-2">{dataset.descriptionAr}</p>
        <div className="flex items-center gap-4 text-xs text-muted-foreground">
          <span className="flex items-center gap-1">
            <Database className="w-3 h-3" />
            {dataset.size}
          </span>
          <span className="flex items-center gap-1">
            <FolderOpen className="w-3 h-3" />
            {dataset.format}
          </span>
        </div>
      </div>
    </div>
  );
}

function CategoryCard({ category, isExpanded, onToggle }: {
  category: Category;
  isExpanded: boolean;
  onToggle: () => void;
}) {
  const IconComponent = iconMap[category.icon] || Database;
  const essentialCount = category.datasets.filter(d => d.priority === "essential").length;

  return (
    <div className="rounded-xl border border-border bg-card overflow-hidden">
      <button
        onClick={onToggle}
        className="w-full flex items-center gap-4 p-5 text-right hover:bg-muted/30 transition-colors"
      >
        <div className={`p-3 rounded-xl bg-gradient-to-br ${category.color}`}>
          <IconComponent className="w-5 h-5 text-foreground" />
        </div>
        <div className="flex-1 min-w-0 text-right">
          <h3 className="font-semibold text-foreground text-base">{category.titleAr}</h3>
          <p className="text-sm text-muted-foreground mt-0.5">{category.descriptionAr}</p>
        </div>
        <div className="flex items-center gap-3 shrink-0">
          <div className="text-left">
            <div className="text-sm font-medium text-foreground">{category.datasets.length}</div>
            <div className="text-xs text-muted-foreground">مصادر</div>
          </div>
          {essentialCount > 0 && (
            <div className="text-left">
              <div className="text-sm font-medium text-emerald-600 dark:text-emerald-400">{essentialCount}</div>
              <div className="text-xs text-muted-foreground">أساسي</div>
            </div>
          )}
          {isExpanded ? (
            <ChevronUp className="w-5 h-5 text-muted-foreground" />
          ) : (
            <ChevronDown className="w-5 h-5 text-muted-foreground" />
          )}
        </div>
      </button>

      {isExpanded && (
        <div className="border-t border-border px-5 pb-4 pt-2">
          <div className="divide-y divide-border/50">
            {category.datasets.map((dataset) => (
              <DatasetRow key={dataset.name} dataset={dataset} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function QuickStartSection() {
  return (
    <div className="rounded-xl border border-border bg-card p-6">
      <div className="flex items-center gap-2 mb-4">
        <Zap className="w-5 h-5 text-amber-500" />
        <h2 className="text-lg font-semibold text-foreground">ابدأ بهذا الترتيب</h2>
      </div>
      <p className="text-sm text-muted-foreground mb-5">
        JWST وحده لن يكفي إذا كان هدفنا "أبكر ما يمكن". هو ممتاز لأول المجرات والضوء المبكر، لكن للوصول أعمق نحتاج معه CMB وHERA/21-cm ومسوح مثل Euclid وDESI.
      </p>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        {quickStartOrder.map((item) => (
          <a
            key={item.step}
            href={item.url}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-3 p-3 rounded-lg border border-border hover:border-primary/30 hover:bg-primary/5 transition-all duration-200 group"
          >
            <div className="flex items-center justify-center w-7 h-7 rounded-full bg-primary/10 text-primary text-sm font-bold shrink-0">
              {item.step}
            </div>
            <span className="text-sm font-medium text-foreground group-hover:text-primary transition-colors flex-1 min-w-0">
              {item.name}
            </span>
            <ArrowRight className="w-4 h-4 text-muted-foreground opacity-0 group-hover:opacity-100 transition-opacity shrink-0" />
          </a>
        ))}
      </div>
    </div>
  );
}

function StatCard({ label, value, icon: Icon }: { label: string; value: string | number; icon: React.ElementType }) {
  return (
    <div className="rounded-xl border border-border bg-card p-4">
      <div className="flex items-center gap-3">
        <div className="p-2 rounded-lg bg-primary/10">
          <Icon className="w-4 h-4 text-primary" />
        </div>
        <div>
          <div className="text-2xl font-bold text-foreground">{value}</div>
          <div className="text-xs text-muted-foreground">{label}</div>
        </div>
      </div>
    </div>
  );
}

export default function Dashboard() {
  const [expandedCategories, setExpandedCategories] = useState<Set<string>>(new Set(["jwst"]));
  const [searchQuery, setSearchQuery] = useState("");
  const [filterPriority, setFilterPriority] = useState<string>("all");

  const toggleCategory = (id: string) => {
    setExpandedCategories((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  };

  const expandAll = () => {
    setExpandedCategories(new Set(categories.map(c => c.id)));
  };

  const collapseAll = () => {
    setExpandedCategories(new Set());
  };

  const filteredCategories = categories.map(cat => ({
    ...cat,
    datasets: cat.datasets.filter(d => {
      const matchesSearch = searchQuery === "" ||
        d.nameAr.includes(searchQuery) ||
        d.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        d.descriptionAr.includes(searchQuery) ||
        d.description.toLowerCase().includes(searchQuery.toLowerCase());
      const matchesPriority = filterPriority === "all" || d.priority === filterPriority;
      return matchesSearch && matchesPriority;
    })
  })).filter(cat => cat.datasets.length > 0);

  return (
    <div className="min-h-screen bg-background" dir="rtl">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-foreground mb-2">
            فهرس بيانات الكون المبكر
          </h1>
          <p className="text-muted-foreground text-base leading-relaxed max-w-2xl">
            جميع مصادر البيانات الفلكية المفتوحة للمراحل الأولى من الكون - من الخلفية الكونية إلى أول المجرات
          </p>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-6">
          <StatCard label="إجمالي المصادر" value={getDatasetCount()} icon={Database} />
          <StatCard label="الفئات" value={getCategoryCount()} icon={FolderOpen} />
          <StatCard label="مصادر أساسية" value={getEssentialCount()} icon={Star} />
          <StatCard label="الحجم التقريبي" value="~1.2 PB+" icon={Zap} />
        </div>

        <QuickStartSection />

        <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 mt-8 mb-4">
          <div className="relative flex-1">
            <Search className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <input
              type="search"
              placeholder="ابحث في المصادر..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pr-10 pl-4 py-2.5 rounded-lg border border-input bg-card text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring"
            />
          </div>
          <div className="flex items-center gap-2">
            <Filter className="w-4 h-4 text-muted-foreground" />
            <select
              value={filterPriority}
              onChange={(e) => setFilterPriority(e.target.value)}
              className="px-3 py-2.5 rounded-lg border border-input bg-card text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-ring"
            >
              <option value="all">كل الأولويات</option>
              <option value="essential">أساسي</option>
              <option value="important">مهم</option>
              <option value="supplementary">تكميلي</option>
            </select>
            <button
              onClick={expandAll}
              className="px-3 py-2.5 rounded-lg border border-input bg-card text-sm text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
            >
              فتح الكل
            </button>
            <button
              onClick={collapseAll}
              className="px-3 py-2.5 rounded-lg border border-input bg-card text-sm text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
            >
              إغلاق الكل
            </button>
          </div>
        </div>

        <div className="space-y-3">
          {filteredCategories.map((category) => (
            <CategoryCard
              key={category.id}
              category={category}
              isExpanded={expandedCategories.has(category.id)}
              onToggle={() => toggleCategory(category.id)}
            />
          ))}
        </div>

        {filteredCategories.length === 0 && (
          <div className="text-center py-12 text-muted-foreground">
            لا توجد نتائج مطابقة للبحث
          </div>
        )}

        <div className="mt-8 p-4 rounded-xl border border-amber-200 dark:border-amber-800/50 bg-amber-50/50 dark:bg-amber-900/10">
          <p className="text-sm text-amber-800 dark:text-amber-300 font-medium mb-1">تنبيه مهم</p>
          <p className="text-sm text-amber-700 dark:text-amber-400/80 leading-relaxed">
            JWST وحده لن يكفي إذا كان هدفنا "أبكر ما يمكن". هو ممتاز لأول المجرات والضوء المبكر، لكن للوصول أعمق نحتاج معه CMB (بلانك) وHERA/21-cm ومسوح مثل Euclid وDESI. كل هذه المصادر مكملة لبعضها.
          </p>
        </div>

        <footer className="mt-8 pt-6 border-t border-border text-center text-xs text-muted-foreground">
          الأحجام تقريبية وقد تتغير مع التحديثات. جميع البيانات متاحة للعموم.
        </footer>
      </div>
    </div>
  );
}
