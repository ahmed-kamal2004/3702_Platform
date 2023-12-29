import React, { useEffect } from "react";
import ChannelLayout from "../Components/ChannelLayout";
import Footer from "../Components/Footer";
import { useParams } from "react-router-dom";
import Question from "../Components/Question";
const Quiz = () => {
	const [data, setdata] = useState([]);
	const [questions, setQuestions] = useState([]);
	const { id } = useParams();
	useEffect(() => {
		axios
			.get("http://127.0.0.1:8000/chn/content/quizes", {
				token: sessionStorage.getItem("token"),
				channel_id: id,
			})
			.then((response) => {
				setdata(response.data);
				console.log(response.data);
			})
			.catch((error) => console.log(error));
		for (let i = 0; i < data.length; i++) {
			axios
				.get(`http://127.0.0.1:8000/chn/content/question/${data["id"]}`)
				.then((response) => {
					(questions) => {
						setQuestions([...questions, response.data]);
					};
					console.log(response.data);
				})
				.catch((error) => console.log(error));
		}
	}, []);
	return (
		<div className="bg-amber-100  ">
			<ChannelLayout />
			<div className="flex flex-col items-center justify-center">
				{data.map((homework, index) => {
					return (
						<Question
							key={index}
							id={data[index]}
							Qtext={data[index]["text"]}
							choices={data[index]["choices"]}
							Answer={data[index]["Answer"]}
							is_last={index === data.length - 1}
						/>
					);
				})}
			</div>
			<Footer />
		</div>
	);
};

export default Quiz;
