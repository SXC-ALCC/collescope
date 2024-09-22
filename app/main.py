from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import List
from .models import College
from .crud import read_colleges
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    """Serve the frontend HTML page."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/colleges", response_model=List[College])
def get_colleges():
    """API endpoint to get all colleges."""
    return read_colleges()

@app.get("/colleges/search", response_model=List[College])
def search_colleges(name: str):
    """Search colleges by name."""
    colleges = read_colleges()
    filtered_colleges = [c for c in colleges if name.lower() in c.name.lower()]
    return filtered_colleges

@app.get("/colleges/location/{location}", response_model=List[College])
def get_colleges_by_location(location: str):
    """Filter colleges by location."""
    colleges = read_colleges()
    filtered_colleges = [c for c in colleges if location.lower() == c.location.lower()]
    return filtered_colleges
