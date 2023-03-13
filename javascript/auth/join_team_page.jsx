import React, { useState } from 'react'

import {CreateTeamForm, JoinTeamForm, FormSection} from '../auth.jsx'


const JoinTeamPage = () => {
    return (
        <section className="section">
            <FormSection title="Join or Create a Team to Continue">
                <label>Join a team with the invite code:</label>
                <JoinTeamForm/>
                <label>Or, create your own team:</label>
                <CreateTeamForm/>
            </FormSection>
        </section>

    )
}


export default JoinTeamPage
