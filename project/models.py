from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)

class Director(models.Base):
    __tablename__ = 'director'

    name = Column(String(100), unique=True, nullable=False)

class User(models.Base):
    __tablename__ = 'user'

    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))

    favourite_genre = Column(Integer, ForeignKey(Genre.id))
    genre = relationship('Genre')

class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

    genre_id = Column(Integer, ForeignKey(Genre.id), nullable=False)
    genre = relationship('Genre')
    director_id = Column(Integer, ForeignKey(Director.id), nullable=False)
    director = relationship('Director')

class FavoriteMovies(models.Base):
    __tablename__ = 'favorite_movies'

    user_id = Column(ForeignKey(User.id))
    movie_id = Column(ForeignKey(Movie.id))