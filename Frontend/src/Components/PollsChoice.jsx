import React, { useState } from "react";
import classNames from "classnames";
const pollsChoice = (props) => {
	const [Chosen, setChosen] = useState("");
	return (
		<div>
			<div className={classNames("flex flex-row  justify-between items-center m-2 hover:border hover:border-black hover:bg-gray-500 hover:text-white hover:rounded-lg pr-4",{"bg-gray-500 rounded-lg text-white":Chosen!=""})} onClick={(e)=>{
				setChosen(`${props.text}`)
			}}>
				<h3 className={"px-4 py-2"}>{props.text}</h3>
				<h3>{props.chosen+((Chosen==`${props.text}`)?1:0)}</h3>
			</div>
		</div>
	);
};

export default pollsChoice;
