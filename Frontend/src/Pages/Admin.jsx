import React,{useState,useEffect} from 'react'
import { Link } from 'react-router-dom';
import axios from 'axios';
import classNames from 'classnames';
const Admin = () => {
  const[Chosen,setChosen]=useState('Dashboard');
  useEffect(() => {
    if(Chosen=="Users"){
      axios.get()
    }
  },[])
  return (
    <div className="bg-amber-100">
        <div className="bg-amber-100" >
            <ul className="flex flex-row justify-evenly list-none bg-black text-white border-amber-100">
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="Dashboard"})}  onClick={(e)=>{setChosen(e.target.innerText)}}>Dashboard</li>
                <li className={classNames("hover:bg-white hover:scale-125 hover:text-black px-4 py-2 rounded-lg",{'underline underline-offset-3': Chosen=="Users"})}  onClick={(e)=>{setChosen(e.target.innerText)}}>Users</li>
            </ul>
        </div>

    </div>
  )
}

export default Admin