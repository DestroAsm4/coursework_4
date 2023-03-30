from flask_restx import Resource, Namespace
from flask import request

from project.container import user_service
from project.setup.api.models import movie
from project.tools.security import get_email_from_token

from project.container import movie_service

favorites_ns = Namespace('favorites')

@favorites_ns.route('/movies/')
class FavoriteMoviesView(Resource):
    @favorites_ns.marshal_with(movie, as_list=True)
    def get(self):
        """
        """
        email = get_email_from_token(request.headers)
        print(request.headers)
        return user_service.get_favorites(email)

@favorites_ns.route('/movies/<int:mid>')
class FavoriteMovieView(Resource):
    def post(self, mid):
        '''
        :param mid:
        :return:
        '''

        return request.headers.get_all()