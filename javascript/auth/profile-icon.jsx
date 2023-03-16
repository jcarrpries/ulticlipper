import React, { useState } from 'react'
import { Link } from 'react-router-dom'

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser } from "@fortawesome/free-regular-svg-icons";
import useAuthState from './auth_state_hook';
library.add(faUser)

import Auth from './auth_manager'


const ProfileIcon = () => {
    const [isActive, setIsActive] = useState(false);
    const toggleDropdown = () => setIsActive(!isActive);

    const authState = useAuthState();
    const userTeams = authState.teams || [];

    const activeTeamId = authState.active_team;

    const handleSelectTeam = (team) => {
        Auth.selectTeam(team);
    }

    return (
        <div className="navbar-end is-flex" style={{ alignItems: 'center' }}>
            <div className={`navbar-item has-dropdown ${isActive ? 'is-active' : ''}`}>
                <button className="button is-primary" onClick={toggleDropdown}>
                    <span className="icon">
                        <div>
                            <FontAwesomeIcon icon="fa-regular fa-user" />
                        </div>
                    </span>
                    <label>Teams & Profile</label>
                </button>
                <div className="navbar-dropdown is-right">
                    <div className="navbar-item">
                        <p className="has-text-weight-bold">Profile</p>
                    </div>
                    <div className="navbar-item">
                        <div>
                            <p>{authState.display_name}</p>
                            <p>{authState.email}</p>
                        </div>
                    </div>
                    <div className="navbar-item">
                        <Link to="/auth" className="button is-primary is-outlined">Edit Profile</Link>
                        <button className="button is-danger is-outlined" onClick={() => Auth.logout()}>
                            Sign Out
                        </button>
                    </div>
                    <hr className="navbar-divider" />
                    <div className="navbar-item">
                        <div>
                            <p className="has-text-weight-bold">Your Teams</p>
                            <p className="has-text-grey">Select a team to view its clips and data.</p>
                        </div>
                    </div>

                    {userTeams.map((team) => (
                        <div className="navbar-item" key={team.id}>
                            <label className="radio">
                                <input
                                    // style={{ marginRight: '0.5rem', transform: 'scale(1.5)' }}
                                    style={{ marginRight: '0.5rem'}}
                                    type="radio"
                                    name="profile-dropdown-team"
                                    checked={activeTeamId === team.id}
                                    onChange={() => handleSelectTeam(team.id)}
                                />
                                <span>{team.name}</span>
                            </label>
                        </div>
                    ))}
                    <div className="navbar-item">
                        <Link to="/auth" className="button is-primary is-outlined">Manage Teams</Link>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ProfileIcon