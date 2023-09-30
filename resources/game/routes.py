from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.users.UserModel import UserModel

from .GameModel import GameModel, GamerTag, Achievement
from schemas import GameSchema , GamerTagSchema, AchievementSchema
from . import bp


@bp.route('/')
class GameList(MethodView):
  
  @jwt_required()
  @bp.response(200, GameSchema(many=True))
  def get(self):
    return GameModel.query.all()

  @jwt_required()
  @bp.arguments(GameSchema)
  @bp.response(200, GameSchema)
  def post(self, game_data):
    user_id = get_jwt_identity()
    p = GameModel(**game_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<game_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, GameSchema)
  def get(self, game_id):
    p = GameModel.query.get(game_id)
    if p:
      return p
    abort(400, message='Invalid Game Id')

  @jwt_required()
  @bp.arguments(GameSchema)
  @bp.response(200, GameSchema)
  def put(self, game_data, game_id):
    p = GameModel.query.get(game_id)
    if p and game_data['body']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = game_data['body']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Game Data')

  @jwt_required()
  def delete(self, game_id):
     user_id = get_jwt_identity()
     p = GameModel.query.get(game_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'game Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid game Id')


@bp.route('/')
class GamerTagList(MethodView):
  
  @jwt_required()
  @bp.response(200, GamerTag(many=True))
  def get(self):
    return GamerTag.query.all()

  @jwt_required()
  @bp.arguments(GamerTagSchema)
  @bp.response(200, GamerTagSchema)
  def post(self, gamertag_data):
    user_id = get_jwt_identity()
    p = GameModel(**gamertag_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<gamertag_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, GamerTagSchema)
  def get(self, game_id):
    p = GamerTag.query.get(game_id)
    if p:
      return p
    abort(400, message='Invalid Gamer Tag')

  @jwt_required()
  @bp.arguments(GamerTagSchema)
  @bp.response(200, GamerTagSchema)
  def put(self, game_data, game_id):
    p = GamerTag.query.get(game_id)
    if p and game_data['gamertag']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = game_data['gamertag']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid gamer Data')

  @jwt_required()
  def delete(self, game_id):
     user_id = get_jwt_identity()
     p = GameModel.query.get(game_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'game Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid game Id')
