import numpy as np
from torchvision.transforms import transforms
from flask import Blueprint, flash, request
from ctypes import *
from skimage import io
from flask import render_template
import pickle
import tensorflow as tf
bp=Blueprint("algorithm",__name__,url_prefix="/algorithm")
@bp.route('/')
def algorithm_root():
    return "这是算法网页"

@bp.route('/A1/',methods=["GET","POST"]) 
def A1():
    return render_template('/algorithms/A1.html')

@bp.route('/A2/',methods=["GET","POST"]) 
def A2():
    return render_template('/algorithms/A2.html')

@bp.route('/A3/',methods=["GET","POST"]) 
def A3():
    return render_template('/algorithms/A3.html')

@bp.route('/A4/',methods=["GET","POST"]) 
def A4():
    return render_template('/algorithms/A4.html')

@bp.route('/A5/',methods=["GET","POST"]) 
def A5():
    return render_template('/algorithms/A5.html')

@bp.route('/A6/',methods=["GET","POST"]) 
def A6():
    return render_template('/algorithms/A6.html')

@bp.route('/A7/',methods=["GET","POST"]) 
def A7():
    return render_template('/algorithms/A7.html')

@bp.route('/A8/',methods=["GET","POST"]) 
def A8():
    return render_template('/algorithms/A8.html')

@bp.route('/A9/',methods=["GET","POST"]) 
def A9():
    return render_template('/algorithms/A9.html')

@bp.route('/A10/',methods=["GET","POST"]) 
def A10():
    return render_template('/algorithms/A10.html')

@bp.route('/A11/',methods=["GET","POST"]) 
def A11():
    return render_template('/algorithms/A11.html')

@bp.route('/A12/',methods=["GET","POST"]) 
def A12():
    return render_template('/algorithms/A12.html')

@bp.route('/A13/',methods=["GET","POST"]) 
def A13():
    return render_template('/algorithms/A13.html')

@bp.route('/A14/',methods=["GET","POST"]) 
def A14():
    return render_template('/algorithms/A14.html')

@bp.route('/A15/',methods=["GET","POST"]) 
def A15():
    return render_template('/algorithms/A15.html')

@bp.route('/A16/',methods=["GET","POST"]) 
def A16():
    return render_template('/algorithms/A16.html')

@bp.route('/A17/',methods=["GET","POST"]) 
def A17():
    return render_template('/algorithms/A17.html')

@bp.route('/A18/',methods=["GET","POST"]) 
def A18():
    return render_template('/algorithms/A18.html')

@bp.route('/A19/',methods=["GET","POST"]) 
def A19():
    return render_template('/algorithms/A19.html')

@bp.route('/A20/',methods=["GET","POST"]) 
def A20():
    return render_template('/algorithms/A20.html')

@bp.route('/A21/',methods=["GET","POST"]) 
def A21():
    return render_template('/algorithms/A21.html')
