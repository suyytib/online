# from torchvision.transforms import transforms
from flask import Blueprint
from flask import render_template

from functool import captcha__is_login
from model import Comment
# import tensorflow as tf
bp=Blueprint("deeplearning",__name__,url_prefix="/deeplearning")
@bp.route('/')
@captcha__is_login
def deeplearning_root():
    return render_template("/deeplearning.html")

@bp.route('/A/<A_id>')
def all_a(A_id):
    comment = Comment.query.filter(Comment.tieba_id == A_id)
    return render_template(f'/deeplearning/A{A_id}.html', comment=comment)