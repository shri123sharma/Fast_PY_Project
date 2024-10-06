from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from typing import List
from app.v1.schemas import *
from app.v1.models import *
from app.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_countries",response_model=CountryResponse,status_code=status.HTTP_201_CREATED)
async def create_countries(country:CountryCreate,db:Session=Depends(get_db)):
    db_country=Country(**country.dict())
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

@router.get("/read_countries",response_model=List[CountryResponse])
async def read_countries(db:Session=Depends(get_db)):
    countries=db.query(Country).all()
    return countries

@router.get("/countries/{country_id}",response_model=List[CountryResponse],status_code=status.HTTP_200_OK)
async def read_countries_obj(country_id:int,db:Session=Depends(get_db)):
    countries=db.query(Country).filter(Country.country_id == country_id)
    if not countries:
        raise HTTPException(status_code=404, detail="Country not found")
    return countries

@router.put("/countries/{country_id}",response_model=List[CountryResponse],status_code=status.HTTP_200_OK)
async def update_countries(country_id:int,updated_country: CountryCreate,db:Session=Depends(get_db)):
    countries=db.query(Country).filter(Country.country_id==country_id).first()
    if not countries:
        raise HTTPException(status_code=404, detail="Country not found")
    
    for key,value in updated_country.dict().items():
        setattr(countries, key, value)

    db.commit()
    db.refresh(countries)
    return [countries]

@router.delete("/countries/{country_id}/")
async def delete_countries(country_id:int,db:Session=Depends(get_db)):
    countries=db.query(Country).filter(Country.country_id==country_id).first()
    if not countries:
        raise HTTPException(status_code=404, detail="Country not found")
    db.delete(countries)
    db.commit()
    return {"message": "Country deleted successfully"}    