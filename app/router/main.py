from fastapi.routing import APIRouter

from app.router.routes import project, product, user, default

api_router = APIRouter()
api_router.include_router(default.router, tags=["Default"])
api_router.include_router(project.router, prefix= "/projects",tags=["Project"])
api_router.include_router(product.router, prefix= "/products",tags=["Product"])
api_router.include_router(user.router, prefix= "/users",tags=["User"])

if __name__ == '__main__':
    ...