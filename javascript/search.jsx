import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'


const Search = () => {
    let [clips, setClips] = useState([])
    let [tagGroups, setTagGroups] = useState([])
    let [tags, setTags] = useState([])
    let [gotResults, setGotResults] = useState(false)
    let [searchLoading, setSearchLoading] = useState(false)

    const searchRequest = (e) => {
        let query = ""

        for (option of e.target) {
            if (option.selectedOptions) {
                let id = option.id
                let sub_query = ""
                for (selectedOption of option.selectedOptions) {
                    sub_query += selectedOption.value + ","
                }
                if (sub_query.length > 0) {
                    sub_query = sub_query.substring(0, sub_query.length - 1)
                    query += id + "=[" + sub_query + "]&"
                }
            }
        }

        if (query[query.length - 1] == "&") {
            query = query.substring(0, query.length - 1)
        }

        // console.log('/api/clips/?' + query)

        setClips([])
        setGotResults(false)
        setSearchLoading(true)
        fetch('/api/clips/?' + query).then((resp) => {
            return resp.json()
        }).then((json) => {
            setClips(json)
            setGotResults(true)
            setSearchLoading(false)
        })
        e.preventDefault()
    }

    // use useEffect to run this code once when the component loads
    useEffect(() => {
        fetch('/api/tag_groups').then((resp) => {
            return resp.json()
        }).then((json) => {
            // console.log('tag groups:', json)
            setTagGroups(json)
        })
    }, [])

    return (
        <section className="section">
            <div className="card">
                <header className="card-header">
                    <div className="card-header-title">Search for clips</div>
                </header>
                <div className="card-content">
                    <div className="container">
                        <form onSubmit={searchRequest}>
                            {tagGroups.map((group, idx) => {
                                return (
                                    <span>
                                        <label for={group.name}>{group.name}</label>
                                        <select id={group.name} name={group.name} multiple>
                                            {group.tags.map((tag, idx) => {
                                                return (
                                                    <option key={'tag-' + idx} value={tag.id}>{tag.name}</option>
                                                )
                                            })}
                                        </select>
                                    </span>
                                )
                            })}
                            <div className="control">
                                <button className="button is-primary" type="submit" id="search-button">Search</button>
                            </div>
                        </form>
                    </div>
                    <div>


                    </div>
                </div>
            </div>
            {searchLoading &&
                <div className="block">
                    <p id="search-loading">Loading results...</p>
                </div>
            }
            {gotResults &&
                <div className="block">
                    <p id="results-count">Results: {clips.length}</p>
                </div>
            }
            {
                clips.map((clip) => {
                    return (
                        <div key={'clip-' + clip.id}>
                            <div className="block"></div>
                            <div className="card">
                                <div className="card-header">
                                    <div className="card-header-title">Video ID: {clip.video.youtube_id}</div>
                                </div>
                                <div className="card-content">
                                    <div className="block">
                                        <Link to={"/clip/" + clip.id} className="button" id={'clip-'+clip.id+'-view-button'}>Link to view</Link>
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
