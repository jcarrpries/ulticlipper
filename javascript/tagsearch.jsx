import React, { useState, useEffect } from 'react'

const TagSearch = () => {
    let [tagGroups, setTagGroups] = useState([])
    let [tags, setTags] = useState([])

    let [clips, setClips] = useState([])

    // use useEffect to run this code once when the component loads
    useEffect(() => {
        fetch('/api/tag_groups').then((resp) => {
            return resp.json()
        }).then((json) => {
            console.log('tag groups:', json)
            setTagGroups(json)
            handleTagGroupChange({ target: { value: json[0].id } })
        })
    }, [])

    const handleTagGroupChange = (e) => {
        fetch('/api/tag_groups/' + e.target.value + '/').then((resp) => {
            return resp.json()
        }).then((json) => {
            setTags(json.tags)
            handleTagChange({ target: { value: json.tags[0].id } })
        })
    }

    const handleTagChange = (e) => {
        fetch('/api/tags/' + e.target.value + '/').then((resp) => {
            return resp.json()
        }).then((json) => {
            setClips(json.clips)
        })
    }

    return (
        <section className="section">
            <div className="card">
                <header className="card-header">
                    <div className="card-header-title">Search clips by tag</div>
                </header>
            </div>
            <div className="card-content">
                <div className="block">
                    <div className="select">
                        <select onChange={handleTagGroupChange}>
                            {tagGroups.map((group, idx) => {
                                return (
                                    <option key={idx} value={group.id}>{group.name}</option>
                                )
                            })}
                        </select>
                    </div>
                </div>
                <div className="block">
                    <div className="select">
                        <select onChange={handleTagChange}>
                            {tags.map((tag, idx) => {
                                return (
                                    <option key={idx} value={tag.id}>{tag.name}</option>
                                )
                            })}
                        </select>
                    </div>
                </div>
                <div className="block">
                    <p>First 10 clips for given tag</p>
                    <pre><code>
                        {JSON.stringify(clips.slice(0, 10), null, 4)}
                    </code></pre>
                </div>
            </div>
        </section>
    )
}

export default TagSearch
