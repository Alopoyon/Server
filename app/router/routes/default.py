from fastapi.routing import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path, PurePath

favicon_path = './favicon.ico' 

router = APIRouter()

@router.get("/")
async def root():
    return {"msg": "Hello World!"}

@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    # print(os.getcwd())
    return FileResponse(favicon_path)