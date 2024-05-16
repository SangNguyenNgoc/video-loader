import { createBrowserRouter } from 'react-router-dom'
import MainLayout from '../components/layouts/MainLayout'
import Home from '../pages/Home'
import VideoDetail from '../pages/Videos/VideoDetail'
import { videoLoader } from '../pages/Videos/VideoDetail/video.loader'
import {VideoDetailSkeleton} from "../pages/Videos/VideoDetail/VideoDetail.skeleton";

export const AllRoute = createBrowserRouter([
    {
        path: '/',
        element: <MainLayout />,
        children: [
            {
                path: '/',
                element: <Home />,
                children: [
                    {
                        path: '/videos/:video_id',
                        loader: videoLoader,
                        element: <VideoDetail />,
                    },
                ],
            },
        ],
    },
])
