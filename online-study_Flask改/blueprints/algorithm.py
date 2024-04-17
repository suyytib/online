import numpy as np
# from torchvision.transforms import transforms
from flask import Blueprint, flash, request
from ctypes import *
# from skimage import io
from flask import render_template
import pickle
# import tensorflow as tf
bp=Blueprint("algorithm",__name__,url_prefix="/algorithm")
@bp.route('/')
def algorithm_root():
    return "这是算法网页"
@bp.route("/A/<A_id>")
def all_a(A_id):
    return render_template(f"/algorithms/A{A_id}.html")