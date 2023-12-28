import React from "react";
import {Link} from "react-router-dom"
export const Home = () => {
	return (
		<div className="bg-amber-100">
			<div className="h-full flex flex-col  items-center justify-center py-24">
				<h1 className="text-6xl font-bold w-[40rem] text-center m-4">
					Unlock your Potential with us
				</h1>
				<h3 className="text-xl m-2">
					Discover new opportunities and grow with our innovative education
					platform
				</h3>
				<button className="bg-black text-white py-2 px-4 m-2 rounded-md">
					<Link to="/SignUp/">Join Now</Link>
				</button>
			</div>
			<div className="h-[40vh] flex flex-row items-center justify-start py-[24rem] px-10">
				<div className="pr-8">
					<h1 className="text-3xl font-semibold">About us</h1>
					<p className="text-xl font-light my-4">
						At 3702_Platform, we are dedicated to revolutionizing education. Our
						mission is to provide innovative solutions that empower students and
						educators alike.
					</p>
					<p className="text-xl font-light">
						With a team of experienced professionals, we strive to create a
						dynamic learning environment where knowledge is accessible to all.
						Through our cutting-edge technology and comprehensive resources, we
						aim to inspire a love for learning and foster personal growth.
					</p>
				</div>
				<img
					alt="group of fresh graduates students throwing their academic hat in the air"
					src="https://images.unsplash.com/photo-1523050854058-8df90110c9f1"
					className="block w-[64rem] h-[20rem] border rounded-xl border-amber-100 blur-0"
				/>
			</div>
			
				<div className="flex flex-row gap-10 p-8 justify-around">
					<div>
						<div>
							<img
								alt="Дфзещз"
								src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3"
								className="block w-[64rem] h-[20rem] border rounded-xl border-amber-100 blur-0"
							/>
							<h2 className="text-center text-2xl font-medium">
								Tutoring for all subjects
							</h2>
							<p className="text-center text-sm font-light">
								Our expert tutors provide personalized help in all subjects to
								ensure your academic success.
							</p>
						</div>
					</div>
					<div>
						<div>
							<img
								alt="Books"
								src="https://images.unsplash.com/photo-1577896851231-70ef18881754"
								className="block w-[64rem] h-[20rem] border rounded-xl border-amber-100 blur-0"
							/>
							<h2 className="text-center text-2xl font-medium">
								Test prep assistance
							</h2>
							<p className="text-center text-sm font-light">
								Prepare for exams with our comprehensive test prep programs
								designed to maximize your scores.
							</p>
						</div>
					</div>
				</div>
			<div className="h-[40vh] flex flex-row justify-start p-6 m-6 mb-0 gap-4">
				<div className="">
                    <h1 className="font-bold text-4xl m-2">Online Learning Platform</h1>
				    <p className="font-light text-medium px-2 my-4 w-2/3">Access our comprehensive online learning platform designed to provide high-quality education to students of all ages. With interactive lessons, engaging activities, and skilled instructors, our platform offers a flexible and effective way to enhance learning outcomes.</p>
                    <button className="bg-black text-white px-4  py-2 rounded-md"><Link to="/Explore/">Explore</Link></button>
                </div>
				<img
					alt="O"
					src="https://images.unsplash.com/photo-1503676260728-1c00da094a0b"
					className="block w-[64rem] h-[20rem] border rounded-xl border-amber-100 blur-0 pl-7 mb-10"
				/>
			</div>
		</div>
	);
};
export default Home;
