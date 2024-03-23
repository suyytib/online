from blueprints.table_config import db
# 用户表
class User(db.Model):
    # 创建的数据库表名
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(10),nullable=False)
    password=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(255),nullable=False)