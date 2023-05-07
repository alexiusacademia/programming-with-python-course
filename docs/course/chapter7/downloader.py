import yt_dlp

class Downloader:
    def __init__(self, url: str):
        self.url = url

    def download(self):
        """
        Download the video.

        Args:
            format_id (str): The format id selected.
        """
        ydl_opts = {
            'format': 'best[ext=mp4]/best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])