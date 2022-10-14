import React, { useState } from 'react'

import SyncUpload from './sync_upload'
import SyncChooseGame from './sync_choose_game'
import SyncHalves from './sync_halves'
import SyncVerify from './sync_verify'
import SyncEdit from './sync_edit'
import SyncDone from './sync_done'

// Sync Steps:
// 1. Upload
// 2. ChooseGame
// 3. Halves
// 4. Verify
//   4a. Edit
// 5. Done

const Sync = () => {
    const [syncStep, setSyncStep] = useState('upload')
    const [url, setUrl] = useState('')
    const [youtubeId, setYoutubeId] = useState('')
    const [games, setGames] = useState(null)
    const [csvFile, setCsvFile] = useState(null)
    const [selectedGame, setSelectedGame] = useState(null)
    const [halftime, setHalftime] = useState(0)
    const [clips, setClips] = useState(null)
    const [commitResult, setCommitResult] = useState(null)

    return (
        <>
            <section className="section">
                <div className="card">
                    <header className="card-header">
                        <div className="card-header-title">Synchronize clips: {syncStep}</div>
                    </header>
                    <div className="card-content">
                        {syncStep == 'upload' &&
                            <SyncUpload 
                                setSyncStep={setSyncStep}
                                setGames={setGames}
                                setCsvFile={setCsvFile}
                                setUrl={setUrl}
                            />
                        }
                        {syncStep == 'chooseGame' &&
                            <SyncChooseGame 
                                setSyncStep={setSyncStep}
                                url={url}
                                setYoutubeId={setYoutubeId}
                                setSelectedGame={setSelectedGame}
                                games={games}
                                csvFile={csvFile}
                                setClips={setClips}
                                setHalftime={setHalftime}
                            />
                        }
                        {syncStep == 'halves' &&
                            <SyncHalves 
                                setSyncStep={setSyncStep}
                                youtubeId={youtubeId}
                                clips={clips}
                                setClips={setClips}
                                halftime={halftime}
                            />
                        }
                        {syncStep == 'verify' &&
                            <SyncVerify 
                                setSyncStep={setSyncStep}
                                clips={clips}
                                selectedGame={selectedGame}
                                setCommitResult={setCommitResult}
                                youtubeId={youtubeId}
                                url={url}
                            />
                        }
                        {syncStep == 'edit' &&
                            <SyncEdit 
                                setSyncStep={setSyncStep}
                                clips={clips}
                                setClips={setClips}
                            />
                        }
                        {syncStep == 'done' &&
                            <SyncDone 
                                commitResult={commitResult}
                            />
                        }
                    </div>
                </div>
            </section>
        </>
    )
}

export default Sync
