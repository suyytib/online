from flask import Blueprint
from flask import render_template
from blueprints.model import User
from blueprints.table_config import db

bp=Blueprint("root",__name__,url_prefix="/")

@bp.route('/')
def root():
    return render_template('root.html')
@bp.route("/h1/")
def func():
    user=User(username='张三',password='111111',email='123456')
    db.session.add(user)
    db.session.commit()
    return "true"