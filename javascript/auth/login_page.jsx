import React, { useState } from 'react'

import Auth from './auth_manager'
import useAuthState from './auth_state_hook.jsx'

const LoginForm = () => {
    const [loginEmail, setLoginEmail] = useState('');
    const [loginPassword, setLoginPassword] = useState('');
    const [errorMsg, setErrorMsg] = useState(null);

    const handleLogin = async (e) => {
        e.preventDefault();
        const success = await Auth.login(loginEmail, loginPassword);
        if (!success) {
            setErrorMsg("Incorrect username or password.")
        }
        console.log("Login success: ", success);
    }

    return <div className="card">
        <header className="card-header">
            <div className="card-header-title">Login</div>
        </header>
        <div className="card-content">
            <div className="block">
                <form onSubmit={handleLogin}>
                    <div className="search-menu">
                        <div style={{ width: '550px'}}>
                            {errorMsg && <div className="notification is-danger">{errorMsg}</div>}
                            <input
                                className="input"
                                type="text"
                                placeholder="Email"
                                value={loginEmail}
                                onChange={ev => setLoginEmail(ev.target.value)}
                            />
                            <input
                                className="input"
                                type="password"
                                placeholder="Password"
                                value={loginPassword}
                                onChange={ev => setLoginPassword(ev.target.value)}
                            />
                        </div>
                    </div>
                    <div className="control">
                        <button className="button is-primary" type="submit">Login</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
}



const RegisterForm = () => {
    const [registerName, setRegisterName] = useState('');
    const [registerEmail, setRegisterEmail] = useState('');
    const [registerPassword, setRegisterPassword] = useState('');

    const [errorMsg, setErrorMsg] = useState(null);

    const handleCreateUser = async (e) => {
        // createuser/<str:username>/<str:new_password>/
        e.preventDefault();
        const outcome = await Auth.register(registerEmail, registerPassword, registerName);
        if (outcome.error == "empty-field") {
            setErrorMsg("All fields are required.")
        }
        if (outcome.error == "username-taken") {
            setErrorMsg("An account already exists with this email.")
        }
        if (outcome.error == false) {
            setErrorMsg(false)
        }
    }




    return <div className="card">
        <header className="card-header">
            <div className="card-header-title">Register</div>
        </header>
        <div className="card-content">
            <div className="block">
                <form onSubmit={handleCreateUser}>
                    <div className="search-menu">
                        <div style={{ width: '550px'}}>
                            {errorMsg && <div className="notification is-danger">{errorMsg}</div>}
                            {errorMsg == false && <div className="notification is-success">Account Created</div>}
                            <input
                                id="register-display-name"
                                className="input"
                                type="text"
                                placeholder="Display Name"
                                value={registerName}
                                onChange={ev => setRegisterName(ev.target.value)}
                            />
                            <input
                                id="register-email"
                                className="input"
                                type="text"
                                placeholder="Email"
                                value={registerEmail}
                                onChange={ev => setRegisterEmail(ev.target.value)}
                            />
                            <input
                                id="register-password"
                                className="input"
                                type="password"
                                placeholder="Password"
                                value={registerPassword}
                                onChange={ev => setRegisterPassword(ev.target.value)}
                            />
                        </div>
                    </div>
                    <div className="control">
                        <button id="register-button" className="button is-primary" type="submit">Register</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
}



const LoginPage = () => {
    return (
        <section className="section">
            <LoginForm/>
            <RegisterForm/>
        </section>
    )
}


export default LoginPage
