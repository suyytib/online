# from torchvision.transforms import transforms
from flask import Blueprint
from ctypes import *
# from skimage import io
from flask import render_template
bp=Blueprint("deplaning",__name__,url_prefix="/deplaning")
@bp.route('/')
def deplaning_root():
    return "这是解刨网页"
@bp.route("/A/<A_id>")
def all_a(A_id):
    return render_template(f"/deplaning/A{A_id}.html")