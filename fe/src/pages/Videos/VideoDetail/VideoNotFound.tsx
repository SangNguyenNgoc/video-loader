import React from 'react'
import { useRouteError } from 'react-router-dom'

function VideoNotFound() {
    const error = useRouteError()
    return (
        <div className="container mt-8 bg-rose-400 p-5  text-center text-rose-700">
            Please input a valid video
        </div>
    )
}

export default VideoNotFound
