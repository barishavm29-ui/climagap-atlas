const API_BASE_URL = (process.env.NEXT_PUBLIC_API_BASE_URL || '/_/backend').replace(/\/$/, '');

function apiUrl(path: string, query?: Record<string, string | undefined>): string {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  const url = `${API_BASE_URL}${normalizedPath}`;
  if (!query) return url;

  const searchParams = new URLSearchParams();
  for (const [key, value] of Object.entries(query)) {
    if (value) searchParams.set(key, value);
  }

  const queryString = searchParams.toString();
  return queryString ? `${url}?${queryString}` : url;
}

async function fetchJson<T>(url: string): Promise<T> {
  const res = await fetch(url, { cache: 'no-store' });
  if (!res.ok) {
    throw new Error(`Request failed with ${res.status} ${res.statusText} for ${url}`);
  }
  return (await res.json()) as T;
}

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
  return fetchJson(apiUrl('/api/countries', params));
}

export async function fetchCountry(iso3: string): Promise<Country> {
  return fetchJson(apiUrl(`/api/countries/${iso3}`));
}

export async function fetchStats(): Promise<Stats> {
  return fetchJson(apiUrl('/api/stats'));
}

export async function fetchFilters(): Promise<Filters> {
  return fetchJson(apiUrl('/api/filters'));
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
