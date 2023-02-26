import React, { useState } from 'react'

import Auth from './auth/auth_manager'
import useAuthState from './auth/auth_state_hook.jsx'


// Just a Card in a form
const FormSection = (props) => {
    return <div className="block">
        <div className="card">
                <header className="card-header">
                    <div className="card-header-title">{props.title}</div>
                </header>
                <div className="card-content">
                    <div className="block">
                        {props.children}
                    </div>
                </div>
        </div>
    </div>
}

const LogoutButton = () => {
    const [actionState, setActionState] = useState("none") // "none", "loading", or "success"

    const buttonClasses = "button is-primary" + (actionState === "loading" ? " is-loading" : "")

    const handleLogout = async (e) => {
        e.preventDefault();
        setActionState("loading")
        await Auth.logout();
        console.log("Logged out")
    }
    return <button className={buttonClasses} onClick={handleLogout}>Log out</button>
}


const ChangeNameForm = () => {
    const authState = useAuthState();
    const name = authState.display_name
    const [newName, setNewName] = useState("");
    const [actionState, setActionState] = useState("none") // "none", "loading", or "success"

    const handleSubmit = async (e) => {
        e.preventDefault();
        setActionState("loading")
        const success = await Auth.changeDisplayName(newName)
        if (success) {
            setActionState("success")
        } else {
            setActionState("none")
        }
    }

    const buttonClasses = "button is-primary" + (actionState === "loading" ? " is-loading" : "")

    return <form onSubmit={handleSubmit}>
        <label>Display Name: {name}</label>
        <div className="field has-addons">
            <div className="control">
                <input
                    className="input"
                    type="text"
                    placeholder=""
                    value={newName}
                    onChange={ev => setNewName(ev.target.value)}
                />
            </div>
            <button className={buttonClasses} type="submit">Change Display Name</button>
        </div>
    </form>
}

const TeamItem = (props) => {
    const team_id = props.team_id
    const team_name = props.team_name
    const member_names = props.member_names
    const active_team = props.active_team

    const [inviteCode, setInviteCode] = useState(null)

    const handleLeaveTeam = (ev) => {
        Auth.leaveOrDeleteTeam(team_id)
    }
    const handleAddPlayer = async () => {
        const code = await Auth.createInviteCode(team_id)
        setInviteCode(code)
        console.log("Invite Code: ", code)
    }
    const handleSelectTeam = async () => {
        Auth.selectTeam(team_id)
    }

    const selectedButton = <button className="button is-primary" disabled={true}>Selected</button>
    const selectButton = <button className="button is-primary is-outlined" onClick={handleSelectTeam}>Select Team</button>

    return <div className="card">
        <div className="card-content">
            <div className="field is-horizontal">
                <div>
                    <h1>{team_name}</h1>
                    {member_names?.join(', ')}
                </div>
            </div>
            <div>
                    {(team_id == active_team) ? selectedButton : selectButton}
                    <button className="button is-secondary" onClick={handleAddPlayer}>Add Player</button>
                    <button className="button is-danger is-outlined" onClick={handleLeaveTeam}>Leave Team</button>

                    {inviteCode &&
                        <div className="notification is-info is-light">
                            Invite Code: <strong>{inviteCode}</strong>.
                            <p>Share this code with another player to invite them to the team.</p>
                        </div>
                    }
                </div>
        </div>
    </div>

}

const TeamsList = () => {
    authState = useAuthState();
    return authState.teams?.map(team => <TeamItem
        key={team.id}
        team_id={team.id}
        team_name={team.name}
        member_names={team.users?.map(u => u.display_name)}
        active_team={authState.active_team}
    />)
}

const CreateTeamForm = () => {
    const [newTeamName, setNewTeamName] = useState("")
    const handleSubmit = (ev) => {
        ev.preventDefault()
        console.log("Creating team with name: ", newTeamName);
        const success = Auth.createTeam(newTeamName);
        console.log("Result: ", success)
    }
    return <form onSubmit={handleSubmit}>
        <div className="field has-addons">
            <div className="control">
                <input
                    className="input"
                    type="text"
                    placeholder="New Team Name"
                    value={newTeamName}
                    onChange={ev => {setNewTeamName(ev.target.value)}}
                />
            </div>
            <button className="button " disabled={newTeamName==""}>Create Team</button>
        </div>
    </form>
}

const JoinTeamForm= () => {
    const [inviteCode, setInviteCode] = useState("")
    const [errorMsg, setErrorMsg] = useState(null)

    const handleSubmit = async (ev) => {
        ev.preventDefault()
        console.log("Joining team with code: ", inviteCode);
        const response = await Auth.joinTeamWithCode(inviteCode);
        if (response === "already-on-team") {
            setErrorMsg("Can't join - you are already on this team.")
        }
        if (response === "code-does-not-exist") {
            setErrorMsg("Invalid or expired code.")
        }
        if (response === true) {
            setErrorMsg(false) // false = success
        }
    }
    return <form onSubmit={handleSubmit}>
        <div className="field has-addons">
            <div className="control">
                <input
                    className="input"
                    type="text"
                    placeholder="Invite Code"
                    value={inviteCode}
                    onChange={ev => {setInviteCode(ev.target.value)}}
                />
            </div>
            <button className="button is-secondary" disabled={inviteCode === ""}>Join Team</button>
            {errorMsg && <p className="has-text-danger">{errorMsg}</p>}
        </div>
    </form>
}


const TeamsComponent = () => {
    return <>
        <div className="block">
            <TeamsList/>
        </div>

        <CreateTeamForm/>
        <JoinTeamForm/>
    </>
}

const AuthView = () => {
    return (
        <section className="section">
            {/* <AuthStateView/> */}


            <FormSection title="Log Out">
                <LogoutButton/>
            </FormSection>

            <FormSection title="Display Name">
                <ChangeNameForm/>
            </FormSection>

            <FormSection title="Teams">
                <TeamsComponent/>
            </FormSection>
        </section>
    )
}

export default AuthView
