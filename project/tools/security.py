import base64
import hashlib
import hmac

import jwt
from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    '''
    генерация хеш пароля
    :param password:
    :return:
    '''
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')

def compare_passwords(password_hash, other_password) -> bool:
    '''
    Сравнение вводного пароля и пароляб хранящегося в БД
    :param password_hash:
    :param other_password:
    :return:
    '''
    return hmac.compare_digest(
        base64.b64decode(password_hash),
        hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            salt=current_app.config['PWD_HASH_SALT'],
            iterations=current_app.config['PWD_HASH_ITERATIONS']
        )
    )

def get_email_from_token(data):
    '''
    получение логина пользователя из  валидного токена
    :param data:
    :return:
    '''

    token = data['Authorization'].split('Bearer ')[-1]
    print(token)
    print(current_app.config['JWT_ALGORITHM'])
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=current_app.config['JWT_ALGORITHM'])
    print(data)
    email = data['email']
    return email

# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)
