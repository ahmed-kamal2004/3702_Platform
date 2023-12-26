import React,{useState} from 'react'
import axios from 'axios'
const SignIn = () => {
  const [type, setType] = useState('Student')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [errors, setErrors] = useState({})
    const [valid,setValid]=useState(false)  
    const typeDetector=(e)=>{
    setType(e.target.id);
    }
    const handleSubmit=(e)=>{
        e.preventDefault();
       
        const errors = {};
    if (!username) {
      errors.username = 'Username is required';
    }
    if (!password) {
      errors.password = 'Password is required';}
       // Submit the form if there are no errors
    if (Object.keys(errors).length === 0) {
        // Perform form submission
        if(type=='Student'){
      axios.post('http://127.0.0.1:8000/login/stu', {
      "username": username,
      "password": password
    })
    .then((response) => {
      //setValid(response.data.data)
      console.log(response.data);
    }, (error) => {
     console.log(error.response);
    });
    }  
    else{
      axios.post('http://127.0.0.1:8000/login/pub', {
      "username": username,
      "password": password
    })
    .then((response) => {
      //setValid(response.data.data)
      console.log(response.data);
    }, (error) => {
     console.log(error.response);
    });
    }
    }
  }
    return (
    <div className=" bg-amber-100 p-10 h-[100vh]">
        <div className="flex  flex-row  justify-between mb-12 min-w-full ">
    <h1 className=" text-2xl md:grow-1 uppercase font-extrabold underline underline-offset-[5px] decoration-2">
        # 3702_Platform
    </h1>
    <hr className="w-2 h-2 text-black"/>
    </div>
        <div className="text-center text-4xl m-4">{type=='Student'?<h1>Student&apos;s Sign In</h1>:<h1>Publisher&apos;s Sign In</h1>}</div>
        
        <div className=" flex flex-col items-center m-8">
        <h1 className="text-xl">Choose who're you?</h1>
        <div>
        <button className="border border-black rounded-md bg-white  px-4 py-2 mx-4 my-2" id="Student" onClick={typeDetector}>Student</button>
        <button className="border border-black rounded-md bg-white  px-4 py-2 mx-4 my-2" id="Publisher" onClick={typeDetector}>Publisher</button>
        </div>
        </div>

        <div className="max-w-md mx-auto my-12 ">
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="username" className="block font-medium mb-1">
            Username
          </label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className={`w-full p-2 border ${
                errors.username ? 'border-red-500' : 'border-gray-300'
            } rounded`}
          />
          {errors.username && (
              <p className="text-red-500 text-sm mt-1">{errors.username}</p>
              )}
        </div>
        <div className="mb-4">
          <label htmlFor="password" className="block font-medium mb-1">
            Password
          </label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className={`w-full p-2 border ${
                errors.password ? 'border-red-500' : 'border-gray-300'
            } rounded`}
            />
          {errors.password && (
              <p className="text-red-500 text-sm mt-1">{errors.password}</p>
              )}
              </div>
              <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded"
          >
           {valid? "Succuessful Login":"Sign In"}
        </button>
              </form>
        </div>
        </div>

  )
}

export default SignIn