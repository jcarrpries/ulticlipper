import React, { useState, useRef } from 'react'

import YouTube from 'react-youtube'
import fmtSeconds from '../util'

const SyncVerify = (props) => {
    const {
        setSyncStep,
        clips,
        selectedGame,
        setCommitResult,
        youtubeId,
        url,
    } = props

    const [clipIdx, setClipIdx] = useState(0)
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
    const handleContinue = () => {
        let data = new FormData()
        data.append('clips', JSON.stringify(clips))
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
                            start: clips[0].timestamp,
                            end: clips[0].timestamp + clips[0].duration
                        }
                    }}
                />
            </div>
            <div className="block">
                <div className="select">
                    <select onChange={handleSelectChange} ref={clipSelectRef}>
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
                    <div className="button is-success" onClick={handleContinue}>
                        Continue
                    </div>
                </div>
            </div>
        </>
    )
}

export default SyncVerify
