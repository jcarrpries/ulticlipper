import React, { useState } from 'react'

let resultStatus = false

const Upload = () => {
    const [result, setResult] = useState('')

    const handleSubmit = (e) => {
        let data = {
            "url": e.target.url.value,
            "start": e.target.start.value,
            "end": e.target.end.value
        }
        fetch("/api/clips/", {
            "method": "POST",
            "body": JSON.stringify(data),
            "headers": new Headers({"Content-Type": "application/json"})
        }).then((resp) => {
            resultStatus = resp.ok
            console.log('resp.ok:', resp.ok)
            console.log('result status:', resultStatus)
            return resp.ok ? resp.json() : resp.text()
        }).then((respData) => {
            console.log('result:', resultStatus, 'data:', respData)
            if (resultStatus) {
                setResult(`Clip uploaded with video ID ${respData.vid_id}`)
            } else {
                setResult(`Upload failed with error: ${respData}`)
            }
        })
        e.preventDefault()
    }

    let randStart = Math.floor(Math.random() * (120 - 10) + 10)
    let randEnd = randStart + 10

    return (
        <section className="section">
            <div className="card">
                <header className="card-header">
                    <div className="card-header-title">Upload Clip</div>
                </header>
                <div className="card-content">
                    <form onSubmit={handleSubmit}>
                        <div className="field is-horizontal">
                            <div className="field-label is-normal">
                                <label className="label">YouTube URL</label>
                            </div>
                            <div className="field-body">
                                <div className="field">
                                    <p className="control is-expanded">
                                        <input name="url" className="input" type="text" defaultValue="https://www.youtube.com/watch?v=dQw4w9WgXcQ"></input>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="field is-horizontal">
                            <div className="field-label is-normal">
                                <label className="label">Start/End (seconds)</label>
                            </div>
                            <div className="field-body">
                                <div className="field">
                                    <p className="control is-expanded">
                                        <input name="start" className="input" type="text" defaultValue={randStart}></input>
                                    </p>
                                </div>
                                <div className="field">
                                    <p className="control is-expanded">
                                        <input name="end" className="input" type="text" defaultValue={randEnd}></input>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="field is-horizontal">
                            <div className="field-label">
                                {/*<!-- Left empty for spacing -->*/}
                            </div>
                            <div className="field-body">
                                <div className="field">
                                    <div className="control">
                                        <button className="button is-primary">Upload</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <div className="block"></div>
            { result.length != 0 &&
                <div className={`notification is-${resultStatus ? "success" : "danger"} is-light`}>
                    {result}
                </div>
            }
        </section>
    )
}

export default Upload
