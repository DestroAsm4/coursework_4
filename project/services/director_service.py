from typing import Optional

from project.dao.director import DirectorDAO
from project.exceptions import ItemNotFound
from project.models import Director

class DirectorService:

    def __init__(self, dao: DirectorDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        '''
        Сервис получения одного режисера
        :param pk:
        :return:
        '''
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        '''
        Сервис получения списка всех режисеров
        :param page:
        :return:
        '''
        return self.dao.get_all(page=page)
