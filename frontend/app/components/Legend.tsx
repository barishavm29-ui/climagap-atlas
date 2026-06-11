export default function Legend() {
  const items = [
    { color: '#991b1b', label: 'Critical gap (50+)' },
    { color: '#dc2626', label: 'High gap (30–50)' },
    { color: '#f97316', label: 'Moderate gap (10–30)' },
    { color: '#eab308', label: 'Low gap (-10–10)' },
    { color: '#22c55e', label: 'Minimal / surplus' },
    { color: '#334155', label: 'No data' },
  ];

  return (
    <div className="absolute bottom-6 left-6 z-20 panel px-5 py-4">
      <p className="text-slate-400 text-xs font-medium mb-2 uppercase tracking-wider">Gap Score</p>
      <div className="flex flex-col gap-2">
        {items.map(item => (
          <div key={item.label} className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-sm flex-shrink-0" style={{ background: item.color }}/>
            <span className="text-slate-300 text-xs">{item.label}</span>
          </div>
        ))}
      </div>
      <div className="mt-3 pt-3 border-t border-slate-700">
        <p className="text-slate-500 text-xs leading-relaxed">
          Gap = Climate risk − Policy response.<br/>
          Higher = more urgent action needed.
        </p>
      </div>
    </div>
  );
}
