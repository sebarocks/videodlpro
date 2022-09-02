
import asyncio

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from fastapi_socketio import SocketManager

from progress import ProgressTracker
from downloader import Downloader, processHookInfo
from models import VideoInfo, VideoUrl, FormatInfo

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.mount("/files", StaticFiles(directory="downloads"), name="downloads")


sm = SocketManager(app=api, cors_allowed_origins=[], socketio_path='')
pt = ProgressTracker()

@api.post("/download")
async def downloadUrl(vidUrl: VideoUrl):
    ydl = Downloader()
    filename = ydl.getFilename(vidUrl.url)
    res = ydl.download([vidUrl.url])
    print(res)
    return filename

@api.post("/mp3")
async def downloadMp3(vidUrl: VideoUrl):
    ydl = Downloader()
    filename = ydl.getFilename(vidUrl.url)
    ydl.mp3Mode()
    res = ydl.download([vidUrl.url])
    print(res)
    return filename

@api.post("/formats")
async def formatsUrl(vidUrl: VideoUrl):
    url = vidUrl.url
    ydl = Downloader()
    info = ydl.getFormats(url)
    if info is None:
        raise HTTPException(status_code=404, detail="URL not supported")
    else:
        return info

@api.post("/info")
async def infoUrl(vidUrl: VideoUrl):
    url = vidUrl.url
    ydl = Downloader()
    info = ydl.getInfo(url)
    if info is None:
        raise HTTPException(status_code=404, detail="URL not supported")
    else:
        return VideoInfo(
            title=info['title'],
            thumbUrl=info['thumbnail'],
            site=info['webpage_url_domain'],
            url=info['webpage_url']
        )


@api.sio.on('queryprogress')
async def handle_join(sid, data):
    #print(f"query: {data}")
    dl_id = int(data)
    res = {
        "status": pt.getStatus(dl_id),
        "percentage": pt.getPercentage(dl_id),
        "filename": pt.getFilename(dl_id)
    }
    await sm.emit(f"progress.{dl_id}", res)
    #print(f"emit progress.{dl_id}")

@api.sio.on('download')
async def handle_join(sid, data):

    print(f"Download requested: {data}")
    
    dl_id = int(data['download_id'])
    url = data['url']
    
    pt.attachDownload(url, dl_id)

    def temphook(d):
        pt.loadHookInfo(dl_id,processHookInfo(d))

    ydl = Downloader()
    filename = ydl.getFilename(url)
    ydl.add_progress_hook(temphook)

    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, ydl.download, url)
    print(res)
    await sm.emit(f"finished.{dl_id}", filename)
    #print(f"emit finished.{dl_id}")


app = FastAPI()
app.mount("/api",api)

# Correr build con /index.html
#app.mount("/", StaticFiles(directory="../app/build"), name="site")

