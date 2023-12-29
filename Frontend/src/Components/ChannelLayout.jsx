import React, { useState } from "react";
import classNames from "classnames";
import { NavLink } from "react-router-dom";
const ChannelLayout = () => {
    const [isOpen, setIsOpen] = useState(false);
	const [chosen, setChosen] = useState("DashBoard");
	return (
		<div className="bg-amber-100">
			<div className="flex flex-row justify-between m-4 my-0 px-4 py-2 ">
				<h1 className=" text-2xl md:grow-1 uppercase font-extrabold underline underline-offset-[5px] decoration-2">
				<NavLink to="/"># 3702_Platform</NavLink>
				</h1>
				<div>
					<button
						className="border border-amber-100 bg-black text-white px-2 py-2 w-48 rounded-md"
						onClick={() => {
							setIsOpen(!isOpen);
						}}>
						{chosen}
					</button>
					<ul
						className={classNames(
							"flex flex-col list-none bg-white px-4 py-2",
							{ hidden: !isOpen }
						)}>
						<li
							className="hover:bg-black hover:text-white text-center w-40"
							onClick={(e) => {
								setChosen(e.target.innerText);
								setIsOpen(false);
							}}>
							DashBoard
						</li>
						<li
							className="hover:bg-black hover:text-white text-center w-40"
							onClick={(e) => {
								setChosen(e.target.innerText);
								setIsOpen(false);
							}}>
							Articles
						</li>
						<li
							className="hover:bg-black hover:text-white text-center w-40"
							onClick={(e) => {
								setChosen(e.target.innerText);
								setIsOpen(false);
							}}>
							HomeWork
						</li>
						<li
							className="hover:bg-black hover:text-white text-center w-40"
							onClick={(e) => {
								setChosen(e.target.innerText);
								setIsOpen(false);
							}}>
							Problemset
						</li>
						<li
							className="hover:bg-black hover:text-white text-center w-40"
							onClick={(e) => {
								setChosen(e.target.innerText);
								setIsOpen(false);
							}}>
							Quizzes
						</li>
						<li
							className="hover:bg-black hover:text-white text-center w-40"
							onClick={(e) => {
								setChosen(e.target.innerText);
								setIsOpen(false);
							}}>
							Polls
						</li>
						<li
							className="hover:bg-black hover:text-white text-center w-40"
							onClick={(e) => {
								setChosen(e.target.innerText);
								setIsOpen(false);
							}}>
							Discussions
						</li>
					</ul>
				</div>
			</div>
		</div>
	);
};

export default ChannelLayout;
