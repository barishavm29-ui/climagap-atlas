'use client';

import { useEffect, useState, useCallback } from 'react';
import WorldMap from './components/WorldMap';
import Header from './components/Header';
import Legend from './components/Legend';
import FilterPanel from './components/FilterPanel';
import CountryDrawer from './components/CountryDrawer';
import Top10Panel from './components/Top10Panel';
import { fetchCountries, fetchStats, fetchFilters, Country, Stats, Filters } from './lib/api';

export default function Home() {
  const [allCountries, setAllCountries] = useState<Country[]>([]);
  const [filteredCountries, setFilteredCountries] = useState<Country[]>([]);
  const [stats, setStats] = useState<Stats | null>(null);
  const [filters, setFilters] = useState<Filters | null>(null);
  const [selectedCountry, setSelectedCountry] = useState<Country | null>(null);
  const [selectedRegion, setSelectedRegion] = useState('');
  const [selectedIncome, setSelectedIncome] = useState('');
  const [selectedTier, setSelectedTier] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    async function loadInitialData() {
      try {
        const [c, s, f] = await Promise.all([fetchCountries(), fetchStats(), fetchFilters()]);
        if (cancelled) return;

        setAllCountries(c.countries);
        setFilteredCountries(c.countries);
        setStats(s);
        setFilters(f);
      } catch (err) {
        if (cancelled) return;
        setError(err instanceof Error ? err.message : 'Failed to load atlas data.');
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    void loadInitialData();

    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    if (loading || error) return;

    if (!selectedRegion && !selectedIncome && !selectedTier) return;

    let cancelled = false;

    void fetchCountries({
      region: selectedRegion || undefined,
      income_group: selectedIncome || undefined,
      gap_tier: selectedTier || undefined,
    })
      .then(r => {
        if (!cancelled) setFilteredCountries(r.countries);
      })
      .catch(err => {
        console.error('Failed to refresh filtered countries', err);
      });

    return () => {
      cancelled = true;
    };
  }, [selectedRegion, selectedIncome, selectedTier, loading, error, allCountries]);

  const handleCountryClick = useCallback((iso3: string) => {
    const c = allCountries.find(c => c.iso3 === iso3);
    if (c) setSelectedCountry(prev => prev?.iso3 === iso3 ? null : c);
  }, [allCountries]);

  const handleTop10Select = useCallback((iso3: string) => {
    const c = allCountries.find(c => c.iso3 === iso3);
    if (c) setSelectedCountry(c);
  }, [allCountries]);

  const handleReset = () => {
    setSelectedRegion('');
    setSelectedIncome('');
    setSelectedTier('');
  };

  const hasFilter = !!(selectedRegion || selectedIncome || selectedTier);
  const visibleCountries = hasFilter ? filteredCountries : allCountries;
  const highlightedIso3s = new Set(visibleCountries.map(c => c.iso3));

  if (loading) return (
    <div className="w-screen h-screen flex items-center justify-center bg-[#0a0f1e]">
      <div className="flex flex-col items-center gap-3">
        <div className="w-8 h-8 border-2 border-red-500 border-t-transparent rounded-full animate-spin"/>
        <p className="text-slate-400 text-sm">Loading atlas...</p>
      </div>
    </div>
  );

  if (error) {
    return (
      <div className="w-screen h-screen flex items-center justify-center bg-[#0a0f1e] px-6">
        <div className="max-w-md text-center">
          <p className="text-white font-semibold text-lg">Could not load the atlas</p>
          <p className="text-slate-400 text-sm mt-2">
            The frontend could not reach the backend service. Check the API base URL and try again.
          </p>
          <p className="text-slate-500 text-xs mt-3 break-words">{error}</p>
          <button
            type="button"
            onClick={() => window.location.reload()}
            className="mt-5 px-4 py-2 rounded-lg bg-red-600 text-white text-sm font-medium hover:bg-red-500 transition-colors"
          >
            Reload
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="map-container">
      <WorldMap
        countries={allCountries}
        selectedIso3={selectedCountry?.iso3 || null}
        onCountryClick={handleCountryClick}
        highlightedIso3s={hasFilter ? highlightedIso3s : undefined}
      />

      {stats && (
        <Header
          totalCountries={stats.total_countries}
          criticalCount={stats.tier_counts['Critical']}
          avgGap={stats.average_gap_score}
        />
      )}

      <Legend />

      {filters && (
        <FilterPanel
          regions={filters.regions}
          incomeGroups={filters.income_groups}
          selectedRegion={selectedRegion}
          selectedIncome={selectedIncome}
          selectedTier={selectedTier}
          onRegionChange={setSelectedRegion}
          onIncomeChange={setSelectedIncome}
          onTierChange={setSelectedTier}
          onReset={handleReset}
          filteredCount={visibleCountries.length}
        />
      )}

      <CountryDrawer
        country={selectedCountry}
        onClose={() => setSelectedCountry(null)}
      />

      {stats && (
        <Top10Panel
          countries={stats.top10_gap_countries}
          onSelect={handleTop10Select}
          selectedIso3={selectedCountry?.iso3 || null}
        />
      )}
    </div>
  );
}
