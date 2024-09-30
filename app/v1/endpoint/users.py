from fastapi import APIRouter,Response
from typing import Annotated,Optional,Any
from app.v1.models import *
from fastapi.responses import JSONResponse,RedirectResponse

router=APIRouter()

@router.post("/create_user")
async def create_user(user:UserIn)->UserIn:
    return user

@router.post('/user',response_model=UserOut)
async def create_user(user:UserIn)->Any:
    return user

@router.post('/user_detail')
async def create_user_detail(user:UserIn)->UserPasswordIn:
    return user

@router.get("/portal")
async def get_portal(telepert:bool=False)->Response:
    if telepert:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw")
    return JSONResponse(content={"message":"Here Your portal"})


