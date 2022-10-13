import React, { useState } from 'react'
import * as ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Home from './home'
import Nav from './nav'
import Search from './search'
import Upload from './upload'
import View from './view'
import TestImport from './testimport'

const App = () => {
    return (
        <BrowserRouter>
            <Nav />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/search" element={<Search />} />
                <Route path="/upload" element={<Upload />} />
                <Route path="/clip/:clipId" element={<View />} />
                <Route path="/testimport" element={<TestImport />} />
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
