from pydantic import BaseModel

class VideoInfo(BaseModel):
    title: str
    thumbUrl: str
    url: str
    site: str    

class VideoUrl(BaseModel):
    url: str