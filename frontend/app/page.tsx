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

  useEffect(() => {
    Promise.all([fetchCountries(), fetchStats(), fetchFilters()]).then(([c, s, f]) => {
      setAllCountries(c.countries);
      setFilteredCountries(c.countries);
      setStats(s);
      setFilters(f);
      setLoading(false);
    });
  }, []);

  useEffect(() => {
    fetchCountries({
      region: selectedRegion || undefined,
      income_group: selectedIncome || undefined,
      gap_tier: selectedTier || undefined,
    }).then(r => setFilteredCountries(r.countries));
  }, [selectedRegion, selectedIncome, selectedTier]);

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

  const highlightedIso3s = new Set(filteredCountries.map(c => c.iso3));
  const hasFilter = !!(selectedRegion || selectedIncome || selectedTier);

  if (loading) return (
    <div className="w-screen h-screen flex items-center justify-center bg-[#0a0f1e]">
      <div className="flex flex-col items-center gap-3">
        <div className="w-8 h-8 border-2 border-red-500 border-t-transparent rounded-full animate-spin"/>
        <p className="text-slate-400 text-sm">Loading atlas...</p>
      </div>
    </div>
  );

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
          filteredCount={filteredCountries.length}
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