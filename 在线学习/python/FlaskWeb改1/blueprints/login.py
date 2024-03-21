from flask import Blueprint
from flask import render_template
# 定义蓝图类,该将类对象实现的视图函数,放到统一的login路径下方
# (访问路径均为:http://127.0.0.1:5100/login/对应视图函数的路径)
bp=Blueprint("login",__name__,url_prefix="/login")
@bp.route('/') # 访问路径:http://127.0.0.1:5100/login/
def login():
    return render_template('login.html')

#todo 实现登录的认证