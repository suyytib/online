# from torchvision.transforms import transforms
from flask import Blueprint, request
from flask import render_template
from functool import captcha__is_login
from model import Comment
# import tensorflow as tf
bp=Blueprint("deeplearning",__name__,url_prefix="/deeplearning")
@bp.route('/A1')
@captcha__is_login
def A1():
    comment = Comment.query.filter(Comment.tieba_id == 1)
    return render_template(f'/deeplearning/A1.html', comment=comment)

@bp.route('/A2',methods=["GET","POST"])
@captcha__is_login
def A2():
    if request.method == "GET":
        comment = Comment.query.filter(Comment.tieba_id == 2)
        return render_template(f'/deeplearning/A2.html', comment=comment)

@bp.route('/A3',methods=["GET","POST"])
@captcha__is_login
def A3():
    if request.method == "GET":
        comment = Comment.query.filter(Comment.tieba_id == 3)
        return render_template(f'/deeplearning/A3.html', comment=comment)


@bp.route('/A4')
@captcha__is_login
def A4():
    comment = Comment.query.filter(Comment.tieba_id == 4)
    return render_template(f'/deeplearning/A4.html', comment=comment)

@bp.route('/A5')
@captcha__is_login
def A5():
    comment = Comment.query.filter(Comment.tieba_id == 5)
    return render_template(f'/deeplearning/A5.html', comment=comment)
