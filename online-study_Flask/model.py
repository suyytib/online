from table_config import db
# 用户表
class User(db.Model):
    # 创建的数据库表名
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(10),nullable=False)
    password=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(255),nullable=False)

class Captcha(db.Model):
    __tablename__="captcha"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(255),nullable=False)
    captcha=db.Column(db.String(255),nullable=False)

class Tieba(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    text = db.Column(db.TEXT)
    create_time = db.Column(db.String(64))
    user = db.Column(db.String(256))

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(256))    # 评论内容
    create_time = db.Column(db.String(64))
    # 关联博客id
    tieba_id = db.Column(db.Integer)
    user = db.Column(db.String(256))

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer = db.Column(db.String(256))    # 评论内容
    question = db.Column(db.String(256))