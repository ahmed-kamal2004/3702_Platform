import React, { useEffect } from "react";
import { useParams } from "react-router-dom";
import Question from "./Question";
import PollsChoice from "./PollsChoice";
const Poll = (props) => {
	const { id } = useParams();
	const [data, setdata] = useState([]);
	useEffect(() => {
		axios
			.get(`http://127.0.0.1:8000/chn/content/polls/${id}`, {
				"token": sessionStorage.getItem("token"),
				"channel_id": id,
			})
			.then((response) => {
				setdata(response.data);
				console.log(response.data);
			})
			.catch((error) => console.log(error));	
	}, []);
	return (
		<div className="border-2 border-black rounded-md py-2 px-4 m-4 bg-gray-200">
			<header className="flex flex-row py-4 items-center">
				<h3 className=" text-md font-extralight px-2 mx-2">{data.Author}</h3>
				<h3 className=" text-md font-extralight px-2 mx-2">{data.Date}</h3>
			</header>
			<hr className="border border-black"/>
			<main>
				<h2 className="font-normal text-xl py-2 px-4">
					{data.text}
				</h2>
				<div className="w-100% px-4 py-2">
					{data.choices.map((choice, index) => {
						return (
							<PollsChoice
								key={index}
								choice={choice}
							/>
						);
					})}
				</div>
			</main>
			<footer></footer>
		</div>
	);
};

export default Poll;
