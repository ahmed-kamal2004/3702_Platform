import React, { useState } from "react";
import Comment from "./Comment";
import classNames from "classnames";
const Article = (props) => {
	const [upVote, setUpVote] = useState(false);
	const [downVote, setdownVote] = useState(false);
  const[showComments,setShowComments]=useState(false);	
  return (
		<div className="border-4 rounded-lg bg-[#f5f5f5] text-[#333] px-4 ">
			<nav className="flex flex-row py-4 items-center">
				<img
					src={props.img}
					className="w-20 h-20 rounded-full mx-4"
					alt={`${props.Author}'s Photo`}
				/>
				<h3 className=" text-md font-extralight mx-2">{props.Author}</h3>
				<h3 className=" text-md font-extralight mx-2">{props.Date}</h3>
			</nav>
			<hr className="border-1 border-[#333]" />
			<main>
				<h1 className="text-3xl font-bold px-8 py-4">{props.Title}</h1>
				<p className="text-justify py-4 px-8">{props.text}</p>
				<figure className="flex flex-col items-center w-50% my-3 ">
				<img src={props.img} alt='Article Photo' className="block w-70% border rounded-md"/>
				</figure>
			</main>
			<footer>
				<div className="flex flex-row justify-around mb-3">
					<h3>Upvotes:{props.Upvotes+upVote}</h3>
					<h3>Downvotes:{props.Downvotes+downVote}</h3>
					<h3>Comments:{props.Comments}</h3>
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
					<button className="w-1/3 border border-l-2 rounded-lg py-2 hover:border-black hover:bg-slate-300" onClick={(e)=>{
					setShowComments(!showComments);
					}}>
						Comments
					</button>
				</div>
        <div className={classNames("flex flex-col items-start mt-4",{'hidden':!showComments})}>
						{/* <Comment Author={"Ahmed Mostafa"} text={`И пусть меня никто не нашёл бы
Клянусь, мне так плевать на твои слова
Сам по себе, сам за себя
Я как Томас Шелби, но с грустью так и шёл бы
И пусть меня никто не нашёл бы
Клянусь, мне так плевать на твои слова
Сам по себе я

[Куплет 1]
Я останусь собой, нет, я не стану другим
Неважно, сколько мне лет, пойми, внутри я погиб
Перепутали пути с тобой, родная
Внутри меня идёт война, fire-fire
Пойми, что мы с тобою в эпицентре войны
Вместе, но одни, над моею головою дуло пистолета
Сегодня есть я, а завтра нету

[Припев]
Я как Томас Шелби всё с грустью так же шёл бы
И пусть меня никто не нашёл бы
Клянусь, мне так плевать на твои слова
Сам по себе, сам за себя
Я как Томас Шелби, но с грустью так и шёл бы
И пусть меня никто не нашёл бы
Клянусь, мне так плевать на твои слова
Сам по себе я
You might also like
Вахтерам (Vahteram)
Бумбокс (Bumboks)
На Титанике (On the Titanic)
INSTASAMKA & Лолита (Lolita)
Lo Siento
Big Baby Tape
[Куплет 2]
А ты так мило смотришь на меня
Заворожила меня своим голосом
Как жаль, что ты ядовитая змея
Но ты разбила сердце Томасу
Перепутали пути с тобой, родная
Скажи мне: «Fire-fire». Но в меня стреляют
Убегай, уходи, между нами дожди
Я останусь один и снова

[Припев]
Я как Томас Шелби всё с грустью так же шёл бы
И пусть меня никто не нашёл бы
Клянусь, мне так плевать на твои слова
Сам по себе, сам за себя
Я как Томас Шелби, но с грустью так и шёл бы
И пусть меня никто не нашёл бы
Клянусь, мне так плевать на твои слова
Сам по себе я

[Аутро]
Я как Томас Шелби всё с грустью так же шёл бы
И пусть меня никто не нашёл бы
Клянусь, мне так плевать на твои слова
Сам по себе, сам за себя
Я как Томас Шелби, но с грустью так и шёл бы
И пусть меня никто не нашёл бы
Клянусь, мне так плевать на твои слова
Сам по себе я`} />
						<Comment Author={"new_pro125"} text={"FUCK,SOCIETY ;<"} /> */}
						{/**here comes the comments section */}
        </div>
			</footer>
		</div>
	);
};

export default Article;
