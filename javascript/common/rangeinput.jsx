import React, { useState, useEffect } from 'react'
 
const RangeInput = ({name, handleChange}) => {
	const [max, setMax] = useState("")
	const [min, setMin] = useState("")

	const handleMaxChange = (e) => {
		setMax(e.target.value)
	}

	const handleMinChange = (e) => {
		setMin(e.target.value)
	}

	useEffect(() => {
		handleChange(name, {max, min})
	}, [max, min])

	return (
		<div style={{ width: '550px'}}>
			<div className="field is-horizontal">
				<div className="field-label is-normal is-flex-grow-0">
					<label className="label">
						{name}
					</label>
				</div>
				<div className='field-body'>
				<div className='field'>
					<div className="control">
						<label htmlFor="min-input" className="label">
							Min
						</label>
						<input
						id="min-input"
						className="input"
						type="number"
						value={min}
						onChange={handleMinChange}
						step="0.01"
						/>
					</div>
					</div>
					<div className='field'>
						<div className="control">
							<label htmlFor="max-input" className="label">
								Max
							</label>
							<input
							id="max-input"
							className="input"
							type="number"
							value={max}
							onChange={handleMaxChange}
							step="0.01"
							/>
						</div>
					</div>
				</div>
			</div>
		</div>
	)
}

export default RangeInput