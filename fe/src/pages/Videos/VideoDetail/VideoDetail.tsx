import React, {Suspense, useState} from 'react'
import { Await, useLoaderData } from 'react-router-dom'
import DownloadButton from '../../../components/buttons/DownloadButton'
import VideoNotFound from './VideoNotFound'
import { IVideo } from '../../../types/video'
import {VideoDetailSkeleton} from "./VideoDetail.skeleton";

function VideoDetail() {
    const { data } = useLoaderData() as { data: IVideo }


    return (
        <Suspense fallback={<VideoDetailSkeleton/>}>
            <Await resolve={data} errorElement={<VideoNotFound />}>
                {(video:IVideo) => {
                    console.log(video);
                    
                    const [thumbnail] = video.formats.filter(format=> format.type.includes('thumbnail')) 
                    const audios = video.formats.filter(format=> (format.url.match('.mp4') && format.type ==="audio"))
                    const videos = video.formats.filter(format=> format.url.match('.mp4')&& format.type !=="audio" )
                    const subtitles = video.formats.filter(format => format.url.match('.txt')) ;
                    
                    return (
                        <>
                            <div className=" container  mt-8 rounded-xl bg-white p-5 shadow-main">
                                <div className="text-center">
                                    <span className="mb-5 inline-block text-center text-5xl font-bold">
                                        {video.name}
                                    </span>{' '}
                                    {/* <span className="text-base font-bold text-gray-500">
                                        (00:00:37)
                                    </span> */}
                                </div>
                                <div className="flex grid-cols-2 gap-x-2.5 md:grid">
                                    <div className="flex items-center flex-col gap-4">
                                        <img
                                            className=" w-1/2 rounded-xl object-contain"
                                            src={thumbnail?.url}
                                            alt=""
                                        />
                                    </div>
                                    <div className="flex flex-col gap-4">
                                        <div className="">
                                            <span className="text-base font-bold">
                                                Download Videos
                                            </span>
                                            <div className="flex mt-2 gap-4 flex-wrap">
                                                {videos.map(video=>

                                                <DownloadButton
                                                key={video.type}
                                                downloadUrl={video.url}
                                                extension="mp4"
                                                resolution={video.type}
                                                type="video"
                                                // size={13.88}
                                                />
                                            )}
                                            </div>
                                        </div>
                                        <div className="">
                                            <span className="text-base font-bold">
                                                Download Audio
                                            </span>
                                            <div className="flex mt-2 gap-4 flex-wrap">
                                            {audios.map(audio=>
                                            <DownloadButton
                                            key={audio.type}
                                            downloadUrl={audio.url}
                                            extension="mp3"
                                            resolution={audio.type}
                                            type="audio"
                                            // size={13.88}
                                            />
                                            )}
                                            </div>
                                        </div>
                                        <div className="">
                                            <span className="text-base font-bold">
                                                Download Caption
                                            </span>
                                            <div className="flex mt-2 gap-4 flex-wrap">
                                            {subtitles?.map(subtitle=>
                                            <DownloadButton
                                            key={subtitle.type}
                                            downloadUrl={subtitle.url}
                                            extension="txt"
                                            resolution={subtitle.type}
                                            type="caption"
                                            // size={13.88}
                                            />
                                            ) || <div>No subtitle</div>}

                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </>
                    )
                }}
            </Await>
        </Suspense>
    )
}

export default VideoDetail
