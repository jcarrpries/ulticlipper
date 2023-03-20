import React, {useState, useEffect} from 'react'

const ProgressBar = ({player, duration, startTime}) => {
	const [currentTime, setCurrentTime] = useState(0);
	
	
	useEffect(() => {
		const intervalId = setInterval(() => {
			if (player) {
				setCurrentTime(player.getCurrentTime());
			}
		}, 1000);
		return () => clearInterval(intervalId);
	}, [player]);

	return (
		<progress className="progress mx-4" value={duration == 0 ? 1 : (currentTime - startTime) / duration} max="1"></progress>
	) 
}

export default ProgressBar