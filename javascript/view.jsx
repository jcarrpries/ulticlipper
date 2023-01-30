import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

import YoutubePlayer from './youtube-player'

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

const View = () => {
    let { clipId } = useParams();

    const [loading, setLoading] = useState(true);
    const [clip, setClip] = useState({});

    const [player, setPlayer] = useState(null);

    useEffect(() => {
        fetch(`/api/clips/${clipId}`).then((resp) => {
            return resp.json();
        }).then((json) => {
            setClip(json);
            setLoading(false);
        })
    }, []);

    return (
        <div className="card">
            <div className="card-content">
                { loading ? <p>loading...</p> :
                    <>
                        <YoutubePlayer clip={clip} setPlayer={setPlayer}/>
                        <JumpButtons player={player} clip={clip}/>
                    </>
                }
            </div>

            <h1>Clip:</h1>
            <div className="block">
                <pre><code>{JSON.stringify(clip, null, 4)}</code></pre>
            </div>
        </div>
    )
}

export default View
