from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from resources.users import bp as user_bp
api.register_blueprint(user_bp)
from resources.game import bp as game_bp
api.register_blueprint(game_bp)

from resources.users import routes
from resources.game import routes

from resources.users.UserModel import UserModel
from resources.game.GameModel import GameModel
