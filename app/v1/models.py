from sqlalchemy import Column, Integer, String
from app.database import Base

class Country(Base):
    __tablename__ = "countries"
    
    country_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    capital = Column(String, nullable=True)  # Optional field
    population = Column(Integer, nullable=False)
    currency = Column(String, nullable=True)  # Optional field
