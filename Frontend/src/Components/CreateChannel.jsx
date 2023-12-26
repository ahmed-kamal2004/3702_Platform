import React, { useState } from "react";

const CreateChannel = () => {
	const [ChannelName, setChannelName] = useState("");
	const [ChannelDescription, setChannelDescription] = useState("");
	const [ChannelType, setChannelType] = useState("Public");
	const [keywords, setKeywords] = useState([]);
	const [error, seterrors] = useState([]);
	const options = ["Public", "Private"];
	const HandleSubmit = (e) => {
		e.preventDefault();
		const errors = {};
		if (!ChannelName) {
			errors.ChannelName = "Channel Name is required";
		}
		if (!ChannelDescription) {
			errors.ChannelDescription = "Channel Description is required";
		}
		if (keywords.length == 0) {
			errors.keywords = "keywords are required";
		}
		seterrors(errors);
		if (Object.keys(errors).length === 0) {
			// Submit the form if there are no errors
			let keywordsarr = keywords.split(/[, ]/);
			keywordsarr.filter((word) => word);
			//console.log(keywordsarr);
			const data = {
				ChannelName: ChannelName,
				ChannelDescription: ChannelDescription,
				ChannelType: ChannelType,
				keywords: keywordsarr,
			};
			console.log(data);
		}
	};
	return (
		<div>
			<h1 className="text-center font-bold text-4xl mb-6">Create a Channel!</h1>
			<form
				onSubmit={HandleSubmit}
				className="bg-amber-100 flex flex-col justify-center  items-center px-4 py-2  ">
				<div className="mb-4">
					<label htmlFor="Name" className=" block mx-4">
						Name
					</label>
					<input
						id="Name"
						name="Name"
						placeholder="Enter the Name:"
						className="  my-1 px-2 py-1 "
						onChange={(e) => {
							setChannelName(e.target.value);
						}}
					/>
					{error.ChannelName && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.ChannelName}
						</p>
					)}
				</div>
				<div className="mb-4">
					<div className="w-64">
						<label htmlFor="Type" className="block font-medium mb-1">
							Type
						</label>
						<select
							id="Type"
							className={`w-full p-2 border ${
								error.Type ? "border-red-500" : "border-gray-300"
							} rounded`}
							onChange={(e) => {
								setChannelType(e.target.value);
							}}>
							{error.Type && (
								<p className="text-red-500 text-sm mt-1">{error.Type}</p>
							)}
							{options.map((Type, index) => (
								<option key={index} value={Type}>
									{Type}
								</option>
							))}
						</select>
					</div>
				</div>
				<div className="mb-4">
					<label htmlFor="Description" className=" block mx-4">
						Description
					</label>
					<textarea
						rows={6}
						cols={60}
						id="Description"
						name="Description"
						placeholder="Enter the Description:"
						className="  my-1 px-2 py-1 "
						onChange={(e) => {
							setChannelDescription(e.target.value);
						}}
					/>
					{error.ChannelDescription && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.ChannelDescription}
						</p>
					)}
				</div>
				<div className="mb-4">
					<label htmlFor="Keywords" className=" block mx-4">
						Keywords
					</label>
					<input
						id="Keywords"
						name="Keywords"
						placeholder="Enter the Keywords:"
						className="  my-1 px-2 py-1 "
						onChange={(e) => {
							setKeywords(e.target.value);
						}}
					/>
					{error.keywords && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.keywords}
						</p>
					)}
				</div>

				<button className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto">
					Create Question
				</button>
			</form>
		</div>
	);
};

export default CreateChannel;
