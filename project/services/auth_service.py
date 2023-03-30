import calendar
import datetime

import jwt
from flask import current_app
from werkzeug.exceptions import abort

from project.services.users_service import UserService
from project.tools.security import compare_passwords

class AuthService:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not compare_passwords(user.password, password):
                raise abort(400)

        data = {
            'email': user.email,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                                  algorithm=current_app.config['JWT_ALGORITHM'])

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                                  algorithm=current_app.config['JWT_ALGORITHM'])

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        '''
        генерация новой пары токенов
        :param refresh_token:
        :return:
        '''



        data = jwt.decode(
            jwt=refresh_token,
            key=current_app.config['SECRET_KEY'],
            algorithms=current_app.config['JWT_ALGORITHM']
        )


        if 'email' not in data:
            raise abort(404)



        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                                  algorithm=current_app.config['JWT_ALGORITHM'])

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                                   algorithm=current_app.config['JWT_ALGORITHM'])

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

