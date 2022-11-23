

import YouTube from 'react-youtube';
import React, { useState, useEffect } from 'react'

// Event types: CATCH, DROP, ENDOFFIRSTQUARTER, ENDOFTHIRDQUARTER,
//              GAMEOVER, GOAL, HALFTIME, PULL, PULLOB, THROWAWAY


const JumpButtons = (props) => {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        fetch(`/api/clips_by_video/${props.clip.video.id}`)
                .then(resp => resp.json())
                .then(json => {
                    hist = {}
                    json.forEach(e => {
                        e_type = (e.event_types).toString()
                        hist[e_type] = (hist[e_type] || 0) + 1
                    })

                    const processed_events = json.map((e, idx) => ({
                        defense: e.event_types.includes("D"),
                        event_type: e.event_types.find(e => e != "D"),
                        timestamp: e.timestamp,
                        idx,
                    }));

                    setEvents(processed_events)
                })
    }, [])

    const notableEvents = () => events.filter(e => e.event_type != "CATCH");

    // Get events representing the start of events
    const pointStartEvents = () => {
        const goal_events = events.filter(e => e.event_type == "GOAL")
        goal_events.pop() // Last goal isn't followed by new point
        const point_starts = events.length ? [events[0]] : []

        goal_events.forEach(goal_event => {
            const point_start = events[goal_event.idx + 1]
            point_starts.push(point_start)
        })

        point_starts.forEach((e, idx) => {
            e.point_start_number = idx + 1
        })

        return point_starts
    }

    // Segment list of events into quarters
    const segmentByQuarter = (event_list) => {
        q0_end = events.find(e => e.event_type == "ENDOFFIRSTQUARTER")?.timestamp
        q1_end = events.find(e => e.event_type == "HALFTIME")?.timestamp
        q2_end = events.find(e => e.event_type == "ENDOFTHIRDQUARTER")?.timestamp
        // q3_end = events.find(e => e.event_type == "GAMEOVER")?.timestamp

        quarters = [[], [], [], []]

        event_list.forEach(e => {
            t = e.timestamp
            if (q2_end && q2_end < t) {
                quarters[3].push(e)
            } else if (q1_end && q1_end < t) {
                quarters[2].push(e)
            } else if (q0_end && q0_end < t) {
                quarters[1].push(e)
            } else {
                quarters[0].push(e)
            }
        })

        return quarters
    }

    const createClickHandler = timestamp => (event) => {
        props.player?.seekTo(timestamp)
    }

    pointsByQuarter = segmentByQuarter(pointStartEvents())
    return <>
        <hr/>
        <h1>Points:</h1>
        {pointsByQuarter.map((points, quarter_idx) => <React.Fragment key={quarter_idx}>
            <h2>Quarter {quarter_idx+1}:</h2>
            <div className="field has-addons">
                {points.map(e => <button
                    key={e.timestamp.toString() + e.event_type}
                    onClick={createClickHandler(e.timestamp)}
                    className={"button"}
                    style={{color: e.defense ? "#00a" : "#a00"}}
                >
                    {e.point_start_number}
                </button>)}
            </div>
        </React.Fragment>)}


        <hr/>
        <h1>Events:</h1>
        {segmentByQuarter(notableEvents()).map((e_list, quarter_idx) => <React.Fragment key={quarter_idx}>
            <h1>Quarter {quarter_idx + 1}</h1>
            {e_list.map(e => <button
                key={e.timestamp.toString() + e.event_type}
                onClick={createClickHandler(e.timestamp)}>
                    {e.event_type + (e.defense ? " (defense)" : "")}
            </button>)}
        </React.Fragment>)}
    </>
}



const YoutubePlayer = (props) => {
    // load default props
    const clip = props.clip

    const [player, setPlayer] = useState(null);

    // youtube api handlers
    const handleReady = (event) => {
        setPlayer(event.target);
    }
    const handlePlay = (event) => {
        // console.log("handlePlay", event)
    }
    const handlePause = (event) => {
        // console.log("handlePause", event)
    }
    const handleEnd = (event) => {
        // console.log("handleEnd", event)
    }
    const handleError = (event) => {
        console.log("handleError", event)
    }
    const handleStateChange = (event) => {
        // console.log("handleStateChange", event)
    }


    return <div>
        <YouTube
            videoId={clip.video.youtube_id} // initial video id
            onReady={handleReady}
            onPlay={handlePlay}
            onPause={handlePause}
            onEnd={handleEnd}
            onError={handleError}
            onStateChange={handleStateChange}

            className="youtube-container"
            opts={{
                playerVars: {
                    // controls: 0, // hide controls
                    modestbranding: 1,
                    rel: 0, // only show related videos from same channel
                    // https://developers.google.com/youtube/player_parameters
                    start: clip.timestamp,
                },
            }}
        />

        <JumpButtons player={player} clip={clip}/>

    </div>

}

export default YoutubePlayer