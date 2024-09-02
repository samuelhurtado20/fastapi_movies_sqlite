import json

from db.database import Session
from models.movie import MovieDb

class MovieService:
    
    def __init__(self, db):
        self.db = db
    
    def get_movies(self):
        movies = self.db.query(MovieDb).all()
        return movies

    def get_movie_by_id(self, id: int):
        movie = self.db.query(MovieDb).filter(MovieDb.id == id).first()
        if movie is None:
            return None
        return movie

    def get_movies_by_category(self, category: str):
        movies = self.db.query(MovieDb).filter(MovieDb.category == category).all()
        return movies

    def post_new_movie(self, new_movie):
        new_movie = MovieDb(**new_movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return self.db.query(MovieDb).all()

    def update_movie(self, id: int, update_movie):
        movie = self.db.query(MovieDb).filter(MovieDb.id == id).first()
        if movie is None:
            return None
        movie.title = update_movie.title
        movie.overview = update_movie.overview
        movie.year = update_movie.year
        movie.rating = update_movie.rating
        movie.category = update_movie.category
        self.db.commit()
        return movie

    def delete_movie(self, id: int):
        movie = self.db.query(MovieDb).filter(MovieDb.id == id).first()
        if movie is None:
            return None
        self.db.delete(movie)
        self.db.commit()
        return self.db.get(MovieDb).all()