import React from 'react';

function Scoreboard({ homeScore, awayScore, time, period }) {
  const scoreboardStyle = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#292929',
    color: '#fff',
    padding: '20px',
    borderRadius: '10px',
    boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.2)',
  };

  const teamStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  };

  const homeStyle = {
    marginRight: '10px',
    borderRight: '5px solid #fff',
    paddingRight: '10px',
  };

  const timeStyle = {
    marginRight: '10px',
    paddingRight: '10px',
    paddingLeft: '10px',

  };

  const scoreStyle = {
    fontSize: '50px',
    fontWeight: 'bold',
    marginBottom: '10px',
    textShadow: '2px 2px 3px rgba(0, 0, 0, 0.3)',
    
  };

  const scoreStyleHome = {
    color: 'red'
  };

  const scoreStyleAway = {
    color: 'blue'
  };
  
  const nameStyle = {
    fontSize: '24px',
    textTransform: 'uppercase',
    letterSpacing: '2px',
    marginTop: '10px',
    textShadow: '2px 2px 3px rgba(0, 0, 0, 0.3)',
  };

  const awayStyle = {
    borderLeft: '5px solid #fff',
    paddingLeft: '10px',
  };

  return (
    <div style={scoreboardStyle}>
      <div style={{ ...teamStyle, ...homeStyle }}>
        <div style={{ ...scoreStyle, ...scoreStyleHome }}>{homeScore}</div>
        <div style={nameStyle}>Home Team</div>
      </div>
      <div style={{ ...teamStyle, ...timeStyle }}>
        <div style={scoreStyle}>{time}</div>
        <div style={nameStyle}>{period}</div>
      </div>
      <div style={{ ...teamStyle, ...awayStyle }}>
        <div style={{ ...scoreStyle, ...scoreStyleAway }}>{awayScore}</div>
        <div style={nameStyle}>Away Team</div>
      </div>
    </div>
  );
}

export default Scoreboard;
