from fastapi import APIRouter
from typing import Annotated,Optional
from app.v1.models import ItemIndex

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


