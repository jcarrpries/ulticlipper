import { useState, useEffect } from 'react'

import Auth from './auth_manager'

// Custom React hook for accessing the automatically-updating AuthState
function useAuthState() {
    const [authState, setAuthState] = useState(Auth.getCurrentState());

    useEffect(() => {
        function listener(newState) {
            setAuthState(newState);
        }

        Auth.subscribe(listener); // Called once, on component mount

        return () => {
            Auth.unsubscribe(listener); // Called once, on component unmount
        };
    }, []);

    return authState;
}

export default useAuthState;