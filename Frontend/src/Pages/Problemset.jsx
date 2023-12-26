import React from 'react'
import Question from '../Components/Question'
import ChannelLayout from '../Components/ChannelLayout'
import Footer from '../Components/Footer'
const Problemset = () => {
  return (
    <div>
        
			<ChannelLayout />
			<Question Qtext={"Hello,World"} choices={[1, 2, 3, 4]} is_last={false} />
			<Footer />
		
    </div>
  )
}

export default Problemset