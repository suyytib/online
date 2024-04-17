import numpy as np
from flask import Blueprint, flash, request
from ctypes import *
from flask import render_template
import pickle
bp=Blueprint("deplaning",__name__,url_prefix="/deplaning")
@bp.route('/')
def deplaning_root():
    return "这是解刨网页"
@bp.route("/A/<A_id>")
def all_a(A_id):
    return render_template(f"/deplaning/A{A_id}.html")