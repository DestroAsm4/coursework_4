from .auth import auth_ns
from .main import genres_ns
from .main.directors import directors_ns
from .main.movies import movies_ns
from .main.favorites import favorites_ns

__all__ = [
    'auth_ns',
    'genres_ns',
    'user_ns',
    'directors_ns',
    'movies_ns',
    'favorites_ns'
]
