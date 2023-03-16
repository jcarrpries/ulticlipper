import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import Select from 'react-select';
import { getCsrfToken } from './auth/auth_manager';


const Search = () => {
    let [clips, setClips] = useState([])
    let [tagGroups, setTagGroups] = useState([])
    let [tags, setTags] = useState([])
    let [selectedOptions, setSelectedOptions] = useState({});
    let [gotResults, setGotResults] = useState(false)
    let [searchLoading, setSearchLoading] = useState(false)

    function searchRequest(e) {
        let query = ""
        e.preventDefault()

        console.time()

        for (id in selectedOptions) {
            if (selectedOptions[id]) {
                let sub_query = ""
                for (selectedOption of selectedOptions[id]) {
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
            console.timeEnd()
            setGotResults(true)
            setSearchLoading(false)
        })
    }

	const deleteClip = (clipId, clipIdx) => {
		fetch(`/api/clips/${clipId}`, {
			method: "DELETE",
			headers: {
				"Content-Type": "application/json",
				'X-CSRFToken': getCsrfToken(),
			},
		}).then(() => {
			const clipsCopy = [...clips]
			clipsCopy.splice(clipIdx, 1)
			setClips(clipsCopy)
		})
	}


    // Function triggered on selection
    function handleSelect(data, item) {
        selectedOptions[item] = data
        setSelectedOptions(selectedOptions);
    }

    // use useEffect to run this code once when the component loads
    useEffect(() => {
        fetch('/api/tag_groups').then((resp) => {
            return resp.json()
        }).then((json) => {
            setTagGroups(json)
        })
    }, [])

    return (
        <section className="section">
			<Link to='/clip/create'><button className='button is-primary'>Create Clip</button></Link>
            <div className="card">
                <header className="card-header">
                    <div className="card-header-title">Search for clips</div>
                </header>
                <div className="card-content">
                    <div className="container">
                        <form onSubmit={searchRequest}>
                            <div className="search-menu">
                                {tagGroups.map((group, idx) => {
                                    return (
                                        <div style={{ width: '550px'}}>
                                            {/* <div className="card-header-title">{group.name}</div> */}

                                            <Select
                                                options={group.tags.map((entry) => {
                                                    return { "value": entry.id, "label": entry.name }
                                                })}
                                                placeholder={"Select " + group.name}
                                                value={selectedOptions[group.name]}
                                                onChange={function (data) {
                                                    handleSelect(data, group.name)
                                                }}
                                                isSearchable={true}
                                                isMulti
                                                classNamePrefix="search-menu"
                                            />
                                        </div>


                                    )
                                })}

                            </div>
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
                clips.map((clip, idx) => {
                    return (
                        <div key={'clip-' + clip.id}>
                            <div className="block"></div>
                            <div className="card">
                                <div className="card-header">
                                    <div className="card-header-title">{clip.video.title.substring(0, clip.video.title.length - 21)}</div>
                                </div>
                                <div className="card-content">
                                    <div className="block">
                                        <Link to={"/clip/" + clip.id}><img src={"//img.youtube.com/vi/" + clip.video.youtube_id + "/0.jpg"} width="200" height="100" /></Link>
										<button className="button is-light is-pulled-right mr-1" id="delete-button" onClick={() => deleteClip(clip.id, idx)}>Delete</button>
                                    </div>
                                    {/* <pre><code>{JSON.stringify(clip, null, 2)}</code></pre> */}
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
