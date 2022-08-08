
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from downloader import Downloader
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:5173",
]

class VideoInfo(BaseModel):
    title: str
    thumbUrl: str
    url: str
    site: str    

class DownloadFile(BaseModel):
    filename: str
    hash: str

class VideoUrl(BaseModel):
    url: str


app = FastAPI()
ydl = Downloader()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.post("/download")
# async def downloadUrl(url : str):
#     ydl.download([url])
#     return url

@app.post("/info")
async def infoUrl(vidUrl : VideoUrl):
    url = vidUrl.url
    info = ydl.getInfo(url)
    if info is None:
        raise HTTPException(status_code=404, detail="URL not supported")
    else:
        return VideoInfo(
            title = info['title'],
            thumbUrl = info['thumbnail'],
            site = info['webpage_url_domain'],
            url = info['webpage_url'])

@app.get("/infotest")
async def infoUrl():
    urlTest = 'https://www.youtube.com/watch?v=Y1zl6WgZSAw'
    return ydl.getInfoSanatized(urlTest)


app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")

@app.get("/file/{id}")
async def hashes(id):
    return FileResponse(id)