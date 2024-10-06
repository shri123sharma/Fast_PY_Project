from fastapi import APIRouter,Response
from typing import Annotated,Optional,Any
from app.v1.schemas import *
from fastapi.responses import JSONResponse,RedirectResponse
from app.v1.utils import fake_save_user
from typing import Union
from fastapi import status
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

@router.get("/portal_data", response_model=None)
async def get_portal_data(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

items = {
    "foo": {"name": "Foo", "price": 50.2,"tags": ["2000"]},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}
@router.get("/items_model/{item_id}/",response_model=ItemModel,)
async def read_item_model(item_id:str):
    return items[item_id]

@router.post("/create_user_one",response_model=UserOut)
async def create_user_one(user_in:UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

@router.post("/user_create_one/", response_model=UserInDB1)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
response_by_model = Union[CarItem, PlaneItem]
@router.get("/multi_items/{item_id}",response_model=response_by_model)
async def get_multi_item(item_id:int):
    if item_id == 1:
        return CarItem(id=1, name="Sports Car", wheels=4, engine="V8")
    elif item_id == 2:
        return PlaneItem(id=2, name="Jet Plane", wingspan=35.5, engines=2)
    else:
        return {"error": "Item not found"}
    

@router.post("/create_post",response_model=PostItem,status_code=201)
async def create_post(post_item:PostItem):
    return post_item

@router.post("/create_items_post/", status_code=status.HTTP_201_CREATED)
async def create_items_post(name: str):
    return {"name": name}
