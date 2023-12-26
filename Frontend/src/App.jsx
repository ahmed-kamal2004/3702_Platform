import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './index.css'
import  Navbar from './Pages/Navbar'
import  Home from './Pages/Home'
import  SignIn from './Pages/SignIn'
import {createBrowserRouter,createRoutesFromElements,Routes,Route, RouterProvider } from 'react-router-dom'
import SignUp from './Pages/SignUp'
import UserLayout from './Components/UserLayout'
import Student from './Pages/Student'
import Channels from './Pages/Channels'
import HomeWork from './Pages/HomeWork'
import Question from './Components/Question'
function App() {
  const router=createBrowserRouter(createRoutesFromElements(
         <>
        <Route path='/' element={<Navbar/>}>
        <Route index element ={<Home/>}/>
        </Route>
        <Route path='SignUp'  element={<SignUp/>}/>
        <Route path='SignIn'  element={<SignIn/>}/>
        <Route path='Student/' element={<UserLayout/>}>
        <Route path=":username" element={<Student/>}/>
        </Route>
        <Route path="Channels/:id" element={<Channels/>}>
        </Route>
        <Route path="Channels/:id/HomeWork/:id2" element={<HomeWork/>}/>
        </>
  ))
  return (
    <RouterProvider router={router}/>
  )
}

export default App
