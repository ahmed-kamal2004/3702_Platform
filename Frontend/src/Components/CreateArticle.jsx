import React,{useState} from 'react'

const CreateArticle = () => {
  const [Head, setHead] = useState(null);
  const [Content, setContent] = useState(null);
  const [Photo, setPhoto] = useState(null);
	const [error,seterror]=useState({});
	const HandleSubmit = (e) => {
	  const errors={};
    if(!Head) errors.Title="Title is required!"	
    if(!Content) errors.Content="Article can't be empty!"	
    if(!Photo) errors.Photo="Photo is required!"	
    e.preventDefault();
		seterror(errors)
    if(Object.keys(errors).length()===0){
      // here is the post request of the
    }
	};
  return (
    <div> 
      <h1 className="text-center font-bold text-4xl mb-6">Create an Article!</h1>
      <form
				onSubmit={HandleSubmit}
				className="bg-amber-100 flex flex-col justify-center  items-center px-4 py-2  ">
				<div className="mb-4">
					<label htmlFor="Article Title" className=" block mx-4">
						Title
					</label>
					<input
						id="Article Title"
						name="Title"
						placeholder="Enter the Title"
						className="  my-1 px-2 py-1 "
					/>
        {error.Title&&<p className="text-red-500 text-sm mt-1 text-center">{error.Title}</p>}
		  	</div>
        <div className="mb-4">
					<label htmlFor="Article Content" className=" block mx-4">
						Content
					</label>
					<textarea
          rows={10}
          cols={80}
						id="Article Content"
						name="Content"
						placeholder="Enter the Content"
						className="  my-1 px-2 py-1 "
						onChange={(e) => {
							setContent(e.target.value);
						  }}
					/>
        {error.Content&&<p className="text-red-500 text-sm mt-1 text-center">{error.Content}</p>}
		  	</div>
        <div className="mb-4">
					<label htmlFor="Article Photo" className=" block mx-4">
						Photo URL
					</label>
					<input
						id="Article Photo"
						name="Photo"
						placeholder="Enter the Photo URL"
						className="  my-1 px-2 py-1 "
					/>
        {error.photo&&<p className="text-red-500 text-sm mt-1 text-center">{error.photo}</p>}
		  	</div>
				<button className="border border-black rounded-xl w-48 my-6 px-4 py-2 hover:bg-black hover:text-white mx-auto">
					Create
				</button>
			</form>

    </div>
  )
}

export default CreateArticle