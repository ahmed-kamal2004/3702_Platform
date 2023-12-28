import React from 'react'
import { redirect,Outlet,Navigate } from 'react-router-dom'

const Authentication = () => {
  if(sessionStorage.getItem('JWTtoken')!=null){
    return <Outlet/>
  }
    return <Navigate to='/SignIn'/> 
}

export default Authentication