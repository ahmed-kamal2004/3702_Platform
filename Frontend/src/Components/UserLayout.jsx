import React from 'react'
import { Outlet } from 'react-router-dom'
import Footer from './Footer'
import HeaderLayout from './HeaderLayout'
const UserLayout = () => {
  return (
    <div>
        <HeaderLayout/>
        <Outlet/>
        <Footer/>
    </div>
  )
}

export default UserLayout