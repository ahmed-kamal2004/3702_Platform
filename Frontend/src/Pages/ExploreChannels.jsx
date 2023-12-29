import React, { useState, useEffect } from "react";
import Channel from "../Components/Channel";
import ChannelLayout from "../Components/ChannelLayout";
import axios from "axios";
const ExploreChannels = () => {
	const [search, setsearch] = useState("");
	const [error, seterror] = useState([]);
	const [loading, setloading] = useState(true);
	const [Channels, setChannels] = useState([]);
	const HandleSubmit = (e) => {
		e.preventDefault();
	};
	useEffect(() => {
		axios
			.get("http://127.0.0.1:8000/chn/get_channels")
			.then((response) => {
				console.log(response.data);
				setChannels(response.data);
				setloading(false);
			})
			.catch((error) => console.log(error));
	}, []);
	return (
		<div className="bg-amber-100 py-4">
			<header>
				<form
					onSubmit={HandleSubmit}
					className="bg-amber-100 flex justify-end px-4 py-8">
					<div className="mb-4">
						<input
							type="Search"
							id="Search"
							name="Search"
							placeholder="Search"
							className=" w-[20rem] my-1 px-2 py-1 "
							onChange={(e) => {
								setsearch(e.target.value);
							}}
						/>
						<button className="border border-black px-4 py-1 bg-black text-white hover:bg-slate-400 hover:text-black">
							Search
						</button>
					</div>
				</form>
			</header>
			<main className="flex flex-col items-center">
				{/* <Channel title={"Channeltitle"} description={"Channel's Description is written here"} CreationDate={"2024-02-04"} Rating={4.4} isPrivate={false}/> */}
				{loading === false ? 
    Channels.map((channel, index) => {
        return (
            <Channel
                key={index}
				id={channel.id}
                title={channel.title}
                description={channel.description}
                CreationDate={channel.creationdate}
                Rating={channel.rating}
                isPrivate={channel.type === "private"}
            />
        );
    })
: <p>Loading...</p>}
			</main>
		</div>
	);
};

export default ExploreChannels;
