from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from typing import Optional

app = FastAPI(title="ClimaGap Atlas API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://*.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'countries.json')

def load_data():
    with open(DATA_PATH) as f:
        return json.load(f)

@app.get("/")
def root():
    return {"message": "ClimaGap Atlas API", "status": "running"}

@app.get("/api/countries")
def get_countries(
    region: Optional[str] = Query(None),
    income_group: Optional[str] = Query(None),
    gap_tier: Optional[str] = Query(None),
    ndc_submitted: Optional[bool] = Query(None),
):
    countries = load_data()
    if region:
        countries = [c for c in countries if c['region'] == region]
    if income_group:
        countries = [c for c in countries if c['income_group'] == income_group]
    if gap_tier:
        countries = [c for c in countries if c['gap_tier'] == gap_tier]
    if ndc_submitted is not None:
        countries = [c for c in countries if c['ndc_submitted'] == ndc_submitted]
    return {"count": len(countries), "countries": countries}

@app.get("/api/countries/{iso3}")
def get_country(iso3: str):
    countries = load_data()
    iso3 = iso3.upper()
    match = next((c for c in countries if c['iso3'] == iso3), None)
    if not match:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=f"Country {iso3} not found")
    return match

@app.get("/api/stats")
def get_stats():
    countries = load_data()
    tiers = ["Critical", "High", "Moderate", "Low", "Minimal"]
    tier_counts = {t: len([c for c in countries if c['gap_tier'] == t]) for t in tiers}
    regions = list(set(c['region'] for c in countries))
    income_groups = list(set(c['income_group'] for c in countries))
    avg_gap = round(sum(c['gap_score'] for c in countries) / len(countries), 2)
    top10 = sorted(countries, key=lambda x: x['gap_score'], reverse=True)[:10]
    return {
        "total_countries": len(countries),
        "average_gap_score": avg_gap,
        "tier_counts": tier_counts,
        "regions": sorted(regions),
        "income_groups": sorted(income_groups),
        "top10_gap_countries": top10,
    }

@app.get("/api/filters")
def get_filters():
    countries = load_data()
    return {
        "regions": sorted(list(set(c['region'] for c in countries))),
        "income_groups": sorted(list(set(c['income_group'] for c in countries))),
        "gap_tiers": ["Critical", "High", "Moderate", "Low", "Minimal"],
        "ndc_tiers": ["Very High", "High", "Medium", "Low", "Very Low"],
    }