import React, { useState } from 'react'

import {CreateTeamForm, JoinTeamForm, FormSection} from '../auth.jsx'


const JoinTeamPage = () => {
    return (
        <section className="section">
            <FormSection title="Join or Create a Team to Continue">
                <CreateTeamForm/>
                <JoinTeamForm/>
            </FormSection>
        </section>

    )
}


export default JoinTeamPage
