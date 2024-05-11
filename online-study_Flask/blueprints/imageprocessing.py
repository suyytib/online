# from torchvision.transforms import transforms
import base64
from io import BytesIO
import os
import cv2
from flask import Blueprint, jsonify, request
# from skimage import io
from flask import render_template
from PIL import Image,ImageFilter
import numpy as np
from functool import captcha__is_login
from model import Comment
# import tensorflow as tf
bp=Blueprint("imageprocessing",__name__,url_prefix="/imageprocessing")
@bp.route('/',methods=["GET","POST"])
@captcha__is_login
def imageprocessing_root():
    if request.method == "GET":
        comment = Comment.query.filter(Comment.tieba_id == 0)
        return render_template(f'imageprocessing.html', comment=comment)

@bp.route('/A1/',methods=["POST"])
@captcha__is_login
def A1():
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        X= image.filter(ImageFilter.GaussianBlur(radius=10))
        X.save('static/images/{}'.format("A1.jpg"))
        with open('static/images/{}'.format("A1.jpg"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A1.jpg")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A2/',methods=["POST"])
@captcha__is_login
def A2():
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        X= image.filter(ImageFilter.SHARPEN)
        X.save('static/images/{}'.format("A2.jpg"))
        with open('static/images/{}'.format("A2.jpg"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A2.jpg")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A3/',methods=["POST"])
@captcha__is_login
def A3():
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        X= image.filter(ImageFilter.SMOOTH)
        X.save('static/images/{}'.format("A3.jpg"))
        with open('static/images/{}'.format("A3.jpg"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A3.jpg")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A4/',methods=["POST"])
@captcha__is_login
def A4():
    try:
        img=request.form.get('data')
        img1=request.form.get('data1')
        head,context=img.split(",")
        head1,context1=img1.split(",")
        img_data = base64.b64decode(context)
        img1_data = base64.b64decode(context1)
        image = Image.open(BytesIO(img_data))
        image2 = Image.open(BytesIO(img1_data))
        img1 = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(np.asarray(image2), cv2.COLOR_BGR2GRAY)
        height, width = img2.shape
        orb = cv2.ORB_create(5000)
        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)
        matches = matches[:int(len(matches)*0.9)]
        no_of_matches = len(matches)
        p1 = np.zeros((no_of_matches, 2))
        p2 = np.zeros((no_of_matches, 2))
        for i in range(len(matches)):
            p1[i, :] = kp1[matches[i].queryIdx].pt
            p2[i, :] = kp2[matches[i].trainIdx].pt
        homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)
        transformed_img = cv2.warpPerspective(img1,homography, (width, height))
        cv2.imwrite('static/images/{}'.format("A4.jpg"), transformed_img)
        with open('static/images/{}'.format("A4.jpg"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A4.jpg")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except Exception as e:
        print(e)
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A5/',methods=["POST"])
@captcha__is_login
def A5():
    try:
        img=request.form.get('data')
        img1=request.form.get('data1')
        head,context=img.split(",")
        head1,context1=img1.split(",")
        img_data = base64.b64decode(context)
        img1_data = base64.b64decode(context1)
        image = Image.open(BytesIO(img_data))
        image = image.resize((400,400)) 
        image2 = Image.open(BytesIO(img1_data))
        image2 = image2.resize((400,400)) 
        X= Image.blend(image,image2,0.5)
        X.save('static/images/{}'.format("A5.jpg"))
        with open('static/images/{}'.format("A5.jpg"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A5.jpg")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})