import React from 'react'
import { InputProps } from './Input.type'

function Input({id,className,...props}:InputProps) {
  return (
    <label htmlFor={id} className='' >
        <input {...props} className={`py-2 px-4 outline-none border-primary  border-2 rounded-tl-md rounded-bl-md ${className}`} id={id} />
    </label>
  )
}

export default Input