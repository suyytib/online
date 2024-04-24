# from torchvision.transforms import transforms
from flask import Blueprint
from ctypes import *
# from skimage import io
from flask import render_template

from functool import captcha__is_login
# import tensorflow as tf
bp=Blueprint("imageprocessing",__name__,url_prefix="/imageprocessing")
@bp.route('/')
@captcha__is_login
def imageprocessing_root():
    return render_template("/imageprocessing.html")