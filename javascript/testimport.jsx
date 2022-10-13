import React, { useEffect, useState, useRef } from 'react'

const TestImport = () => {
    let [results, setResults] = useState({})
    let fileInputRef = useRef(null);
    let urlInputRef = useRef(null);

    useEffect(() => {
        // get sample data and set form to sample data
        fetch('/test_data/RaleighFlyers2019-stats.csv').then((resp) => {
            return resp.text()
        }).then((text) => {
            let file = new File([text], 'testimport.csv')
            const dataTransfer = new DataTransfer()
            dataTransfer.items.add(file)
            fileInputRef.current.files = dataTransfer.files

            urlInputRef.current.value = 'https://www.youtube.com/watch?v=B_RPq7Gh_20'
        }).then(() => {
            // send request to API
            let data = new FormData()
            data.append('file', fileInputRef.current.files[0])
            data.append('url', urlInputRef.current.value)
            data.append('tournament', 'AUDL')
            data.append('opponent', 'Dallas Roughnecks')
            data.append('video_offset', 0)
            data.append('game_date', '2019-04-05')
            fetch('/api/testimport/', {
                'method': 'POST',
                'body': data,
            }).then((resp) => {
                return resp.json()
            }).then((json) => {
                setResults(json)
            })
        })
    }, [])

    return (
        <div className="card">
            <div className="card-content">
                <div className="container">
                    <div className="field">
                        <div className="control is-expanded">
                            <input ref={fileInputRef} type="file"></input>
                        </div>
                    </div>
                    <div className="field">
                        <div className="control is-expanded">
                            <input ref={urlInputRef} type="text"></input>
                        </div>
                    </div>
                </div>
            </div>
            <pre><code>{JSON.stringify(results, null, 4)}</code></pre>
        </div>
    )
}

export default TestImport
