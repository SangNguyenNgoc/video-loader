import json
import os
import time
import urllib.request
import uuid
import xml.etree.ElementTree as ET
import zipfile
import re
from fastapi.exceptions import HTTPException
from urllib.parse import urlparse, parse_qs

from pytube import YouTube

from models.Repository import VideoRepository, FormatRepository
from Service.DiscordBot import upload


class YoutubeService:
    videoRepository = VideoRepository()
    formatRepository = FormatRepository()

    @staticmethod
    def sanitize_filename(filename):
        # Thay thế các ký tự không hợp lệ bằng ký tự _
        return re.sub(r'[<>:"/\\|?*]', '_', filename)

    async def download_youtube_video(self, url, id, yt):
        print("Downloading video")
        try:
            streams = yt.streams.all()
            print(streams)
            url_discords = []
            for stream in streams:
                if stream.mime_type == "video/mp4" and stream.resolution and stream.audio_codec:
                    print(stream.mime_type)
                    # Kiểm tra kích thước của video trước khi tải về
                    if stream.filesize_mb <= 25:  # MAX_FILESIZE là kích thước tối đa cho phép
                        if not os.path.exists("./downloads"):
                            os.makedirs("./downloads")
                        video_path = stream.download(output_path="./downloads", filename=str(uuid.uuid4())+".mp4")
                        url_discord = await upload(video_path)
                        self.formatRepository.add_format(stream.resolution, url_discord, id, stream.filesize_mb)
                        print("Download complete")
                        # os.remove(video_path)
                        url_discords.append(url_discord)
                    else:
                        print(f"Video size exceeds the maximum allowed size: {stream.filesize} bytes")
            return url_discords
        except Exception as e:
            print("error: Không tìm thấy" + e.__str__())
            return "error: Không tìm thấy" + e.__str__()

    async def download_youtube_audio(self, url, id, yt):
        try:
            # yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            if not os.path.exists("./downloads"):
                os.makedirs("./downloads")
            video_path = stream.download(output_path="./downloads")
            url_discord = await upload(video_path)
            self.formatRepository.add_format("audio", url_discord, id, stream.filesize_mb)
            return url_discord
        except Exception as e:
            return "error: Không tìm thấy" + e.__str__()

    async def thumbnail(self, url, id, yt):
        sax = yt.thumbnail_url
        file_name = yt.title[:10]
        if not os.path.exists("./thumbnails"):
            os.makedirs("./thumbnails")
        sanitized_file_name = self.sanitize_filename(file_name)
        path = os.path.join("./thumbnails", sanitized_file_name + '.jpg')
        # print(path)
        with open(path, 'wb') as f:
            f.write(urllib.request.urlopen(sax).read())
            f.close()
        print('Image sucessfully Downloaded: ')
        url_discord = await upload(os.path.abspath(path))
        self.formatRepository.add_format("thumbnail", url_discord, id, None)
        time.sleep(6)
        return url_discord

    @staticmethod
    def get_subtitle_tracks(url):
        subtitle_url = None
        with urllib.request.urlopen(url) as response:
            data = response.read()
            pos = data.find(b'"playerCaptionsTracklistRenderer"')
            if pos == -1:
                print("No captions found")
                return 0
            pos = data.find(b':', pos)
            pos += 1

            # Parse until first JSON error
            track_list = None

            def hook(obj):
                nonlocal track_list
                track_list = obj
                return obj

            try:
                json.loads(data[pos:], object_hook=hook)
            except json.JSONDecodeError:
                pass

            return track_list['captionTracks']

    async def download_subtitle(self, url, id):
        tracks = self.get_subtitle_tracks(url)

        if not tracks:
            return

        # for track in tracks:
        #     print(track)

        if not tracks:
            print("No", "captions found")
            return

        def isASR(track):
            return 'kind' in track and track['kind'] == 'asr'

        url_discords = []
        if not os.path.exists("./captions"):
            os.makedirs("./captions")
        for track in tracks:
            with urllib.request.urlopen(track['baseUrl']) as response:
                xml_data = self.xml_to_text(response.read())
            filename = urllib.parse.urlsplit(url).query + (
                "-asr" if isASR(track) else "") + f"-{track['languageCode']}" + ".txt"
            with open(os.path.join("./captions", filename), 'wb') as f:
                f.write(xml_data.encode('utf-8'))
                f.close()
            url_discord = await upload(os.path.abspath(os.path.join("./captions", filename)))
            url_discords.append({'name': track['languageCode'], 'url': url_discord})
            self.formatRepository.add_format("subtitle" + track['languageCode'], url_discord, id, None)
            print("Written", filename, track['languageCode'], "ASR" if isASR(track) else "")
        return url_discords

    @staticmethod
    def xml_to_text(xml_string):
        # Parse XML string
        root = ET.fromstring(xml_string)

        # Initialize an empty list to store text values
        text_list = []

        # Iterate through all text elements and append their values to the list
        for text_elem in root.findall('.//text'):
            text_list.append(text_elem.text)

        # Join all text values into a single string
        text_result = '\n'.join(text_list)

        return text_result

    async def download_video(self, video_url):
        parsed_url = urlparse(video_url)
        # Lấy ra các tham số từ URL
        query_params = parse_qs(parsed_url.query)
        # Trả về tham số 'param' nếu tồn tại
        video_id = query_params.get('v', None)
        print(video_id)
        if video_id is None or "www.youtube.com" not in video_url:
            raise HTTPException(404, "Not Found")
        else:
            video_id = video_id[0]
            video = self.videoRepository.get_video_by_id(video_id)
            if video:
                formats_list = [{'type': format.type, 'url': format.url} for format in video.formats]
                formats_dict = {'id': video.id, 'name': video.name, 'url': video.url, 'formats': formats_list}
                return formats_dict
            yt = YouTube(video_url)
            self.videoRepository.add_video(video_id, yt.title, video_url)
            await self.download_youtube_video(video_url, video_id, yt)
            await self.download_youtube_audio(video_url, video_id, yt)
            await self.thumbnail(video_url, video_id, yt)
            await self.download_subtitle(video_url, video_id)
            new_video = self.videoRepository.get_video_by_id(video_id)
            formats_list = [{'type': format.type, 'url': format.url} for format in new_video.formats]
            formats_dict = {'id': new_video.id, 'name': new_video.name, 'url': new_video.url, 'formats': formats_list}
            return formats_dict
