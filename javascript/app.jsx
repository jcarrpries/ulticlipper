import React, { useState } from 'react'
import * as ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Home from './home'
import Nav from './nav'
import Search from './search'
import View from './view'
import TagSearch from './tagsearch'

import Sync from './sync/sync'

const App = () => {
    return (
        <BrowserRouter>
            <Nav />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/sync" element={<Sync />} />
                <Route path="/search" element={<Search />} />
                <Route path="/clip/:clipId" element={<View />} />
                <Route path="/tagsearch" element={<TagSearch />} />
            </Routes>
        </BrowserRouter>
    )
}

document.addEventListener('DOMContentLoaded', () => {
    const root = ReactDOM.createRoot(document.getElementById('root'))
    root.render(
        <App />
    )
})

export default App
