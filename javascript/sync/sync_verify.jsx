import React, { useState, useRef } from 'react'

import YouTube from 'react-youtube'
import fmtSeconds from '../util'

const SyncVerify = (props) => {
    const {
        setSyncStep,
        clipIdx,
        setClipIdx,
        clips,
        events,
        selectedGame,
        setCommitResult,
        youtubeId,
        url,
    } = props

    const [player, setPlayer] = useState(null)
    const clipSelectRef = useRef(null)
    const handleReady = (e) => {
        setPlayer(e.target)
    }
    const handleSelectChange = (e) => {
        setClipIdx(e.target.value)
        player.seekTo(clips[e.target.value].timestamp)
    }
    const jumpStart = () => {
        player.seekTo(clips[clipIdx].timestamp)
    }
    const jumpEnd = () => {
        player.seekTo(clips[clipIdx].timestamp + clips[clipIdx].duration)
    }
    const nextClip = () => {
        clipSelectRef.current.selectedIndex++
        handleSelectChange({target: clipSelectRef.current})
    }
    const handleSubmit = () => {
        // Modify events to fit final set of clips
        let point = 0
        let newEvents = []
        let offset = clips[point].timestamp - events[0].event_start_elapsed
        for (let i = 0; i < events.length; i++) {
            events[i].event_start_elapsed += offset
            newEvents.push(events[i])
            // if the event type is goal, increment point and set offset
            if (events[i].event_type == 'GOAL') {
                // console.log('event time:', events[i].event_start_elapsed)
                // console.log('clip time:', clips[point].timestamp + clips[point].duration)
                // only update offset if we're not on the last event
                point++
                if (point < clips.length) {
                    offset = clips[point].timestamp - events[i+1].event_start_elapsed
                }
            }
        }

        let data = new FormData()
        data.append('clips', JSON.stringify(clips))
        data.append('events', JSON.stringify(events))
        data.append('url', url)
        data.append('game_date', selectedGame.game_date)
        data.append('tournament', selectedGame.tournament)
        data.append('opponent', selectedGame.opponent)
        fetch('/api/sync/commit/', {
            'method': 'POST',
            'body': data,
        }).then((resp) => {
            return resp.json()
        }).then((json) => {
            setCommitResult(json)
            setSyncStep('done')
        })
    }
    const handleEdit = () => {
        setSyncStep('edit')
    }

    return (
        <>
            <div className="block">
                <p>Verify generated clips</p>
            </div>
            <div className="block">
                <YouTube
                    onReady={handleReady}
                    videoId={youtubeId}
                    className="youtube-container"
                    opts={{
                        playerVars: {
                            modestBranding: 1,
                            rel: 0,
                            start: clips[clipIdx].timestamp,
                            end: clips[clipIdx].timestamp + clips[clipIdx].duration
                        }
                    }}
                />
            </div>
            <div className="block">
                <div className="select">
                    <select onChange={handleSelectChange} ref={clipSelectRef} value={clipIdx}>
                        {clips.map((clip, idx) => {
                            return (
                                <option key={idx} value={idx}>Point {idx+1}</option>
                            )
                        })}
                    </select>
                </div>
            </div>
            <div className="block">
                <div className="buttons">
                    <div className="button" onClick={nextClip}>
                        Next Clip
                    </div>
                    <div className="button" onClick={jumpStart}>
                        Start: {fmtSeconds(clips[clipIdx].timestamp)}
                    </div>
                    <div className="button" onClick={jumpEnd}>
                        End: {fmtSeconds(clips[clipIdx].timestamp + clips[clipIdx].duration)}
                    </div>
                    <div className="button is-warning" onClick={handleEdit}>Edit</div>
                    <div className="button is-success" onClick={handleSubmit}>
                        Submit
                    </div>
                </div>
            </div>
        </>
    )
}

export default SyncVerify
