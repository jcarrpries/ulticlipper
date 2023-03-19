import React, { useState, useEffect, useRef } from 'react'
import { useParams } from 'react-router-dom'
import PopulationPyramid from './population-pyramid';
import Scoreboard from './scoreboard';
import Timeline from './game-timeline';
import CommentSection from './comments';

import YoutubePlayer from './youtube-player'

const StatsPanel = (props) => {
    const [events, setEvents] = useState([]);
    const [loading, setLoading] = useState(true);

    const [currentTime, setCurrentTime] = useState(props.clip ? props.clip.timestamp : -1);
    const [previousTime, setPreviousTime] = useState(props.clip ? props.clip.timestamp : -1);
    const [stats, setStats] = useState({ theirScore: 0, ourScore: 0, theirTurnovers: 0, ourTurnovers: 0, theirOChances: 0, ourOChances: 0, theirHolds: 0, ourHolds: 0, theirBreakChances: 0, ourBreakChances: 0, theirBreaks: 0, ourBreaks: 0, period: "1st" });

    useEffect(() => {
        const interval = setInterval(() => {
            setPreviousTime(currentTime);

            let theirScore = stats.theirScore;
            let ourScore = stats.ourScore;
            let theirTurnovers = stats.theirTurnovers;
            let ourTurnovers = stats.ourTurnovers;
            let theirOChances = stats.theirOChances;
            let ourOChances = stats.ourOChances;
            let ourHolds = stats.ourHolds;
            let theirHolds = stats.theirHolds;
            let theirBreakChances = stats.theirBreakChances;
            let ourBreakChances = stats.ourBreakChances;
            let ourBreaks = stats.ourBreaks;
            let theirBreaks = stats.theirBreaks;
            let period = stats.period;


            events.forEach(event => {
                if (event.timestamp > previousTime && event.timestamp <= currentTime) {
                    if (event.defense && event.event_type === 'GOAL') {
                        theirScore += 1;
                    } else if (!event.defense && event.event_type === 'GOAL') {
                        ourScore += 1;
                    }

                    if (!event.defense && (event.event_type === 'THROWAWAY' || event.event_type === 'DROP')) {
                        ourTurnovers += 1;
                    } else if (event.defense && (event.event_type === 'THROWAWAY' || event.event_type === 'D')) {
                        theirTurnovers += 1;
                    }

                    if (event.line_type === "O" && !event.defense && event.event_type === 'GOAL') {
                        ourHolds += 1;
                    } else if (event.line_type === "D" && event.defense && event.event_type === 'GOAL') {
                        theirHolds += 1;
                    }

                    // Offensive conversion rate = Number of Holds / number of times O has the opprotunity to score (Multiple times per point if there are turns)
                    if (event.line_type === "O" && !event.defense && (event.event_type === 'THROWAWAY' || event.event_type === 'DROP' || event.event_type === 'GOAL')) {
                        ourOChances += 1;
                    } else if (event.line_type === "D" && event.defense && (event.event_type === 'THROWAWAY' || event.event_type === 'D' || event.event_type === 'GOAL')) {
                        theirOChances += 1;
                    }

                    if (event.line_type === "D" && !event.defense && event.event_type === 'GOAL') {
                        ourBreaks += 1;
                    } else if (event.line_type === "O" && event.defense && event.event_type === 'GOAL') {
                        theirBreaks += 1;
                    }

                    // Break Chances = Number of Breaks / number of times D has the opprotunity to score (Multiple times per point if there are turns)
                    if (event.line_type === "D" && !event.defense && (event.event_type === 'THROWAWAY' || event.event_type === 'DROP' || event.event_type === 'GOAL')) {
                        ourBreakChances += 1;
                    } else if (event.line_type === "O" && event.defense && (event.event_type === 'THROWAWAY' || event.event_type === 'D' || event.event_type === 'GOAL')) {
                        theirBreakChances += 1;
                    }

                    if (event.event_type == "ENDOFFIRSTQUARTER") {
                        period = '2nd'
                    } else if (event.event_type == "HALFTIME") {
                        if (period == "1st") {
                            period = "2nd"
                        } else if (period == "2nd") {
                            period = "3rd"
                        }
                    } else if (event.event_type == "ENDOFTHIRDQUARTER") {
                        period = "4th"
                    }
                }
            });

            setStats({ theirScore, ourScore, theirTurnovers, ourTurnovers, theirOChances, ourOChances, theirHolds, ourHolds, theirBreakChances, ourBreakChances, theirBreaks, ourBreaks, period });
            setCurrentTime(~~props.player?.getCurrentTime());
        }, 500);
        return () => clearInterval(interval);
    }, [props.player, currentTime, previousTime]);

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
                    defense: e.possession_types.includes("Defense"),
                    event_type: e.event_types[0],
                    line_type: e.line_type,
                    passer: e.passer,
                    defender: e.defender,
                    receiver: e.receiver,
                    timestamp: e.timestamp,
                    idx,
                }));
                setEvents(processed_events)
                setLoading(false);
            })
    }, [])

    function convertSecondsToTime(seconds) {
        const h = Math.floor(seconds / 3600); // Get the number of hours
        const m = Math.floor((seconds % 3600) / 60); // Get the number of minutes
        const s = seconds % 60; // Get the number of seconds
        return `${h}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    }

    return <>
        {loading ? <p>loading...</p> :

            <>
                <Scoreboard homeScore={stats.ourScore} awayScore={stats.theirScore} time={convertSecondsToTime(currentTime)} period={stats.period} />

                <hr />
                <div>
                    <PopulationPyramid data={[
                        { label: 'Offensive Chances', theirPercent: stats.theirOChances == 0 ? 0 : stats.theirHolds / stats.theirOChances, ourPercent: stats.ourOChances == 0 ? 0 : stats.ourHolds / stats.ourOChances, theirText: `${stats.theirHolds}/${stats.theirOChances}`, ourText: `${stats.ourHolds}/${stats.ourOChances}` },
                        { label: 'Break Chances', theirPercent: stats.theirBreakChances == 0 ? 0 : stats.theirBreaks / stats.theirBreakChances, ourPercent: stats.ourBreakChances == 0 ? 0 : stats.ourBreaks / stats.theirBreakChances, theirText: `${stats.theirBreaks}/${stats.theirBreakChances}`, ourText: `${stats.ourBreaks}/${stats.theirBreakChances}` },
                        { label: 'Turnovers', theirPercent: stats.theirTurnovers, ourPercent: stats.ourTurnovers, theirText: `${stats.theirTurnovers}`, ourText: `${stats.ourTurnovers}` },
                    ]} />
                    {/* <p>Previous Time: {previousTime}</p> */}
                    <JumpTimeline player={props.player} clip={props.clip} />
                </div>
            </>}
    </>
}

const JumpTimeline = (props) => {
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
                const notableEvents = json.filter(e => e.event_types[0] == "GOAL")

                const processed_events = notableEvents.map(function (e, idx) {

                    if (e.event_types[0] == "GOAL") {
                        return { id: idx, timestamp: e.timestamp, icon: '🥏', our: e.possession_types.includes("Offense") }
                    }

                }
                );
                setEvents(processed_events)
            })
    }, [])


    const createClickHandler = timestamp => (event) => {
        props.player?.seekTo(timestamp)
    }

    return <>
        <div>
            <Timeline goals={events} player={props.player} />
        </div>
    </>
}

const View = () => {
    let { clipId } = useParams();

    const [loading, setLoading] = useState(true);
    const [clip, setClip] = useState({});
	const [tagGroups, setTagGroups] = useState([])
    const [player, setPlayer] = useState(null);

    const [viewedNote, setViewedNote] = useState('');
    const [annotating, setAnnotating] = useState(false);

    useEffect(() => {
        fetch(`/api/clips/${clipId}`).then((resp) => {
            return resp.json();
        }).then((json) => {
			setTagGroups(json["tag_groups"])
			delete json["tag_groups"]
            setClip(json);
            setLoading(false);
        })
    }, []);

    useEffect(() => {
        if (player != null) {
            console.log(player.h.width)
        }
    }, [player])

    const canvasRef = useRef(null);

    return (
        <div className="card">
            {loading ? <p>loading...</p> :
                // <div className="card-content" style={{ display: 'flex', flexDirection: 'row' }}>
                <div className="card-content">
                    <div className="columns">
                        <div className="column">
                            <div style={{ position: "relative", display: "table"}}>
                                <YoutubePlayer clip={clip} setPlayer={setPlayer}/>
                                {annotating &&
                                    <canvas ref={canvasRef} id="canv" style={{
                                        border: "3px solid red",
                                        position: "absolute",
                                        top: 0,
                                        left: 0,
                                        height: "100%",
                                        width: "100%"
                                    }}></canvas>
                                }
                                {(!annotating && viewedNote != '') &&
                                    <img onClick={() => {
                                        setViewedNote('');
                                        if (player != null) {
                                            player.playVideo();
                                        }
                                    }}
                                        style={{
                                            border: "3px solid red",
                                            position: "absolute",
                                            top: 0,
                                            left: 0,
                                            height: "100%",
                                            width: "100%"
                                        }}
                                        src={`data:image/svg+xml;utf8,${encodeURIComponent(viewedNote)}`} />
                                }
                            </div>
                            <div style={{width: player == null ? "640" : player.h.width}}>
                                <CommentSection ref={canvasRef} player={player} videoId={clip.video.id} annotating={annotating}
                                    viewedNote={viewedNote} setAnnotating={setAnnotating} setViewedNote={setViewedNote} />
                            </div>
                        </div>
                        <div className="column">
                            <StatsPanel player={player} clip={clip} />
                        </div>
                    </div>
                </div>
            }

            <h1 className='subtitle'>Clip:</h1>
			{tagGroups.map(group => {
				return (<div key={group.id} className='block'>
					<div>{group.name}</div>
					<div className='tags'>
						{group.tags.map((tag) =>
							<span key={tag.id} className='tag'>{tag.name || tag.value}</span>
						)}
					</div>
				</div>)
			})}
            <div className="block">
                <pre><code>{JSON.stringify(clip, null, 4)}</code></pre>
            </div>
        </div>
    )
}

export default View
