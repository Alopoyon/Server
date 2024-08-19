from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv() 
PROJECT_DIRECTORY = Path(os.environ['PROJECT_PATH'])

from project_management import ProjectManagement

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/api/projects")
async def projects():
    _project = ProjectManagement(PROJECT_DIRECTORY)
    _contents = _project.directory_contents()
    # print(f"N{contents=}")
    return _contents

@app.get("/api/projects/d_{project_name_dir}")
async def project_contents(project_name_dir):
    _project = ProjectManagement(PROJECT_DIRECTORY.joinpath(project_name_dir))
    _contents = _project.directory_contents()
    # print(f"N{contents=}")
    return _contents

@app.get("/api/projects/f_{project_name_file}")
async def project_contents(project_name_file):
    _project = ProjectManagement(PROJECT_DIRECTORY.joinpath(project_name_file))
    _contents = _project.read_file_contents()
    # print(f"N{contents=}")
    return _contents