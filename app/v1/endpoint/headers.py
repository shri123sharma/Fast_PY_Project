from fastapi import APIRouter,Body,Cookie,Header,Response
from app.v1.schemas import CommonHeaders
from typing import Annotated,Optional,List

router=APIRouter()

@router.get("/set_headers")
async def set_headers(response:Response):
    response.headers["host"] = "127.0.0.1997"
    response.headers["save_data"] = "True"
    response.headers["if_modified_since"] = "Tue, 15 Nov 1994 12:45:26 GMT"
    response.headers["traceparent"] = "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-00"
    response.headers["x_tag"] = "tag1,tag2,tag3"  # Add multiple values as a comma-separated string
    return {"message": "Headers have been set"}

@router.get("/read_headers")
async def read_headers(
    host: str = Header(None),
    save_data: bool = Header(None),
    if_modified_since: Optional[str] = Header(None),
    traceparent: Optional[str] = Header(None),
    x_tag: Optional[List[str]] = Header(None),
):
    headers = CommonHeaders(
        host=host,
        save_data=save_data,
        if_modified_since=if_modified_since,
        traceparent=traceparent,
        x_tag=x_tag or []
    )
    
    return headers
