'use client';
import { Country } from '../lib/api';

interface Top10Props {
  countries: Country[];
  onSelect: (iso3: string) => void;
  selectedIso3: string | null;
}

export default function Top10Panel({ countries, onSelect, selectedIso3 }: Top10Props) {
  const colors = [
    '#991b1b','#b91c1c','#dc2626','#ef4444','#f97316',
    '#fb923c','#fbbf24','#facc15','#a3e635','#4ade80',
  ];

  return (
    <div className="absolute bottom-6 right-6 z-20 panel w-64 p-4">
      <p className="text-slate-400 text-xs font-medium uppercase tracking-wider mb-3">
        Top 10 — Highest gap
      </p>
      <div className="flex flex-col gap-1.5">
        {countries.map((c, i) => (
          <button
            key={c.iso3}
            onClick={() => onSelect(c.iso3)}
            className={`flex items-center gap-2 px-2 py-2 rounded-lg text-left transition-all hover:bg-slate-700 ${
              selectedIso3 === c.iso3 ? 'bg-slate-700' : ''
            }`}
          >
            <span className="text-slate-500 text-xs w-4">{i + 1}</span>
            <div
              className="w-2 h-2 rounded-sm flex-shrink-0"
              style={{ background: colors[i] }}
            />
            <span className="text-slate-200 text-xs flex-1 truncate">{c.country}</span>
            <span className="text-slate-400 text-xs">{c.gap_score.toFixed(0)}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
