'use client';

import { useState, useCallback } from 'react';
import { ComposableMap, Geographies, Geography, ZoomableGroup } from 'react-simple-maps';
import { Country, getGapColor } from '../lib/api';

const GEO_URL = 'https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json';

const ISO_NUMERIC_TO_ALPHA3: Record<string, string> = {
  "004":"AFG","008":"ALB","012":"DZA","024":"AGO","032":"ARG","051":"ARM",
  "036":"AUS","040":"AUT","031":"AZE","050":"BGD","112":"BLR","056":"BEL",
  "084":"BLZ","204":"BEN","064":"BTN","068":"BOL","070":"BIH","072":"BWA",
  "076":"BRA","096":"BRN","100":"BGR","854":"BFA","108":"BDI","132":"CPV",
  "116":"KHM","120":"CMR","124":"CAN","140":"CAF","148":"TCD","152":"CHL",
  "156":"CHN","170":"COL","174":"COM","180":"COD","178":"COG","188":"CRI",
  "384":"CIV","191":"HRV","192":"CUB","196":"CYP","203":"CZE","208":"DNK",
  "262":"DJI","214":"DOM","218":"ECU","818":"EGY","222":"SLV","226":"GNQ",
  "232":"ERI","233":"EST","748":"SWZ","231":"ETH","242":"FJI","246":"FIN",
  "250":"FRA","266":"GAB","270":"GMB","268":"GEO","276":"DEU","288":"GHA",
  "300":"GRC","320":"GTM","324":"GIN","624":"GNB","328":"GUY","332":"HTI",
  "340":"HND","348":"HUN","356":"IND","360":"IDN","364":"IRN","368":"IRQ",
  "372":"IRL","376":"ISR","380":"ITA","388":"JAM","392":"JPN","400":"JOR",
  "398":"KAZ","404":"KEN","408":"PRK","410":"KOR","414":"KWT","417":"KGZ",
  "418":"LAO","428":"LVA","422":"LBN","426":"LSO","430":"LBR","434":"LBY",
  "440":"LTU","442":"LUX","450":"MDG","454":"MWI","458":"MYS","462":"MDV",
  "466":"MLI","478":"MRT","484":"MEX","498":"MDA","496":"MNG","504":"MAR",
  "508":"MOZ","104":"MMR","516":"NAM","524":"NPL","528":"NLD","554":"NZL",
  "558":"NIC","562":"NER","566":"NGA","807":"MKD","578":"NOR","512":"OMN",
  "586":"PAK","591":"PAN","598":"PNG","600":"PRY","604":"PER","608":"PHL",
  "616":"POL","620":"PRT","634":"QAT","642":"ROU","643":"RUS","646":"RWA",
  "682":"SAU","686":"SEN","694":"SLE","702":"SGP","703":"SVK","705":"SVN",
  "706":"SOM","710":"ZAF","728":"SSD","724":"ESP","144":"LKA","729":"SDN",
  "740":"SUR","752":"SWE","756":"CHE","760":"SYR","762":"TJK","834":"TZA",
  "764":"THA","626":"TLS","768":"TGO","780":"TTO","788":"TUN","792":"TUR",
  "795":"TKM","800":"UGA","804":"UKR","784":"ARE","826":"GBR","840":"USA",
  "858":"URY","860":"UZB","862":"VEN","704":"VNM","887":"YEM","894":"ZMB",
  "716":"ZWE","158":"TWN",
};

interface WorldMapProps {
  countries: Country[];
  selectedIso3: string | null;
  onCountryClick: (iso3: string) => void;
  highlightedIso3s?: Set<string>;
}

export default function WorldMap({ countries, selectedIso3, onCountryClick, highlightedIso3s }: WorldMapProps) {
  const [tooltip, setTooltip] = useState<{ x: number; y: number; content: string } | null>(null);

  const dataMap = new Map(countries.map(c => [c.iso3, c]));

  const getColor = useCallback((geoId: string): string => {
    const numericId = String(geoId).padStart(3, '0');
    const iso3 = ISO_NUMERIC_TO_ALPHA3[numericId];
    if (!iso3) return '#1e293b';
    const c = dataMap.get(iso3);
    if (!c) return '#1e293b';
    if (highlightedIso3s && highlightedIso3s.size > 0 && !highlightedIso3s.has(iso3)) {
      return '#1e293b';
    }
    return getGapColor(c.gap_score);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [countries, highlightedIso3s]);

  return (
    <div className="absolute inset-0 bg-[#0a0f1e]">
      <ComposableMap
        projection="geoNaturalEarth1"
        style={{ width: '100%', height: '100%' }}
        projectionConfig={{ scale: 160 }}
      >
        <ZoomableGroup zoom={1} minZoom={1} maxZoom={8}>
          <Geographies geography={GEO_URL}>
            {({ geographies }) =>
              geographies.map((geo) => {
                const numericId = String(geo.id).padStart(3, '0');
                const iso3 = ISO_NUMERIC_TO_ALPHA3[numericId];
                const country = iso3 ? dataMap.get(iso3) : undefined;
                const isSelected = iso3 === selectedIso3;
                const fillColor = getColor(String(geo.id));

                return (
                  <Geography
                    key={geo.rsmKey}
                    geography={geo}
                    fill={fillColor}
                    stroke={isSelected ? '#ffffff' : '#0f172a'}
                    strokeWidth={isSelected ? 1.5 : 0.4}
                    style={{
                      default: { outline: 'none' },
                      hover: { outline: 'none', opacity: 0.8, cursor: country ? 'pointer' : 'default' },
                      pressed: { outline: 'none' },
                    }}
                    onMouseMove={(evt: React.MouseEvent) => {
                      if (country) {
                        setTooltip({
                          x: evt.clientX,
                          y: evt.clientY,
                          content: `${country.country} · Gap: ${country.gap_score.toFixed(1)} (${country.gap_tier})`,
                        });
                      }
                    }}
                    onMouseLeave={() => setTooltip(null)}
                    onClick={() => {
                      if (iso3 && country) onCountryClick(iso3);
                    }}
                  />
                );
              })
            }
          </Geographies>
        </ZoomableGroup>
      </ComposableMap>

      {tooltip && (
        <div
          className="fixed z-50 panel px-3 py-2 text-xs text-slate-200 pointer-events-none"
          style={{ left: tooltip.x + 12, top: tooltip.y - 36 }}
        >
          {tooltip.content}
        </div>
      )}
    </div>
  );
}