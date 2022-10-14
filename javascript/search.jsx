import React, { useState } from 'react'
import { Link } from 'react-router-dom'

const Search = () => {
    let [results, setResults] = useState([])

    const searchRequest = (e) => {
        fetch('/api/clips').then((resp) => {
            return resp.json()
        }).then((json) => {
            setResults(json)
        })
        e.preventDefault()
    }

    return (
        <section className="section">
            <div className="card">
                <header className="card-header">
                    <div className="card-header-title">Search for clips</div>
                </header>
                <div className="card-content">
                    <div className="container">
                        <form onSubmit={searchRequest}>
                            <div className="field has-addons">
                                <div className="control is-expanded">
                                    <input type="text" className="input"></input>
                                </div>
                                <div className="control">
                                    <button className="button is-primary" type="submit">Go</button>
                                </div>
                            </div>
                        </form>
                    </div>
                    { results.length > 0 &&
                        <div className="block">
                            <p>Results: {results.length}</p>
                        </div>
                    }
                </div>
            </div>
            {
                results.map((clip) => {
                    return (
                        <div key={clip.id}>
                            <div className="block"></div>
                            <div className="card">
                                <div className="card-header">
                                    <div className="card-header-title">Video ID: {clip.video.youtube_id}</div>
                                </div>
                                <div className="card-content">
                                    <div className="block">
                                        <Link to={"/clip/"+clip.id} className="button">Link to view</Link>
                                    </div>
                                    <pre><code>{JSON.stringify(clip, null, 2)}</code></pre>
                                </div>
                            </div>
                        </div>
                    )
                })
            }
        </section>
    )
}

export default Search
