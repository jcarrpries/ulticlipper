import React, { useState } from 'react'

const SyncChooseGame = (props) => {
    const {
        setSyncStep,
        url,
        setYoutubeId,
        setSelectedGame,
        games,
        csvFile,
        setClips,
        setEvents,
        setHalftime,
    } = props

    const handleSelectGame = (game) => {
        setSelectedGame(game)
        let data = new FormData()
        data.append('file', csvFile)
        data.append('tournament', game.tournament)
        data.append('opponent', game.opponent)
        data.append('game_date', game.game_date)
        data.append('video_offset', 0)
        data.append('url', url)
        fetch('/api/sync/choosegame/', {
            'method': 'POST',
            'body': data,
        }).then((resp) => {
            return resp.json()
        }).then((json) => {
            setClips(json.clips)
            setEvents(json.events)
            setHalftime(json.halftime)
            setYoutubeId(json.youtube_id)
            setSyncStep('halves')
        })
    }

    return (
        <table className="table">
            <thead>
                <tr>
                    <th>Tournament</th>
                    <th>Opponent</th>
                    <th>Game Date</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {games.map((game, idx) => {
                    return (
                        <tr key={idx}>
                            <td>{game.tournament}</td>
                            <td>{game.opponent}</td>
                            <td>{game.game_date}</td>
                            <td>
                                <button 
                                    className="button is-primary is-small" 
                                    onClick={() => handleSelectGame(game)}
                                >Select</button>
                            </td>
                        </tr>
                    )
                })}
            </tbody>
        </table>
    )
}

export default SyncChooseGame
