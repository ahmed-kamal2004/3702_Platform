import React, { useState } from "react";
import classNames from "classnames";
import { Link } from "react-router-dom";
import axios from "axios";
const Channel = (props) => {
	const [code, setcode] = useState("");
	const [appear, setappear] = useState(false);
	let [error, seterror] = useState("");
	const HandleSubmit = (e) => {
		e.preventDefault();
        if(!props.isPrivate){
				axios.post("http://127.0.0.1:8000/stu/join-channel", {
					"username":sessionStorage.getItem("username"),"channel_id": props.id,
					"code":code
				}).then((response) => {
				console.log(response.data);
			}).catch((error) => console.log(error));
	}
        let errors="";
		if (code == "" && props.isPrivate) errors = "Code is required!";
		seterror(errors);
		if (errors == "") {
			axios.post("http://127.0.0.1:8000/stu/join-channel", {
				"username":sessionStorage.getItem("username"),"channel_id": props.id,
				"code":code
			}).then((response) => {
			console.log(response.data);
		}).catch((error) => console.log(error));
		}

	};
	return (
		<div className=" w-1/2 border border-black mx-4 mb-4 px-4 py-2 bg-slate-100 rounded-lg">
			<header>
				<h1 className="font-semibold text-2xl px-4">
				<Link to={`/Channels/${props.id}`}>{props.title}</Link></h1>
			</header>
			<main className="flex flex-col justify-center items-start px-4 py-2">
				<h2 className="py-2 font-medium">Description: {props.description}</h2>
				<h2 className="py-2 font-medium">CreationDate: {props.CreationDate}</h2>
				<h2 className="py-2 font-medium">Rating: {props.Rating}</h2>
			</main>
			<footer className="flex flex-col items-center">
				{props.isPrivate && appear && (
					<div>
						{" "}
						<form onSubmit={HandleSubmit}>
							<label>
								Code:
								<input
									type="Code"
									id="Code"
									name="Code"
									placeholder=" Enter the Channel Code"
									className={"my-2 px-2 py-1 "}
									onChange={(e) => {
										setcode(e.target.value);
									}}
								/>
							</label>
							<button className="border rounded-lg bg-black text-white ml-4 px-1 py-1">
								Submit
							</button>
						</form>
						{error && <p className="text-red-500 text-sm my-2 text-center">{error}</p>}
					</div>
				)}
				{sessionStorage.getItem("type")!=="Publisher"&&<button
					className="border border-slate-100 bg-black text-white px-4 py-2 rounded-md"
					onClick={(e) => {
						if(props.isPrivate)
                            setappear(true);
                        else HandleSubmit(e);
					}}>
					Join Channel
				</button>}
			</footer>
		</div>
	);
};


export default Channel;
