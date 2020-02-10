
import os

_basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TEMPLATE_DIR = os.path.join(_basedir, 'application', 'templates')

class BaseConfig(object):
    MONGODB_SETTINGS = {
        'db': 'auflux',
        'host': 'localhost',
        'port': 27017,
    }

    USER_DB_CONFIG = {
        'alias': 'user_db',
        'name': 'user_db',
        'host': 'localhost',
        'port': 27017,
    }

    DATA_DB_CONFIG = {
        'alias': 'data_db',
        'name': 'data',
        'host': 'localhost',
        'port': 27017,
    }

    INVENTORY_DB_CONFIG = {
        'alias': 'inventory_db',
        'name': 'inventory',
        'host': 'localhost',
        'port': 27017,
    }

    #flask_login
    SECRET_KEY = 'dj9023tyu829-9!((()$U(*$*!(4790'
