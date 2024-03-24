import random
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_mail import Message
from config import MAIL_DEFAULT_SENDER
from blueprints.table_config import mail,db
from blueprints.forms import Login_Form, Register_Form
from blueprints.model import User
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
    # 你get哪里来的数据
    if request.method == "GET":
        return render_template('/login/register.html')
    else:
        number_list=[]
        number_list=[str(i) for i in range(10)]
        temp_password=''.join(random.choices(number_list,k=6))
        print(temp_password)
        user_temp_password=request.form.get("temp_password")
        form=Register_Form(request.form)
        msg=Message(subject='懒人tool网站验证码发送',
                    body=f'验证码:{temp_password}谢谢您注册懒人tool在线学习平台,望您使用开心',
                    recipients=[form.email.data])
        mail.send(msg)
        if form.validate() and user_temp_password==temp_password:
            new_user=User(username=form.username.data , password=form.passwd.data , email=form.email.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login.login"))
        else:
            print(form.errors)
            return redirect(url_for('login.register'))
