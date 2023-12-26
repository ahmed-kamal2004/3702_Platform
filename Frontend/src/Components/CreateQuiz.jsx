import React,{useState} from 'react'

const CreateQuiz = () => {
    const[duration,setduration]=useState(0)
    let[startingdate,setstartingdate]=useState("")
    const[error,seterror]=useState({})
    const HandleSubmit=(e)=>{ 
        e.preventDefault();
        const error={}
        if(!duration) error.duration="Quiz duration Can't be zero"
        if(!startingdate) error.startingdate="Quiz starting date Can't be empty"
        seterror(error)
        startingdate=startingdate.replace("T"," ")
        if(Object.keys(error).length===0){
            console.log({duration,startingdate})
            // here is the post request of the
        }
        // use this please datetime.strptime(date_time_str, "%m/%d/%Y %S:%M:%H")
        return null
    }
    return (
    <div>
			<h1 className="text-center font-bold text-4xl mb-6">Create a Quiz!</h1>
			<form
				onSubmit={HandleSubmit}
				className="bg-amber-100 flex flex-col justify-center  items-center px-4 py-2  ">
				<div className="mb-4">
					
					<label htmlFor="Duration" className=" block mx-4">
                    <input
						id="Duration"
						name="Duration"
						type="number"
                        min='1'
                        max='360'
						className="  my-1 px-2 py-1 "
						onChange={(e) => {
							setduration(e.target.value);
						}}
					/>  Duration in Minutes
					</label>
					{error.duration && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.duration}
						</p>
					)}
				</div>

				<div className="mb-4">
					<label htmlFor="Starting Date" className=" block mx-4">
						Starting Date
					</label>
					<input
                        type="datetime-local"
						id="Starting Date"
						name="Starting Date"
						placeholder="Enter the Starting Date:"
						className="  my-1 px-2 py-1 "
						onChange={(e) => {
							setstartingdate(e.target.value);
						}}
					/>
					{error.startingdate && (
						<p className="text-red-500 text-sm mt-1 text-center">
							{error.startingdate}
						</p>
					)}
				</div>
                            {/** here comes the questions we'll choose from */}
				<button className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto">
					Create 
				</button>
			</form>
    </div>
  )
}

export default CreateQuiz