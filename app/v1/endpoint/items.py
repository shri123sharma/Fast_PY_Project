from fastapi import APIRouter
from enum import Enum
from app.v1.models import Item,FilterParams
from typing import Annotated
from fastapi import Query,Path

router=APIRouter()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@router.get("/read_item")
def read_item():
    result={"item_id":1,"type":"int"}
    return result
@router.get("/items/{item_id}")
def read_item(item_id:int):
    return {"item_id":item_id}

@router.get("/get_models/model_name")
def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

@router.get("/query_items/{item_id}")
def query_items(item_id:int,q:str | None=None):
    if q:
        return {"item_id": item_id, "q":q}
    return {"item_id": item_id}

@router.get("/type_item/{item_id}")
def type_item(item_id:int,q:str |None=None,short:bool=False):
    result={"item_id": item_id}
    if q:
        result.update({"q":q})
    if not short:
        result.update({"descripation":"This is amazing item that is long description"})

    return result

@router.get("/user_item/{item_id}")
def read_user_item(item_id:int,needy:str):
    item={"item_id":item_id,"needy":needy}
    return item

@router.post("/create_item")
def create_item(item:Item):
    return {
        "item_name":item.item_name,
        "price":10000.0,
        }

@router.get("/query_value_item")
def query_value_item(q:Annotated [list[str] |None,Query(min_length=0,max_length=50)]="hello_query"):
    result={"item_name":"Foo","item_value":"Bar"}
    if q:
        result.update({"q":q})
    return result

@router.get("/items_path/{item_id}")
async def items_path(item_id: int = Path(title="The ID of the item to get"), q: str |None=None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@router.get("/items_annote_path/{item_id}")
async def items_annote_path(
    item_id:Annotated[int,Path(title="the ID of the item to get",ge=1)],q:str |None=None
):
    results={"item_id":item_id}
    if q:
        results.update({"q": q})
    return results

@router.get("/items_validate_path/{item_id}")
async def items_validate_path(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str |None=None,
    size: Annotated[float, Query(gt=0, lt=10.5)] =None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results


@router.get("/items_pydant/")
async def items_pydant(item: Annotated[FilterParams, Query()]):
    return item




