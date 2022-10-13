

import YouTube from 'react-youtube';
import React, { useState, useEffect } from 'react'

const YoutubePlayer = (props) => {
    const [player, setPlayer] = useState(null);
    const [timestampInput, setTimestampInput] = useState(null);
    const [vidIdInput, setVidIdInput] = useState("");

    // Controller handlers
    const handleTimestampInput = (event) => {
        setTimestampInput(event.target.value);
    }
    const handleVidIdInput = (event) => {
        setVidIdInput(event.target.value);
    }
    const handlePlayButton = (event) => {
        player?.playVideo();
    }
    const handlePauseButton = (event) => {
        player?.pauseVideo();
    }

    const handleJumpButton = (event) => {
        player?.seekTo(timestampInput);
    }
    const handleSpeedButton = (speed) => {
        player?.setPlaybackRate(speed);
    }
    const handleChangeVidButton = (speed) => {
        player?.loadVideoById(vidIdInput);
    }

    // youtube api handlers
    const handleReady = (event) => {
        console.log("handleReady", event);

        setPlayer(event.target);

        // For temp debugging (remove):
        window.p = event.target;
    }
    const handlePlay = (event) => {
        console.log("handlePlay", event)
    }
    const handlePause = (event) => {
        console.log("handlePause", event)
    }
    const handleEnd = (event) => {
        console.log("handleEnd", event)
    }
    const handleError = (event) => {
        console.log("handleError", event)
    }
    const handleStateChange = (event) => {
        console.log("handleStateChange", event)
    }


    return <div>
        <YouTube
            videoId={"dQw4w9WgXcQ"} // initial video id
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
                }

            }}
        />


        {/* Play/Pause: */}
        <div className="field has-addons">
            <button className="button" onClick={handlePlayButton}>Play</button>
            <button className="button" onClick={handlePauseButton}>Pause</button>
        </div>

        {/* Jump to timestamp: */}
        <div className="field has-addons">
            <div className="control">
                <input className="input" onChange={handleTimestampInput} placeholder="Seconds"></input>
            </div>
            <div className="control">
                <button className="button" onClick={handleJumpButton}>Jump</button>
            </div>
        </div>

        {/* Set Speed: */}
        <div className="field has-addons">
            <h3>Speed:</h3>
            <div className="control">
                {player?.getAvailablePlaybackRates().map(speed => (
                    <button className="button" key={speed} onClick={() => handleSpeedButton(speed)}>{`${speed}x`}</button>
                ))}
            </div>
        </div>

        {/* Change Video: */}
        <div className="field has-addons">
            <div className="control">
                <input className="input" onChange={handleVidIdInput} placeholder="Video Id"></input>
            </div>
            <div className="control">
                <button className="button" onClick={handleChangeVidButton}>Play New Video By Id</button>
            </div>
        </div>

        <p>Documentation for youtube API: <a href="https://developers.google.com/youtube/iframe_api_reference">https://developers.google.com/youtube/iframe_api_reference</a></p>
        <p>Documentation for embed configuration:  <a href="https://developers.google.com/youtube/player_parameters">https://developers.google.com/youtube/player_parameters</a></p>
    </div>

}

export default YoutubePlayer