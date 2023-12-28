import React,{useState} from 'react'
import { Link } from 'react-router-dom'
import classNames from 'classnames'
const Student = () => {
    const[Chosen,setChosen]=useState('Dashboard');
  return (
    <div className="bg-amber-100">
        <div className="bg-amber-100" >
            <ul className="flex flex-row justify-evenly list-none bg-black text-white border-amber-100">
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="Notifications"})}  onClick={(e)=>{setChosen(e.target.innerText)}}>Notifications</li>
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="Dashboard"})}  onClick={(e)=>{setChosen(e.target.innerText)}}>Dashboard</li>
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="HomeWork"})} onClick={(e)=>{setChosen(e.target.innerText)}}>HomeWork</li>
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="Quiz"})} onClick={(e)=>{setChosen(e.target.innerText)}}>Quiz</li>
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="MyDiscussions"})} onClick={(e)=>{setChosen(e.target.innerText)}}>MyDiscussions</li>
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="MyChannels"})} onClick={(e)=>{setChosen(e.target.innerText)}}>MyChannels</li>
            </ul>
        </div>
    </div>
  )
}

export default Student