from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from db.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie
from services.movies import MovieService


movie_router = APIRouter()
movieService = MovieService(Session())


@movie_router.get("/movies", tags=["Movies"], response_model=List[Movie], dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    movies = movieService.get_movies()
    return JSONResponse(content=jsonable_encoder(movies), status_code=200)


@movie_router.get(path="/movies/{id}", tags=["Movies"], response_model=Movie)
def get_movies(id: int = Path(ge=1, le=2000)) -> Movie:
    movie = movieService.get_movie_by_id(id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content=jsonable_encoder(movie), status_code=200)


@movie_router.get('/movies/', tags=['Movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    movies = movieService.get_movies_by_category(category)
    if not movies:
        raise HTTPException(status_code=404, detail="Movies not found")
    return JSONResponse(content=movies, status_code=200)


@movie_router.post('/movies/', response_model=list[Movie], tags=['Movies'])
def post_new_movie(new_movie: Movie) -> list[Movie]:
    movies = movieService.post_new_movie(new_movie)
    return JSONResponse(content=jsonable_encoder(movies), status_code=201)


@movie_router.put('/movies/{id}', tags=['Movies'], response_model=Movie)
async def update_movie(id: int, movie: Movie) -> Movie:
    movie = movieService.update_movie(id, movie)
    return JSONResponse(content=jsonable_encoder(movie), status_code=200)


@movie_router.delete('/movies/{id}', tags=['Movies'], response_model=list[Movie])
async def delete_movie(id: int) -> list[Movie]:
    movies = movieService.delete_movie(id)
    if not movies:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content=jsonable_encoder(movies), status_code=200)
