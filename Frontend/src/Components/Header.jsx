import React from "react";
import { Link,NavLink } from "react-router-dom";
const Header = () => {
	return (
		<div className="flex  flex-row  justify-between m-0 min-w-full bg-amber-100 p-10 ">
			<h1 className=" text-2xl md:grow-1 uppercase font-extrabold underline underline-offset-[5px] decoration-2">
				<NavLink to="/"># 3702_Platform</NavLink>
			</h1>
			<div>
				<button className=" w-36 border-2 border-gray-900 p-2 mx-2 mb-1 rounded-xl hover:bg-black hover:text-white md:grow-0 basis-1/3">
					<Link to="/Explore"> Explore Channels</Link>
				</button>
				<button className=" w-24 border-2 border-gray-900 p-2 mx-2 mb-1 rounded-xl hover:bg-black hover:text-white md:grow-0 basis-1/3">
					<Link to="SignUp"> Join Us</Link>
				</button>
			{<button className=" w-24 border-2 border-gray-900 p-2 mx-2 mb-1 rounded-xl hover:bg-black hover:text-white md:grow-0 basis-1/3">
					<Link to="/SignIn"> Sign In</Link>
				</button>}
			</div>
		</div>
	);
};

export default Header;
