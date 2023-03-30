from typing import Optional

from project.dao.user import UserDAO
from project.models import User
from project.tools.security import generate_password_hash

class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        '''
        Сервис получения одного пользователя
        :param uid:
        :return:
        '''
        return self.dao.get_by_id(uid)

    def get_by_email(self, email):
        '''
        Сервис поска пользователя по логину (email)
        :param email:
        :return:
        '''
        return self.dao.get_by_email(email)

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> list[User]:
        '''
        Сервис полчения всех пользователей
        :return:
        '''
        users = self.dao.get_all()
        return users

    def create(self, user_data: dict[str: str]):
        '''
        Сервис создания пользователя
        :param user_data:
        :return:
        '''
        user_data['password'] = generate_password_hash(user_data['password'])
        return self.dao.create(user_data)

    def update(self, user_data):
        '''
        Сервис обновления данных пользоваетля
        :param user_data:
        :return:
        '''
        self.dao.update(user_data)
        return self.dao

    def update_password(self, email, new_password):
        '''
        Сервис обновления пароля пользователя
        :param email:
        :param new_password:
        :return:
        '''
        self.dao.update_password(email, new_password)

    def delte(self, uid):
        '''

        :param uid:
        :return:
        '''
        self.dao.delete(uid)

    def get_favorites(self, email):
        user = self.get_by_email(email)
        favorites = self.dao.get_favorites(user.id)
        return favorites