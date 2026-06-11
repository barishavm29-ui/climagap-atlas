'use client';

interface FilterPanelProps {
  regions: string[];
  incomeGroups: string[];
  selectedRegion: string;
  selectedIncome: string;
  selectedTier: string;
  onRegionChange: (v: string) => void;
  onIncomeChange: (v: string) => void;
  onTierChange: (v: string) => void;
  onReset: () => void;
  filteredCount: number;
}

const TIERS = ['Critical', 'High', 'Moderate', 'Low', 'Minimal'];

const tierColors: Record<string, string> = {
  Critical: 'text-red-400',
  High: 'text-red-300',
  Moderate: 'text-orange-400',
  Low: 'text-yellow-400',
  Minimal: 'text-green-400',
};

export default function FilterPanel({
  regions, incomeGroups, selectedRegion, selectedIncome,
  selectedTier, onRegionChange, onIncomeChange, onTierChange,
  onReset, filteredCount,
}: FilterPanelProps) {
  const hasFilter = selectedRegion || selectedIncome || selectedTier;

  return (
    <div className="absolute top-20 right-6 z-20 panel w-56 p-4">
      <div className="flex items-center justify-between mb-3">
        <p className="text-slate-300 text-xs font-medium uppercase tracking-wider">Filters</p>
        {hasFilter && (
          <button onClick={onReset} className="text-slate-400 hover:text-white text-xs transition-colors">
            Reset
          </button>
        )}
      </div>

      <div className="flex flex-col gap-4">
        <div>
          <label className="text-slate-400 text-xs mb-2 block">Region</label>
          <select
            value={selectedRegion}
            onChange={e => onRegionChange(e.target.value)}
            className="w-full bg-slate-800 border border-slate-700 text-slate-200 text-xs rounded-lg px-3 py-2 focus:outline-none focus:border-slate-500"
          >
            <option value="">All regions</option>
            {regions.map(r => <option key={r} value={r}>{r}</option>)}
          </select>
        </div>

        <div>
          <label className="text-slate-400 text-xs mb-2 block">Income group</label>
          <select
            value={selectedIncome}
            onChange={e => onIncomeChange(e.target.value)}
            className="w-full bg-slate-800 border border-slate-700 text-slate-200 text-xs rounded-lg px-3 py-2 focus:outline-none focus:border-slate-500"
          >
            <option value="">All income groups</option>
            {incomeGroups.map(g => <option key={g} value={g}>{g}</option>)}
          </select>
        </div>

        <div>
          <label className="text-slate-400 text-xs mb-2 block">Gap tier</label>
          <div className="flex flex-col gap-2">
            {TIERS.map(tier => (
              <button
                key={tier}
                onClick={() => onTierChange(selectedTier === tier ? '' : tier)}
                className={`text-left px-3 py-2 rounded text-xs transition-all ${
                  selectedTier === tier
                    ? 'bg-slate-600 ' + tierColors[tier]
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                }`}
              >
                {tier}
              </button>
            ))}
          </div>
        </div>

        <div className="pt-2 border-t border-slate-700">
          <p className="text-slate-400 text-xs">
            Showing <span className="text-white font-medium">{filteredCount}</span> countries
          </p>
        </div>
      </div>
    </div>
  );
}
