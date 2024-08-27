# SERVER PACKAGES
import uvicorn
from fastapi import FastAPI, Request
from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse

# UTILITY

import os
import sys

# ENVIRONMENT SETUP
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, os.environ['SERVER_PATH']) 

# DATABASE SETUP
from app.db.session import get_db, Base, engine

# ROUTES
from app.router.main import api_router

# CUSTOM PACKAGES/SCRIPTS


# DECALRE PATHS 



Base.metadata.create_all(bind=engine)


app = FastAPI(
    title= "Server"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.on_event("startup")
def on_startup():
    get_db()

 
if __name__ == "__main__":
    uvicorn.run(app="main:app",host="127.0.0.1",port=8000,reload=True)