import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./index.css";
import Navbar from "./Pages/Navbar";
import Home from "./Pages/Home";
import SignIn from "./Pages/SignIn";
import {
	createBrowserRouter,
	createRoutesFromElements,
	Routes,
	Route,
	RouterProvider,
} from "react-router-dom";
import SignUp from "./Pages/SignUp";
import UserLayout from "./Components/UserLayout";
import Student from "./Pages/Student";
import Channels from "./Pages/Channels";
import HomeWork from "./Pages/HomeWork";
import Question from "./Components/Question";
import Article from "./Components/Article";
import Discussion from "./Components/Discussion";
import Quiz from "./Pages/Quiz";
import Problemset from "./Pages/Problemset";
import ExploreChannels from "./Pages/ExploreChannels";
import ChannelLayout from "./Components/ChannelLayout";
import Authentication from "./Components/Authentication";
import Publisher from "./Pages/Publisher";
import CreateChannel from "./Components/CreateChannel";
function App() {
	const router = createBrowserRouter(
		createRoutesFromElements(
			<>
				<Route path="/" element={<Navbar />}>
					<Route index element={<Home />} />
				</Route>
				<Route path="SignUp" element={<SignUp />} />
				<Route path="SignIn" element={<SignIn />} />
				{/** to edit the routes to become  */}
				<Route element={<Authentication />}>
					<Route path="Student/:username" element={<UserLayout />}>
						<Route index element={<Student />} />
					</Route>
					<Route path="Publisher/:username" element={<UserLayout />}>
						<Route index element={<Publisher />} />
					</Route>
					<Route path="Channels/:id" element={<Channels />}>
						<Route path="HomeWork/:id1" element={<HomeWork />} />
						<Route path="Question/:id2" element={<Question />} />
						<Route path="Articles/:id3" element={<Article />} />
						<Route path="Dicussion/:id4" element={<Discussion />} />
						<Route path="Quiz/:id5" element={<Quiz />} />
						<Route path="Problemset/:id6" element={<Problemset />} />
					</Route>
					<Route
						path="/Explore"
						element={
							<>
								<ChannelLayout />
								<ExploreChannels />
							</>
						}
					/>
          <Route path="/create-channels/" element={<><ChannelLayout/><CreateChannel/></>} />
				</Route>
			</>
		)
	);
	return <RouterProvider router={router} />;
}

export default App;
