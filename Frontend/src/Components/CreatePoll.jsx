import React, { useState } from "react";

const CreatePoll = () => {
	const [question, setQuestion] = useState("");
	const [choices, setChoices] = useState([]);
	const [Errors, setErrors] = useState([]);

	const handleQuestionChange = (event) => {
		setQuestion(event.target.value);
	};

	const handleChoiceChange = (index, event) => {
		const newChoices = [...choices];
		newChoices[index] = event.target.value;
		setChoices(newChoices);
	};

	const addChoice = (e) => {
        e.preventDefault();
		setChoices([...choices, ""]);
	};

	const removeChoice = (index) => {
		const newChoices = [...choices];
		newChoices.splice(index, 1);
		setChoices(newChoices);
	};
	const Handlesubmit = (e) => {
		e.preventDefault();
        const Errors={};
		if (question=="")  Errors.question = "Question is required!";
		if(choices.length<2) Errors.choices = "Choices must be more than 2!";
        choices.forEach((choice, index) => {
            if (choice=="") Errors[`choice${index}`] = `Choice can't be empty!`;
		});
		setErrors(Errors);
		if (Object.keys(Errors).length === 0) {
            console.log({question,choices});
			// here is the post request of the
		}
	};
	return (
		<div>
			<form
				
				className="bg-amber-100 flex flex-col justify-center  items-center px-4 py-2  ">
				<div className="mb-4">
					<label>
						Question:
						<input
							type="text"
                            className="  my-1 px-2 py-1 "
							value={question}
							onChange={handleQuestionChange}
						/>
					</label>
					<br />
                    {Errors.question && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{Errors.question}
						</p>
					)}
				</div>
				<label>
					Choices:
					{choices.map((choice, index) => (
						<div key={index}>
							<input
								type="text"
								value={choice}
								onChange={(event) => handleChoiceChange(index, event)}
                                className="  my-1 px-2 py-1 "
							/>
							<button onClick={() => removeChoice(index)} className="border border-black rounded-xl w-24 ml-4 px-4 py-2 hover:bg-black hover:text-white mx-auto">Remove</button>
                            {Errors[`choice${index}`] && (
                                <p className="text-red-500 text-sm mt-1 text-center">
                                    {Errors[`choice${index}`]}
                                </p>
                            )}
						</div>
					))}
				</label>
				<button onClick={addChoice} className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto">Add Choice</button>
                <button className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto" type="submit" onClick={Handlesubmit}>Create</button>
                    {Errors.choices && (
                <p className="text-red-500 text-sm mt-1 text-center">
                    {Errors.choices}
                </p>
            )}
			</form>
		</div>
	);
};
export default CreatePoll;
