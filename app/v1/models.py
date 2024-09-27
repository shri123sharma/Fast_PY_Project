from pydantic import BaseModel,Field,HttpUrl
from typing import Annotated, Literal,Union,List

class Item(BaseModel):
    item_name:str
    description:str |None=None
    price:float
    tax:float |None=None

class FilterParams(BaseModel):
    limit:int=Field(100,gt=0,le=100)
    offset:int=Field(0,ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

class User(BaseModel):
    username :str
    fullname :str | None=None


class Product(BaseModel):
    name : str
    description: str |None =Field(default=None,title="The description of the item", max_length=300
    )
    price:float = Field(gt=0, description="The price must be greater than zero")
    tax:float |None=None

class ItemProduct(BaseModel):
    name:str
    description :Union[str,None]=None
    price:float
    tax:Union[float,None]=None
    tags:List[str]=[]

class Post(BaseModel):
    post_name:str 
    post_location: str
    post_url:HttpUrl
    post_user:User |None=None

class Author(BaseModel):
    author_name:str
    author_location:str

class Book(BaseModel):
    book_name:str
    book_publish:str
    book_description:str
    book_price:float
    book_tax:float
    book_author:Author |None=None

class BookSummary(BaseModel):
    book_title:str
    book_summary:str
    book:List[Book]

class FirstItem(BaseModel):
    name:str =Field(examples=["Foo"])
    description:str |None=Field(default=None,examples=["A very Nice teams"])
    price:float=Field(examples=[35.5])
    tax:float |None=Field(default=None, examples=[3.2])

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

class SecondItem(BaseModel):
    name : str
    description:str |None=None
    price:float
    tax :float |None=None

class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


class CommonHeaders(BaseModel):
    host: str
    save_data: bool |None=None
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

class ItemIndex(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    