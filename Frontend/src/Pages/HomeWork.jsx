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
import ExploreChannels from './ExploreChannels'
const HomeWork = () => {
  return (
    <div className="bg-amber-100  ">
        <ChannelLayout/>
        <ExploreChannels/>
        {/* <Article/> */}
        {/* <CreateDicussion/> */}
          {/* <Poll Author={"Ahmed Mostafa"} Date={"20-2-2011"} text={"lk;jhgfdryetuiokjnm"}/> */}
        {/* <Question Qtext={'Hello,World'} choices={[1,2,3,4]} is_last={false}/> */}
        {/* <Discussion Author={'Ahmed Mostafa'} Date={'12/12/2021'} Title={'Hello,World'} text={`
        [Текст песни «Томас Шелби»] [Припев]
         как Томас Шелби всё с грустью так же шёл бы
         пусть меня никто не нашёл бы
        лянусь, мне так плевать на твои слова
        ам по себе, сам за себя
         как Томас Шелби, но с грустью так и шёл бы
         пусть меня никто не нашёл бы
        лянусь, мне так плевать на твои слова
        ам по себе я
          
        Куплет 1]
         останусь собой, нет, я не стану другим
        еважно, сколько мне лет, пойми, внутри я погиб
        ерепутали пути с тобой, родная
        нутри меня идёт война, fire-fire
        ойми, что мы с тобою в эпицентре войны
        месте, но одни, над моею головою дуло пистолета
        егодня есть я, а завтра нету
          
        Припев]
         как Томас Шелби всё с грустью так же шёл бы
         пусть меня никто не нашёл бы
        лянусь, мне так плевать на твои слова
        ам по себе, сам за себя
         как Томас Шелби, но с грустью так и шёл бы
         пусть меня никто не нашёл бы
        лянусь, мне так плевать на твои слова
        ам по себе я
        ou might also like
        ахтерам (Vahteram)
        умбокс (Bumboks)
        а Титанике (On the Titanic)
        NSTASAMKA & Лолита (Lolita)
        o Siento
        ig Baby Tape
        Куплет 2]
         ты так мило смотришь на меня
        аворожила меня своим голосом
        ак жаль, что ты ядовитая змея
        о ты разбила сердце Томасу
        ерепутали пути с тобой, родная
        кажи мне: «Fire-fire». Но в меня стреляют
        бегай, уходи, между нами дожди
         останусь один и снова
          
        Припев]
         как Томас Шелби всё с грустью так же шёл бы
         пусть меня никто не нашёл бы
        лянусь, мне так плевать на твои слова
        ам по себе, сам за себя
         как Томас Шелби, но с грустью так и шёл бы
         пусть меня никто не нашёл бы
        лянусь, мне так плевать на твои слова
        ам по себе я
          
        Аутро]
         как Томас Шелби всё с грустью так же шёл бы
         пусть меня никто не нашёл бы
        лянусь, мне так плевать на твои слова
        ам по себе, сам за себя
         как Томас Шелби, но с грустью так и шёл бы
         пусть меня никто не нашёл бы
        лянусь, мне так плевать на твои слова
        ам по себе я`} Comments={120} Articles={['AHmes','Beronulli trials','Cars']}/> */}
        <Footer/>
    </div>
  )
}

export default HomeWork