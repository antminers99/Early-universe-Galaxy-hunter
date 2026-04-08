import { useState, useMemo } from "react";
import { Link } from "wouter";
import {
  tripleCandidates,
  BANDS,
  getLocalCutoutUrl,
  getRgbCompositeUrl,
  PSF_FWHM_ARCSEC,
  PIXEL_SCALE_ARCSEC,
  CUTOUT_SIZE_PX,
  type Candidate,
  type StretchMode,
} from "@/data/candidates";
import {
  ArrowLeft,
  Check,
  HelpCircle,
  X,
  AlertTriangle,
  Eye,
  Filter,
  Bug,
  Crosshair,
  Circle,
  Ruler,
} from "lucide-react";

type UserVerdict = "PASS" | "MAYBE" | "FAIL" | null;

const SCALE_BAR_ARCSEC = 0.2;
const SCALE_BAR_PX = SCALE_BAR_ARCSEC / PIXEL_SCALE_ARCSEC;
const DISPLAY_SIZE = 120;
const PX_TO_DISPLAY = DISPLAY_SIZE / CUTOUT_SIZE_PX;

function SnrBar({ value, band }: { value: number | null; band: string }) {
  if (value === null) return <span className="text-xs text-gray-400">N/A</span>;
  const clamped = Math.min(Math.max(value, -5), 100);
  const width = Math.min(100, Math.max(0, (clamped / 50) * 100));
  let color = "bg-red-400";
  if (value >= 3) color = "bg-green-400";
  else if (value >= 2) color = "bg-yellow-400";

  return (
    <div className="flex items-center gap-1.5">
      <span className="text-[10px] text-gray-500 w-10 text-right font-mono">{band}</span>
      <div className="flex-1 h-2 bg-gray-100 dark:bg-gray-800 rounded overflow-hidden">
        <div className={`h-full ${color} rounded`} style={{ width: `${width}%` }} />
      </div>
      <span className={`text-[10px] font-mono w-8 ${value >= 3 ? 'text-green-600' : value >= 2 ? 'text-yellow-600' : 'text-red-500'}`}>
        {value.toFixed(1)}
      </span>
    </div>
  );
}

function CheckBadge({ ok, label }: { ok: boolean; label: string }) {
  return (
    <span className={`inline-flex items-center gap-0.5 px-1.5 py-0.5 rounded text-[10px] font-medium ${
      ok ? 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400'
         : 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400'
    }`}>
      {ok ? <Check className="w-2.5 h-2.5" /> : <X className="w-2.5 h-2.5" />}
      {label}
    </span>
  );
}

function CutoutPanel({
  field,
  id,
  band,
  stretch,
  showCrosshair,
  showPsf,
  showScale,
  fwhmArcsec,
}: {
  field: string;
  id: string;
  band: string;
  stretch: StretchMode;
  showCrosshair: boolean;
  showPsf: boolean;
  showScale: boolean;
  fwhmArcsec: number;
}) {
  const [status, setStatus] = useState<"loading" | "ok" | "empty" | "error">("loading");
  const url = getLocalCutoutUrl(field, id, band, stretch);

  const psfArcsec = PSF_FWHM_ARCSEC[band] || 0.145;
  const psfDisplayPx = (psfArcsec / PIXEL_SCALE_ARCSEC) * PX_TO_DISPLAY;
  const fwhmDisplayPx = (fwhmArcsec / PIXEL_SCALE_ARCSEC) * PX_TO_DISPLAY;
  const scaleBarDisplayPx = SCALE_BAR_PX * PX_TO_DISPLAY;

  const cx = DISPLAY_SIZE / 2;
  const cy = DISPLAY_SIZE / 2;

  return (
    <div className="flex flex-col items-center gap-1">
      <span className="text-[10px] font-mono text-gray-400 font-bold tracking-wider">{band}</span>
      <div className="relative bg-black rounded border border-gray-700 overflow-hidden"
           style={{ width: DISPLAY_SIZE, height: DISPLAY_SIZE }}>
        {status === "loading" && (
          <div className="absolute inset-0 flex items-center justify-center z-10">
            <div className="w-4 h-4 border-2 border-gray-500 border-t-transparent rounded-full animate-spin" />
          </div>
        )}
        {(status === "error" || status === "empty") ? (
          <div className="absolute inset-0 flex flex-col items-center justify-center text-gray-500">
            <span className="text-[10px]">{status === "empty" ? "No coverage" : "Missing"}</span>
          </div>
        ) : (
          <img
            src={url}
            alt={`${band} cutout`}
            className="w-full h-full object-contain"
            style={{ imageRendering: "pixelated" }}
            onLoad={(e) => {
              const img = e.target as HTMLImageElement;
              const canvas = document.createElement("canvas");
              canvas.width = Math.min(img.naturalWidth, 60);
              canvas.height = Math.min(img.naturalHeight, 60);
              const ctx = canvas.getContext("2d");
              if (ctx) {
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
                let nonZero = 0;
                for (let i = 0; i < data.length; i += 16) {
                  if (data[i] > 5 || data[i+1] > 5 || data[i+2] > 5) nonZero++;
                }
                setStatus(nonZero < 3 ? "empty" : "ok");
              } else {
                setStatus("ok");
              }
            }}
            onError={() => setStatus("error")}
            loading="lazy"
          />
        )}

        {status === "ok" && (
          <svg className="absolute inset-0 w-full h-full pointer-events-none" viewBox={`0 0 ${DISPLAY_SIZE} ${DISPLAY_SIZE}`}>
            {showCrosshair && (
              <g stroke="rgba(0,255,255,0.6)" strokeWidth="0.5">
                <line x1={cx - 8} y1={cy} x2={cx - 3} y2={cy} />
                <line x1={cx + 3} y1={cy} x2={cx + 8} y2={cy} />
                <line x1={cx} y1={cy - 8} x2={cx} y2={cy - 3} />
                <line x1={cx} y1={cy + 3} x2={cx} y2={cy + 8} />
              </g>
            )}

            {showPsf && (
              <>
                <circle cx={cx} cy={cy} r={psfDisplayPx / 2}
                  fill="none" stroke="rgba(255,100,100,0.7)" strokeWidth="0.8"
                  strokeDasharray="3 2" />
                {fwhmArcsec > 0 && fwhmDisplayPx > 1 && (
                  <circle cx={cx} cy={cy} r={fwhmDisplayPx / 2}
                    fill="none" stroke="rgba(100,255,100,0.7)" strokeWidth="0.8" />
                )}
              </>
            )}

            {showScale && (
              <g>
                <line x1={5} y1={DISPLAY_SIZE - 8} x2={5 + scaleBarDisplayPx} y2={DISPLAY_SIZE - 8}
                  stroke="rgba(255,255,255,0.8)" strokeWidth="1.5" />
                <line x1={5} y1={DISPLAY_SIZE - 11} x2={5} y2={DISPLAY_SIZE - 5}
                  stroke="rgba(255,255,255,0.8)" strokeWidth="0.8" />
                <line x1={5 + scaleBarDisplayPx} y1={DISPLAY_SIZE - 11} x2={5 + scaleBarDisplayPx} y2={DISPLAY_SIZE - 5}
                  stroke="rgba(255,255,255,0.8)" strokeWidth="0.8" />
                <text x={5 + scaleBarDisplayPx / 2} y={DISPLAY_SIZE - 13}
                  fill="rgba(255,255,255,0.8)" fontSize="7" textAnchor="middle" fontFamily="monospace">
                  {SCALE_BAR_ARCSEC}&quot;
                </text>
              </g>
            )}
          </svg>
        )}
      </div>
      {showPsf && status === "ok" && (
        <div className="text-[8px] text-gray-500 text-center leading-tight">
          <span className="text-red-400">---</span> PSF {psfArcsec.toFixed(3)}&quot;
          {fwhmArcsec > 0 && <> | <span className="text-green-400">—</span> FWHM</>}
        </div>
      )}
    </div>
  );
}

function CandidateCard({
  candidate,
  index,
  userVerdict,
  onVerdict,
  debugMode,
  stretch,
  showCrosshair,
  showPsf,
  showScale,
}: {
  candidate: Candidate;
  index: number;
  userVerdict: UserVerdict;
  onVerdict: (v: UserVerdict) => void;
  debugMode: boolean;
  stretch: StretchMode;
  showCrosshair: boolean;
  showPsf: boolean;
  showScale: boolean;
}) {
  const verdictColor = {
    PASS: "border-green-500/30 bg-green-50/50 dark:bg-green-950/20",
    MAYBE: "border-yellow-500/30 bg-yellow-50/50 dark:bg-yellow-950/20",
    FAIL: "border-red-500/30 bg-red-50/50 dark:bg-red-950/20",
  };

  const autoVerdictBg = candidate.verdict === "PASS"
    ? "bg-green-100 text-green-700 dark:bg-green-900/40 dark:text-green-400"
    : candidate.verdict === "MAYBE"
    ? "bg-yellow-100 text-yellow-700 dark:bg-yellow-900/40 dark:text-yellow-400"
    : "bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-400";

  const fwhmPsfRatio = candidate.fwhmArcsec / 0.145;

  return (
    <div className={`rounded-lg border-2 p-4 transition-colors ${
      userVerdict ? verdictColor[userVerdict] : 'border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900'
    }`}>
      <div className="flex items-start justify-between mb-3">
        <div>
          <div className="flex items-center gap-2">
            <span className="text-sm font-bold text-gray-400">#{index + 1}</span>
            <h3 className="font-mono font-bold text-base">{candidate.field} — {candidate.id}</h3>
            <span className={`text-[10px] px-1.5 py-0.5 rounded font-medium ${autoVerdictBg}`}>
              Auto: {candidate.verdict}
            </span>
            {debugMode && (
              <span className="text-[10px] px-1.5 py-0.5 rounded font-mono bg-gray-100 dark:bg-gray-800 text-gray-600">
                FWHM/PSF = {fwhmPsfRatio.toFixed(3)}
              </span>
            )}
          </div>
          <p className="text-xs text-gray-500 mt-0.5">
            RA={candidate.ra.toFixed(6)}, Dec={candidate.dec.toFixed(6)} | z={candidate.zPeak} | P(z{">"}6)={candidate.probGt6}
          </p>
          {debugMode && (
            <p className="text-[10px] text-gray-400 mt-0.5 font-mono">
              Source: JADES DR5 mosaics (UCSC) | Cutout: {CUTOUT_SIZE_PX}×{CUTOUT_SIZE_PX} px ({(CUTOUT_SIZE_PX * PIXEL_SCALE_ARCSEC).toFixed(1)}&quot;×{(CUTOUT_SIZE_PX * PIXEL_SCALE_ARCSEC).toFixed(1)}&quot;) | Scale: {PIXEL_SCALE_ARCSEC * 1000} mas/px | Stretch: {stretch}
            </p>
          )}
        </div>

        <div className="flex items-center gap-1">
          <button
            onClick={() => onVerdict(userVerdict === "PASS" ? null : "PASS")}
            className={`px-3 py-1.5 rounded-l text-xs font-medium border transition-colors ${
              userVerdict === "PASS"
                ? 'bg-green-500 text-white border-green-500'
                : 'bg-white dark:bg-gray-800 text-green-600 border-gray-300 dark:border-gray-600 hover:bg-green-50'
            }`}
          >
            <Check className="w-3.5 h-3.5 inline mr-1" />PASS
          </button>
          <button
            onClick={() => onVerdict(userVerdict === "MAYBE" ? null : "MAYBE")}
            className={`px-3 py-1.5 text-xs font-medium border-y transition-colors ${
              userVerdict === "MAYBE"
                ? 'bg-yellow-500 text-white border-yellow-500'
                : 'bg-white dark:bg-gray-800 text-yellow-600 border-gray-300 dark:border-gray-600 hover:bg-yellow-50'
            }`}
          >
            <HelpCircle className="w-3.5 h-3.5 inline mr-1" />MAYBE
          </button>
          <button
            onClick={() => onVerdict(userVerdict === "FAIL" ? null : "FAIL")}
            className={`px-3 py-1.5 rounded-r text-xs font-medium border transition-colors ${
              userVerdict === "FAIL"
                ? 'bg-red-500 text-white border-red-500'
                : 'bg-white dark:bg-gray-800 text-red-600 border-gray-300 dark:border-gray-600 hover:bg-red-50'
            }`}
          >
            <X className="w-3.5 h-3.5 inline mr-1" />FAIL
          </button>
        </div>
      </div>

      <div className="mb-3">
        <div className="flex items-center justify-between mb-1">
          <span className="text-[10px] text-gray-500 font-medium uppercase tracking-wider">
            JWST JADES DR5 — {stretch.toUpperCase()} stretch — {(CUTOUT_SIZE_PX * PIXEL_SCALE_ARCSEC).toFixed(1)}&quot; × {(CUTOUT_SIZE_PX * PIXEL_SCALE_ARCSEC).toFixed(1)}&quot;
          </span>
          {debugMode && showPsf && (
            <div className="flex items-center gap-2 text-[9px]">
              <span className="text-red-400">- - - PSF FWHM</span>
              <span className="text-green-400">—— Source FWHM</span>
              <span className="text-cyan-400">+ Crosshair</span>
            </div>
          )}
        </div>
        <div className="flex items-start gap-3 bg-black/90 rounded-lg p-3 overflow-x-auto">
          <div className="flex flex-col items-center gap-1 flex-shrink-0">
            <span className="text-[10px] font-mono text-yellow-400 font-bold tracking-wider">RGB</span>
            <div className="relative bg-black rounded border-2 border-yellow-500/40 overflow-hidden"
                 style={{ width: DISPLAY_SIZE * 1.5, height: DISPLAY_SIZE * 1.5 }}>
              <img
                src={getRgbCompositeUrl(candidate.field, candidate.id)}
                alt="RGB composite"
                className="w-full h-full object-contain"
                style={{ imageRendering: "pixelated" }}
                loading="lazy"
              />
              {(showCrosshair || showPsf || showScale) && (
                <svg className="absolute inset-0 w-full h-full pointer-events-none"
                     viewBox={`0 0 ${DISPLAY_SIZE * 1.5} ${DISPLAY_SIZE * 1.5}`}>
                  {showCrosshair && (
                    <g stroke="rgba(255,255,255,0.5)" strokeWidth="0.5">
                      <line x1={DISPLAY_SIZE*0.75-12} y1={DISPLAY_SIZE*0.75} x2={DISPLAY_SIZE*0.75-4} y2={DISPLAY_SIZE*0.75} />
                      <line x1={DISPLAY_SIZE*0.75+4} y1={DISPLAY_SIZE*0.75} x2={DISPLAY_SIZE*0.75+12} y2={DISPLAY_SIZE*0.75} />
                      <line x1={DISPLAY_SIZE*0.75} y1={DISPLAY_SIZE*0.75-12} x2={DISPLAY_SIZE*0.75} y2={DISPLAY_SIZE*0.75-4} />
                      <line x1={DISPLAY_SIZE*0.75} y1={DISPLAY_SIZE*0.75+4} x2={DISPLAY_SIZE*0.75} y2={DISPLAY_SIZE*0.75+12} />
                    </g>
                  )}
                  {showScale && (() => {
                    const scalePx = SCALE_BAR_PX * PX_TO_DISPLAY * 1.5;
                    return (
                      <g>
                        <line x1={8} y1={DISPLAY_SIZE*1.5-12} x2={8 + scalePx} y2={DISPLAY_SIZE*1.5-12}
                          stroke="rgba(255,255,255,0.8)" strokeWidth="1.5" />
                        <text x={8 + scalePx/2} y={DISPLAY_SIZE*1.5-18}
                          fill="rgba(255,255,255,0.8)" fontSize="9" textAnchor="middle" fontFamily="monospace">
                          {SCALE_BAR_ARCSEC}&quot;
                        </text>
                      </g>
                    );
                  })()}
                </svg>
              )}
            </div>
            <span className="text-[8px] text-gray-400 text-center">
              <span className="text-red-400">R</span>=F444W <span className="text-green-400">G</span>=F277W <span className="text-blue-400">B</span>=F150W
            </span>
          </div>

          <div className="flex-shrink-0 w-px bg-gray-700 self-stretch" />

          <div className="flex items-start gap-2">
            {BANDS.map((band) => (
              <CutoutPanel
                key={`${band}-${stretch}`}
                field={candidate.field}
                id={candidate.id}
                band={band}
                stretch={stretch}
                showCrosshair={showCrosshair}
                showPsf={showPsf}
                showScale={showScale}
                fwhmArcsec={candidate.fwhmArcsec}
              />
            ))}
          </div>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-3">
        <div className="space-y-1">
          <h4 className="text-[10px] font-medium text-gray-500 uppercase tracking-wider">Photometry</h4>
          <div className="text-xs space-y-0.5">
            <div>F444W = <span className="font-mono font-medium">{candidate.f444wFlux?.toFixed(1)}</span> nJy (SNR {candidate.f444wSnr?.toFixed(1)})</div>
            <div>FWHM = <span className="font-mono font-medium">{candidate.fwhmArcsec?.toFixed(4)}&quot;</span> <span className="text-gray-400">({candidate.fwhmPix?.toFixed(3)} px)</span></div>
            {candidate.red1 !== null && <div>red_1 = <span className="font-mono font-medium text-red-500">{candidate.red1.toFixed(3)}</span></div>}
            {candidate.red2 !== null && <div>red_2 = <span className="font-mono font-medium text-red-500">{candidate.red2.toFixed(3)}</span></div>}
            {candidate.compactProxy !== null && <div>compact = <span className="font-mono font-medium">{candidate.compactProxy.toFixed(3)}</span></div>}
            <div>NN dist = <span className="font-mono">{candidate.nnDistArcsec?.toFixed(2)}&quot;</span></div>
          </div>
        </div>

        <div className="space-y-1">
          <h4 className="text-[10px] font-medium text-gray-500 uppercase tracking-wider">SNR Profile</h4>
          <div className="space-y-0.5">
            <SnrBar value={candidate.snrF090W} band="F090W" />
            <SnrBar value={candidate.snrF115W} band="F115W" />
            <SnrBar value={candidate.snrF150W} band="F150W" />
            <SnrBar value={candidate.snrF200W} band="F200W" />
            <SnrBar value={candidate.snrF277W} band="F277W" />
            <SnrBar value={candidate.snrF356W} band="F356W" />
            <SnrBar value={candidate.snrF444W} band="F444W" />
          </div>
        </div>

        <div className="space-y-1">
          <h4 className="text-[10px] font-medium text-gray-500 uppercase tracking-wider">Audit Checks</h4>
          <div className="flex flex-wrap gap-1">
            <CheckBadge ok={candidate.dropoutOk} label="Dropout" />
            <CheckBadge ok={candidate.detectionOk} label="Detection" />
            <CheckBadge ok={candidate.sizeOk} label="Size" />
            <CheckBadge ok={candidate.errorsOk} label="Errors" />
            <CheckBadge ok={candidate.centerOk} label="Center" />
            <CheckBadge ok={candidate.multiBandOk} label="MultiBand" />
          </div>
          {candidate.issues && candidate.issues !== "None" && (
            <div className="mt-1 p-1.5 bg-yellow-50 dark:bg-yellow-900/20 rounded text-[10px] text-yellow-700 dark:text-yellow-400">
              <AlertTriangle className="w-3 h-3 inline mr-1" />
              {candidate.issues}
            </div>
          )}
          {debugMode && (
            <div className="mt-1 p-1.5 bg-blue-50 dark:bg-blue-900/20 rounded text-[10px] text-blue-700 dark:text-blue-400 font-mono">
              FWHM/PSF(F444W) = {fwhmPsfRatio.toFixed(4)}<br />
              PSF F150W = {PSF_FWHM_ARCSEC.F150W}&quot; | F444W = {PSF_FWHM_ARCSEC.F444W}&quot;
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default function Inspection() {
  const [verdicts, setVerdicts] = useState<Record<string, UserVerdict>>({});
  const [filterField, setFilterField] = useState<string>("all");
  const [filterBin, setFilterBin] = useState<string>("all");
  const [filterVerdict, setFilterVerdict] = useState<string>("all");
  const [debugMode, setDebugMode] = useState(false);
  const [stretch, setStretch] = useState<StretchMode>("asinh");
  const [showCrosshair, setShowCrosshair] = useState(true);
  const [showPsf, setShowPsf] = useState(true);
  const [showScale, setShowScale] = useState(true);

  const setVerdict = (id: string, v: UserVerdict) => {
    setVerdicts((prev) => ({ ...prev, [id]: v }));
  };

  const filtered = useMemo(() => {
    return tripleCandidates.filter((c) => {
      if (filterField !== "all" && c.field !== filterField) return false;
      if (filterBin !== "all" && c.binZ !== filterBin) return false;
      if (filterVerdict === "unmarked" && verdicts[`${c.field}-${c.id}`] !== undefined) return false;
      if (filterVerdict === "PASS" && verdicts[`${c.field}-${c.id}`] !== "PASS") return false;
      if (filterVerdict === "MAYBE" && verdicts[`${c.field}-${c.id}`] !== "MAYBE") return false;
      if (filterVerdict === "FAIL" && verdicts[`${c.field}-${c.id}`] !== "FAIL") return false;
      return true;
    });
  }, [filterField, filterBin, filterVerdict, verdicts]);

  const stats = useMemo(() => {
    const total = tripleCandidates.length;
    const marked = Object.keys(verdicts).length;
    const pass = Object.values(verdicts).filter((v) => v === "PASS").length;
    const maybe = Object.values(verdicts).filter((v) => v === "MAYBE").length;
    const fail = Object.values(verdicts).filter((v) => v === "FAIL").length;
    return { total, marked, pass, maybe, fail, unmarked: total - marked };
  }, [verdicts]);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-950">
      <div className="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 py-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Link href="/" className="text-gray-400 hover:text-gray-600">
                <ArrowLeft className="w-5 h-5" />
              </Link>
              <div>
                <h1 className="text-lg font-bold flex items-center gap-2">
                  <Eye className="w-5 h-5 text-indigo-500" />
                  Visual Inspection — Triple Overlap Candidates
                </h1>
                <p className="text-xs text-gray-500">
                  {stats.total} candidates | z {">"} 8 | brightness + redness + compactness overlap
                </p>
              </div>
            </div>

            <div className="flex items-center gap-4 text-xs">
              <button
                onClick={() => setDebugMode(!debugMode)}
                className={`flex items-center gap-1 px-3 py-1.5 rounded-lg font-medium transition-colors ${
                  debugMode
                    ? 'bg-purple-100 text-purple-700 dark:bg-purple-900/40 dark:text-purple-400'
                    : 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400 hover:bg-purple-50'
                }`}
              >
                <Bug className="w-3.5 h-3.5" />
                Debug Mode
              </button>
              <div className="flex items-center gap-2 bg-gray-100 dark:bg-gray-800 rounded-lg px-3 py-1.5">
                <span className="text-gray-500">Reviewed:</span>
                <span className="font-bold">{stats.marked}/{stats.total}</span>
                {stats.pass > 0 && <span className="text-green-600 font-medium">{stats.pass}P</span>}
                {stats.maybe > 0 && <span className="text-yellow-600 font-medium">{stats.maybe}M</span>}
                {stats.fail > 0 && <span className="text-red-600 font-medium">{stats.fail}F</span>}
              </div>
            </div>
          </div>

          <div className="flex items-center gap-3 mt-2">
            <Filter className="w-3.5 h-3.5 text-gray-400" />
            <select
              value={filterField}
              onChange={(e) => setFilterField(e.target.value)}
              className="text-xs border rounded px-2 py-1 bg-white dark:bg-gray-800 dark:border-gray-700"
            >
              <option value="all">All Fields</option>
              <option value="GOODS-S">GOODS-S</option>
              <option value="GOODS-N">GOODS-N</option>
            </select>
            <select
              value={filterBin}
              onChange={(e) => setFilterBin(e.target.value)}
              className="text-xs border rounded px-2 py-1 bg-white dark:bg-gray-800 dark:border-gray-700"
            >
              <option value="all">All z-bins</option>
              <option value="8-10">z = 8–10</option>
              <option value="10-15">z = 10–15</option>
            </select>
            <select
              value={filterVerdict}
              onChange={(e) => setFilterVerdict(e.target.value)}
              className="text-xs border rounded px-2 py-1 bg-white dark:bg-gray-800 dark:border-gray-700"
            >
              <option value="all">All Verdicts</option>
              <option value="unmarked">Unmarked</option>
              <option value="PASS">PASS only</option>
              <option value="MAYBE">MAYBE only</option>
              <option value="FAIL">FAIL only</option>
            </select>
            <span className="text-xs text-gray-400">Showing {filtered.length} of {stats.total}</span>
          </div>

          {debugMode && (
            <div className="flex items-center gap-4 mt-2 p-2 bg-purple-50 dark:bg-purple-900/20 rounded-lg border border-purple-200 dark:border-purple-800">
              <span className="text-[10px] font-bold text-purple-700 dark:text-purple-400 uppercase">Debug Controls</span>

              <div className="flex items-center gap-1">
                <span className="text-[10px] text-gray-500">Stretch:</span>
                {(["asinh", "sqrt", "linear"] as StretchMode[]).map((s) => (
                  <button
                    key={s}
                    onClick={() => setStretch(s)}
                    className={`px-2 py-0.5 text-[10px] rounded font-mono ${
                      stretch === s
                        ? 'bg-purple-600 text-white'
                        : 'bg-white dark:bg-gray-800 text-gray-600 border border-gray-300 dark:border-gray-600 hover:bg-purple-50'
                    }`}
                  >
                    {s}
                  </button>
                ))}
              </div>

              <button
                onClick={() => setShowCrosshair(!showCrosshair)}
                className={`flex items-center gap-0.5 px-2 py-0.5 text-[10px] rounded ${
                  showCrosshair ? 'bg-cyan-100 text-cyan-700' : 'bg-gray-100 text-gray-500'
                }`}
              >
                <Crosshair className="w-3 h-3" /> Crosshair
              </button>

              <button
                onClick={() => setShowPsf(!showPsf)}
                className={`flex items-center gap-0.5 px-2 py-0.5 text-[10px] rounded ${
                  showPsf ? 'bg-red-100 text-red-700' : 'bg-gray-100 text-gray-500'
                }`}
              >
                <Circle className="w-3 h-3" /> PSF Circle
              </button>

              <button
                onClick={() => setShowScale(!showScale)}
                className={`flex items-center gap-0.5 px-2 py-0.5 text-[10px] rounded ${
                  showScale ? 'bg-yellow-100 text-yellow-700' : 'bg-gray-100 text-gray-500'
                }`}
              >
                <Ruler className="w-3 h-3" /> Scale Bar
              </button>
            </div>
          )}
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-4">
        <div className="mb-4 p-3 bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-800 rounded-lg">
          <div className="flex items-start gap-2">
            <AlertTriangle className="w-4 h-4 text-yellow-500 mt-0.5 flex-shrink-0" />
            <div className="text-xs text-yellow-700 dark:text-yellow-400">
              <strong>Phase 0 — Verdicts Suspended:</strong> All 35 candidates have FWHM well below the PSF limit (unresolved/point-like).
              Pipeline validation passed (center ✓, band mapping ✓, compactness ✓).
              Use Debug Mode to verify cutout integrity before assigning verdicts.
              Any verdict here is <em>preliminary</em> — not a discovery claim.
            </div>
          </div>
        </div>

        {debugMode && (
          <div className="mb-4 p-3 bg-purple-50 dark:bg-purple-900/20 border border-purple-200 dark:border-purple-800 rounded-lg">
            <div className="text-xs text-purple-700 dark:text-purple-400">
              <strong>Pipeline Validation Results:</strong>
              <div className="grid grid-cols-3 gap-2 mt-1">
                <div className="bg-white dark:bg-gray-800 rounded p-2">
                  <div className="font-bold text-green-600">Test 1: Center ✓</div>
                  <div className="text-[10px] text-gray-500">Peak within ≤2px of catalog position across all bands (4/5 tested, 1 low-SNR skip)</div>
                </div>
                <div className="bg-white dark:bg-gray-800 rounded p-2">
                  <div className="font-bold text-green-600">Test 2: Band Mapping ✓</div>
                  <div className="text-[10px] text-gray-500">F444W/F150W brightness ratios match catalog SNR ratios (5/5 tested)</div>
                </div>
                <div className="bg-white dark:bg-gray-800 rounded p-2">
                  <div className="font-bold text-green-600">Test 3: Point-Source ✓</div>
                  <div className="text-[10px] text-gray-500">FWHM/PSF &lt; 0.15 sources show high concentration in raw pixels (3/3 tested)</div>
                </div>
              </div>
            </div>
          </div>
        )}

        <div className="space-y-4">
          {filtered.map((c, i) => (
            <CandidateCard
              key={`${c.field}-${c.id}`}
              candidate={c}
              index={tripleCandidates.indexOf(c)}
              userVerdict={verdicts[`${c.field}-${c.id}`] || null}
              onVerdict={(v) => setVerdict(`${c.field}-${c.id}`, v)}
              debugMode={debugMode}
              stretch={stretch}
              showCrosshair={debugMode && showCrosshair}
              showPsf={debugMode && showPsf}
              showScale={debugMode && showScale}
            />
          ))}
        </div>

        {filtered.length === 0 && (
          <div className="text-center py-12 text-gray-400">
            <Eye className="w-8 h-8 mx-auto mb-2 opacity-50" />
            <p className="text-sm">No candidates match current filters.</p>
          </div>
        )}
      </div>
    </div>
  );
}
