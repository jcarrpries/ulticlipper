import React from 'react';

const PopulationPyramid = ({ data }) => {
  const maxYValue = Math.max(...data.map((item) => item.our + item.their));

  return (
    <svg viewBox="0 0 600 170" >
      {data.map((item, index) => {
        const total = item.ourPercent + item.theirPercent > 0 ? item.ourPercent + item.theirPercent : 1;
        const ourPercent = (item.ourPercent / total) * 100 ?? 0;
        const theirPercent = (item.theirPercent / total) * 100 ?? 0;

        const x1 = 300 - (ourPercent * 2);
        const x2 = 300 + (theirPercent * 2);
        const y = index * 55 +10;

        return (
          <React.Fragment key={item.age}>
            <rect x={x1} y={y+10} width={ourPercent * 2} height={20} fill="red" fillOpacity={0.8}/>
            <rect x={x2 - theirPercent * 2} y={y+10} width={theirPercent * 2} height={20} fill="blue" fillOpacity={0.8} />
            <line x1="300" y1={y+7} x2="300" y2={y+33} stroke="#aaa" />

            <text x={x1 - 10} y={y + 22} textAnchor="end" dominantBaseline="middle">
              {item.ourText}
            </text>
            <text x={x2 + 10} y={y + 22} textAnchor="start" dominantBaseline="middle">
              {item.theirText}
            </text>
            <text x={300} y={y} textAnchor="middle" dominantBaseline="middle">
              {item.label}
            </text>
          </React.Fragment>
        );
      })}
    </svg>
  );
};

export default PopulationPyramid;