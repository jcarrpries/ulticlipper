import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

import YoutubePlayer from './youtube-player'

const View = () => {
    let { clipId } = useParams()

    const [loading, setLoading] = useState(true)
    const [clip, setClip] = useState({})

    useEffect(() => {
        fetch(`/api/clips/${clipId}`).then((resp) => {
            return resp.json()
        }).then((json) => {
            setClip(json)
            setLoading(false)
        })
    }, [])

    let origin = window.location.hostname

    return (
        <div className="card">
            <div className="card-content">
                {/* {loading ? <p>loading...</p>
                :
                <iframe id="ytplayer" type="text/html" width="640" height="360"
                    src={`https://www.youtube.com/embed/${clip.vid_id}?&origin=${origin}`}
                    frameBorder="0"></iframe>
                } */}
                { loading ? <p>loading...</p> :
                    <YoutubePlayer clip={clip}/>
                }
            </div>
            <div className="block">
                <pre><code>{JSON.stringify(clip, null, 4)}</code></pre>
            </div>
        </div>
    )
}

export default View
