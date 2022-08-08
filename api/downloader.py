from yt_dlp import YoutubeDL

def my_hook(d):
    if d['status'] == 'finished':
        name = d['filename']
        print(f'finished. file {name}')

ydl_opts = {      
    'outtmpl': '%(id)s',      
    'progress_hooks': [my_hook],
    #'paths': 'downloads'
}


class Downloader(YoutubeDL):

    def __init__(self):
        super().__init__(ydl_opts)
    
    def getInfo(self,url):
        try:
            info = self.extract_info(url, download=False)
        except:
            return None
        return info

    def getInfoSanatized(self,url):
        try:
            info = self.extract_info(url, download=False)
        except:
            return None
        return self.sanitize_info(info)

    def tryDownload(self,url):
        try:
            return self.download([url])
        except:
            return None
