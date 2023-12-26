import React from 'react'

const Comment = (props) => {
  return (
    <div className="border hover:border-black hover:bg-slate-300 rounded-xl mb-4 mt-1 w-[calc(100vw-3rem)]">
        <h4 className="px-4 py-1 text-sm text-start">{props.Author}</h4>
        <p className="p-4 text-lg">{props.text}</p>
    </div>
  )
}

export default Comment