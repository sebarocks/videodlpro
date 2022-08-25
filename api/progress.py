
from typing import List


class ProgressTracker():

    def __init__(self):
        self.urls = {}
        self.statusList = {}
        self.percentage = {}
        self.filename = {}

    def attachDownload(self, url, download_id):
        self.urls[download_id] = url
        self.statusList[download_id] = 'created'
        self.percentage[download_id] = 0
        self.filename[download_id] = ''

    def setStatus(self, download_id, status):
        self.statusList[download_id] = status

    def getStatus(self, download_id):
        return self.statusList[download_id]

    def getPercentage(self, download_id):
        return self.percentage[download_id]

    def getFilename(self, download_id):
        return self.filename[download_id]

    def loadHookInfo(self, download_id, hook_info):
        self.statusList[download_id] = hook_info['status']
        total = float( hook_info['total_bytes'] )
        current = float( hook_info['downloaded_bytes'] )
        self.percentage[download_id] = 100 * current / total  if total != 0 else 0
        self.filename[download_id] = hook_info['filename']



