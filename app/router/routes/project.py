from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
import os
from pathlib import Path, PurePath

PROJECT_DIRECTORY = Path(os.environ['PROJECT_PATH'])
from app.utils.projectManagement import ProjectManagement


router = APIRouter()

@router.get("/")
async def projects():
    _project = ProjectManagement(PROJECT_DIRECTORY)
    _contents = _project.directory_contents()
    # print(f"N{contents=}")
    return _contents

@router.get("/{project_name:path}")
async def project_contents(project_name: str = ""):
    if project_name == "":
        return JSONResponse(status_code=404, content={"message":"Invalid path!"})
    # print(f"{project_name=}")
    try:
        _project = ProjectManagement(PROJECT_DIRECTORY.joinpath(project_name))
        # print("Current path: ",_project)
        _contents = _project.directory_contents()
        # print(f"{_contents=}")
        return _contents
    except:
        return JSONResponse(status_code=404, content={"message":"Item does not exist"})


# @app.api_route("/api/projects/{path_name:path}", methods=["GET"])
# async def catch_all_project_sub_calls(request:Request, path_name:str ):
#     return {"request_method": request.method, "path_name": path_name}

