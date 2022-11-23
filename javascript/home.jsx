import React from 'react'

import Search from './search'

const Home = () => {
    return (
        <>
            <section className="hero is-fullheight is-primary">
                <div className="hero-body">
                    <div className="">
                        <p className="title" id="hero-title-text">
                        The Ultimate Clipper Tool
                        </p>
                        <p className="subtitle">
                        Search for tagged clips across all your game footage
                        </p>
                    </div>
                </div>
            </section>
            <section className="hero has-background-primary-light">
                <Search />
            </section>
        </>
    )
}

export default Home
