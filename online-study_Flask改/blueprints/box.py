import numpy as np
# from torchvision.transforms import transforms
from flask import Blueprint, flash, request
from ctypes import *
# from skimage import io
from flask import render_template
import pickle
# import tensorflow as tf
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
    if request.method == "GET":
        return render_template('/root/Digitalprediction.html')
    img=request.files.get('pic')
    img.save("1.jpg")
    img_src = io.imread("1.jpg")
    print(img_src)
    transform = transforms.Compose([transforms.ToTensor()])
    X = transform(img_src)
    print(X)
    with open('my_model.pkl', 'rb') as f:
        model = pickle.load(f)
    # predict using the loaded model
    y_pred=np.argmax(model.predict(X),axis=1)
    flash(y_pred)
    return render_template('/root/Digitalprediction.html')
