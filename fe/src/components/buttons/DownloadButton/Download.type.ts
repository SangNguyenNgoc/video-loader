export type DownloadButtonProps = {
    downloadUrl: string
    type: 'video' | 'audio' | 'caption'
    // size: number
    resolution?: string
    extension: string
}

export type DownloadButtonTypes = {
    video: {
        icon: React.ReactNode
    }
    audio: {
        icon: React.ReactNode
    }
    caption: {
        icon: React.ReactNode
    }
}
