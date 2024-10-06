from fastapi import APIRouter,Cookie,Response,Header
from app.v1.schemas import Cookies
from typing import Annotated,Optional


router=APIRouter()

@router.get("/set_cookie/")
def set_cookie(response: Response):
    response.set_cookie(key="ads_id", value="123456")  # You can set any value
    return {"message": "Cookie has been set"}

@router.get("/read_cookie/")
def read_cookie(ads_id:Annotated[str |None,Cookie()]=None):
    return {"ads_id":ads_id}


@router.get("/set_header")
async def read_headers(response: Response):
    response.headers["X-Ads-Id"] = "123456" 
    return {"message": "Header has been set"}

@router.get("/read_header/")
def read_header(ads_id: Annotated[str | None, Header(alias="X-Ads-Id")] = None):
    return {"ads_id": ads_id}

@router.get("/set_cookies/")
def set_cookies(response: Response):
    response.set_cookie(key="session_id", value="abc123")
    response.set_cookie(key="fatebook_tracker", value="track123")
    response.set_cookie(key="googall_tracker", value="gtrack456")
    return {"message": "Cookies have been set"}

@router.get("/read_item_cookie/")
def read_item_cookie(
    session_id: Optional[str] = Cookie(None),
    fatebook_tracker: Optional[str] = Cookie(None),
    googall_tracker: Optional[str] = Cookie(None),
):
    cookies = Cookies(
        session_id=session_id,
        fatebook_tracker=fatebook_tracker,
        googall_tracker=googall_tracker
    )
    return cookies
