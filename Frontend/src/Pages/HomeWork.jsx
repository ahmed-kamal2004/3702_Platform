import React from 'react'
import Question from '../Components/Question'
import ChannelLayout from '../Components/ChannelLayout'
import Footer from '../Components/Footer'
import Article from '../Components/Article'
import CreatePoll from '../Components/CreatePoll'
import CreateQuestion from '../Components/CreateQuestion'
import CreateArticle from '../Components/createArticle'
import CreateDicussion from '../Components/CreateDicussion'
import CreateChannel from '../Components/CreateChannel'
import CreateQuiz from '../Components/CreateQuiz'
import CreatePS from '../Components/CreatePS'
import CreateHW from '../Components/CreateHW'
import Discussion from '../Components/Discussion'
const HomeWork = () => {
  return (
    <div className="bg-amber-100  ">
        <ChannelLayout/>
        {/* <Article/> */}
        {/* <CreateDicussion/> */}
          {/* <Poll Author={"Ahmed Mostafa"} Date={"20-2-2011"} text={"lk;jhgfdryetuiokjnm"}/> */}
        {/* <Question Qtext={'Hello,World'} choices={[1,2,3,4]} is_last={false}/> */}
        <Discussion Author={'Ahmed Mostafa'} Date={'12/12/2021'} Title={'Hello,World'} text={`[Текст песни «Томас Шелби»]

[Припев]
Я как Томас Шелби всё с грустью так же шёл бы
И пусть меня никто не нашёл бы
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
Сам по себе я`} Comments={120} Articles={['AHmes','Beronulli trials','Cars']}/>
        <Footer/>
    </div>
  )
}

export default HomeWork