'use client';
import Link from 'next/link';

interface HeaderProps {
  totalCountries: number;
  criticalCount: number;
  avgGap: number;
}

export default function Header({ totalCountries, criticalCount, avgGap }: HeaderProps) {
  return (
    <div className="absolute top-0 left-0 right-0 z-20 flex items-center justify-between px-6 py-4">
      <div className="flex items-center gap-3">
        <div className="w-8 h-8 rounded-lg bg-red-900 flex items-center justify-center">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fca5a5" strokeWidth="2">
            <circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
          </svg>
        </div>
        <div>
          <h1 className="text-white font-semibold text-base leading-tight">ClimaGap Atlas</h1>
          <p className="text-slate-400 text-xs">Climate Vulnerability vs Policy Response</p>
        </div>
      </div>

      <div className="flex items-center gap-3">
        <div className="panel px-5 py-3 flex items-center gap-8">
          <div className="text-center">
            <p className="text-slate-400 text-xs">Countries</p>
            <p className="text-white font-semibold text-sm">{totalCountries}</p>
          </div>
          <div className="w-px h-6 bg-slate-700"/>
          <div className="text-center">
            <p className="text-slate-400 text-xs">Critical gaps</p>
            <p className="text-red-400 font-semibold text-sm">{criticalCount}</p>
          </div>
          <div className="w-px h-6 bg-slate-700"/>
          <div className="text-center">
            <p className="text-slate-400 text-xs">Avg gap score</p>
            <p className="text-orange-400 font-semibold text-sm">{avgGap.toFixed(1)}</p>
          </div>
        </div>
        <Link
          href="/methodology"
          className="text-slate-400 hover:text-white text-xs transition-colors px-3 py-1.5 panel"
        >
          Methodology
        </Link>
      </div>
    </div>
  );
}
