from typing import Optional
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

class FormatInfo(BaseModel):
    format_id: str
    ext: str
    resolution: str
    fps: Optional[str]
    filesize: Optional[int]
    tbr: Optional[float]
    vcodec: str
    acodec: str
    format_note: str

class VideoProgress(BaseModel):
    url : str
    status : str
    percentage : float
    filename : str