from yt_dlp import YoutubeDL

class MyLogger():
    def __init__(self) -> None:
        self.last = None

    def debug(self, msg):
        print('i: '+msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        pass
            


def my_hook(d):
    print(d['status'])

def my_post_hook(d):
    print(d['info_dict']['_filename'])

ydl_opts = {      
    'outtmpl': './downloads/%(id)s.%(extractor)s.%(ext)s',      
    'progress_hooks': [my_hook],
    'postprocessor_hooks': [my_post_hook]
}


class Downloader(YoutubeDL):

    def __init__(self):
        super().__init__(ydl_opts)

    def tryInfo(self, url):
        try:
            info = self.extract_info(url, download=False)
        except:
            return None
        return info
    
    def getInfo(self, url):
        return self.tryInfo(url)

    def getInfoSanitized(self,url):
        info = self.tryInfo(url)
        return self.sanitize_info(info)

    def getFilename(self, url):
        info = self.tryInfo(url)
        if info is None:
            return ""
        return f"{info['id']}.{info['extractor']}.{info['ext']}"

    def tryDownload(self, url):
        try:
            return self.download([url])
        except:
            return -1
    
    def setLogger(self, logger):
        self.params['logger'] = logger


if __name__ == "__main__":
    yee = 'https://www.youtube.com/watch?v=q6EoRBvdVPQ'
    ydl = Downloader()
    download = ydl.download