from flask_mongoengine import MongoEngine
db = MongoEngine()

from flask_login import LoginManager
login_manager = LoginManager()

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask_babel import Babel
babel = Babel()

from flask_admin import Admin
admin = Admin()

from flask_mail import Mail
mail = Mail()

from flask_principal import Principal
principal = Principal()