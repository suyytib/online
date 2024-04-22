import time
import numpy as np
# from torchvision.transforms import transforms
from flask import Blueprint, flash, g, request, session
from ctypes import *
# from skimage import io
from flask import render_template
from functool import captcha__is_login
from table_config import mail,db

from model import Comment, User
# import tensorflow as tf
bp=Blueprint("tieba",__name__,url_prefix="/tieba")
@bp.route('/')
@captcha__is_login
def tieba_root():
    return render_template("/tieba.html")

@bp.route('/writeBlog', methods=['POST', 'GET'])
@captcha__is_login
def writeblog():
    if request.method == 'GET':
        return render_template('tieba.html')
    else:
        title = request.form.get("title")
        text = request.form.get("text")
        username = session.get('username')
        # 获取当前系统时间
        create_time = time.strftime("%Y-%m-%d %H:%M:%S")
        user = User.query.filter(User.username == username).first()
        blog = blog(title=title, text=text, create_time=create_time, user_id=user.id)
        db.session.add(blog)
        db.session.commit()
        blog = blog.query.filter(blog.create_time == create_time).first()
        return render_template('blogSuccess.html', title=title, id=blog.id)
    
@bp.route('/comment/',methods=['POST']) 
def comment():
    text = request.values.get('text')
    tiebaId = request.values.get('tiebaId')
    user=User.query.get(g.user_id)
    username=user.username
    print(username)
    # 获取当前系统时间
    create_time = time.strftime("%Y-%m-%d %H:%M:%S")
    comment = Comment(text=text, create_time=create_time, tieba_id=tiebaId, user=username)
    db.session.add(comment)
    db.session.commit()
    return {
        'success': True,
        'message': '评论成功！',
    }