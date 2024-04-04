from flask import Blueprint, request
from ctypes import *
from flask import render_template
bp=Blueprint("box",__name__,url_prefix="/box")
@bp.route('/')
def box_root():
    return "这是工具网页"

@bp.route('/choujiang/',methods=["GET","POST"]) 
def choujiang():
    return render_template('/root/choujiang.html')

@bp.route('/text/',methods=["GET","POST"]) 
def text():
    return render_template('/root/text.html')

@bp.route('/Digitalprediction/',methods=["GET","POST"]) 
def Digitalprediction():
    return render_template('/root/Digitalprediction.html')
