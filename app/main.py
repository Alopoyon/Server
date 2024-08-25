# SERVER PACKAGES
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse

# CUSTOM PACKAGES/SCRIPTS
from project_management import ProjectManagement

# UTILITY
from pathlib import Path, PurePath
import os

from dotenv import load_dotenv
load_dotenv()

# DECALRE PATHS 
PROJECT_DIRECTORY = Path(os.environ['PROJECT_PATH'])
favicon_path = './favicon.ico' 

def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # here
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    @app.get("/")
    async def root():
        return {"message": "Hello World!"}

    @app.get('/favicon.ico', include_in_schema=False)
    async def favicon():
        print(os.getcwd())
        return FileResponse(favicon_path)

    @app.get("/api/projects")
    async def projects():
        _project = ProjectManagement(PROJECT_DIRECTORY)
        _contents = _project.directory_contents()
        # print(f"N{contents=}")
        return _contents

    # @app.api_route("/api/projects/{path_name:path}", methods=["GET"])
    # async def catch_all_project_sub_calls(request:Request, path_name:str ):
    #     return {"request_method": request.method, "path_name": path_name}


    @app.get("/api/projects/{project_name:path}")
    async def project_contents(project_name: str = ""):
        if project_name == "":
            return JSONResponse(status_code=404, content={"message":"Invalid path!"})
        # print(f"{project_name=}")

        try:
            _project = ProjectManagement(PROJECT_DIRECTORY.joinpath(project_name))
            print("Current path: ",_project)
            _contents = _project.directory_contents()
            # print(f"{_contents=}")
            return _contents
        except:
            return JSONResponse(status_code=404, content={"message":"Item does not exist"})

    return app
 
if __name__ == "__main__":
    uvicorn.run(app="main:create_app",host="127.0.0.1",port=8000,reload=True)