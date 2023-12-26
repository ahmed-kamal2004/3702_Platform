import React,{useState} from 'react'

const Question = ({Qtext,choices,is_last}) => {
  const [answer,setanswer]=useState(null);
  const handleSubmit=(e)=>{
    e.preventDefault();
    console.log({Qtext,answer});
}
    return (
    <div className="bg-amber-100">
        <fieldset>
        <form className="flex flex-col items-start px-4 py-8" onSubmit={handleSubmit}>
            <h1 className="text-2xl font-bold mb-4 ">{Qtext}</h1>
            <div><input id='ch1' type='radio' name='Choice' value={choices[0]}  onChange={(e)=>{setanswer(e.target.value)}} /><label htmlFor='ch1' className='px-3 my-6'>{choices[0]}</label></div>
            <div><input id='ch2' type='radio' name='Choice' value={choices[1]}  onChange={(e)=>{setanswer(e.target.value)}} /><label htmlFor='ch2' className='px-3 my-6'>{choices[1]}</label></div>
            <div><input id='ch3' type='radio' name='Choice' value={choices[2]}  onChange={(e)=>{setanswer(e.target.value)}} /><label htmlFor='ch3' className='px-3 my-6'>{choices[2]}</label></div>
            <div><input id='ch4' type='radio' name='Choice' value={choices[3]}  onChange={(e)=>{setanswer(e.target.value)}} /><label htmlFor='ch4' className='px-3 my-6'>{choices[3]}</label></div>
            <button className="bg-black text-white py-2 px-4 rounded-lg my-4" type='submit'>{(!is_last)?'Next':'Submit'}</button>
        </form>
        </fieldset>
    </div>
  )
}

export default Question