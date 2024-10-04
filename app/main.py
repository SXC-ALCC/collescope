import json
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
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

@app.get("/add", response_class=HTMLResponse)
async def get_add_college(request: Request):
    """Add new colleges page"""
    return templates.TemplateResponse("add.html", {"request": request})

@app.post("/add")
async def add_college(request: Request, name: str = Form(...), location: str = Form(...), website: str = Form(...), logo: str = Form(...)):
    """Add new colleges"""
    colleges_JSON_file = "app/colleges.json"

    with open(colleges_JSON_file, "r") as file:
        colleges_list = json.load(file)

    new_college = {
        "id": colleges_list[-1]["id"] + 1,
        "name": name,
        "location": location,
        "website": website,
        "logo": logo
    }
    colleges_list.append(new_college)

    with open(colleges_JSON_file, "w") as file:
        json.dump(colleges_list, file, indent=4)

    return RedirectResponse(url="/", status_code=303)

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
