
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from fastapi_socketio import SocketManager

from downloader import Downloader
from models import VideoInfo, VideoUrl

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")

sm = SocketManager(app=app,cors_allowed_origins=[],socketio_path= '')


@app.post("/download")
async def downloadUrl(vidUrl : VideoUrl):
    ydl = Downloader()
    filename = ydl.getFilename(vidUrl.url)
    res = ydl.download([vidUrl.url])
    print(res)
    return filename

@app.post("/info")
async def infoUrl(vidUrl : VideoUrl):
    url = vidUrl.url
    ydl = Downloader()
    info = ydl.getInfo(url)
    if info is None:
        raise HTTPException(status_code=404, detail="URL not supported")
    else:
        return VideoInfo(
            title = info['title'],
            thumbUrl = info['thumbnail'],
            site = info['webpage_url_domain'],
            url = info['webpage_url']
        )

@app.sio.on('msg')
async def handle_join(sid, data):
    print(f"msg: {data}")

@app.sio.on('download')
async def handle_join(sid, data):
    print(f"Download requested: {data}")

    ydl = Downloader()

    filename = ydl.getFilename(data)
    res = ydl.download(data)
    
    await sm.emit('finished',filename)



