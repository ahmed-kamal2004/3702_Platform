import React, { useState } from "react";
import Channel from "../Components/Channel";
import ChannelLayout from "../Components/ChannelLayout";
const ExploreChannels = () => {
	const [search, setsearch] = useState("");
	const [error, seterror] = useState([]);
	const HandleSubmit = (e) => {
		e.preventDefault();
	};
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
                <Channel title={"Channeltitle"} description={"Channel's Description is written here"} CreationDate={"2024-02-04"} Rating={4.4} isPrivate={false}/>
            </main>
		</div>
	);
};

export default ExploreChannels;
