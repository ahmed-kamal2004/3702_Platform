import React,{useState} from 'react'
import { Link } from 'react-router-dom';
import classNames from 'classnames';
const Publisher = () => {
   const[Chosen,setChosen]=useState('Dashboard');
  return (
    <div className="bg-amber-100">
        <div className="bg-amber-100" >
            <ul className="flex flex-row justify-evenly list-none bg-black text-white border-amber-100">
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="Dashboard"})}  onClick={(e)=>{setChosen(e.target.innerText)}}>Dashboard</li>
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="MyChannels"})} onClick={(e)=>{setChosen(e.target.innerText)}}>MyChannels</li>
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="Create Channel"})} onClick={(e)=>{setChosen(e.target.innerText)}}><Link to="/create-channels/">Create Channel</Link></li>
            </ul>
        </div>

    </div>
  )
}

export default Publisher