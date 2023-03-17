import React, { useState, useEffect } from 'react'
import YouTube from 'react-youtube'
import fmtSeconds from './util'
import { getCsrfToken } from './auth/auth_manager';
import Notificaton from './common/notification';
import CreatableSelect from 'react-select/creatable';
import { useNavigate } from "react-router-dom";


const ClipCreate = () => {
	const navigate = useNavigate()
	const [videos, setVideos] = useState([])
	const [selectedVideoIdx, setselectedVideoIdx] = useState()
    const [selection, setSelection] = useState('start')
	const [start, setStart] = useState(0)
	const [end, setEnd] = useState(0)
	const [curTime, setCurTime] = useState(0)
    const [player, setPlayer] = useState(null)
	const [error, setError] = useState()
	const [tagGroups, setTagGroups] = useState([])
    const [selectedTags, setSelectedTags] = useState({});
	const [numericTags, setNumericTags] = useState({});
	const [tagIsLoading, setTagIsLoading] = useState(false);

    const fetchVideos = () => {
		fetch('/api/videos/').then((resp) => {
			return resp.json()
		}).then((json) => {
			setVideos(json)
		})
	}

	const fetchTagGroups = () => {
		fetch('/api/tag_groups').then((resp) => {
            return resp.json()
        }).then((json) => {
            setTagGroups(json)
        })
	}

	const handleReady = (e) => {
        setPlayer(e.target)
    }

    const handleSelectionChange = () => {
        if (selection === 'start') {
            setSelection('end')
        } else {
            setSelection('start')
            player.seekTo(start)
        }
    }

	const handleReset = () => {
        player.seekTo(0)
        setStart(0)
        setEnd(0)
    }

	const handleChangeNumericTags = (name, value) => {
		setNumericTags({...numericTags, [name]: value})
	}

	const handleSubmit = async () => {
		if (start >= end) {
			setError("End time must be greater than start time")
			return
		}
		const tagIds = Object.entries(selectedTags).reduce((acc, [_key, value])=> acc.concat(value.map(option => option["value"])), [])
		const data = {
			timestamp: start,
			duration: end - start,
			video_id: videos[selectedVideoIdx].id,
			tag_ids: tagIds,
			tag_values: numericTags
		}

		const response = await fetch('/api/clips/', {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				'X-CSRFToken': getCsrfToken(),
			},
			body: JSON.stringify(data)
		})
		const {id: clipId} = await response.json()
		navigate(`/clip/${clipId}`)
	}

	const handleCreateTag = async (tagName, groupId) => {
		setTagIsLoading(true)
		const data = {name: tagName, group_id: groupId}
		const response = await fetch('/api/tags/', {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				'X-CSRFToken': getCsrfToken(),
			},
			body: JSON.stringify(data)
		})

		const newTag = await response.json()
		const newGroups = tagGroups.map(group => {
			if (group.id == groupId) {
				return {...group, tags: [...group.tags, newTag]}
			} else {
				return group
			}
		})
		setTagGroups(newGroups)
		const newOption = {"value": newTag.id, "label": newTag.name}
		const prevTags = selectedTags[groupId] || []

		setSelectedTags({...selectedTags, [groupId]: [...prevTags, newOption]})
		setTagIsLoading(false)
	}

	const handleSelectedTag = (tags, groupId) => {
		setSelectedTags({...selectedTags, [groupId]: tags})
	}

	useEffect(() => {
		fetchVideos()
		fetchTagGroups()}, [])

    useEffect(() => {
        const interval = setInterval(() => {
            if (player != null) {
                cur = ~~player.getCurrentTime()
                setCurTime(cur)
                if (selection == 'start') {
                    setStart(cur)
                } else {
                    setEnd(cur)
                }
            }
        }, 100)
        return () => clearInterval(interval)
    }, [player, selection])

	return (
		<div className="block">
			{selectedVideoIdx == undefined ? 
			videos.map((video, idx) => {
			return (
				<div key={idx}>
					<div className="card">
						<div className="card-header">
							<div className="card-header-title">{video.title}</div>
						</div>
						<div className="card-content">
							<div className="block is-clickable" onClick={() => setselectedVideoIdx(idx)}>
								<img src={"//img.youtube.com/vi/" + video.youtube_id + "/0.jpg"} width="200" height="100" />
							</div>
						</div>
					</div>
				</div>
			)
		}) : 
		<div>
			{error && <Notificaton message={error} onDismiss={() => setError()}/>}
			<h1 className="title">Create a Clip for {videos[selectedVideoIdx].title}</h1>
			<div className="columns">
				<div className="column">
					<div className="block">
						<YouTube
							onReady={handleReady}
							videoId={videos[selectedVideoIdx].youtube_id}
							className="youtube-container"
							opts={{
								playerVars: {
									modestBranding: 1,
									rel: 0,
									start: 1
								}
							}}
						/>
					</div>
					<div className="block">
						<div className="buttons">
							<div className="button is-outlined">Current time: {fmtSeconds(curTime)}</div>
							<button className="button is-primary" onClick={handleSelectionChange}>
								Select {selection === 'start' ? 'end' : 'start'} of clip
							</button>
							<button className="button is-danger" onClick={handleReset} id="reset-button">
								Reset
							</button>
						</div>
					</div>
					<div className="block">
						<div className="buttons">
							<div className="button is-outlined">Start: {fmtSeconds(start)}</div>
							<div className="button is-outlined">End: {fmtSeconds(end)}</div>
						</div>
					</div>
				</div>
				<div className="column">
					{tagGroups.map((group, idx) => {
						if (group.type == "numeric") {
							return (
							<div style={{ width: '550px'}} className="control">
								<label htmlFor="min-input" className="label">
									{group.name}
								</label>
								<input
								id="min-input"
								className="input"
								type="number"
								value={numericTags[group.name]}
								onChange={e => handleChangeNumericTags(group.name, e.target.value)}
								step="0.01"
								/>
							</div>)
						}
						return (
							<div style={{ width: '550px'}} key={idx}>
								<CreatableSelect
									options={group.tags.map((entry) => {
										return { "value": entry.id, "label": entry.name }
									})}
									onCreateOption={(name) => handleCreateTag(name, group.id)}
									placeholder={"Select " + group.name}
									isSearchable={true}
									isMulti
									classNamePrefix="search-menu"
									value={selectedTags[group.id]}
									onChange={(tags) => handleSelectedTag(tags, group.id)}
									isDisabled={tagIsLoading}
									isLoading={tagIsLoading}
								/>
							</div>
						)
                    })}
				</div>
			</div>
			<button className="button is-success" onClick={handleSubmit} id="submit-button">Submit</button>
		</div>
		}
		</div>
	)
}

export default ClipCreate