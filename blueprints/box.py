import time
from cv2 import imshow
import cv2
import numpy as np
import torch
from torchvision.transforms import transforms
from flask import Blueprint, flash, make_response, request, send_file, session
from ctypes import *
from table_config import db
from skimage import io
from flask import render_template
from keras.models import load_model
import pickle
import tensorflow as tf
from PIL import Image,ImageFilter
from model import User,Comment,Tieba
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
        return render_template('/deeplearning/A1.html')
    img=request.files.get('pic')
    img.save("1.jpg")
    img_src = io.imread("1.jpg")
    print(img_src.shape)
    img_src=img_src[:,:,1]
    print(img_src.shape)
    X=tf.reshape(img_src,(1,28,28))
    model = load_model('modea.h5')
    y_pred=np.argmax(model.predict(X),axis=1)
    # predict using the loaded model
    context = {'y_pred': str(y_pred[0])}
    return render_template('/deeplearning/A1.html',**context)

@bp.route('/Grayscale/',methods=["GET","POST"]) 
def Grayscale():
    if request.method == "GET":
        return render_template('/imageprocessing/A1.html')
    img=request.files.get('pic')
    img.save('static/images/{}'.format("A1.jpg"))
    image=Image.open('static/images/{}'.format("A1.jpg"))
    X=image.convert('L')
    X.save('static/images/{}'.format("B1.jpg"))
    return send_file('static/images/{}'.format("B1.jpg"))

@bp.route('/Binarization/',methods=["GET","POST"]) 
def Binarization():
    if request.method == "GET":
        return render_template('/imageprocessing/A2.html')
    img=request.files.get('pic')
    img.save('static/images/{}'.format("A2.jpg"))
    image=Image.open('static/images/{}'.format("A2.jpg"))
    threshold  = 50 
    table  =  []
    for  i  in  range( 256 ):
        if  i  <  threshold:
            table.append(0)
        else :
            table.append(1)
    #  convert to binary image by the table 
    X  =  image.point(table,"1" )
    """ X=image.convert('1') """
    X.save('static/images/{}'.format("B2.jpg"))
    return send_file('static/images/{}'.format("B2.jpg"))

@bp.route('/gaussian/',methods=["GET","POST"]) 
def gaussian():
    if request.method == "GET":
        return render_template('/imageprocessing/A3.html')
    img=request.files.get('pic')
    img.save('static/images/{}'.format("A3.jpg"))
    image=Image.open('static/images/{}'.format("A3.jpg"))
    X= image.filter(ImageFilter.GaussianBlur(radius=10))
    X.save('static/images/{}'.format("B3.jpg"))
    return send_file('static/images/{}'.format("B3.jpg"))