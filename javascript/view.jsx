import React, { useState, useEffect, useRef } from 'react'
import { useParams, useLocation, useNavigate } from 'react-router-dom'
import PopulationPyramid from './population-pyramid';
import Scoreboard from './scoreboard';
import Timeline from './game-timeline';
import CommentSection from './comments';

import YoutubePlayer from './youtube-player';
import ProgressBar from './common/progressBar';

const loadingStyle = {
    fontSize: '24px',
    fontWeight: 'bold',
    color: '#4a4a4a',
    textAlign: 'center',
    padding: '20px',
}

const StatsPanel = (props) => {

    events = props.events
    const [currentTime, setCurrentTime] = useState(props.clip ? props.clip.timestamp : -1);
    const [nextPoint, setNextPoint] = useState(0);
    const [previousTime, setPreviousTime] = useState(props.clip ? props.clip.timestamp : -1);
    const [stats, setStats] = useState({ theirScore: 0, ourScore: 0, theirTurnovers: 0, ourTurnovers: 0, theirOChances: 0, ourOChances: 0, theirHolds: 0, ourHolds: 0, theirBreakChances: 0, ourBreakChances: 0, theirBreaks: 0, ourBreaks: 0, period: "1st" });

    useEffect(() => {
        const interval = setInterval(() => {

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
            let prevTime = previousTime

            if (~~props.player?.getCurrentTime() < currentTime) {
                prevTime = 0;
                theirScore = 0
                ourScore = 0
                theirTurnovers = 0;
                ourTurnovers = 0
                theirOChances = 0
                ourOChances = 0
                ourHolds = 0
                theirHolds = 0
                theirBreakChances = 0
                ourBreakChances = 0
                ourBreaks = 0
                theirBreaks = 0
                period = "1st"
            } else {
                prevTime = currentTime;
            }

            setPreviousTime(prevTime)

            let currTime = ~~props.player?.getCurrentTime()
            setCurrentTime(currTime);

            events.forEach((event, index) => {
                if (event.timestamp > prevTime && event.timestamp <= currTime) {
                    if (event.defense && event.event_type === 'GOAL') {
                        theirScore += 1;
                    } else if (!event.defense && event.event_type === 'GOAL') {
                        ourScore += 1;
                    }

                    if (event.event_type === 'GOAL') {
                        console.log("1")
                        const nextEvent = events[index + 1];
                        console.log("2")
                        
                        console.log(nextEvent.timestamp)
                        if (nextEvent) {
                            console.log("3")
                            console.log(nextEvent.timestamp)
                            setNextPoint(nextEvent.timestamp);
                        }
                    } else if ((nextPoint != 0 && event.event_type !== 'GOAL') || nextPoint > currTime) {
                        setNextPoint(0)
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
        }, 500);
        return () => clearInterval(interval);
    }, [props.player, currentTime, previousTime, stats]);

    function convertSecondsToTime(seconds) {
        const h = Math.floor(seconds / 3600); // Get the number of hours
        const m = Math.floor((seconds % 3600) / 60); // Get the number of minutes
        const s = seconds % 60; // Get the number of seconds
        return `${h}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    }

    return (<>
        <Scoreboard homeScore={stats.ourScore} awayScore={stats.theirScore} time={convertSecondsToTime(currentTime)} period={stats.period} nextPoint={nextPoint} player={props.player} setNextPoint={setNextPoint} />

        <hr />
        <div>
            <PopulationPyramid data={[
                { label: 'Offensive Chances', theirPercent: stats.theirOChances == 0 ? 0 : stats.theirHolds / stats.theirOChances, ourPercent: stats.ourOChances == 0 ? 0 : stats.ourHolds / stats.ourOChances, theirText: `${stats.theirHolds}/${stats.theirOChances}`, ourText: `${stats.ourHolds}/${stats.ourOChances}` },
                { label: 'Break Chances', theirPercent: stats.theirBreakChances == 0 ? 0 : stats.theirBreaks / stats.theirBreakChances, ourPercent: stats.ourBreakChances == 0 ? 0 : stats.ourBreaks / stats.theirBreakChances, theirText: `${stats.theirBreaks}/${stats.theirBreakChances}`, ourText: `${stats.ourBreaks}/${stats.theirBreakChances}` },
                { label: 'Turnovers', theirPercent: stats.theirTurnovers, ourPercent: stats.ourTurnovers, theirText: `${stats.theirTurnovers}`, ourText: `${stats.ourTurnovers}` },
            ]} />
            {/* <p>Previous Time: {previousTime}</p> */}
            <JumpTimeline player={props.player} clip={props.clip} events={events} />
        </div>
    </>)
}

const JumpTimeline = (props) => {

    const notableEvents = props.events.filter(e => e.event_type == "GOAL")

    const processed_events = notableEvents.map(function (e, idx) {

        if (e.event_type == "GOAL") {
            return { id: idx, timestamp: e.timestamp, icon: '🥏', our: !e.defense }
        }

    }
    );

    return <>
        <div>
            <Timeline goals={processed_events} player={props.player} />
        </div>
    </>
}

const View = () => {
    const location = useLocation()
    const { curClipIdx, clipIds } = location.state
    let { clipId: clipIdParam } = useParams();
    const navigate = useNavigate()

    const [loading, setLoading] = useState(true);
    const [clip, setClip] = useState({});
    const [clipId, setClipId] = useState({});
    const [tagGroups, setTagGroups] = useState([])
    const [player, setPlayer] = useState(null);
    const [events, setEvents] = useState([]);


    const [viewedNote, setViewedNote] = useState('');
    const [annotating, setAnnotating] = useState(false);


    const handleChangeClip = (diff) => {
        const id = clipIds[curClipIdx + diff]
        navigate(`/clip/${id}`, { state: { curClipIdx: curClipIdx + diff, clipIds } })
    }

    useEffect(() => {
        setLoading(true)
        fetch(`/api/clips/${clipId}`).then((resp) => {
            return resp.json();
        }).then((json) => {
            setTagGroups(json["tag_groups"])
            delete json["tag_groups"]
            setClip(json);
            return json
        }).then((c) => {

            fetch(`/api/clips_by_video/${c.video.id}`)
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
        })
    }, [clipId]);

    useEffect(() => {
        if (clipId !== clipIdParam) {
            setClipId(clipIdParam)
        }
    }, [clipId, clipIdParam])

    const canvasRef = useRef(null);

    return (
        <div className="card">
            {loading ? <p style={loadingStyle}>Loading...</p> :
                <div>
                    {curClipIdx != undefined &&
                        <div className="level m-3">
                            <div className='level-left'>
                                {curClipIdx > 0 &&
                                    <div className='level-item'>
                                        <button onClick={() => handleChangeClip(-1)} className='button is-primary is-medium'>Previous Clip</button>
                                    </div>
                                }
                            </div>
                            <ProgressBar player={player} duration={clip.duration} startTime={clip.timestamp} />
                            <div className='level-right'>
                                {curClipIdx < clipIds.length - 1 &&
                                    <div className='level-item'>
                                        <button onClick={() => handleChangeClip(1)} className='button is-primary is-medium'>Next Clip</button>
                                    </div>
                                }
                            </div>
                        </div>
                    }
                    <div className="card-content">
                        <div className="columns">
                            <div className="column">
                                <div style={{ position: "relative", display: "table" }}>
                                    <YoutubePlayer clip={clip} setPlayer={setPlayer} />
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
                                <div style={{ width: player?.h?.width == null ? "640" : player.h.width }}>
                                    <CommentSection ref={canvasRef} player={player} videoId={clip.video.id} annotating={annotating}
                                        viewedNote={viewedNote} setAnnotating={setAnnotating} setViewedNote={setViewedNote} />
                                </div>
                            </div>
                            <div className="column">
                                <StatsPanel player={player} clip={clip} events={events} />
                            </div>
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
