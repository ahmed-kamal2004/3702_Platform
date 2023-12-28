import React, { useState } from "react";
import axios from "axios";
import {useNavigate} from 'react-router-dom'
const SignUp = () => {
	const [Type, setType] = useState("Student");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [email, setEmail] = useState("");
	const [nickname, setNickname] = useState("");
	const [phoneNumber, setPhoneNumber] = useState("");
	const [birthdate, setBirthdate] = useState("");
	const [linkedinUrl, setlinkedinUrl] = useState("");
	const [Job, setJob] = useState("Software Engineer");
	const [profilePhoto, setProfilePhoto] = useState(null);
	const [errors, setErrors] = useState({});
	const [valid, setValid] = useState(false);
	const navigate=useNavigate();
	const telephoneCheck=(str)=>{
		let regex = /^\d{11}$/;
		if (regex.test(str)) {
			return true;
		} else {
			return false;
		}
	}
	const jobOptions = [
		"Software Engineer",
		"Web Developer",
		"Data Analyst",
		"Product Manager",
		"Graphic Designer",
		"Marketing Specialist",
		"Accountant",
		"Project Manager",
		"Sales Representative",
		"Human Resources Manager",
	];
	const handleSubmit = (e) => {
		e.preventDefault();

		// Validate form data
		const errors = {};
		if (!username) {
			errors.username = "Username is required";
		}
		if (!password) {
			errors.password = "Password is required";
		}
		if (!email) {
			errors.email = "Email is required";
		}
		if (!nickname) {
			errors.nickname = "Nickname is required";
		}
		if (!phoneNumber) {
			errors.phoneNumber = "Phone number is required";
		}
		if (!birthdate) {
			errors.birthdate = "Birthdate is required";
		}
		if (!profilePhoto) {
			errors.profilePhoto = "Profile photo is required";
		}
		if (!linkedinUrl && Type == "Publisher")
			errors.linkedinUrl = "Linkedin URL is required";
		if(!telephoneCheck(phoneNumber))
			errors.phoneNumber="Phone number is not valid"
		setErrors(errors);

		// Submit the form if there are no errors
		if (Object.keys(errors).length === 0) {
			if (Type == "Student") {
				axios
					.post("http://127.0.0.1:8000/stu/stu-sign-up/", {
						username: username,
						email: email,
						password: password,
						DOB: birthdate,
						nickname: nickname,
						phonenumber: phoneNumber,
						photo: profilePhoto,
					})
					.then(
						(response) => {
							navigate("/SignIn");
						},
						(error) => {
							console.log(error.response)
							if(error.response.data.detail=="Username in Use")
								errors.username="Username in Use";
							else
								errors.email="Email in Use";
							setErrors(errors);	
						}
					);
			} else {
				// console.log({
				//      'username':username,'email':email,'password':password,'DOB':birthdate,'nickname':nickname,'phonenumber':phoneNumber,"linked_url":linkedinUrl,"job":Job
				//    })
				axios
					.post("http://127.0.0.1:8000/pub/pub-sign-up/", {
						username: username,
						email: email,
						password: password,
						DOB: birthdate,
						nickname: nickname,
						phonenumber: phoneNumber,
						linked_url: linkedinUrl,
						job: Job,
						photo: profilePhoto,
					})
					.then(
						(response) => {
							navigate("/SignIn");
						},
						(error) => {
							console.log(error.response)
							if(error.response.data.detail==="Username in Use")
							errors.username="Username in Use";
							else
							errors.email="Email in Use";
						setErrors(errors);	
						}
					);
			}
		}
	};
	const typeDetector = (e) => {
		setType(e.target.id);
	};
	return (
		<div className="bg-amber-100 p-10">
			<div className="flex  flex-row  justify-between m-0 min-w-full  ">
				<h1 className=" text-2xl md:grow-1 uppercase font-extrabold underline underline-offset-[5px] decoration-2">
					# 3702_Platform
				</h1>
				<hr className="w-2 h-2 text-black" />
			</div>
			<div className=" flex flex-col items-center m-8">
				<h1 className="text-xl">Choose who're you?</h1>
				<div>
					<button
						className="border border-black rounded-md bg-white  px-4 py-2 mx-4 my-2"
						id="Student"
						onClick={typeDetector}>
						Student
					</button>
					<button
						className="border border-black rounded-md bg-white  px-4 py-2 mx-4 my-2"
						id="Publisher"
						onClick={typeDetector}>
						Publisher
					</button>
				</div>
			</div>
			<div className="max-w-md mx-auto my-12 ">
				<h2 className="text-2xl font-bold mb-4">Sign Up</h2>
				<form onSubmit={handleSubmit}>
					<div className="mb-4">
						<label htmlFor="username" className="block font-medium mb-1">
							Username
						</label>
						<input
							type="text"
							id="username"
							value={username}
							onChange={(e) => setUsername(e.target.value)}
							className={`w-full p-2 border ${
								errors.username ? "border-red-500" : "border-gray-300"
							} rounded`}
						/>
						{errors.username && (
							<p className="text-red-500 text-sm mt-1">{errors.username}</p>
						)}
					</div>
					<div className="mb-4">
						<label htmlFor="password" className="block font-medium mb-1">
							Password
						</label>
						<input
							type="password"
							id="password"
							value={password}
							onChange={(e) => setPassword(e.target.value)}
							className={`w-full p-2 border ${
								errors.password ? "border-red-500" : "border-gray-300"
							} rounded`}
						/>
						{errors.password && (
							<p className="text-red-500 text-sm mt-1">{errors.password}</p>
						)}
					</div>
					<div className="mb-4">
						<label htmlFor="email" className="block font-medium mb-1">
							Email
						</label>
						<input
							type="email"
							id="email"
							value={email}
							onChange={(e) => setEmail(e.target.value)}
							className={`w-full p-2 border ${
								errors.email ? "border-red-500" : "border-gray-300"
							} rounded`}
						/>
						{errors.email && (
							<p className="text-red-500 text-sm mt-1">{errors.email}</p>
						)}
					</div>
					<div className="mb-4">
						<label htmlFor="nickname" className="block font-medium mb-1">
							Nickname
						</label>
						<input
							type="text"
							id="nickname"
							value={nickname}
							onChange={(e) => setNickname(e.target.value)}
							className={`w-full p-2 border ${
								errors.nickname ? "border-red-500" : "border-gray-300"
							} rounded`}
						/>
						{errors.nickname && (
							<p className="text-red-500 text-sm mt-1">{errors.nickname}</p>
						)}
					</div>
					<>
						{Type == "Publisher" ? (
							<>
								<div className="mb-4">
									<label
										htmlFor="linkedinUrl"
										className="block font-medium mb-1">
										LinkedinURL
									</label>
									<input
										type="text"
										id="linkedinUrl"
										value={linkedinUrl}
										onChange={(e) => setlinkedinUrl(e.target.value)}
										className={`w-full p-2 border ${
											errors.linkedinUrl ? "border-red-500" : "border-gray-300"
										} rounded`}
									/>
									{errors.linkedinUrl && (
										<p className="text-red-500 text-sm mt-1">
											{errors.linkedinUrl}
										</p>
									)}
								</div>
								<div className="mb-4">
									<div className="w-64">
										<label htmlFor="job" className="block font-medium mb-1">
											Job
										</label>
										<select
											id="job"
											className={`w-full p-2 border ${
												errors.Job ? "border-red-500" : "border-gray-300"
											} rounded`}
											onChange={(e) => {
												setJob(e.target.value);
											}}>
											{errors.Job && (
												<p className="text-red-500 text-sm mt-1">
													{errors.Job}
												</p>
											)}
											{jobOptions.map((job, index) => (
												<option key={index} value={job}>
													{job}
												</option>
											))}
										</select>
									</div>
								</div>
							</>
						) : null}
					</>
					<div className="mb-4">
						<label htmlFor="phoneNumber" className="block font-medium mb-1">
							Phone Number
						</label>
						<input
							type="text"
							id="phoneNumber"
							value={phoneNumber}
							// pattern='\\d{4}\\d{3}\d{4}'
							onChange={(e) => setPhoneNumber(e.target.value)}
							className={`w-full p-2 border ${
								errors.phoneNumber ? "border-red-500" : "border-gray-300"
							} rounded`}
						/>
						{/* {isValid ? (
        <p style={{ color: 'green' }}>Valid phone number!</p>
      ) : (
        <p style={{ color: 'red' }}>Please enter a valid phone number (###-###-####).</p>
      )} */}
						{errors.phoneNumber && (
							<p className="text-red-500 text-sm mt-1">{errors.phoneNumber}</p>
						)}
					</div>
					<div className="mb-4">
						<label htmlFor="birthdate" className="block font-medium mb-1">
							Birthdate
						</label>
						<input
							type="date"
							id="birthdate"
							//value={birthdate}
							onChange={(e) => setBirthdate(e.target.value)}
							className={`w-full p-2 border ${
								errors.birthdate ? "border-red-500" : "border-gray-300"
							} rounded`}
						/>
						{errors.birthdate && (
							<p className="text-red-500 text-sm mt-1">{errors.birthdate}</p>
						)}
					</div>
					<div className="mb-4">
						<label htmlFor="profilePhoto" className="block font-medium mb-1">
							Profile Photo URL
						</label>
						<input
							type="text"
							id="profilePhoto"
							onChange={(e) => setProfilePhoto(e.target.value)}
							className={`w-full p-2 border ${
								errors.profilePhoto ? "border-red-500" : "border-gray-300"
							} rounded`}
						/>
						{errors.profilePhoto && (
							<p className="text-red-500 text-sm mt-1">{errors.profilePhoto}</p>
						)}
					</div>
					<button
						type="submit"
						className="bg-black text-white px-4  py-2 rounded-md">
						Sign Up
					</button>
				</form>
			</div>
		</div>
	);
};

export default SignUp;
