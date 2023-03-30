from sqlalchemy.exc import IntegrityError

from project.dao.base import BaseDAO
from project.exceptions import UserAlreadyExists
from project.models import User, FavoriteMovies, Movie
from project.tools.security import generate_password_hash

class UserDAO(BaseDAO[User]):
    __model__ = User


    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).first()

    def create(self, user_data):
        try:
            user = User(**user_data)
            self._db_session.add(user)
            self._db_session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return user

    def delete(self, uid):
        user = self.get_by_id(uid)
        self._db_session.add(user)
        self._db_session.commit()

    def update(self, user_data):
        print(user_data)
        user = self.get_by_id(user_data.get('id'))
        if user_data.get('email'):
            user.email = user_data.get('email')
        if user_data.get('password'):
            user.password = user_data.get('password')
        if user_data.get('name'):
            user.name = user_data.get('name')
        if user_data.get('surname'):
            user.surname = user_data.get('surname')
        if user_data.get('favourite_genre'):
            user.favourite_genre = user_data.get('favourite_genre')
        print(user.name)
        try:
            self._db_session.add(user)
            self._db_session.commit()
        except IntegrityError:
            raise UserAlreadyExists

    def update_password(self, email, new_password):
        user = self.get_by_email(email)
        user.password = generate_password_hash(new_password)

        self._db_session.add(user)
        self._db_session.commit()

    def get_favorites(self, user_id):
        result = self._db_session.query(
            Movie,
        ).join(
            FavoriteMovies
        ).filter(
            FavoriteMovies.user_id == user_id
        ).all()
        return result

    # def add_favirite_movie(self, data):
    #     try:
    #         movie = User(**user_data)
    #         self._db_session.add(user)
    #         self._db_session.commit()
    #     except IntegrityError:
    #         raise UserAlreadyExists
    #     return user


