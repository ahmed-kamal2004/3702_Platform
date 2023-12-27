import React,{useState} from "react";
import classNames from "classnames";
import Comment from "./Comment";
const Discussion = (props) => {
	const [showComments, setShowComments] = useState(false);
	const [Comments, setComments] = useState("");
	const [addcomment, setaddcomment] = useState(false);
	const [errors, seterrors] = useState([]);
	const HandleSubmit = (e) => {
		e.preventDefault();
		const errors = {};
		if (Comments.length == 0) errors.Comments = "Comment can't be empty";
		seterrors(errors);
		if (Object.keys(errors).length == 0) {
			console.log({ Comments });
		}
	};
	return (
		<div className="border-4 rounded-lg bg-[#f5f5f5] text-[#333] px-4 ">
			<nav className="flex flex-row py-4 items-center">
				<h3 className=" text-md font-extralight mx-2">{props.Author}</h3>
				<h3 className=" text-md font-extralight mx-2">{props.Date}</h3>
			</nav>
			<hr className="border-1 border-[#333]" />
			<main>
				<h1 className="text-3xl font-bold px-8 py-4">{props.Title}</h1>
				<div>
                    <h1 className="text-3xl font-semibold px-8 py-1">Related Articles:</h1>
                    <br />
					{props.Articles.map((Article, index) => (
						<div key={index} className=" inline-block font-medium mx-3 px-6 py-1">
							{Article}
						</div>
					))}
                    <span></span>
				</div>

                <p className="text-justify py-4 px-8">{props.text}</p>
			</main>
			<footer>
				<div className="flex flex-row justify-around mb-3">
					<h3>Comments:{props.Comments}</h3>
				</div>
				<div className="flex flex-row justify-around">
				<button
						className="w-full border border-l-2 rounded-lg py-2 hover:border-black hover:bg-slate-300"
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
					<Comment
						Author={"Ahmed Mostafa"}
						text={`И пусть меня никто не нашёл бы
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
Сам по себе я`}
					/>
					<Comment Author={"new_pro125"} text={"FUCK,SOCIETY ;<"} />
					{/**here comes the comments section */}
					<div>
						<form onSubmit={HandleSubmit}>
							<div className="mb-4">
								<label
									htmlFor="Comments"
									className={classNames("block font-medium mb-1", {
										hidden: !addcomment,
									})}>
									<input
										type="text"
										id="Comments"
										value={Comments}
										onChange={(e) => setComments(e.target.value)}
										className={`w-full p-2 border rounded`}
									/>
									<button
										className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto"
										onClick={(e) => {
											setComments(e.target.value);
											setaddcomment(false);
											HandleSubmit(e);
										}}>
										Submit
									</button>
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

export default Discussion;
