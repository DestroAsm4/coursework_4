import logging

from project.config import config
from project.models import Genre
from project.server import create_app, db

logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)sset FLASK_APP=run.py')

app = create_app(config)


if __name__ == '__main__':
    app.run(port=25000)
