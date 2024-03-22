from blueprints.table_config import db
class User(db.Model):
    __tablename__="user"
    username=db.Column(db.Integer,primary_key=True,autoincrement=True)
    password=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(255),nullable=False)
    