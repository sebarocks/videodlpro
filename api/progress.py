from models import VideoProgress


class ProgressTracker():

    def __init__(self):
        self.videos: dict[int, VideoProgress] = {}

    def attachDownload(self, url, download_id):
        self.videos[download_id] = VideoProgress(
            url=url,
            status='created',
            percentage=0,
            filename=''
        )

    def setStatus(self, download_id, status):
        self.videos[download_id].status = status

    def getStatus(self, download_id):
        vidProg = self.videos.get(download_id, None)
        if vidProg:
            return vidProg.status
        else:
            return 'unknown'

    def getPercentage(self, download_id):
        vidProg = self.videos.get(download_id, None)
        if vidProg:
            return vidProg.percentage
        else:
            return 0

    def getFilename(self, download_id):
        vidProg = self.videos.get(download_id, None)
        if vidProg:
            return vidProg.filename
        else:
            return '-'

    def loadHookInfo(self, download_id, hook_info):
        vidProg = self.videos.get(download_id, None)
        if vidProg:
            vidProg.status = hook_info['status']
            total = float(hook_info['total_bytes'])
            current = float(hook_info['downloaded_bytes'])
            vidProg.percentage = 100 * current / total if total != 0 else 0
            vidProg.filename = hook_info['filename']
