import requests
import pandas as pd
import json
import os

RAW = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(RAW, exist_ok=True)

def fetch_ndgain():
    print("Fetching ND-GAIN data...")
    url = "https://raw.githubusercontent.com/NDGAIN/ndgain-data/master/gain/yearly/2021.csv"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        path = os.path.join(RAW, 'ndgain.csv')
        with open(path, 'wb') as f:
            f.write(r.content)
        print(f"  saved to {path}")
        return True
    except Exception as e:
        print(f"  ND-GAIN fetch failed: {e}")
        return False

def fetch_inform():
    print("Fetching INFORM Risk Index data...")
    url = "https://drmkc.jrc.ec.europa.eu/inform-index/Portals/0/InfoRM/INFORM2024/INFORM_Risk_2024_v068.xlsx"
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        path = os.path.join(RAW, 'inform.xlsx')
        with open(path, 'wb') as f:
            f.write(r.content)
        print(f"  saved to {path}")
        return True
    except Exception as e:
        print(f"  INFORM fetch failed: {e}")
        return False

def fetch_worldbank_vulnerability():
    print("Fetching World Bank Climate Vulnerability data...")
    url = "https://api.worldbank.org/v2/country/all/indicator/EN.CLC.MDAT.ZS?format=json&per_page=300&mrv=1"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        path = os.path.join(RAW, 'wb_vulnerability.json')
        with open(path, 'w') as f:
            json.dump(r.json(), f)
        print(f"  saved to {path}")
        return True
    except Exception as e:
        print(f"  World Bank fetch failed: {e}")
        return False

def fetch_ndc_data():
    print("Creating NDC policy quality dataset...")
    ndc_data = [
        {"iso3":"AFG","country":"Afghanistan","ndc_score":25,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2015},
        {"iso3":"ALB","country":"Albania","ndc_score":55,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"DZA","country":"Algeria","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"AGO","country":"Angola","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ARG","country":"Argentina","ndc_score":50,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ARM","country":"Armenia","ndc_score":45,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"AUS","country":"Australia","ndc_score":52,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"AUT","country":"Austria","ndc_score":72,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"AZE","country":"Azerbaijan","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BGD","country":"Bangladesh","ndc_score":48,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BLR","country":"Belarus","ndc_score":35,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BEL","country":"Belgium","ndc_score":70,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"BLZ","country":"Belize","ndc_score":42,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BEN","country":"Benin","ndc_score":33,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BTN","country":"Bhutan","ndc_score":60,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BOL","country":"Bolivia","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BIH","country":"Bosnia and Herzegovina","ndc_score":30,"ndc_tier":"Low","ndc_submitted":False,"ndc_year":None},
        {"iso3":"BWA","country":"Botswana","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BRA","country":"Brazil","ndc_score":55,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"BRN","country":"Brunei","ndc_score":28,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"BGR","country":"Bulgaria","ndc_score":62,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"BFA","country":"Burkina Faso","ndc_score":28,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"BDI","country":"Burundi","ndc_score":22,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"CPV","country":"Cabo Verde","ndc_score":50,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"KHM","country":"Cambodia","ndc_score":42,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"CMR","country":"Cameroon","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"CAN","country":"Canada","ndc_score":65,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"CAF","country":"Central African Republic","ndc_score":18,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"TCD","country":"Chad","ndc_score":20,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"CHL","country":"Chile","ndc_score":62,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"CHN","country":"China","ndc_score":58,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"COL","country":"Colombia","ndc_score":58,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"COM","country":"Comoros","ndc_score":25,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"COD","country":"Congo, Dem. Rep.","ndc_score":20,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"COG","country":"Congo, Rep.","ndc_score":28,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"CRI","country":"Costa Rica","ndc_score":72,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"CIV","country":"Cote d'Ivoire","ndc_score":32,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"HRV","country":"Croatia","ndc_score":65,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"CUB","country":"Cuba","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"CYP","country":"Cyprus","ndc_score":60,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"CZE","country":"Czech Republic","ndc_score":68,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"DNK","country":"Denmark","ndc_score":85,"ndc_tier":"Very High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"DJI","country":"Djibouti","ndc_score":25,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"DOM","country":"Dominican Republic","ndc_score":45,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"ECU","country":"Ecuador","ndc_score":50,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"EGY","country":"Egypt","ndc_score":42,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"SLV","country":"El Salvador","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"GNQ","country":"Equatorial Guinea","ndc_score":20,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ERI","country":"Eritrea","ndc_score":15,"ndc_tier":"Very Low","ndc_submitted":False,"ndc_year":None},
        {"iso3":"EST","country":"Estonia","ndc_score":70,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"SWZ","country":"Eswatini","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ETH","country":"Ethiopia","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"FJI","country":"Fiji","ndc_score":60,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"FIN","country":"Finland","ndc_score":82,"ndc_tier":"Very High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"FRA","country":"France","ndc_score":78,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"GAB","country":"Gabon","ndc_score":35,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"GMB","country":"Gambia","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"GEO","country":"Georgia","ndc_score":45,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"DEU","country":"Germany","ndc_score":80,"ndc_tier":"Very High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"GHA","country":"Ghana","ndc_score":42,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"GRC","country":"Greece","ndc_score":65,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"GTM","country":"Guatemala","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"GIN","country":"Guinea","ndc_score":22,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"GNB","country":"Guinea-Bissau","ndc_score":20,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"GUY","country":"Guyana","ndc_score":45,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"HTI","country":"Haiti","ndc_score":20,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"HND","country":"Honduras","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"HUN","country":"Hungary","ndc_score":62,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"IND","country":"India","ndc_score":55,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"IDN","country":"Indonesia","ndc_score":50,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"IRN","country":"Iran","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2015},
        {"iso3":"IRQ","country":"Iraq","ndc_score":22,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"IRL","country":"Ireland","ndc_score":75,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"ISR","country":"Israel","ndc_score":58,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ITA","country":"Italy","ndc_score":72,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"JAM","country":"Jamaica","ndc_score":48,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"JPN","country":"Japan","ndc_score":70,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"JOR","country":"Jordan","ndc_score":45,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"KAZ","country":"Kazakhstan","ndc_score":35,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"KEN","country":"Kenya","ndc_score":50,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"PRK","country":"North Korea","ndc_score":15,"ndc_tier":"Very Low","ndc_submitted":False,"ndc_year":None},
        {"iso3":"KOR","country":"South Korea","ndc_score":62,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"KWT","country":"Kuwait","ndc_score":22,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"KGZ","country":"Kyrgyzstan","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"LAO","country":"Laos","ndc_score":32,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"LVA","country":"Latvia","ndc_score":68,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"LBN","country":"Lebanon","ndc_score":25,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"LSO","country":"Lesotho","ndc_score":28,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"LBR","country":"Liberia","ndc_score":22,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"LBY","country":"Libya","ndc_score":18,"ndc_tier":"Very Low","ndc_submitted":False,"ndc_year":None},
        {"iso3":"LTU","country":"Lithuania","ndc_score":68,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"LUX","country":"Luxembourg","ndc_score":75,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"MDG","country":"Madagascar","ndc_score":28,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MWI","country":"Malawi","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MYS","country":"Malaysia","ndc_score":48,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MDV","country":"Maldives","ndc_score":62,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"MLI","country":"Mali","ndc_score":20,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MRT","country":"Mauritania","ndc_score":25,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MEX","country":"Mexico","ndc_score":52,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"MDA","country":"Moldova","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MNG","country":"Mongolia","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MAR","country":"Morocco","ndc_score":60,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MOZ","country":"Mozambique","ndc_score":32,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MMR","country":"Myanmar","ndc_score":28,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"NAM","country":"Namibia","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"NPL","country":"Nepal","ndc_score":42,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"NLD","country":"Netherlands","ndc_score":78,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"NZL","country":"New Zealand","ndc_score":65,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"NIC","country":"Nicaragua","ndc_score":35,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"NER","country":"Niger","ndc_score":22,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"NGA","country":"Nigeria","ndc_score":35,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"MKD","country":"North Macedonia","ndc_score":45,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"NOR","country":"Norway","ndc_score":85,"ndc_tier":"Very High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"OMN","country":"Oman","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"PAK","country":"Pakistan","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"PAN","country":"Panama","ndc_score":55,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"PNG","country":"Papua New Guinea","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"PRY","country":"Paraguay","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"PER","country":"Peru","ndc_score":55,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"PHL","country":"Philippines","ndc_score":52,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"POL","country":"Poland","ndc_score":58,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"PRT","country":"Portugal","ndc_score":75,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"QAT","country":"Qatar","ndc_score":20,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ROU","country":"Romania","ndc_score":60,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"RUS","country":"Russia","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"RWA","country":"Rwanda","ndc_score":48,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"SAU","country":"Saudi Arabia","ndc_score":25,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"SEN","country":"Senegal","ndc_score":42,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"SLE","country":"Sierra Leone","ndc_score":25,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"SGP","country":"Singapore","ndc_score":60,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"SVK","country":"Slovakia","ndc_score":65,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"SVN","country":"Slovenia","ndc_score":68,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"SOM","country":"Somalia","ndc_score":15,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ZAF","country":"South Africa","ndc_score":52,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"SSD","country":"South Sudan","ndc_score":12,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ESP","country":"Spain","ndc_score":75,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"LKA","country":"Sri Lanka","ndc_score":45,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"SDN","country":"Sudan","ndc_score":18,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"SUR","country":"Suriname","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"SWE","country":"Sweden","ndc_score":88,"ndc_tier":"Very High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"CHE","country":"Switzerland","ndc_score":80,"ndc_tier":"Very High","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"SYR","country":"Syria","ndc_score":15,"ndc_tier":"Very Low","ndc_submitted":False,"ndc_year":None},
        {"iso3":"TWN","country":"Taiwan","ndc_score":50,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"TJK","country":"Tajikistan","ndc_score":28,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"TZA","country":"Tanzania","ndc_score":38,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"THA","country":"Thailand","ndc_score":52,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"TLS","country":"Timor-Leste","ndc_score":35,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"TGO","country":"Togo","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"TTO","country":"Trinidad and Tobago","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"TUN","country":"Tunisia","ndc_score":48,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"TUR","country":"Turkey","ndc_score":42,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"TKM","country":"Turkmenistan","ndc_score":18,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"UGA","country":"Uganda","ndc_score":35,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"UKR","country":"Ukraine","ndc_score":40,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ARE","country":"United Arab Emirates","ndc_score":32,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"GBR","country":"United Kingdom","ndc_score":82,"ndc_tier":"Very High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"USA","country":"United States","ndc_score":62,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"URY","country":"Uruguay","ndc_score":65,"ndc_tier":"High","ndc_submitted":True,"ndc_year":2020},
        {"iso3":"UZB","country":"Uzbekistan","ndc_score":28,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"VEN","country":"Venezuela","ndc_score":20,"ndc_tier":"Very Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"VNM","country":"Vietnam","ndc_score":50,"ndc_tier":"Medium","ndc_submitted":True,"ndc_year":2022},
        {"iso3":"YEM","country":"Yemen","ndc_score":15,"ndc_tier":"Very Low","ndc_submitted":False,"ndc_year":None},
        {"iso3":"ZMB","country":"Zambia","ndc_score":35,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
        {"iso3":"ZWE","country":"Zimbabwe","ndc_score":30,"ndc_tier":"Low","ndc_submitted":True,"ndc_year":2021},
    ]
    path = os.path.join(RAW, 'ndc_scores.json')
    with open(path, 'w') as f:
        json.dump(ndc_data, f, indent=2)
    print(f"  saved to {path} ({len(ndc_data)} countries)")
    return True

if __name__ == '__main__':
    print("=== ClimaGap Atlas — Data Fetcher ===\n")
    fetch_ndgain()
    fetch_inform()
    fetch_worldbank_vulnerability()
    fetch_ndc_data()
    print("\nDone. Check backend/data/raw/ for files.")