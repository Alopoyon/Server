from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/")#, include_in_schema=False)
async def read_prducts():
    return [{"product_id": "Foo"}]