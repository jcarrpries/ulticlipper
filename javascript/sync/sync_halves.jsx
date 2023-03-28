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

            player.seekTo(halftime+firstHalfTime-clips[0].duration)
            setSecondHalfTime(halftime+firstHalfTime-clips[0].duration)

        } else {
            setHalfSelection('first')
            player.seekTo(firstHalfTime)
        }
    }

    const handleReady = (e) => {
        setPlayer(e.target)
    }

    const handleContinue = () => {
        let secondHalfIdx = 0;
        // Modify clips to account for first point and halftime selection.
        for (let i = 0; i < clips.length; i++) {
            const clip = clips[i];
            
            if (clip.timestamp > halftime+2) {
                secondHalfIdx = i;
                break;
            }
        }
        let secondHalfOffset = (secondHalfTime - clips[secondHalfIdx].duration) - clips[secondHalfIdx].timestamp


        let newClips = []
        clips.forEach((clip) => {
            // Any clip before the original halftime needs to be bumped by firstHalfTime
            let newTimestamp = clip.timestamp + firstHalfTime - clips[0].duration

            // Assume any clip after the original halftime needs to be bumped
            // by (new_halftime - original_halftime)
            if (clip.timestamp > halftime) {
                newTimestamp = clip.timestamp + secondHalfOffset

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
                <p>Select when the first GOAL of the {halfSelection} half is caught:</p>
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
                            start: clips[0].timestamp + clips[0].duration
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
                    <button className="button is-success" onClick={handleContinue} id="continue-button">Continue</button>
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
