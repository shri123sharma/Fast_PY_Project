from fastapi import Query,Path
from app.v1.models import Product,Item,User,ItemProduct,Post,BookSummary,FirstItem,SecondItem
from typing import Annotated,List
from fastapi import APIRouter,Body
from datetime import datetime,time,timedelta
from uuid import UUID

router=APIRouter()

@router.put("/mix_product/{item_id}")
def put_mix_product(
    item_id=Annotated[int,Path(title="this ID is already in the product",ge=0,le=100)],
    item:Item |None=None,
    q:str |None=None,

):
    results={"item_id":item_id}
    if q:
        results.update({'q':q})
    if item:
        results.update({'item_id':item})
    return results

@router.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    user: User,
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user,}
    if q:
        results.update({"q": q})
    return results

@router.post("/create_product/")
def create_product(product:Product):
    results={"product":product}
    return results

@router.put("/update_product/{product_id}")
def update_products(product_id:int,product:Annotated[Product, Body(embed=True)]):
    results={"product_id":product_id,"product":product}
    return results

@router.post("/create_product_item/")
def create_item_product(item_product:ItemProduct):
    results={"product_item":item_product}
    return results

@router.post("/create_post")
def create_post(post:Post):
    result={"user_post":post}
    return result

@router.post("/create_book_summary")
def create_book_summary(book_summary:BookSummary):
    return book_summary

@router.post("/create_first_items/")
async def create_first_item(firstitem: FirstItem):
    results = {"item": firstitem}
    return results

@router.post("/create_second_items/{item_id}")
async def create_second_item(
    item_id: int,  # item_id as a query parameter
    seconditem: Annotated[
        SecondItem,
        Body(
            example={
                "name": "speaker",
                "description": "this is party speaker",
                "price": 10000.0,
                "tax": 100.0
            }
        )
    ]
):
    results = {"item_id": item_id, "second_item_result": seconditem}
    return results   

@router.post("/read_data_items/")
async def read_data_items(
    # item_id:UUID,
    start_datetime:Annotated[datetime,Body()],
    end_datetime:Annotated[datetime,Body()],
    process_after:Annotated[timedelta,Body()],
    repeat_at:Annotated [time |None,Body()]=None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        # "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }


