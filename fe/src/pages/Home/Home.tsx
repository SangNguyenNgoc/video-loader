import React, { useMemo, useState } from 'react'
import Input from '../../components/inputs/Input'
import Button from '../../components/buttons/Button'
import { Outlet } from 'react-router-dom'

const steps = [
    {
        demo: './demo-1.gif',
        title: '1. Paste your link',
        description:
            "Paste your link for us to start searching for your video, after pasting the link, you can initiate the search by clicking on the 'Start Download' button or pressing Enter.",
    },
    {
        demo: '/demo-1.gif',
        title: '2. Choose your video',
        description:
            'Select a format and quality for your video. The format refers to the type of video file you prefer, such as MP4, AVI, or MOV. The quality refers to the resolution of the video, which can range from low (360p) to high definition (720p, 1080p) or even ultra high definition (4K). Once you’ve made your selections, you can proceed with the next step.',
    },
    {
        demo: '/demo-1.gif',
        title: '3. Get your video',
        description:
            'Click on the ‘Download’ button to initiate the download process for your video.  Please note that the download time may vary depending on the size of the video and your internet speed. Enjoy your video! 😊',
    },
]

function Home() {
    const [videoLink, setVideoLink] = useState('')

    function youtube_parser(url: string) {
        const regExp =
            /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/
        const match = url.match(regExp)
        return match && match[7].length == 11 ? match[7] : ''
    }

    const handleOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setVideoLink(e.target.value)
    }

    const handleLink = useMemo(() => youtube_parser(videoLink), [videoLink])

    return (
        <div>
            <div className="flex min-h-[calc(100vh_-_105px)] flex-col items-center justify-center bg-secondary px-8 pb-16 pt-20">
                <h1 className="mb-8 text-5xl font-bold text-[#202020]">
                    Youtube Downloader
                </h1>
                <p className="mb-8 font-semibold text-[#535353]">
                    Download video from to your devices with just some few
                    clicks
                </p>
                <div className="rounded-xl bg-white p-8 shadow-main">
                    <div className="">
                        <Input
                            onChange={handleOnChange}
                            id="video-input"
                            className=" w-[600px] text-lg"
                            placeholder="Paste link here..."
                        />
                        <Button
                            to={`/videos/${handleLink}`}
                            className="text-lg"
                        >
                            Start Download
                        </Button>
                    </div>
                    <div className="mt-1">
                        <p className="text-sm text-[#b0b7bf]">
                            Please provide a valid link
                        </p>
                    </div>
                </div>
                <Outlet />
            </div>
            <div className="flex flex-col items-center gap-16 px-10 py-[120px]">
                <h2 className="text-4xl font-bold">
                    Download your video with{' '}
                    <span className="text-primary  underline">3</span> steps
                </h2>
                <div className="flex grid-cols-3 flex-col md:grid md:gap-x-16">
                    {steps.map((step) => (
                        <div
                            key={step.title}
                            className="flex flex-col items-center gap-6 text-center"
                        >
                            <img src={step.demo} alt="" />
                            <div className="">
                                <h4 className="text-2xl font-bold text-[#05080d]">
                                    {step.title}
                                </h4>
                                <p className="text-lg font-light">
                                    {step.description}
                                </p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Home
