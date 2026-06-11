import Link from 'next/link';

export default function Methodology() {
  return (
    <div style={{ height: '100vh', background: '#0a0f1e', color: '#e2e8f0', overflowY: 'auto', fontFamily: 'sans-serif' }}>
      <div style={{ maxWidth: '720px', margin: '0 auto', padding: '40px 32px' }}>

        <Link href="/" style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', color: '#94a3b8', textDecoration: 'none', fontSize: '13px', marginBottom: '40px' }}>
          ← Back to Atlas
        </Link>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '8px' }}>
          <div style={{ width: '36px', height: '36px', borderRadius: '10px', background: '#7f1d1d', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fca5a5" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
          </div>
          <div>
            <h1 style={{ color: '#fff', fontSize: '20px', fontWeight: 600, margin: 0 }}>ClimaGap Atlas</h1>
            <p style={{ color: '#64748b', fontSize: '12px', margin: 0 }}>Methodology &amp; Data Sources</p>
          </div>
        </div>

        <div style={{ height: '1px', background: '#1e293b', margin: '32px 0' }}/>

        {/* Gap Score */}
        <section style={{ marginBottom: '40px' }}>
          <h2 style={{ color: '#fff', fontSize: '15px', fontWeight: 500, marginBottom: '16px' }}>What is the Gap Score?</h2>
          <div style={{ background: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px', padding: '20px', fontSize: '13px', lineHeight: '1.7', color: '#cbd5e1' }}>
            <p style={{ marginBottom: '16px' }}>
              The <span style={{ color: '#fb923c', fontWeight: 500 }}>Gap Score</span> measures the difference between a country&apos;s climate vulnerability and its policy response quality.
            </p>
            <div style={{ background: '#1e293b', border: '1px solid #334155', borderRadius: '8px', padding: '12px 16px', textAlign: 'center', fontFamily: 'monospace', fontSize: '13px', color: '#e2e8f0', margin: '16px 0' }}>
              Gap Score = Risk Score − Policy Score
            </div>
            <p style={{ marginBottom: '12px' }}>
              A <span style={{ color: '#f87171', fontWeight: 500 }}>high gap score</span> means severe climate risk with weak adaptation policy — countries most urgently needing international climate finance.
            </p>
            <p>
              A <span style={{ color: '#4ade80', fontWeight: 500 }}>low or negative gap score</span> means policy ambition meets or exceeds the current risk level.
            </p>
          </div>
        </section>

        {/* Data Sources */}
        <section style={{ marginBottom: '40px' }}>
          <h2 style={{ color: '#fff', fontSize: '15px', fontWeight: 500, marginBottom: '16px' }}>Data Sources</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {[
              { name: 'ND-GAIN Country Index', org: 'University of Notre Dame', use: 'Climate vulnerability scores — measures exposure to climate-related hazards including floods, droughts, sea level rise, and food insecurity.', sdg: 'SDG 13', sdgColor: '#f87171', sdgBg: 'rgba(127,29,29,0.4)' },
              { name: 'INFORM Risk Index', org: 'EU Joint Research Centre (JRC)', use: 'Humanitarian risk index — combines hazard exposure, vulnerability, and coping capacity to produce a composite country-level risk score.', sdg: 'SDG 16', sdgColor: '#fb923c', sdgBg: 'rgba(124,45,18,0.4)' },
              { name: 'UNFCCC NDC Registry', org: 'United Nations Framework Convention on Climate Change', use: 'Nationally Determined Contributions — assessed for submission status, quality, ambition, and year of latest update.', sdg: 'SDG 17', sdgColor: '#60a5fa', sdgBg: 'rgba(30,58,138,0.4)' },
              { name: 'World Bank Climate Data', org: 'World Bank Open Data', use: 'Country income classifications and supplementary climate vulnerability indicators.', sdg: 'SDG 1', sdgColor: '#4ade80', sdgBg: 'rgba(20,83,45,0.4)' },
            ].map(src => (
              <div key={src.name} style={{ background: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px', padding: '16px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '4px' }}>
                  <p style={{ color: '#fff', fontSize: '13px', fontWeight: 500, margin: 0 }}>{src.name}</p>
                  <span style={{ fontSize: '11px', padding: '2px 10px', borderRadius: '6px', background: src.sdgBg, color: src.sdgColor, flexShrink: 0, marginLeft: '12px' }}>{src.sdg}</span>
                </div>
                <p style={{ color: '#475569', fontSize: '11px', margin: '0 0 8px' }}>{src.org}</p>
                <p style={{ color: '#94a3b8', fontSize: '12px', margin: 0, lineHeight: '1.6' }}>{src.use}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Scoring */}
        <section style={{ marginBottom: '40px' }}>
          <h2 style={{ color: '#fff', fontSize: '15px', fontWeight: 500, marginBottom: '16px' }}>Scoring Methodology</h2>
          <div style={{ background: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px', padding: '20px', display: 'flex', flexDirection: 'column', gap: '20px' }}>
            <div>
              <p style={{ color: '#fff', fontSize: '13px', fontWeight: 500, marginBottom: '6px' }}>Risk Score (0–100)</p>
              <p style={{ color: '#64748b', fontSize: '12px', marginBottom: '10px' }}>Composite of two indices, equally weighted:</p>
              <div style={{ background: '#1e293b', border: '1px solid #334155', borderRadius: '8px', padding: '10px 16px', fontFamily: 'monospace', fontSize: '12px', color: '#cbd5e1' }}>
                Risk Score = (ND-GAIN × 0.5) + (INFORM × 0.5)
              </div>
              <p style={{ color: '#475569', fontSize: '11px', marginTop: '8px' }}>Normalised to 0–100. Higher = more vulnerable.</p>
            </div>
            <div style={{ height: '1px', background: '#1e293b' }}/>
            <div>
              <p style={{ color: '#fff', fontSize: '13px', fontWeight: 500, marginBottom: '6px' }}>Policy Score (0–100)</p>
              <p style={{ color: '#64748b', fontSize: '12px', marginBottom: '10px' }}>Derived from NDC quality assessment covering:</p>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                {['NDC submission status to the UNFCCC', 'Year of most recent submission (recency weighted)', 'Ambition level based on Climate Action Tracker ratings', 'Sectoral coverage and conditional/unconditional targets'].map(item => (
                  <div key={item} style={{ display: 'flex', gap: '8px', fontSize: '12px', color: '#94a3b8' }}>
                    <span style={{ color: '#334155', flexShrink: 0 }}>—</span>{item}
                  </div>
                ))}
              </div>
            </div>
            <div style={{ height: '1px', background: '#1e293b' }}/>
            <div>
              <p style={{ color: '#fff', fontSize: '13px', fontWeight: 500, marginBottom: '12px' }}>Gap Tiers</p>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {[
                  { tier: 'Critical', range: 'Gap ≥ 50', bg: 'rgba(127,29,29,0.5)', color: '#fca5a5', border: '#7f1d1d' },
                  { tier: 'High', range: 'Gap 30–50', bg: 'rgba(153,27,27,0.3)', color: '#f87171', border: '#991b1b' },
                  { tier: 'Moderate', range: 'Gap 10–30', bg: 'rgba(154,52,18,0.3)', color: '#fdba74', border: '#9a3412' },
                  { tier: 'Low', range: 'Gap -10–10', bg: 'rgba(113,63,18,0.3)', color: '#fde68a', border: '#713f12' },
                  { tier: 'Minimal', range: 'Gap < -10', bg: 'rgba(20,83,45,0.3)', color: '#86efac', border: '#14532d' },
                ].map(t => (
                  <div key={t.tier} style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <span style={{ fontSize: '11px', padding: '4px 0', borderRadius: '8px', background: t.bg, color: t.color, border: `1px solid ${t.border}`, width: '90px', textAlign: 'center', fontWeight: 500 }}>{t.tier}</span>
                    <span style={{ color: '#64748b', fontSize: '12px' }}>{t.range}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* SDGs */}
        <section style={{ marginBottom: '40px' }}>
          <h2 style={{ color: '#fff', fontSize: '15px', fontWeight: 500, marginBottom: '16px' }}>SDGs Addressed</h2>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '12px' }}>
            {[
              { num: '13', title: 'Climate Action', desc: 'Identifying where climate adaptation is most urgently needed', color: '#f87171' },
              { num: '16', title: 'Strong Institutions', desc: 'Assessing governance quality through NDC ambition scores', color: '#60a5fa' },
              { num: '17', title: 'Partnerships', desc: 'Supporting prioritisation of international climate finance', color: '#4ade80' },
            ].map(sdg => (
              <div key={sdg.num} style={{ background: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px', padding: '16px', textAlign: 'center' }}>
                <div style={{ fontSize: '28px', fontWeight: 700, color: sdg.color, marginBottom: '6px' }}>{sdg.num}</div>
                <p style={{ color: '#e2e8f0', fontSize: '12px', fontWeight: 500, marginBottom: '8px' }}>{sdg.title}</p>
                <p style={{ color: '#64748b', fontSize: '11px', lineHeight: '1.5', margin: 0 }}>{sdg.desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Tech Stack */}
        <section style={{ marginBottom: '40px' }}>
          <h2 style={{ color: '#fff', fontSize: '15px', fontWeight: 500, marginBottom: '16px' }}>Technical Stack</h2>
          <div style={{ background: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px', padding: '20px' }}>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px' }}>
              {[
                { layer: 'Frontend', tech: 'Next.js 15, TypeScript, Tailwind CSS' },
                { layer: 'Map rendering', tech: 'React Simple Maps, TopoJSON' },
                { layer: 'Backend', tech: 'Python, FastAPI, Uvicorn' },
                { layer: 'Data pipeline', tech: 'Pandas, NumPy, requests' },
                { layer: 'Deployment', tech: 'Vercel (frontend), Render (backend)' },
                { layer: 'Data sources', tech: 'ND-GAIN, INFORM, UNFCCC, World Bank' },
              ].map(row => (
                <div key={row.layer}>
                  <p style={{ color: '#475569', fontSize: '11px', margin: '0 0 2px' }}>{row.layer}</p>
                  <p style={{ color: '#e2e8f0', fontSize: '13px', margin: 0 }}>{row.tech}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* About */}
        <section style={{ marginBottom: '40px' }}>
          <h2 style={{ color: '#fff', fontSize: '15px', fontWeight: 500, marginBottom: '16px' }}>About this project</h2>
          <div style={{ background: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px', padding: '20px', fontSize: '13px', color: '#cbd5e1', lineHeight: '1.7', display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <p style={{ margin: 0 }}>
              ClimaGap Atlas was built to make visible a problem at the heart of international climate negotiations: the countries most exposed to climate impacts are often the least equipped — in policy, finance, and institutional capacity — to respond to them.
            </p>
            <p style={{ margin: 0 }}>
              This tool is designed for researchers, policy analysts, and international development practitioners who need to quickly identify where climate adaptation support is most urgently needed.
            </p>
            <p style={{ margin: 0, color: '#475569', fontSize: '12px' }}>
              Built as a portfolio project exploring the intersection of data science, climate policy, and international development — aligned with UN SDGs 13, 16, and 17.
            </p>
          </div>
        </section>

        {/* Footer */}
        <div style={{ borderTop: '1px solid #1e293b', paddingTop: '24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <p style={{ color: '#334155', fontSize: '11px', margin: 0 }}>ClimaGap Atlas · 2025 · Open source</p>
          <Link href="/" style={{ color: '#64748b', fontSize: '12px', textDecoration: 'none' }}>← Back to map</Link>
        </div>

      </div>
    </div>
  );
}
