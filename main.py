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

@app.get("/api/projects/")
async def projects():
    project = ProjectManagement(PROJECT_DIRECTORY)
    contents = project.directory_contents()
    # print(f"{contents=}")
    return contents