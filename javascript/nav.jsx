import React from 'react'
import { Link } from 'react-router-dom'

const Nav = () => {
    return (
        <div className="navbar is-primary">
            <div className="navbar-brand">
                <div className="navbar-item">
                    <Link to="/"><h6 className="title">Ultimate Clipper</h6></Link>
                </div>
                <Link to="/sync" className="navbar-item" id="sync-nav-item">Sync</Link>
                {/* <Link to="/testimport" className="navbar-item">TestImport</Link> */}
                <Link to="/search" className="navbar-item" id="search-nav-item">Search</Link>
                <Link to="/tagsearch" className="navbar-item">TagSearch</Link>
                <Link to="/drawdemo" className="navbar-item">DrawDemo</Link>
                <Link to="/auth" className="navbar-item">Teams and Profile</Link>
            </div>
        </div>
    )
}

export default Nav
