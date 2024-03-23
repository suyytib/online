from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_mail import Message
from blueprints.table_config import mail
from blueprints.forms import Register_Form,Login_Form
import random
# 实例化蓝图对象,该对象用于生成视图函数,这些函数都在蓝图的指定url为基础上绑定各自的url
bp=Blueprint("login",__name__,url_prefix='/login')

@bp.route('/',methods=["GET","POST"]) # 登录视图函数
def login():
    if request.method=="GET":
        return render_template('login/login.html')
    else:
        login_form=Login_Form()
        if login_form.validate():
            return redirect(url_for('root.root'))
        else:
            return redirect(url_for('login.login'))
        
@bp.route('/register/', methods=['GET', 'POST'])
def register():   # 注册视图函数
    if request.method == "GET":
        return render_template('/login/register.html')
    else:
        # username = request.form.get("username")
        # passwd = request.form.get("passwd")
        # 使用4位随机数验证码
        temp_password=''.join(random.choices(number_list,k=4))
        user_temp_password=request.form.get("temp_password")
        email=request.form.get("email")
        # print(email)
        number_list=[i for i in range(10)]
        msg=Message(subject='懒人tool网站验证码发送',
                    body=f'验证码:{temp_password}谢谢您注册懒人tool在线学习平台,望您使用开心',
                    recipients=[email])
        mail.send(msg)
        # 参与验证
        register_form=Register_Form()
        # 验证成功进入登陆界面，失败重回注册界面
        if register_form.validate() and user_temp_password==temp_password:
            return redirect(url_for("login.login"))
        else:
            return redirect(url_for('login.register'))
        