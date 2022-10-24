import React, { useState, useRef, useEffect } from 'react'

import YouTube from 'react-youtube'

import fmtSeconds from '../util'

const SyncHalves = (props) => {
    const {
        setSyncStep,
        youtubeId,
        clips,
        setClips,
        halftime,
    } = props

    const [player, setPlayer] = useState(null)
    const [halfSelection, setHalfSelection] = useState('first')
    const [firstHalfTime, setFirstHalfTime] = useState(0)
    const [secondHalfTime, setSecondHalfTime] = useState(halftime)
    const [curTime, setCurTime] = useState(0)

    const handleSelectionChange = () => {
        if (halfSelection == 'first') {
            setHalfSelection('second')
            player.seekTo(secondHalfTime)
        } else {
            setHalfSelection('first')
            player.seekTo(firstHalfTime)
        }
    }

    const handleReady = (e) => {
        setPlayer(e.target)
    }

    const handleContinue = () => {
        // Modify clips to account for first point and halftime selection.
        let newClips = []
        clips.forEach((clip) => {
            // Any clip before the original halftime needs to be bumped by firstHalfTime
            let newTimestamp = clip.timestamp + firstHalfTime
            // Assume any clip after the original halftime needs to be bumped
            // by (new_halftime - original_halftime)
            let secondHalfOffset = secondHalfTime - halftime
            if (clip.timestamp - secondHalfOffset > secondHalfTime) {
                newTimestamp = clip.timestamp - secondHalfOffset
            }

            clip.timestamp = newTimestamp

            newClips.push(clip)
        })
        setClips(newClips)
        setSyncStep('verify')
    }

    useEffect(() => {
        const interval = setInterval(() => {
            if (player != null) {
                cur = ~~player.getCurrentTime() // ~~ is shorthand for Math.floor, round to seconds
                setCurTime(cur)
                if (halfSelection == 'first') {
                    setFirstHalfTime(cur)
                } else {
                    setSecondHalfTime(cur)
                }
            }
        }, 100)
        return () => clearInterval(interval);
    }, [player, halfSelection])

    return (
        <>
            <div className="block">
                <p>Select when the {halfSelection} half starts:</p>
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
                        Select {halfSelection == 'first' ? 'second' : 'first'} half
                    </button>
                    <button className="button is-success" onClick={handleContinue}>Continue</button>
                </div>
            </div>
            <div className="block">
                <div className="buttons">
                    <div className="button is-outlined">First half: {fmtSeconds(firstHalfTime)}</div>
                    <div className="button is-outlined">Second half: {fmtSeconds(secondHalfTime)}</div>
                </div>
            </div>
        </>
    )
}

export default SyncHalves
