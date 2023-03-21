import React, { useState, useEffect } from 'react'
import Select from 'react-select';
import { getCsrfToken } from './auth/auth_manager';
import RangeInput from './common/rangeinput';
import { useNavigate, Link } from 'react-router-dom';

const Search = () => {
	const navigate = useNavigate()
    let [clips, setClips] = useState([])
	const [clipIds, setClipIds] = useState([])
    let [tagGroups, setTagGroups] = useState([])
    let [tags, setTags] = useState([])
    let [selectedOptions, setSelectedOptions] = useState({});
	let [selectedRanges, setSelectedRanges] = useState({});
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

		for ([group, range] of Object.entries(selectedRanges)) {
			query += `${group}[min]=${range.min}&${group}[max]=${range.max}&`
		}

        if (query[query.length - 1] == "&") {
            query = query.substring(0, query.length - 1)
        }

        setClips([])
        setGotResults(false)
        setSearchLoading(true)
        fetch('/api/clips/?' + query).then((resp) => {
            return resp.json()
        }).then((json) => {
            setClips(json)
			const ids = json.map(clip => clip.id)
			setClipIds(ids)
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
        setSelectedOptions({...selectedOptions, [item]: data});
    }

	const handleRangeChange = (name, data) => {
		setSelectedRanges({...selectedRanges, [name]: data})
	}
	
	const handleClipSelect = (clipId, clipIdx) => {
		navigate(`/clip/${clipId}`, {state: {curClipIdx: clipIdx, clipIds}})
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
									if (group.type == 'numeric') {
										return <RangeInput key={idx} name={group.name} handleChange={handleRangeChange}/>
									}
                                    return (
                                        <div style={{ width: '550px'}} key={idx}>
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
                                        <img onClick={() => handleClipSelect(clip.id, idx)} src={"//img.youtube.com/vi/" + clip.video.youtube_id + "/0.jpg"} width="200" height="100" />
										<button className="button is-light is-pulled-right mr-1" id="delete-button" onClick={() => deleteClip(clip.id, idx)}>Delete</button>
                                    </div>
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
