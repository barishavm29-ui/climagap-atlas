const API = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface Country {
  iso3: string;
  country: string;
  region: string;
  income_group: string;
  vulnerability_score: number;
  inform_risk: number;
  risk_score: number;
  ndc_score: number;
  ndc_tier: string;
  ndc_submitted: boolean;
  ndc_year: number | null;
  policy_score: number;
  gap_score: number;
  gap_tier: string;
  gap_rank: number;
}

export interface Stats {
  total_countries: number;
  average_gap_score: number;
  tier_counts: Record<string, number>;
  regions: string[];
  income_groups: string[];
  top10_gap_countries: Country[];
}

export interface Filters {
  regions: string[];
  income_groups: string[];
  gap_tiers: string[];
  ndc_tiers: string[];
}

export async function fetchCountries(params?: {
  region?: string;
  income_group?: string;
  gap_tier?: string;
}): Promise<{ count: number; countries: Country[] }> {
  const url = new URL(`${API}/api/countries`);
  if (params?.region) url.searchParams.set('region', params.region);
  if (params?.income_group) url.searchParams.set('income_group', params.income_group);
  if (params?.gap_tier) url.searchParams.set('gap_tier', params.gap_tier);
  const res = await fetch(url.toString(), { cache: 'no-store' });
  return res.json();
}

export async function fetchCountry(iso3: string): Promise<Country> {
  const res = await fetch(`${API}/api/countries/${iso3}`, { cache: 'no-store' });
  return res.json();
}

export async function fetchStats(): Promise<Stats> {
  const res = await fetch(`${API}/api/stats`, { cache: 'no-store' });
  return res.json();
}

export async function fetchFilters(): Promise<Filters> {
  const res = await fetch(`${API}/api/filters`, { cache: 'no-store' });
  return res.json();
}

export function getGapColor(gapScore: number | null): string {
  if (gapScore === null || gapScore === undefined) return '#334155';
  if (gapScore >= 50) return '#991b1b';
  if (gapScore >= 30) return '#dc2626';
  if (gapScore >= 10) return '#f97316';
  if (gapScore >= -10) return '#eab308';
  return '#22c55e';
}

export function getTierBadgeClass(tier: string): string {
  const map: Record<string, string> = {
    'Critical': 'gap-critical',
    'High': 'gap-high',
    'Moderate': 'gap-moderate',
    'Low': 'gap-low',
    'Minimal': 'gap-minimal',
  };
  return map[tier] || 'gap-low';
}

export function getNDCBadgeClass(tier: string): string {
  const map: Record<string, string> = {
    'Very High': 'tier-very-high',
    'High': 'tier-high',
    'Medium': 'tier-medium',
    'Low': 'tier-low',
    'Very Low': 'tier-very-low',
  };
  return map[tier] || 'tier-low';
}