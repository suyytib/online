import numpy as np
# from torchvision.transforms import transforms
from flask import Blueprint, flash, request
from ctypes import *
# from skimage import io
from flask import render_template
import pickle

from functool import captcha__is_login
from model import Comment, Tieba
# import tensorflow as tf
bp=Blueprint("deeplearning",__name__,url_prefix="/deeplearning")
@bp.route('/')
@captcha__is_login
def deeplearning_root():
    return render_template("/deeplearning.html")

@bp.route('/A1/')
def A1():
    comment = Comment.query.filter(Comment.tieba_id == 1)
    return render_template('/deeplearning/A1.html', comment=comment)