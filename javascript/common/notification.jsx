import React from 'react'

const Notificaton = ({type = "is-danger", message, onDismiss}) => {
	return (
		<div className={`notification ${type}`}>
			<button className="delete" onClick={onDismiss}></button>
			{message}
		</div>
	) 
}

export default Notificaton