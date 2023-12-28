import React from 'react'
import { Link,NavLink } from 'react-router-dom'

const HeaderLayout = () => {
  return (
    <div>
        <>
        <div className="flex  flex-row  justify-between m-0 min-w-full bg-amber-100 p-10 ">
			<h1 className=" text-2xl md:grow-1 uppercase font-extrabold underline underline-offset-[5px] decoration-2">
      <NavLink to="/"># 3702_Platform</NavLink>
			</h1>
			<ul className="list-none flex flex-row mr-8">
                <li className="font-medium mx-3 border-2 border-black px-2 py-1 rounded-xl bg-slate-50 hover:text-white hover:bg-black"><Link to='/Explore'>ExploreChannels</Link></li>
			</ul>
		</div>
        </>
    </div>
  )
}

export default HeaderLayout