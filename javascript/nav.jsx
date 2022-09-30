import React from 'react'
import { Link } from 'react-router-dom'

const Nav = () => {
    return (
        <div className="navbar is-primary">
            <div className="navbar-brand">
                <div className="navbar-item">
                    <Link to="/"><h6 className="title">Ultimate Clipper</h6></Link>
                </div>
                <Link to="/upload" className="navbar-item">Upload</Link>
                <Link to="/search" className="navbar-item">Search</Link>
            </div>
        </div>
    )
}

export default Nav
