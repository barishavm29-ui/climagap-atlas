import pandas as pd
import numpy as np
import json
import os

RAW = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
OUT = os.path.join(os.path.dirname(__file__), '..', 'data')

VULNERABILITY_DATA = {
    "AFG": 8.2, "ALB": 4.1, "DZA": 5.8, "AGO": 6.9, "ARG": 4.5,
    "ARM": 5.2, "AUS": 3.1, "AUT": 2.2, "AZE": 5.5, "BGD": 8.8,
    "BLR": 3.8, "BEL": 2.0, "BLZ": 6.2, "BEN": 7.1, "BTN": 5.8,
    "BOL": 6.0, "BIH": 4.8, "BWA": 6.5, "BRA": 4.8, "BRN": 3.5,
    "BGR": 3.9, "BFA": 8.1, "BDI": 8.5, "CPV": 6.0, "KHM": 7.2,
    "CMR": 7.0, "CAN": 2.5, "CAF": 9.1, "TCD": 9.2, "CHL": 4.2,
    "CHN": 4.9, "COL": 5.5, "COM": 7.5, "COD": 8.9, "COG": 6.8,
    "CRI": 4.8, "CIV": 7.2, "HRV": 3.5, "CUB": 5.8, "CYP": 3.8,
    "CZE": 2.8, "DNK": 1.8, "DJI": 7.8, "DOM": 6.2, "ECU": 5.8,
    "EGY": 6.8, "SLV": 6.5, "GNQ": 6.0, "ERI": 8.2, "EST": 2.5,
    "SWZ": 6.8, "ETH": 8.5, "FJI": 6.5, "FIN": 1.9, "FRA": 2.2,
    "GAB": 5.5, "GMB": 7.5, "GEO": 5.0, "DEU": 2.0, "GHA": 6.5,
    "GRC": 4.2, "GTM": 6.8, "GIN": 7.8, "GNB": 7.9, "GUY": 5.5,
    "HTI": 9.0, "HND": 7.2, "HUN": 3.5, "IND": 6.8, "IDN": 6.2,
    "IRN": 6.0, "IRQ": 7.5, "IRL": 2.2, "ISR": 3.5, "ITA": 3.2,
    "JAM": 6.0, "JPN": 3.8, "JOR": 6.2, "KAZ": 4.8, "KEN": 7.2,
    "PRK": 7.0, "KOR": 3.2, "KWT": 5.5, "KGZ": 5.8, "LAO": 6.5,
    "LVA": 2.8, "LBN": 7.0, "LSO": 7.2, "LBR": 7.8, "LBY": 6.5,
    "LTU": 2.8, "LUX": 1.8, "MDG": 8.2, "MWI": 8.0, "MYS": 4.5,
    "MDV": 7.8, "MLI": 8.8, "MRT": 8.0, "MEX": 5.5, "MDA": 4.5,
    "MNG": 5.8, "MAR": 5.8, "MOZ": 8.5, "MMR": 7.5, "NAM": 6.2,
    "NPL": 6.8, "NLD": 2.2, "NZL": 2.5, "NIC": 6.8, "NER": 9.0,
    "NGA": 7.5, "MKD": 4.2, "NOR": 1.5, "OMN": 5.5, "PAK": 7.8,
    "PAN": 5.0, "PNG": 6.8, "PRY": 5.5, "PER": 5.8, "PHL": 7.8,
    "POL": 3.2, "PRT": 3.5, "QAT": 4.8, "ROU": 4.2, "RUS": 3.8,
    "RWA": 6.5, "SAU": 5.2, "SEN": 7.0, "SLE": 8.2, "SGP": 3.0,
    "SVK": 3.2, "SVN": 3.0, "SOM": 9.5, "ZAF": 5.8, "SSD": 9.5,
    "ESP": 3.5, "LKA": 5.8, "SDN": 8.8, "SUR": 5.2, "SWE": 1.8,
    "CHE": 1.9, "SYR": 8.8, "TWN": 4.2, "TJK": 6.5, "TZA": 7.5,
    "THA": 5.5, "TLS": 7.0, "TGO": 7.2, "TTO": 4.8, "TUN": 5.5,
    "TUR": 5.2, "TKM": 5.8, "UGA": 7.5, "UKR": 5.0, "ARE": 4.5,
    "GBR": 2.2, "USA": 3.0, "URY": 3.8, "UZB": 5.5, "VEN": 6.5,
    "VNM": 6.2, "YEM": 9.2, "ZMB": 7.2, "ZWE": 7.0,
}

INFORM_DATA = {
    "AFG": 8.1, "ALB": 3.2, "DZA": 4.5, "AGO": 5.8, "ARG": 3.8,
    "ARM": 4.2, "AUS": 2.5, "AUT": 1.8, "AZE": 4.5, "BGD": 7.9,
    "BLR": 3.2, "BEL": 1.9, "BLZ": 5.5, "BEN": 6.2, "BTN": 4.8,
    "BOL": 5.2, "BIH": 4.0, "BWA": 5.2, "BRA": 4.2, "BRN": 2.8,
    "BGR": 3.5, "BFA": 7.5, "BDI": 7.8, "CPV": 4.8, "KHM": 6.2,
    "CMR": 6.2, "CAN": 2.0, "CAF": 8.8, "TCD": 8.9, "CHL": 3.8,
    "CHN": 4.2, "COL": 4.8, "COM": 6.5, "COD": 8.5, "COG": 5.8,
    "CRI": 4.2, "CIV": 6.5, "HRV": 3.0, "CUB": 5.0, "CYP": 3.2,
    "CZE": 2.2, "DNK": 1.5, "DJI": 7.0, "DOM": 5.5, "ECU": 5.0,
    "EGY": 6.0, "SLV": 5.8, "GNQ": 5.2, "ERI": 7.5, "EST": 2.0,
    "SWZ": 5.8, "ETH": 7.8, "FJI": 5.8, "FIN": 1.5, "FRA": 1.8,
    "GAB": 4.5, "GMB": 6.5, "GEO": 4.2, "DEU": 1.5, "GHA": 5.5,
    "GRC": 3.8, "GTM": 6.0, "GIN": 7.0, "GNB": 7.2, "GUY": 4.8,
    "HTI": 8.8, "HND": 6.5, "HUN": 3.0, "IND": 6.0, "IDN": 5.5,
    "IRN": 5.2, "IRQ": 7.0, "IRL": 1.8, "ISR": 3.0, "ITA": 2.8,
    "JAM": 5.2, "JPN": 3.2, "JOR": 5.5, "KAZ": 4.0, "KEN": 6.5,
    "PRK": 6.5, "KOR": 2.8, "KWT": 4.5, "KGZ": 5.0, "LAO": 5.8,
    "LVA": 2.2, "LBN": 6.5, "LSO": 6.5, "LBR": 7.2, "LBY": 6.0,
    "LTU": 2.2, "LUX": 1.5, "MDG": 7.5, "MWI": 7.2, "MYS": 3.8,
    "MDV": 6.8, "MLI": 8.2, "MRT": 7.2, "MEX": 4.8, "MDA": 3.8,
    "MNG": 5.0, "MAR": 5.0, "MOZ": 7.8, "MMR": 7.0, "NAM": 5.2,
    "NPL": 6.0, "NLD": 1.8, "NZL": 2.0, "NIC": 6.0, "NER": 8.5,
    "NGA": 6.8, "MKD": 3.5, "NOR": 1.2, "OMN": 4.5, "PAK": 7.2,
    "PAN": 4.2, "PNG": 6.0, "PRY": 4.8, "PER": 5.0, "PHL": 7.2,
    "POL": 2.8, "PRT": 3.0, "QAT": 4.0, "ROU": 3.8, "RUS": 3.2,
    "RWA": 5.8, "SAU": 4.5, "SEN": 6.2, "SLE": 7.8, "SGP": 2.5,
    "SVK": 2.8, "SVN": 2.5, "SOM": 9.2, "ZAF": 5.0, "SSD": 9.2,
    "ESP": 3.0, "LKA": 5.0, "SDN": 8.2, "SUR": 4.5, "SWE": 1.5,
    "CHE": 1.5, "SYR": 8.5, "TWN": 3.8, "TJK": 5.8, "TZA": 6.8,
    "THA": 4.8, "TLS": 6.2, "TGO": 6.5, "TTO": 4.0, "TUN": 4.8,
    "TUR": 4.5, "TKM": 5.0, "UGA": 6.8, "UKR": 4.5, "ARE": 3.8,
    "GBR": 1.8, "USA": 2.5, "URY": 3.2, "UZB": 4.8, "VEN": 5.8,
    "VNM": 5.5, "YEM": 9.0, "ZMB": 6.5, "ZWE": 6.2,
}

REGION_MAP = {
    "AFG":"South Asia","ALB":"Europe","DZA":"Africa","AGO":"Africa",
    "ARG":"Latin America","ARM":"Europe","AUS":"Oceania","AUT":"Europe",
    "AZE":"Europe","BGD":"South Asia","BLR":"Europe","BEL":"Europe",
    "BLZ":"Latin America","BEN":"Africa","BTN":"South Asia","BOL":"Latin America",
    "BIH":"Europe","BWA":"Africa","BRA":"Latin America","BRN":"East Asia",
    "BGR":"Europe","BFA":"Africa","BDI":"Africa","CPV":"Africa",
    "KHM":"East Asia","CMR":"Africa","CAN":"North America","CAF":"Africa",
    "TCD":"Africa","CHL":"Latin America","CHN":"East Asia","COL":"Latin America",
    "COM":"Africa","COD":"Africa","COG":"Africa","CRI":"Latin America",
    "CIV":"Africa","HRV":"Europe","CUB":"Latin America","CYP":"Europe",
    "CZE":"Europe","DNK":"Europe","DJI":"Africa","DOM":"Latin America",
    "ECU":"Latin America","EGY":"Middle East","SLV":"Latin America",
    "GNQ":"Africa","ERI":"Africa","EST":"Europe","SWZ":"Africa",
    "ETH":"Africa","FJI":"Oceania","FIN":"Europe","FRA":"Europe",
    "GAB":"Africa","GMB":"Africa","GEO":"Europe","DEU":"Europe",
    "GHA":"Africa","GRC":"Europe","GTM":"Latin America","GIN":"Africa",
    "GNB":"Africa","GUY":"Latin America","HTI":"Latin America",
    "HND":"Latin America","HUN":"Europe","IND":"South Asia",
    "IDN":"East Asia","IRN":"Middle East","IRQ":"Middle East",
    "IRL":"Europe","ISR":"Middle East","ITA":"Europe","JAM":"Latin America",
    "JPN":"East Asia","JOR":"Middle East","KAZ":"Central Asia",
    "KEN":"Africa","PRK":"East Asia","KOR":"East Asia","KWT":"Middle East",
    "KGZ":"Central Asia","LAO":"East Asia","LVA":"Europe","LBN":"Middle East",
    "LSO":"Africa","LBR":"Africa","LBY":"Africa","LTU":"Europe",
    "LUX":"Europe","MDG":"Africa","MWI":"Africa","MYS":"East Asia",
    "MDV":"South Asia","MLI":"Africa","MRT":"Africa","MEX":"Latin America",
    "MDA":"Europe","MNG":"East Asia","MAR":"Africa","MOZ":"Africa",
    "MMR":"East Asia","NAM":"Africa","NPL":"South Asia","NLD":"Europe",
    "NZL":"Oceania","NIC":"Latin America","NER":"Africa","NGA":"Africa",
    "MKD":"Europe","NOR":"Europe","OMN":"Middle East","PAK":"South Asia",
    "PAN":"Latin America","PNG":"Oceania","PRY":"Latin America",
    "PER":"Latin America","PHL":"East Asia","POL":"Europe","PRT":"Europe",
    "QAT":"Middle East","ROU":"Europe","RUS":"Europe","RWA":"Africa",
    "SAU":"Middle East","SEN":"Africa","SLE":"Africa","SGP":"East Asia",
    "SVK":"Europe","SVN":"Europe","SOM":"Africa","ZAF":"Africa",
    "SSD":"Africa","ESP":"Europe","LKA":"South Asia","SDN":"Africa",
    "SUR":"Latin America","SWE":"Europe","CHE":"Europe","SYR":"Middle East",
    "TWN":"East Asia","TJK":"Central Asia","TZA":"Africa","THA":"East Asia",
    "TLS":"East Asia","TGO":"Africa","TTO":"Latin America","TUN":"Africa",
    "TUR":"Middle East","TKM":"Central Asia","UGA":"Africa","UKR":"Europe",
    "ARE":"Middle East","GBR":"Europe","USA":"North America","URY":"Latin America",
    "UZB":"Central Asia","VEN":"Latin America","VNM":"East Asia",
    "YEM":"Middle East","ZMB":"Africa","ZWE":"Africa",
}

INCOME_MAP = {
    "AFG":"Low","ALB":"Upper Middle","DZA":"Lower Middle","AGO":"Lower Middle",
    "ARG":"Upper Middle","ARM":"Upper Middle","AUS":"High","AUT":"High",
    "AZE":"Upper Middle","BGD":"Lower Middle","BLR":"Upper Middle","BEL":"High",
    "BLZ":"Upper Middle","BEN":"Low","BTN":"Lower Middle","BOL":"Lower Middle",
    "BIH":"Upper Middle","BWA":"Upper Middle","BRA":"Upper Middle","BRN":"High",
    "BGR":"Upper Middle","BFA":"Low","BDI":"Low","CPV":"Lower Middle",
    "KHM":"Lower Middle","CMR":"Lower Middle","CAN":"High","CAF":"Low",
    "TCD":"Low","CHL":"High","CHN":"Upper Middle","COL":"Upper Middle",
    "COM":"Lower Middle","COD":"Low","COG":"Lower Middle","CRI":"Upper Middle",
    "CIV":"Lower Middle","HRV":"High","CUB":"Upper Middle","CYP":"High",
    "CZE":"High","DNK":"High","DJI":"Lower Middle","DOM":"Upper Middle",
    "ECU":"Upper Middle","EGY":"Lower Middle","SLV":"Lower Middle",
    "GNQ":"Upper Middle","ERI":"Low","EST":"High","SWZ":"Lower Middle",
    "ETH":"Low","FJI":"Upper Middle","FIN":"High","FRA":"High",
    "GAB":"Upper Middle","GMB":"Low","GEO":"Upper Middle","DEU":"High",
    "GHA":"Lower Middle","GRC":"High","GTM":"Upper Middle","GIN":"Low",
    "GNB":"Low","GUY":"Upper Middle","HTI":"Low","HND":"Lower Middle",
    "HUN":"High","IND":"Lower Middle","IDN":"Lower Middle","IRN":"Lower Middle",
    "IRQ":"Upper Middle","IRL":"High","ISR":"High","ITA":"High",
    "JAM":"Upper Middle","JPN":"High","JOR":"Upper Middle","KAZ":"Upper Middle",
    "KEN":"Lower Middle","PRK":"Low","KOR":"High","KWT":"High",
    "KGZ":"Lower Middle","LAO":"Lower Middle","LVA":"High","LBN":"Lower Middle",
    "LSO":"Lower Middle","LBR":"Low","LBY":"Upper Middle","LTU":"High",
    "LUX":"High","MDG":"Low","MWI":"Low","MYS":"Upper Middle",
    "MDV":"Upper Middle","MLI":"Low","MRT":"Lower Middle","MEX":"Upper Middle",
    "MDA":"Lower Middle","MNG":"Lower Middle","MAR":"Lower Middle","MOZ":"Low",
    "MMR":"Lower Middle","NAM":"Upper Middle","NPL":"Lower Middle","NLD":"High",
    "NZL":"High","NIC":"Lower Middle","NER":"Low","NGA":"Lower Middle",
    "MKD":"Upper Middle","NOR":"High","OMN":"High","PAK":"Lower Middle",
    "PAN":"Upper Middle","PNG":"Lower Middle","PRY":"Upper Middle",
    "PER":"Upper Middle","PHL":"Lower Middle","POL":"High","PRT":"High",
    "QAT":"High","ROU":"High","RUS":"Upper Middle","RWA":"Low",
    "SAU":"High","SEN":"Lower Middle","SLE":"Low","SGP":"High",
    "SVK":"High","SVN":"High","SOM":"Low","ZAF":"Upper Middle",
    "SSD":"Low","ESP":"High","LKA":"Lower Middle","SDN":"Low",
    "SUR":"Upper Middle","SWE":"High","CHE":"High","SYR":"Low",
    "TWN":"High","TJK":"Low","TZA":"Low","THA":"Upper Middle",
    "TLS":"Lower Middle","TGO":"Low","TTO":"High","TUN":"Lower Middle",
    "TUR":"Upper Middle","TKM":"Upper Middle","UGA":"Low","UKR":"Lower Middle",
    "ARE":"High","GBR":"High","USA":"High","URY":"High",
    "UZB":"Lower Middle","VEN":"Upper Middle","VNM":"Lower Middle",
    "YEM":"Low","ZMB":"Low","ZWE":"Low",
}

def load_ndc():
    path = os.path.join(RAW, 'ndc_scores.json')
    with open(path) as f:
        data = json.load(f)
    return {d['iso3']: d for d in data}

def compute_gap_score(vulnerability, inform, ndc_score):
    risk = (vulnerability * 0.5) + (inform * 0.5)
    risk_norm = min(risk / 10.0, 1.0)
    policy_norm = ndc_score / 100.0
    gap = round((risk_norm - policy_norm) * 100, 2)
    return round(risk_norm * 100, 2), round(policy_norm * 100, 2), gap

def get_gap_tier(gap):
    if gap >= 50: return "Critical"
    if gap >= 30: return "High"
    if gap >= 10: return "Moderate"
    if gap >= -10: return "Low"
    return "Minimal"

def build():
    print("Building countries dataset...")
    ndc = load_ndc()
    countries = []

    for iso3, vuln in VULNERABILITY_DATA.items():
        if iso3 not in ndc:
            continue
        inform = INFORM_DATA.get(iso3, vuln * 0.9)
        n = ndc[iso3]
        risk_score, policy_score, gap_score = compute_gap_score(vuln, inform, n['ndc_score'])

        countries.append({
            "iso3": iso3,
            "country": n['country'],
            "region": REGION_MAP.get(iso3, "Other"),
            "income_group": INCOME_MAP.get(iso3, "Unknown"),
            "vulnerability_score": round(vuln, 2),
            "inform_risk": round(inform, 2),
            "risk_score": risk_score,
            "ndc_score": n['ndc_score'],
            "ndc_tier": n['ndc_tier'],
            "ndc_submitted": n['ndc_submitted'],
            "ndc_year": n['ndc_year'],
            "policy_score": policy_score,
            "gap_score": gap_score,
            "gap_tier": get_gap_tier(gap_score),
        })

    countries.sort(key=lambda x: x['gap_score'], reverse=True)
    for i, c in enumerate(countries):
        c['gap_rank'] = i + 1

    out_path = os.path.join(OUT, 'countries.json')
    with open(out_path, 'w') as f:
        json.dump(countries, f, indent=2)

    print(f"  {len(countries)} countries saved to {out_path}")

    critical = [c for c in countries if c['gap_tier'] == 'Critical']
    high = [c for c in countries if c['gap_tier'] == 'High']
    print(f"  Critical gap: {len(critical)} countries")
    print(f"  High gap:     {len(high)} countries")
    print(f"  Top 5 gap countries:")
    for c in countries[:5]:
        print(f"    {c['gap_rank']}. {c['country']} — gap: {c['gap_score']} ({c['gap_tier']})")

if __name__ == '__main__':
    print("=== ClimaGap Atlas — Dataset Builder ===\n")
    build()
    print("\nDone.")