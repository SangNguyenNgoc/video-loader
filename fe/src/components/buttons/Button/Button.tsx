import React from 'react'
import { ButtonProps } from './Button.type'
import { Link } from 'react-router-dom'

function Button({ className, children, to, ...props }: ButtonProps) {
    if (to) {
        return (
            <Link
                to={to}
                replace
                className={`inline-block rounded-br-md rounded-tr-md border-2 border-primary bg-primary px-8 py-2 text-white ${className}`}
            >
                {children}
            </Link>
        )
    }

    return (
        <button
            {...props}
            className={`rounded-br-md rounded-tr-md border-2 border-primary bg-primary px-8 py-2 text-white ${className}`}
        >
            {children}
        </button>
    )
}

export default Button
