import os

DEBUG = True

MONGO_DBNAME = os.environ.get('MONGO_DB', 'gitshots')
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_POST', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', None)
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', None)

CACHE_TYPE = 'filesystem'
CACHE_DIR = 'static/imgs'

UPLOAD_FOLDER = 'uploads'

MAX_CONTENT_LENGTH = 4 * 1024 * 1024  # No more than 4MB per filesystem