import os
import re
import time
from datetime import datetime

import requests

class FacebookServicde:

    def get_downloadlink(self, video_url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',  # Adjust language preference as needed
            'Referer': 'https://www.facebook.com/',  # The URL of the page that linked to the resource being requested
            'Upgrade-Insecure-Requests': '1',  # Indicates that the client supports a newer version of HTTP
            'DNT': '1',  # Do Not Track setting, indicating the user's preference regarding tracking
            'Connection': 'keep-alive',  # Specifies options that are desired for a particular connection
            'Cache-Control': 'max-age=0',  # Specifies directives for caching mechanisms in both requests and responses
            'Sec-Fetch-Dest': 'document',  # Indicates how a particular type of resource will be used
            'Sec-Fetch-Mode': 'navigate',  # Specifies how a particular resource is fetched
            'Sec-Fetch-Site': 'same-origin',  # Indicates the site of the resource being fetched
            'Sec-Fetch-User': '?1',  # Indicates whether or not user credentials are sent with the request
        }
        response = requests.get(video_url, headers=headers)
        if response.status_code == 200:
            data = response.text
            # Extract SD link
            sd_link_match = re.search(r'browser_native_sd_url":"([^"]+)"', data)
            sd_link = sd_link_match.group(1) if sd_link_match else None
            if sd_link:
                sd_link = sd_link.replace("\\/", "/")  # Replace escaped slashes
            # Extract HD link
            hd_link_match = re.search(r'browser_native_hd_url":"([^"]+)"', data)
            hd_link = hd_link_match.group(1) if hd_link_match else None
            if hd_link:
                hd_link = hd_link.replace("\\/", "/")

            thumbnail_uri_match = re.search(r'"preferred_thumbnail":"(https?:\/\/[^"]+)"', data)
            # print(thumbnail_uri_match)
            thumbnail_uri = thumbnail_uri_match.group(1) if thumbnail_uri_match else None

            return sd_link, hd_link, thumbnail_uri
        else:
            return None, None, None

    def download_FB(self, url):

            # Validates Link and download Video
            # global Url_Val
            # Validating Input
            if not "www.facebook.com" in url:
                return "Lỗi"
            link_sd, link_hd, thumbnail_link = self.get_downloadlink(url)
            filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
            print(thumbnail_link)

            if thumbnail_link:
                self.thumbnail(thumbnail_link, filename)
            if link_sd:
                self.download_link(link_sd, filename + "-sd", ".mp4")
            if link_hd:
                self.download_link(link_hd, filename + "-hd", ".mp4")


    def download_link(self, link, filename, type):
        if link:
            if not os.path.exists("./downloads"):
                os.makedirs("./downloads")
            with requests.get(link, stream=True) as r:
                # name = r.headers.get("content")
                video_file_path = os.path.join("./downloads", filename + type)
                with open(video_file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            time.sleep(0.01)
                    f.close()
        else:
            print("Lỗi")

    def thumbnail(self, link, file_name):

        if not os.path.exists("./thumbnails"):
            os.makedirs("./thumbnails")
        path = os.path.join("./thumbnails", file_name + '.jpg')
        print(path)
        response = requests.get(link)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)
            f.close()
            print("Download successful.")
        else:
            print("Failed to download image.")
        time.sleep(6)

    # def audio_to_text(self, audio_path):
    #     recognizer = sr.Recognizer()
    #     audio = sr.AudioFile(audio_path)
    #
    #     with audio as source:
    #         audio_file = recognizer.record(source)
    #
    #     return recognizer.recognize_google(audio_file)

    # Hàm để tạo phụ đề từ văn bản
    # def create_subtitle(self, text, output_path):
    #     with open(output_path, 'w') as f:
    #         f.write(text)


if __name__ == '__main__':
    facebook_service = FacebookServicde()
    facebook_service.download_FB("https://www.facebook.com/watch?v=3692178374434829")






