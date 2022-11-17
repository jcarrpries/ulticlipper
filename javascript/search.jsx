import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import Select from 'react-select';


const Search = () => {
    let [clips, setClips] = useState([])
    let [tagGroups, setTagGroups] = useState([])
    let [tags, setTags] = useState([])
    let [selectedOptions, setSelectedOptions] = useState({});

    function searchRequest(e) {
        let query = ""
        e.preventDefault()

        console.time()
        // console.log("hi")
        // console.log(typeof(selectedOptions))
        // let string_options = JSON.stringify(selectedOptions)
        // console.log(string_options)
        // let selectedOptionsStatic = selectedOptions
        // let map = JSON.parse(string_options)
        // console.log(selectedOptions['opponent'])
        // console.log(selectedOptionsStatic['defender'])

        for(id in selectedOptions){
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
        // map.forEach(function (value, key) {
        //     console.log(key + " = " + value);
        //     query += key + "=" + value + "&";
        // })

        // for (option of e.target) {
        //     if (option.selectedOptions) {
        //         let id = option.id
        //         let sub_query = ""
        //         for (selectedOption of option.selectedOptions) {
        //             sub_query += selectedOption.value + ","
        //         }
        //         if (sub_query.length > 0) {
        //             sub_query = sub_query.substring(0, sub_query.length - 1)
        //             query += id + "=[" + sub_query + "]&"
        //         }
        //     }
        // }

        if (query[query.length - 1] == "&") {
            query = query.substring(0, query.length - 1)
        }

        console.log(query)

        fetch('/api/clips/?' + query).then((resp) => {
            return resp.json()
        }).then((json) => {
            setClips(json)
            console.timeEnd()

        })
    }

    var at = {
        opponent: function (data) {
            handleSelect(data, "opponent")
        },
        tournament: function (data) {
            handleSelect(data, "tournament")
        },
        players_on: function (data) {
            handleSelect(data, "players_on")
        },
        their_score: function (data) {
            handleSelect(data, "their_score")
        },
        event_type: function (data) {
            handleSelect(data, "event_type")
        },
        line_type: function (data) {
            handleSelect(data, "line_type")
        },
        our_score: function (data) {
            handleSelect(data, "our_score")
        },
        passer: function (data) {
            handleSelect(data, "passer")
        },
        reciever: function (data) {
            handleSelect(data, "reciever")
        }, 
        defender: function (data) {
            handleSelect(data, "defender")
        }, 
        hang_time: function (data) {
            handleSelect(data, "hang_time")
        }
    }
    // Function triggered on selection
    function handleSelect(data, item) {
        selectedOptions[item] = data
        console.log(selectedOptions)
        setSelectedOptions(selectedOptions);
    }

    // use useEffect to run this code once when the component loads
    useEffect(() => {
        fetch('/api/tag_groups').then((resp) => {
            return resp.json()
        }).then((json) => {
            console.log('tag groups:', json)
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
                            <div className="search-menu">
                                {tagGroups.map((group, idx) => {
                                    return (
                                        <div style={{ width: '250px' }}>
                                            {/* <div className="card-header-title">{group.name}</div> */}

                                            <Select
                                                options={group.tags.map((entry) => {
                                                    return { "value": entry.id, "label": entry.name }
                                                })}
                                                placeholder={"Select " + group.name}
                                                value={selectedOptions[group.name]}
                                                onChange={at[group.name]}
                                                isSearchable={true}
                                                isMulti
                                            />
                                        </div>


                                    )
                                })}

                            </div>
                            <div className="control">
                                <button className="button is-primary" type="submit">Search</button>
                            </div>
                        </form>


                    </div>
                    <div>


                    </div>
                </div>
            </div>
            <div className="block">
                <p>Results: {clips.length}</p>
            </div>
            {
                clips.map((clip) => {
                    return (
                        <div key={clip.id}>
                            <div className="block"></div>
                            <div className="card">
                                <div className="card-header">
                                    <div className="card-header-title">Video ID: {clip.video.title.substring(0, clip.video.title.length - 21)}</div>
                                </div>
                                <div className="card-content">
                                    <div className="block">

                                        <Link to={"/clip/" + clip.id}><img src={"//img.youtube.com/vi/" + clip.video.youtube_id + "/0.jpg"} width="200" height="100" /></Link>
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
