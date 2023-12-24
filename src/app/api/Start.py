from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import dependencies, crud, schemas

router = APIRouter()

@router.get('/')
def start():
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"start": "Welcome to the API"})