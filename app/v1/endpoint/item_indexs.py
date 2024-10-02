from fastapi import APIRouter
from typing import Annotated,Optional,Any
from app.v1.schemas import ItemIndex,FirstItemIndex

router=APIRouter()

@router.post("/create_index_items/")
async def create_index_items(item:ItemIndex) -> ItemIndex:
    return item

@router.get("/read_index_items/")
async def read_index_items() -> list[ItemIndex]:
    return [
        ItemIndex(name="Portal Gun", price=42.0),
        ItemIndex(name="Plumbus", price=32.0),
    ]

@router.post("/first_create_index_items/",response_model=FirstItemIndex)
async def first_create_index_items(firstitemindex:FirstItemIndex)  -> Any:
    return firstitemindex

@router.get("/first_get_index_items/", response_model=list[FirstItemIndex])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

