from pydantic import BaseModel

class VideoInfo(BaseModel):
    title: str
    thumbUrl: str
    url: str
    site: str    

class VideoUrl(BaseModel):
    url: str

class ProgressInfo(BaseModel):
    download_id : int
    status : str
    percentage : float
    filename : str