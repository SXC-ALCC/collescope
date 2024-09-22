import json
from typing import List
from pathlib import Path
from .models import College

JSON_FILE = Path(__file__).parent / "colleges.json"

def read_colleges() -> List[College]:
    with open(JSON_FILE, "r") as f:
        colleges = json.load(f)
        return [College(**college) for college in colleges]

def write_colleges(colleges: List[College]):
    with open(JSON_FILE, "w") as f:
        json.dump([college.dict() for college in colleges], f, indent=4)
