from datetime import datetime
from yt_dlp import YoutubeDL

# dict_keys(['status', 'downloaded_bytes', 'total_bytes', 'tmpfilename', 'filename', 'eta', 'speed', 'elapsed', 'ctx_id', 'info_dict', '_eta_str',
#           '_speed_str', '_percent_str', '_total_bytes_str', '_total_bytes_estimate_str', '_downloaded_bytes_str', '_elapsed_str', '_default_template'])

def processHookInfo(d):
    info={
        "status": d['status'],
        "downloaded_bytes": d['downloaded_bytes'],
        "total_bytes": d['total_bytes'],
        "filename": d['filename'].split("\\")[-1],
    }
    return info


def my_hook(d):
    #print(d.keys())
    print(d['status'])
    print(d['downloaded_bytes'])
    print(d['total_bytes'])
    print(d['filename'])
    print(datetime.now().time())
    

def my_post_hook(d):
    print('<X>'+d['info_dict']['_filename'])

ydl_opts = {
    'outtmpl': './downloads/%(id)s.%(extractor)s.%(ext)s',
    'quiet': False,
    'no_color': True
    # 'progress_hooks': [my_hook],
    # 'postprocessor_hooks': [my_post_hook]
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

    def getInfoSanitized(self, url):
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


if __name__ == "__main__":
    yee = 'https://www.youtube.com/watch?v=q6EoRBvdVPQ'
    ydl = Downloader()
    ydl.add_progress_hook(my_hook)
    download = ydl.download


