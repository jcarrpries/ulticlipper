import React, { useState, useRef, useEffect } from 'react'

const SyncUpload = (props) => {
    let fileInputRef = useRef(null)
    let urlInputRef = useRef(null)

    const {
        setSyncStep,
        setGames,
        setCsvFile,
        setUrl,
    } = props

    const handleSubmit = (e) => {
        e.preventDefault()
        setUrl(urlInputRef.current.value)
        let file = fileInputRef.current.files[0]
        setCsvFile(file)
        let data = new FormData()
        data.append('file', file)
        fetch('/api/sync/upload/', {
            'method': 'POST',
            'body': data,
        }).then((resp) => {
            return resp.json()
        }).then((json) => {
            setGames(json)
            setSyncStep('chooseGame')
        })
    }

    // LOAD DEFAULT FORM VALUE - FOR TESTING ONLY
    useEffect(() => {
        fetch('/test_data/RaleighFlyers2019-stats.csv').then((resp) => {
            return resp.text()
        }).then((text) => {
            let file = new File([text], 'testimport.csv')
            const dataTransfer = new DataTransfer()
            dataTransfer.items.add(file)
            fileInputRef.current.files = dataTransfer.files

            urlInputRef.current.value = 'https://www.youtube.com/watch?v=B_RPq7Gh_20'
        })
    }, [])

    return (
        <form onSubmit={handleSubmit}>
            <div className="field">
                <div className="field-label">
                    <div className="label">YouTube URL</div>
                </div>
                <div className="field">
                    <p className="control is-expanded">
                        <input ref={urlInputRef} className="input" type="text"></input>
                    </p>
                </div>
                <div className="field-label">
                    <div className="label">UltiAnalytics File</div>
                </div>
                <div className="field">
                    <p className="control is-expanded">
                        <input ref={fileInputRef} className="input" type="file"></input>
                    </p>
                </div>
                <div className="field">
                    <div className="control">
                        <button className="button is-primary">Upload</button>
                    </div>
                </div>
            </div>
        </form>
    )
}

export default SyncUpload
