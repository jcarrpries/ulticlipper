import React, { useState, useRef, useEffect } from 'react'

import YouTube from 'react-youtube'

import fmtSeconds from '../util'

const SyncEdit = (props) => {
    const {
        setSyncStep,
        clipIdx,
        clips,
        setClips,
        youtubeId,
    } = props

    const [player, setPlayer] = useState(null)
    const [selection, setSelection] = useState('start')
    const [start, setStart] = useState(clips[clipIdx].timestamp)
    const [end, setEnd] = useState(clips[clipIdx].timestamp + clips[clipIdx].duration)
    const [curTime, setCurTime] = useState(clips[clipIdx].timestamp)
    const handleReady = (e) => {
        setPlayer(e.target)
    }

    const handleSelectionChange = () => {
        if (selection == 'start') {
            setSelection('end')
            player.seekTo(end)
        } else {
            setSelection('start')
            player.seekTo(start)
        }
    }

    const handleReset = () => {
        player.seekTo(clips[clipIdx].timestamp)
        setStart(clips[clipIdx].timestamp)
        setEnd(clips[clipIdx].timestamp + clips[clipIdx].duration)
    }

    const handleContinue = () => {
        // Modify just the clip at clipIdx
        newClips = []
        clips.forEach((clip, idx) => {
            if (idx == clipIdx) {
                clip.timestamp = start
                clip.duration = end - start
            }
            newClips.push(clip)
        })
        setClips(newClips)
        setSyncStep('verify')
    }

    useEffect(() => {
        const interval = setInterval(() => {
            if (player != null) {
                cur = ~~player.getCurrentTime()
                setCurTime(cur)
                if (selection == 'start') {
                    setStart(cur)
                } else {
                    setEnd(cur)
                }
            }
        }, 100)
        return () => clearInterval(interval)
    }, [player, selection])

    return (
        <>
            <div className="block">
                <p>Edit {selection} of clip {parseInt(clipIdx)+1}</p>
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
                            start: 0,
                        }
                    }}
                />
            </div>
            <div className="block">
                <div className="buttons">
                    <div className="button is-outlined">Current time: {fmtSeconds(curTime)}</div>
                    <button className="button is-primary" onClick={handleSelectionChange}>
                        Select {selection == 'start' ? 'end' : 'start'} of clip
                    </button>
                    <button className="button is-danger" onClick={handleReset} id="reset-button">
                        Reset
                    </button>
                    <button className="button is-success" onClick={handleContinue} id="continue-button">Continue</button>
                </div>
            </div>
            <div className="block">
                <div className="buttons">
                    <div className="button is-outlined">Start: {fmtSeconds(start)}</div>
                    <div className="button is-outlined">End: {fmtSeconds(end)}</div>
                </div>
            </div>
        </>
    )
}

export default SyncEdit
