import React, { useState } from 'react'
import * as ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Home from './home'
import Nav from './nav'
import Search from './search'
import View from './view'
import TagSearch from './tagsearch'

import Auth from './auth'
import DrawDemo from './drawdemo'

import Sync from './sync/sync'
import useAuthState from './auth/auth_state_hook'

import LoginPage from './auth/login_page'


// The main App, shown when the User is signed in
const MainApp = () => {
    return <BrowserRouter>
        <Nav />
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/sync" element={<Sync />} />
            <Route path="/search" element={<Search />} />
            <Route path="/clip/:clipId" element={<View />} />
            <Route path="/tagsearch" element={<TagSearch />} />
            <Route path="/drawdemo" element={<DrawDemo />} />
            <Route path="/auth" element={<Auth />} />
        </Routes>
    </BrowserRouter>
}


const App = () => {
    const authState = useAuthState()
    return (authState.is_authenticated !== false) ? <MainApp/> : <LoginPage/>
}

document.addEventListener('DOMContentLoaded', () => {
    const root = ReactDOM.createRoot(document.getElementById('root'))
    root.render(
        <App />
    )
})

export default App
