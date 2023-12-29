import React, { useEffect, useState } from "react";
import Comment from "./Comment";
import classNames from "classnames";
import { useParams } from "react-router-dom";
const Article = (props) => {
	const [upVote, setUpVote] = useState(false);
	const [downVote, setdownVote] = useState(false);
	const [showComments, setShowComments] = useState(false);
	const [Comments, setComments] = useState("");
	const [addcomment, setaddcomment] = useState(false);
	const[errors,seterrors]=useState([]);
	const[data,setdata]=useState([])
	const {id}=useParams();
	useEffect(() => {
		axios
				.get(`http://127.0.0.1:8000/chn/content/articles/${id}`, {
					"token": sessionStorage.getItem("token"),
					"channel_id": id,
				})
				.then((response) => {
					setdata(response.data);
					console.log(response.data);
				})
				.catch((error) => console.log(error));
	},[]);
const HandleSubmit=(e)=>{
	e.preventDefault();
	const errors={};
	if(Comments.length==0) errors.Comments="Comment can't be empty"
	seterrors(errors);
	if(Object.keys(errors).length==0){
		console.log({Comments})
	}
}
	return (
		<div className="border-4 rounded-lg bg-[#f5f5f5] text-[#333] px-4 ">
			<nav className="flex flex-row py-4 items-center">
				<img
					src={dataimg}
					className="w-20 h-20 rounded-full mx-4"
					alt={`${data["Author"]}'s Photo`}
				/>
				<h3 className=" text-md font-extralight mx-2">{data["Author"]}</h3>
				<h3 className=" text-md font-extralight mx-2">{data["Date"]}</h3>
			</nav>
			<hr className="border-1 border-[#333]" />
			<main>
				<h1 className="text-3xl font-bold px-8 py-4">{data["Title"]}</h1>
				<p className="text-justify py-4 px-8">{data["text"]}</p>
				<figure className="flex flex-col items-center w-50% my-3 ">
					<img
						src={data["img"]}
						alt="Article Photo"
						className="block w-70% border rounded-md"
					/>
				</figure>
			</main>
			<footer>
				<div className="flex flex-row justify-around mb-3">
					<h3>Upvotes:{data["Upvotes"] + upVote}</h3>
					<h3>Downvotes:{data["Downvotes"] + downVote}</h3>
					<h3>Comments:{data["Comments"]}</h3>
				</div>
				<div className="flex flex-row justify-around">
					<button
						className="border border-l-2 rounded-lg w-1/3 py-2 hover:border-black hover:bg-slate-300"
						onClick={(e) => {
							if (downVote) {
								setdownVote(false);
							}
							setUpVote(!upVote);
						}}>
						UpVote
					</button>
					<button
						className="border border-l-2 rounded-lg w-1/3 py-2 hover:border-black hover:bg-slate-300"
						onClick={(e) => {
							if (upVote) {
								setUpVote(false);
							}
							setdownVote(!downVote);
						}}>
						DownVote
					</button>
					<button
						className="w-1/3 border border-l-2 rounded-lg py-2 hover:border-black hover:bg-slate-300"
						onClick={(e) => {
							setShowComments(!showComments);
						}}>
						Comments
					</button>
				</div>
				<div
					className={classNames("flex flex-col items-start mt-4", {
						hidden: !showComments,
					})}>
					
					{/**here comes the comments section */}
					{data["Comments"].map((comment, index) => {
						return (
							<Comment
								key={index}
								Author={comment["Author"]}
								Date={comment["Date"]}
								text={comment["text"]}
							/>
						);
					})}
					<div>
						<form onSubmit={HandleSubmit}>
							<div className="mb-4">
								<label htmlFor="Comments" className={classNames("block font-medium mb-1",{"hidden":!addcomment})}>
									<input
										type="text"
										id="Comments"
										value={Comments}
										onChange={(e) => setComments(e.target.value)}
										className={`w-full p-2 border rounded`}
									/>
									<button className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto" onClick={(e)=>{
										setComments(e.target.value);
										setaddcomment(false);
										HandleSubmit(e)
									}} >Submit</button>
								</label>
								{errors.Comments && (
									<p className="text-red-500 text-sm mt-1">{errors.Comments}</p>
								)}
							</div>
						</form>
					</div>
					<button
						className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto"
						onClick={(e) => {
							setaddcomment(true);
						}}>
						AddComment
					</button>
				</div>
			</footer>
		</div>
	);
};

export default Article;
