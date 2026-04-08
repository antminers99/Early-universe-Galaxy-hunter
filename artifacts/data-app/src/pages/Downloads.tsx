import { useState } from "react";
import { Link } from "wouter";
import { downloadSources, type DownloadSource } from "@/data/downloads";
import {
  Download,
  ExternalLink,
  HardDrive,
  Telescope,
  Globe,
  BookOpen,
  ChevronDown,
  ChevronUp,
  FileDown,
  Database,
  Star,
  Shield,
  Filter,
  Search,
} from "lucide-react";

const categoryMeta: Record<string, { label: string; color: string; icon: React.ElementType; description: string }> = {
  "primary-jwst": {
    label: "Primary JWST",
    color: "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400",
    icon: Telescope,
    description: "Core JWST survey catalogs for the anomaly search",
  },
  "cross-validation": {
    label: "Cross-Validation",
    color: "bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400",
    icon: Shield,
    description: "Independent datasets for verifying candidates",
  },
  support: {
    label: "Support",
    color: "bg-gray-100 text-gray-600 dark:bg-gray-800/50 dark:text-gray-400",
    icon: Database,
    description: "Historical and supplementary datasets",
  },
};

function SourceCard({ source }: { source: DownloadSource }) {
  const [expanded, setExpanded] = useState(true);
  const cat = categoryMeta[source.category];

  return (
    <div className="rounded-xl border border-border bg-card overflow-hidden">
      <div
        className="flex items-start gap-4 p-5 cursor-pointer hover:bg-muted/30 transition-colors"
        onClick={() => setExpanded(!expanded)}
      >
        <div className="p-2.5 rounded-xl bg-primary/10 shrink-0">
          <cat.icon className="w-5 h-5 text-primary" />
        </div>
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 flex-wrap mb-1">
            <h3 className="font-semibold text-foreground text-base">{source.program}</h3>
            <span className={`inline-flex px-2 py-0.5 rounded-full text-xs font-medium ${cat.color}`}>
              {cat.label}
            </span>
          </div>
          <p className="text-sm text-muted-foreground leading-relaxed">{source.description}</p>
          <div className="flex items-center gap-4 mt-2 text-xs text-muted-foreground">
            <span className="flex items-center gap-1">
              <FileDown className="w-3 h-3" />
              {source.files.length} {source.files.length === 1 ? "file" : "files"}
            </span>
            <span className="flex items-center gap-1">
              <BookOpen className="w-3 h-3" />
              {source.reference}
            </span>
          </div>
        </div>
        <div className="shrink-0 pt-1">
          {expanded ? (
            <ChevronUp className="w-5 h-5 text-muted-foreground" />
          ) : (
            <ChevronDown className="w-5 h-5 text-muted-foreground" />
          )}
        </div>
      </div>

      {expanded && (
        <div className="border-t border-border">
          <div className="px-5 py-2 bg-muted/20 flex items-center gap-4 text-xs text-muted-foreground">
            <a
              href={source.homepage}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-1 text-primary hover:underline"
            >
              <Globe className="w-3 h-3" />
              Homepage
            </a>
          </div>
          <div className="divide-y divide-border/50">
            {source.files.map((file, idx) => (
              <div key={idx} className="px-5 py-3 flex items-center gap-4 hover:bg-muted/20 transition-colors">
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="font-medium text-sm text-foreground">{file.name}</span>
                    {file.field && (
                      <span className="text-xs px-1.5 py-0.5 rounded bg-violet-100 dark:bg-violet-900/20 text-violet-700 dark:text-violet-400">
                        {file.field}
                      </span>
                    )}
                  </div>
                  <p className="text-xs text-muted-foreground mt-0.5">{file.description}</p>
                </div>
                <div className="flex items-center gap-3 shrink-0">
                  <div className="text-right">
                    <div className="text-sm font-mono font-medium text-foreground">{file.size}</div>
                    <div className="text-xs text-muted-foreground">{file.format}</div>
                  </div>
                  <a
                    href={file.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className={`flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors shrink-0 ${
                      file.linkType === "direct"
                        ? "bg-primary text-primary-foreground hover:bg-primary/90"
                        : "bg-muted text-foreground hover:bg-muted/80 border border-border"
                    }`}
                    onClick={(e) => e.stopPropagation()}
                  >
                    {file.linkType === "direct" ? (
                      <Download className="w-4 h-4" />
                    ) : (
                      <ExternalLink className="w-4 h-4" />
                    )}
                    {file.linkType === "direct" ? "Download" : "Open"}
                  </a>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default function Downloads() {
  const [filterCategory, setFilterCategory] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState("");

  const filtered = downloadSources.filter((source) => {
    if (filterCategory !== "all" && source.category !== filterCategory) return false;
    if (searchQuery) {
      const q = searchQuery.toLowerCase();
      return (
        source.program.toLowerCase().includes(q) ||
        source.description.toLowerCase().includes(q) ||
        source.files.some(
          (f) =>
            f.name.toLowerCase().includes(q) ||
            f.field?.toLowerCase().includes(q)
        )
      );
    }
    return true;
  });

  const totalFiles = downloadSources.reduce((sum, s) => sum + s.files.length, 0);

  const categories = [
    { key: "all", label: "All" },
    { key: "primary-jwst", label: "Primary JWST" },
    { key: "cross-validation", label: "Cross-Validation" },
    { key: "support", label: "Support" },
  ];

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 py-8">
        <nav className="flex items-center gap-1 mb-6 p-1 rounded-lg bg-muted/50 w-fit">
          <Link
            href="/"
            className="px-4 py-2 rounded-md text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
          >
            Data Catalog
          </Link>
          <Link
            href="/research"
            className="px-4 py-2 rounded-md text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
          >
            Research Plan
          </Link>
          <Link
            href="/downloads"
            className="px-4 py-2 rounded-md text-sm font-medium bg-card text-foreground shadow-sm"
          >
            Downloads
          </Link>
          <Link href="/inspection"
            className="px-4 py-2 rounded-md text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">
            Inspection
          </Link>
        </nav>

        <div className="mb-8">
          <div className="flex items-center gap-3 mb-3">
            <div className="p-2.5 rounded-xl bg-gradient-to-br from-cyan-500/20 to-blue-500/20">
              <HardDrive className="w-6 h-6 text-foreground" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-foreground">Download Center</h1>
              <p className="text-sm text-muted-foreground">
                {downloadSources.length} sources, {totalFiles} files
              </p>
            </div>
          </div>
          <p className="text-muted-foreground leading-relaxed max-w-3xl">
            Direct download links for all research catalogs. Click "Get" to open each file in a new tab.
            Large FITS files can be opened directly in Python with <code className="text-xs bg-muted px-1.5 py-0.5 rounded font-mono">astropy.io.fits</code>.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row gap-3 mb-6">
          <div className="relative flex-1 max-w-sm">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <input
              type="text"
              placeholder="Search programs, fields..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-9 pr-4 py-2 rounded-lg border border-border bg-card text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary/30"
            />
          </div>
          <div className="flex items-center gap-1 p-1 rounded-lg bg-muted/50 w-fit">
            {categories.map((cat) => (
              <button
                key={cat.key}
                onClick={() => setFilterCategory(cat.key)}
                className={`px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${
                  filterCategory === cat.key
                    ? "bg-card text-foreground shadow-sm"
                    : "text-muted-foreground hover:text-foreground"
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-6">
          {Object.entries(categoryMeta).map(([key, meta]) => {
            const count = downloadSources.filter((s) => s.category === key).length;
            const fileCount = downloadSources
              .filter((s) => s.category === key)
              .reduce((sum, s) => sum + s.files.length, 0);
            return (
              <div
                key={key}
                className="rounded-xl border border-border bg-card p-4 cursor-pointer hover:bg-muted/30 transition-colors"
                onClick={() => setFilterCategory(filterCategory === key ? "all" : key)}
              >
                <div className="flex items-center gap-2 mb-1">
                  <meta.icon className="w-4 h-4 text-primary" />
                  <span className="font-medium text-sm text-foreground">{meta.label}</span>
                </div>
                <p className="text-xs text-muted-foreground">{meta.description}</p>
                <div className="flex gap-4 mt-2 text-xs text-muted-foreground">
                  <span>{count} programs</span>
                  <span>{fileCount} files</span>
                </div>
              </div>
            );
          })}
        </div>

        <div className="space-y-4">
          {filtered.map((source) => (
            <SourceCard key={source.program} source={source} />
          ))}
          {filtered.length === 0 && (
            <div className="text-center py-12 text-muted-foreground">
              <Filter className="w-8 h-8 mx-auto mb-3 opacity-40" />
              <p>No matching sources found.</p>
            </div>
          )}
        </div>

        <div className="rounded-xl border border-amber-200 dark:border-amber-800/50 bg-amber-50/50 dark:bg-amber-900/10 p-5 mt-6">
          <p className="text-sm text-amber-800 dark:text-amber-300 font-medium mb-1">Download Tips</p>
          <ul className="text-sm text-amber-700 dark:text-amber-400/80 space-y-1">
            <li>- Large FITS files ({">"} 1 GB) may take time. Use <code className="text-xs bg-amber-100 dark:bg-amber-900/30 px-1 rounded font-mono">wget</code> or <code className="text-xs bg-amber-100 dark:bg-amber-900/30 px-1 rounded font-mono">curl</code> for resumable downloads.</li>
            <li>- Some links go to landing pages where you select specific files — not all are direct downloads.</li>
            <li>- For UNCOVER DR3, Google Drive links may require manual "Download" confirmation.</li>
            <li>- After downloading, place files in <code className="text-xs bg-amber-100 dark:bg-amber-900/30 px-1 rounded font-mono">data/catalogs/</code> for processing.</li>
          </ul>
        </div>

        <footer className="pt-6 mt-6 border-t border-border text-center text-xs text-muted-foreground">
          All data is publicly available. Cite the original papers when using these datasets.
        </footer>
      </div>
    </div>
  );
}
