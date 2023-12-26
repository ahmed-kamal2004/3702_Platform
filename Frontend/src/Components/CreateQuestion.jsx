import React, { useState } from "react";

const CreateQuestion = () => {
	const [Head, setHead] = useState(null);
	const [choice1, setchoice1] = useState(null);
	const [choice2, setchoice2] = useState(null);
	const [choice3, setchoice3] = useState(null);
	const [choice4, setchoice4] = useState(null);
	const [answer, setAnswer] = useState(null);
	const [error, setError] = useState({});
	const HandleSubmit = (e) => {
		e.preventDefault();
		const errors = {};
		if (!Head) errors.Head = "Question text is required!";
		if (!choice1) errors.choice1 = "Choice can't be empty!";
		if (!choice2) errors.choice2 = "Choice can't be empty!";
		if (!choice3) errors.choice3 = "Choice can't be empty!";
		if (!choice4) errors.choice4 = "Choice can't be empty!";
		if (!answer) errors.answer = "Answer can't be empty!";
		setError(errors);
		if (Object.keys(errors).length === 0) {
		}
		// here is the post request of the
	};
	return (
		<div>
			<h1 className="text-center font-bold text-4xl mb-6">
				Create a Question!
			</h1>
			<form
				onSubmit={HandleSubmit}
				className="bg-amber-100 flex flex-col justify-center  items-center px-4 py-2  ">
				<div className="mb-4">
					<label htmlFor="Question Head" className=" block mx-4">
						Question
					</label>
					<textarea
						rows={4}
						cols={40}
						id="Question Head"
						name="Question"
						placeholder="Enter the Question:"
						className="  my-1 px-2 py-1 "
						onChange={(e) => {
							setHead(e.target.value);
						  }}
					/>
					{error.Head && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.Head}
						</p>
					)}
				</div>
				<div>
					<label htmlFor="Choice 1" className="  mx-4 align-center ">
						Choice1
					</label>
					<input
						type="text"
						id="Choice1"
						name="Choice"
						placeholder="Enter Choice 1 :"
						onChange={(e) => {
							setchoice1(e.target.value);
						}}
						className="my-1 px-2 py-1"
					/>
					{error.choice1 && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.choice1}
						</p>
					)}
				</div>
				<div>
					<label htmlFor="Choice 2" className="  mx-4 align-center ">
						Choice2
					</label>
					<input
						type="text"
						id="Choice2"
						name="Choice"
						placeholder="Enter Choice 2 :"
						onChange={(e) => {
							setchoice2(e.target.value);
						}}
						className="my-1 px-2 py-1"
					/>
					{error.choice2 && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.choice2}
						</p>
					)}
				</div>{" "}
				<div>
					<label htmlFor="Choice 3" className="  mx-4 align-center ">
						Choice3
					</label>
					<input
						type="text"
						id="Choice3"
						name="Choice"
						placeholder="Enter Choice 3 :"
						onChange={(e) => {
							setchoice3(e.target.value);
						}}
						className="my-1 px-2 py-1"
					/>
					{error.choice3 && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.choice3}
						</p>
					)}
				</div>
				<div>
					<label htmlFor="Choice 4" className="  mx-4 align-center ">
						Choice4
					</label>
					<input
						type="text"
						id="Choice4"
						name="Choice"
						placeholder="Enter Choice 4 :"
						onChange={(e) => {
							setchoice4(e.target.value);
						}}
						className="my-1 px-2 py-1"
					/>
					{error.choice4 && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.choice4}
						</p>
					)}
				</div>
				<div className="mb-4">
					<label htmlFor="Answer" className="  mx-4 align-center ">
						Answer
					</label>
					<input
						type="text"
						id="Choice4"
						name="Choice"
						placeholder="Enter no of Choice whose the answer"
						onChange={(e) => {
							let cond = e.target.value;
							if (cond > 0 && cond < 5) setAnswer(cond);
						}}
						className="my-1 px-2 py-1"
					/>
					{error.answer && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.answer}
						</p>
					)}
				</div>
				<button className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto">
					Create 
				</button>
			</form>
		</div>
	);
};

export default CreateQuestion;
