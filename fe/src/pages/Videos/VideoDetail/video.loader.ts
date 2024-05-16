import axios from 'axios'
import { LoaderFunctionArgs, defer, json } from 'react-router-dom'

async function getVideo(url?: string) {
    const res = await axios.get(`http://127.0.0.1:8000/?url=https://www.youtube.com/watch?v=${url}`)
    if (res.status === 404) {
        throw json('Not found', { status: 404 })
    }

    return res.data
}

export const videoLoader = ({ params }: LoaderFunctionArgs) => {
    return defer({
        data: getVideo(params.video_id),
    })
}
