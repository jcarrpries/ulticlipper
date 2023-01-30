

import YouTube from 'react-youtube';
import React from 'react'

// Event types: CATCH, DROP, ENDOFFIRSTQUARTER, ENDOFTHIRDQUARTER,
//              GAMEOVER, GOAL, HALFTIME, PULL, PULLOB, THROWAWAY



const YoutubePlayer = (props) => {
    // load default props
    const clip = props.clip
    const setPlayer = props.setPlayer

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

    </div>

}

export default YoutubePlayer