import React from 'react'
import { DownloadButtonProps, DownloadButtonTypes } from './Download.type'
import {
    ChatBubbleBottomCenterTextIcon,
    MicrophoneIcon,
    VideoCameraIcon,
} from '@heroicons/react/24/solid'

const types = {
    video: {
        icon: VideoCameraIcon,
        bgColor: 'bg-primary',
    },
    audio: { icon: MicrophoneIcon, bgColor: 'bg-[#36d480]' },
    caption: { icon: ChatBubbleBottomCenterTextIcon, bgColor: 'bg-[#FF5E00]' },
}

function DownloadButton({
    downloadUrl,
    resolution,
    // size,
    type,
    extension,
}: DownloadButtonProps) {
    const { icon: IconComponent, bgColor } = types[type]

    return (
        <a
            className={`flex flex-col items-center justify-center rounded-md ${bgColor} px-6 py-3 text-white hover:bg-opacity-80 `}
            href={downloadUrl}
        >
            <span className="font-bold">{resolution}</span>
            <p>
                {/* @ts-ignore */}
                <IconComponent className="inline-block h-4 w-5" />{' '}
                <span>{extension}</span>
            </p>
            {/* <span>({size})</span> */}
        </a>
    )
}

export default DownloadButton
