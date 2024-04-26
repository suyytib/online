# from torchvision.transforms import transforms
from flask import Blueprint
from flask import render_template

from functool import captcha__is_login
from model import Comment
# import tensorflow as tf
bp=Blueprint("deeplearning",__name__,url_prefix="/deeplearning")
@bp.route('/')
def deeplearning_root():
    return render_template("/deeplearning.html")

@bp.route('/A1')
def A1():
    comment = Comment.query.filter(Comment.tieba_id == 1)
    return render_template(f'/deeplearning/A1.html', comment=comment)

@bp.route('/A2')
def A2():
    comment = Comment.query.filter(Comment.tieba_id == 2)
    return render_template(f'/deeplearning/A2.html', comment=comment)

@bp.route('/A3')
def A3():
    comment = Comment.query.filter(Comment.tieba_id == 3)
    return render_template(f'/deeplearning/A3.html', comment=comment)
