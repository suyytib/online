# python的第三方模块
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_mail import Message
from flask import jsonify
from flask import session
from flask import flash
from flask import get_flashed_messages
# python的内置模块
import random

# 自己写的python模块
from table_config import mail
from table_config import db
from forms import Login_Form, Retrieve_Form
from forms import Register_Form
from model import User
from model import Captcha
# 实例化蓝图对象,该对象用于生成视图函数,这些函数都在蓝图的指定url为基础上绑定各自的url
bp=Blueprint("login",__name__,url_prefix='/login')

@bp.route('/',methods=["GET"])
def login():
    temp:dict=get_flashed_messages()
    if temp:
        temp=temp[0]
    temp_error_tuple=("user_name","user_passwd")
    temp_tuple=("username_error","password_error")
    temp_dict={"username_error":None,"password_error":None}
    for i in range(len(temp)):
        temp_dict[temp_tuple[i]]=temp.get(temp_error_tuple[i])
        if temp_dict[temp_tuple[i]]:
            temp_dict[temp_tuple[i]]=temp_dict[temp_tuple[i]][0]
    return render_template('login/login.html',**temp_dict)

@bp.route('/captcha/',methods=["POST"])
def login_captcha():
    form=Login_Form(request.form)
    # 成功回到主页,不成功回到登录
    if form.validate():
        user=User.query.filter_by(username=form.user_name.data).first()
        if user and (user.password==form.user_passwd.data):
            session["user_id"]=user.id
            return redirect(url_for('root'))
        return redirect(url_for('login.login'))
    else:
        # 将表单验证的错误消息发送给登录网页
        flash(message=form.errors)
        return redirect(url_for('login.login'))
    
@bp.route('/register/', methods=['GET'])
def register():   # 注册视图函数
    temp=get_flashed_messages()
    if temp:
        temp=temp[0]
    if temp=="用户名已存在":
        return render_template('/login/register.html',usernames=temp)
    if temp=="邮箱已注册":
        return render_template('/login/register.html',usernames=temp)
    temp_error_tuple=("username","passwd","re_password","email")
    temp_tuple=("username_error","password_error","re_password_error","email_error")
    temp_dict={"username_error":None,"password_error":None,"re_password_error":None,"email_error":None}
    for i in range(len(temp)):
        temp_dict[temp_tuple[i]]=temp.get(temp_error_tuple[i])
        if temp_dict[temp_tuple[i]]:
            temp_dict[temp_tuple[i]]=temp_dict[temp_tuple[i]][0]
    return render_template('/login/register.html',**temp_dict)

# 注册验证
@bp.route('/register/captcha/',methods=["POST"])
def register_captcha():
    form=Register_Form(request.form)
    # 从数据库中查找验证码
    true_captcha=Captcha.query.filter_by(email=form.email.data).all()
    usera=User.query.filter_by(username=form.username.data).first()
    emaila=User.query.filter_by(email=form.email.data).first()
    if usera:
        flash(message="用户名已存在")
        return redirect(url_for('login.register'))
    if emaila:
        flash(message="邮箱已注册")
        return redirect(url_for('login.register'))
    # 判断验证是否成功，以及查询对象是否存在
    if form.validate() and true_captcha:
        # 判断查找到的验证码是否匹配
        if request.form.get("captcha")==true_captcha[-1].captcha:
            # 创建用户并同步到数据库
            new_user=User(username=form.username.data , password=form.passwd.data , email=form.email.data)
            db.session.add(new_user)
            db.session.commit()
            # 重定向到登陆界面
            return redirect(url_for("login.login"))
    # 重定向到注册
    flash(message=form.errors)
    return redirect(url_for('login.register'))

# 邮箱发送验证码
@bp.route('/register/email_send/')
def email_send():
    # 获取邮箱地址
    email=request.args.get("email")
    # 生成验证码
    number_list=[str(i) for i in range(10)]
    captcha=''.join(random.choices(number_list,k=6))
    # 生成邮箱消息
    msg=Message(subject='医影智学tool网站验证码发送',body=f'验证码:{captcha},谢谢您注册医影智学tool在线学习平台,望您使用开心',
                recipients=[email])
    # 发送邮箱
    mail.send(msg)
    # 将生成的验证码和对应邮箱上传到数据库
    temp=Captcha(email=email,captcha=captcha)
    db.session.add(temp)
    db.session.commit()
    # 返回json字符串作为jquery的ajax获取结果
    return jsonify({"code":200, "message": "success!", "data": None})

@bp.route('/retrieve/', methods=['GET'])
def retrieve():   # 注册视图函数
    temp=get_flashed_messages()
    if temp:
        temp=temp[0]
    temp_error_tuple=("passwd","re_password","email")
    temp_tuple=("password_error","re_password_error","email_error")
    temp_dict={"password_error":None,"re_password_error":None,"email_error":None}
    for i in range(len(temp)):
        temp_dict[temp_tuple[i]]=temp.get(temp_error_tuple[i])
        if temp_dict[temp_tuple[i]]:
            temp_dict[temp_tuple[i]]=temp_dict[temp_tuple[i]][0]
    return render_template('/login/retrieve.html',**temp_dict)

@bp.route('/retrieve/captcha/',methods=["POST"])
def retrieve_captcha():
    form=Retrieve_Form(request.form)
    usera=User.query.filter_by(email=form.email).first()
    if form.validate() and usera and usera.password==form.password.data:
        new_user=User(username=form.username.data , password=form.re_password.data , email=form.email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login.login"))
    flash(message=form.errors)
    return redirect(url_for('login.retrieve'))

@bp.route('/retrieve/retrieve_send/')
def retrieve_send():
    email=request.args.get("email")
    usera=User.query.filter_by(email=email).first()
    passa=usera.password
    msg=Message(subject='医影智学tool网站密码发送',body=f'原密码:{passa},谢谢您登录医影智学tool在线学习平台,望您使用开心',
            recipients=[email])
    mail.send(msg)
    return jsonify({"code":200, "message": "success!", "data": None})
    