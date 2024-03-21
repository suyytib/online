from flask import Blueprint
from flask import render_template
from flask import request
# 实例化蓝图对象,该对象用于生成视图函数,这些函数都在蓝图的指定url为基础上绑定各自的url
bp=Blueprint("login",__name__,url_prefix='/login')
@bp.route('/') # 登录视图函数
def login():
    return render_template('login.html')
@bp.route('/register', methods=['GET', 'POST'])
def register():   # 注册视图函数
    if request.method == "GET":
        return render_template('register.html')
    else:
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        print(username, passwd)
        get_info = request.args
        return get_info