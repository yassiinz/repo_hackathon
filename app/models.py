from .extentions import db

class Cementeries(db.Model):
    __tablename__ = "cementeries"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True)
    code = db.Column(db.String(150), index=True, unique=True)
