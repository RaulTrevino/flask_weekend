from app import db

class GameModel(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key = True)
    game_name = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return f'<Game: {self.game_name}>'

   

class GamerTag(db.Model):
    __tablename__ = 'gamertag'
    id = db.Column(db.Integer, primary_key = True)
    gamertag = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

   
class Achievement(db.Model):
    __tablename__ = 'achievement'
    id = db.Column(db.Integer, primary_key = True)
    achievement = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)


