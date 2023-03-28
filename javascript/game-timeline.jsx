import React from 'react';

const Timeline = ({ goals, player }) => {

    // Sort goals by timestamp
    const sortedGoals = goals;

    // Calculate the total duration of the game
    const gameDuration = goals.reduce((max, current) => {
        return current.timestamp > max ? current.timestamp : max;
    }, 0);;

    // Calculate the percentage of the game's duration for each goal
    const goalPositions = sortedGoals.map(goal => ({
        ...goal,
        position: `${(goal.timestamp / gameDuration) * 100}%`
    }));

    const createClickHandler = timestamp => (event) => {
        player?.seekTo(timestamp-3)
    }

    return (
        <>
            <span style={{ color: 'red', fontSize: '24px', fontWeight: 'bold', marginBottom: '100px' }}>Home</span>
            <div style={{ marginRight: '20px', marginLeft: '80px' , marginTop: '10px'  }}>
                <div style={{ height: '1px', width: '100%', backgroundColor: 'black' }}></div>
                <div style={{ display: 'flex', alignItems: 'center', position: 'relative' }}>
                    {goalPositions.map(goal => (
                        <div key={goal.id} style={{ position: 'absolute', left: goal.position, top: goal.our ? '-35px' : '7px' }}>
                            <span style={{ fontSize: '15px', cursor: 'pointer' }} onClick={createClickHandler(goal.timestamp)}>
                                {goal.icon}
                            </span>
                        </div>
                    ))}
                </div>
            </div>
            <span style={{ color: 'blue', fontSize: '24px', fontWeight: 'bold' }}>Away</span>
        </>
    );

};

export default Timeline;
