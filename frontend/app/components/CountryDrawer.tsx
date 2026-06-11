'use client';
import { Country, getTierBadgeClass, getNDCBadgeClass } from '../lib/api';

interface DrawerProps {
  country: Country | null;
  onClose: () => void;
}

function ScoreBar({ value, max = 100, color }: { value: number; max?: number; color: string }) {
  return (
    <div className="w-full bg-slate-700 rounded-full h-1.5 mt-1">
      <div
        className="h-1.5 rounded-full transition-all duration-500"
        style={{ width: `${(value / max) * 100}%`, background: color }}
      />
    </div>
  );
}

export default function CountryDrawer({ country, onClose }: DrawerProps) {
  if (!country) return null;

  return (
    <div className="absolute top-20 left-6 bottom-20 z-20 w-72 panel p-6 overflow-y-auto scrollbar-thin flex flex-col gap-5">
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-white font-semibold text-base leading-tight">{country.country}</h2>
          <p className="text-slate-400 text-xs mt-0.5">{country.region} · {country.income_group}</p>
        </div>
        <button
          onClick={onClose}
          className="text-slate-500 hover:text-white transition-colors mt-0.5"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M18 6L6 18M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <div className="flex items-center gap-2">
        <span className={`text-xs px-2 py-0.5 rounded-md font-medium ${getTierBadgeClass(country.gap_tier)}`}>
          {country.gap_tier} Gap
        </span>
        <span className="text-slate-400 text-xs">Rank #{country.gap_rank} globally</span>
      </div>

      <div className="bg-slate-800 rounded-xl p-4">
        <p className="text-slate-400 text-xs uppercase tracking-wider mb-1">Gap Score</p>
        <p className="text-white text-3xl font-bold">{country.gap_score.toFixed(1)}</p>
        <p className="text-slate-500 text-xs mt-1">Risk − Policy response</p>
        <ScoreBar value={Math.max(0, country.gap_score)} color={
          country.gap_score >= 50 ? '#991b1b' :
          country.gap_score >= 30 ? '#dc2626' :
          country.gap_score >= 10 ? '#f97316' : '#22c55e'
        }/>
      </div>

      <div className="flex flex-col gap-3">
        <div>
          <div className="flex justify-between items-center">
            <p className="text-slate-400 text-xs">Climate risk score</p>
            <p className="text-red-400 text-xs font-medium">{country.risk_score.toFixed(1)}</p>
          </div>
          <ScoreBar value={country.risk_score} color="#dc2626"/>
          <p className="text-slate-600 text-xs mt-1">Vulnerability: {country.vulnerability_score} · INFORM: {country.inform_risk}</p>
        </div>

        <div>
          <div className="flex justify-between items-center">
            <p className="text-slate-400 text-xs">Policy response score</p>
            <p className="text-blue-400 text-xs font-medium">{country.policy_score.toFixed(1)}</p>
          </div>
          <ScoreBar value={country.policy_score} color="#3b82f6"/>
        </div>
      </div>

      <div className="border-t border-slate-700 pt-4">
        <p className="text-slate-400 text-xs uppercase tracking-wider mb-3">NDC Status</p>
        <div className="flex items-center justify-between mb-2">
          <span className="text-slate-300 text-xs">NDC submitted</span>
          <span className={`text-xs px-2 py-0.5 rounded ${country.ndc_submitted ? 'bg-green-900 text-green-300' : 'bg-red-900 text-red-300'}`}>
            {country.ndc_submitted ? `Yes (${country.ndc_year})` : 'No'}
          </span>
        </div>
        <div className="flex items-center justify-between mb-2">
          <span className="text-slate-300 text-xs">NDC quality tier</span>
          <span className={`text-xs px-2 py-0.5 rounded-md font-medium ${getNDCBadgeClass(country.ndc_tier)}`}>
            {country.ndc_tier}
          </span>
        </div>
        <div className="flex items-center justify-between">
          <span className="text-slate-300 text-xs">NDC score</span>
          <span className="text-slate-200 text-xs font-medium">{country.ndc_score}/100</span>
        </div>
        <ScoreBar value={country.ndc_score} color="#3b82f6"/>
      </div>

      <div className="border-t border-slate-700 pt-4">
        <p className="text-slate-400 text-xs uppercase tracking-wider mb-2">What this means</p>
        <p className="text-slate-300 text-xs leading-relaxed">
          {country.country} faces{' '}
          <span className="text-red-300">{country.gap_tier.toLowerCase()} climate risk</span>{' '}
          with a risk score of {country.risk_score.toFixed(0)}/100, but its climate policy
          response scores only {country.policy_score.toFixed(0)}/100 — a gap of{' '}
          <span className="text-orange-300 font-medium">{country.gap_score.toFixed(1)} points</span>.
          {country.gap_score >= 30
            ? ' This country is among those most urgently needing international climate finance and adaptation support.'
            : country.gap_score >= 0
            ? ' Climate adaptation efforts need to be scaled up to match the level of exposure.'
            : ' Policy ambition currently exceeds measured risk levels.'}
        </p>
      </div>
    </div>
  );
}
