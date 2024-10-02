from fastapi import APIRouter,Form,status
from typing_extensions import Annotated
from app.v1.schemas import *
from fastapi import FastAPI,File,UploadFile

router=APIRouter()

@router.post("/login",status_code=201)
async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
    return {"username":username, "password":password}

@router.post("/form_login",status_code=status.HTTP_201_CREATED)
async def form_login(data:Annotated[FormData,Form()]):
    return data

@router.get("/get_form_data",response_model=FormData,status_code=status.HTTP_200_OK)
async def get_form_data(
    username: str = Form(...), 
    password: str = Form(...),
    ):
    form_data = FormData(username=username, password=password)
    return form_data

@router.post("/uploadfile")
async def create_upload_file(file:UploadFile):
    return {"filename":file.filename}