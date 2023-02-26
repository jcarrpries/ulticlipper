/*
This file implements the Auth Manager.

Actions like Auth.createTeam() make a POST requeset, and the response is a new AuthState.
The AuthState describes the state of the use (whether they're logged in, their display
name, a list of teams of the user, etc).

The auth manager keeps track of the AuthState and alerts components when it updates.

Components can subscribe using the Auth.subscribe() and Auth.unsubscribe() methods,
or with the useAuthState() hook (defined in auth_state_hook.jsx)

*/


function getCsrfToken() {
    if (!document.cookie) {
      return null;
    }

    const xsrfCookies = document.cookie.split(';')
      .map(c => c.trim())
      .filter(c => c.startsWith('csrftoken='));

    if (xsrfCookies.length === 0) {
      return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

// Helper func to send POST request with CSRF token set
async function post(url, body) {
    resp = await fetch(
        url, {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify(body)
        }
    )

    j = await resp.json();

    return j
}

const Auth = (() => {
    let state = {
        is_authenticated: null, // null means uninitialized (neither true/false)
    }
    let refreshing = false;
    let listeners = [];

    function subscribe(cb) { // add listener
        listeners.push(cb)

        if (state.is_authenticated === null) {
            refresh();
        } else {
            cb(state)
        }
    }
    function unsubscribe(cb) { // remove listener
        listeners = listeners.filter(l => l != cb)
    }

    function getCurrentState() {
        return state
    }

    const update_state = (new_state) => {
        state = new_state;

        // alert all listeners
        listeners.forEach(cb => {
            // make a copy before sending out the state.
            // Ensures that React components get updated in case state is mutated.
            const state_copy = JSON.parse(JSON.stringify(state))
            cb(state_copy)
        })
    }

    async function refresh() {
        if (refreshing == true) {
            // Ensures that refresh() doesn't get spammed while loading
            return
        }
        refreshing = true;
        const resp = await fetch("/api/authstate")
        new_state = await resp.json();
        update_state(new_state);
        refreshing = false;
    }

    async function login(email, password) {
        new_state = await post("/api/login/", {
            email,
            password
        })

        update_state(new_state);

        return new_state.is_authenticated; // true if successful
    }

    async function logout() {
        new_state = await post("/api/logout/", {})
        update_state(new_state);
    }

    async function register(email, password, display_name) {
        new_state = await post("/api/createuser/", {
            email,
            password,
            display_name
        })

        if (new_state == "empty-field") {
            return {error: "empty-field"}
        } else if (new_state == "username-taken") {
            return {error: "username-taken"}
        } else {
            update_state(new_state);
            return {error: false} // Success
        }
    }

    async function changeDisplayName(newName) {
        new_state = await post('/api/setdisplayname/', {
            "display_name": newName
        })

        update_state(new_state)

        return true; // true for success
    }

    async function createTeam(teamName) {
        new_state = await post("/api/create_team/", {
            "team_name": teamName,
        })

        update_state(new_state)

        return true;
    }

    async function leaveOrDeleteTeam(teamId) {
        // teamId must be an integer
        new_state = await post("/api/leave_or_delete_team/", {
            "team_id": teamId,
        })

        update_state(new_state)

        return true;
    }

    async function createInviteCode(teamId) {
        invite_code = await post("/api/create_invite_code/", {
            "team_id": teamId,
        })

        return invite_code;

    }

    async function joinTeamWithCode(code) {
        new_state = await post("/api/join_team_with_code/", {
            "invite_code": code,
        })

        if (new_state == "code-does-not-exist") {
            return "code-does-not-exist"
        }
        if (new_state == "already-on-team") {
            return "already-on-team"
        }

        update_state(new_state)

        return true;
    }

    // Only data from the active_team gets returned in API responses.
    // If user wants to view data from another team, they use set_active_team to select a new team.
    async function selectTeam(team_id) {
        const new_state = await post("/api/set_active_team/", {
            "team_id": team_id,
        })

        update_state(new_state)

        return true;
    }

    return {
        subscribe,
        unsubscribe,
        getCurrentState,
        refresh,
        login,
        logout,
        register,
        changeDisplayName,
        createTeam,
        leaveOrDeleteTeam,
        createInviteCode,
        joinTeamWithCode,
        selectTeam,
    }

})()

// Example use of subscribe()
Auth.subscribe(s => {
    console.log("New Auth State: ", s);
})

export default Auth
export {getCsrfToken}
