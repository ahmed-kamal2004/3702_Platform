import React, { useEffect, useState, } from "react";
import classNames from "classnames";
import { NavLink,useParams } from "react-router-dom";
import Footer from "../Components/Footer";
import axios from "axios";
const Channels = () => {
	const [isOpen, setIsOpen] = useState(false);
	const [chosen, setChosen] = useState("DashBoard");
	const [data, setdata] = useState([]);
	const {id}= useParams();
	useEffect(() => {
		if (chosen === "Articles") {
			axios
				.get("http://127.0.0.1:8000/chn/content/articles", {
					"token": sessionStorage.getItem("token"),
					"channel_id": id,
				})
				.then((response) => {
					setdata(response.data);
					console.log(response.data);
				})
				.catch((error) => console.log(error));
		}
		else if (chosen === "HomeWork") {
			axios
				.get("http://127.0.0.1:8000/chn/content/homeworks", {
					"token": sessionStorage.getItem("token"),
					"channel_id": id,
				})
				.then((response) => {
					setdata(response.data);
					console.log(response.data);
				})
				.catch((error) => console.log(error));}
		else if (chosen === "Problemset") {
			axios
				.get("http://127.0.0.1:8000/chn/content/problemsets", {
					"token": sessionStorage.getItem("token"),
					"channel_id": id,
				})
				.then((response) => {
					setdata(response.data);
					console.log(response.data);
				})
				.catch((error) => console.log(error));}
		else if(chosen === "Quizzes"){
			axios
				.get("http://127.0.0.1:8000/chn/content/quizes", {
					"token": sessionStorage.getItem("token"),
					"channel_id": id,
				})
				.then((response) => {
					setdata(response.data);
					console.log(response.data);
				})
				.catch((error) => console.log(error));
		}
		else if(chosen === "Discussions"){
			axios
			.get("http://127.0.0.1:8000/chn/content/Discussions", {
				"token": sessionStorage.getItem("token"),
				"channel_id": id,
			})
			.then((response) => {
				setdata(response.data);
				console.log(response.data);
			})
			.catch((error) => console.log(error));	
		}
		else if(chosen === "Polls"){
			axios
			.get("http://127.0.0.1:8000/chn/content/polls", {
				"token": sessionStorage.getItem("token"),
				"channel_id": id,
			})
			.then((response) => {
				setdata(response.data);
				console.log(response.data);
			})
			.catch((error) => console.log(error));	
		}

	}, []);
	return (
		<div className="bg-amber-100 ">
			<header>
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
			</header>
			<main className="flex flex-col items-center">
				{data.map((item, index) => {
					return(<div className=" w-1/2 border border-black mx-4 mb-4 px-4 py-2 bg-slate-100 rounded-lg">
						{chosen==="Articles"&&<NavLink to={`/Channels/${id}/Articles/${item.id}`}><h1 className="font-semibold text-2xl px-4">{item.title}</h1></NavLink>}
						{chosen==="HomeWork"&&<NavLink to={`/Channels/${id}/HomeWork/${item.id}`}><h1 className="font-semibold text-2xl px-4">{item.title}</h1></NavLink>}
						{chosen==="Problemset"&&<NavLink to={`/Channels/${id}/Problemset/${item.id}`}><h1 className="font-semibold text-2xl px-4">{item.title}</h1></NavLink>}
						{chosen==="Quizzes"&&<NavLink to={`/Channels/${id}/Quiz/${item.id}`}><h1 className="font-semibold text-2xl px-4">{item.title}</h1></NavLink>}
						{chosen==="Polls"&&<NavLink to={`/Channels/${id}/Poll/${item.id}`}><h1 className="font-semibold text-2xl px-4">{item.title}</h1></NavLink>}
						{chosen==="Discussions"&&<NavLink to={`/Channels/${id}/Discussion/${item.id}`}><h1 className="font-semibold text-2xl px-4">{item.title}</h1></NavLink>}
					</div>)
				})}
			</main>

			<Footer />
		</div>
	);
};

export default Channels;
