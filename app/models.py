from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class College(BaseModel):
    id: int
    name: str
    location: str
    website: str
    logo: str
