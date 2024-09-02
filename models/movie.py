from typing import Optional
from pydantic import BaseModel, Field
from db.database import Base
from sqlalchemy import Column, Integer, String, Float


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=10)

    model_config = {
     "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción"
                }
            ]
        }
    }


class MovieDb(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)