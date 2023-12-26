import React from "react";
import Question from "./Question";
import PollsChoice from "./PollsChoice";
const Poll = (props) => {
	return (
		<div className="border-2 border-black rounded-md py-2 px-4 m-4 bg-gray-200">
			<header className="flex flex-row py-4 items-center">
				<h3 className=" text-md font-extralight px-2 mx-2">{props.Author}</h3>
				<h3 className=" text-md font-extralight px-2 mx-2">{props.Date}</h3>
			</header>
			<hr className="border border-black"/>
			<main>
				<h2 className="font-normal text-xl py-2 px-4">
					{props.text}
				</h2>
				<div className="w-100% px-4 py-2">
					<PollsChoice text={"HEllo,World!"} chosen={120}/>
				</div>
			</main>
			<footer></footer>
		</div>
	);
};

export default Poll;
