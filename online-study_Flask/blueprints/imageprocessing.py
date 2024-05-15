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
def A1():   #高斯模糊
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        X= image.filter(ImageFilter.GaussianBlur(radius=10))
        X.save('static/images/{}'.format("A1.png"))
        with open('static/images/{}'.format("A1.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A1.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A2/',methods=["POST"])
@captcha__is_login
def A2():   #图像锐化
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        X= image.filter(ImageFilter.SHARPEN)
        X.save('static/images/{}'.format("A2.png"))
        with open('static/images/{}'.format("A2.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A2.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A3/',methods=["POST"])
@captcha__is_login
def A3():   #图像平滑
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        X= image.filter(ImageFilter.SMOOTH)
        X.save('static/images/{}'.format("A3.png"))
        with open('static/images/{}'.format("A3.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A3.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A4/',methods=["POST"])
@captcha__is_login
def A4():   #图像配准
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
        cv2.imwrite('static/images/{}'.format("A4.png"), transformed_img)
        with open('static/images/{}'.format("A4.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A4.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except Exception as e:
        print(e)
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A5/',methods=["POST"])
@captcha__is_login
def A5():   #图像融合
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
        image = image.convert('RGBA')
        image2 = image2.convert('RGBA')
        X= Image.blend(image,image2,0.5)
        X.save('static/images/{}'.format("A5.png"))
        with open('static/images/{}'.format("A5.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A5.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A6/',methods=["POST"])
@captcha__is_login
def A6():   #伪彩色处理
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        image.save('static/images/{}'.format("A6.png"))
        im_gray = cv2.imread('static/images/{}'.format("A6.png"), cv2.IMREAD_GRAYSCALE)
        im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
        cv2.imwrite('static/images/{}'.format("A6.png"),im_color)
        with open('static/images/{}'.format("A6.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A6.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A7/',methods=["POST"])
@captcha__is_login
def A7():   #自动阈值分割
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        image.save('static/images/{}'.format("A6.png"))
        image = cv2.imread('static/images/{}'.format("A6.png"), cv2.IMREAD_GRAYSCALE)
        ratio=0.15
        I_mean = cv2.boxFilter(image, cv2.CV_32FC1, (5, 5))
        out = image - (1.0 - ratio) * I_mean
        out[out >= 0] = 255
        out[out < 0] = 0
        out = out.astype(np.uint8)
        cv2.imwrite('static/images/{}'.format("A7.png"),out)
        with open('static/images/{}'.format("A7.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A7.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A8/',methods=["POST"])
@captcha__is_login
def A8():   #直方图均衡化
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        gray_image = image.convert('L')
        gray_arr = np.array(gray_image)
        hist, bins = np.histogram(gray_arr, 255)
        cdf = np.cumsum(hist)
        cdf = 255 * (cdf/cdf[-1])
        res = np.interp(gray_arr.flatten(), bins[:-1], cdf)
        res = res.reshape(gray_arr.shape)
        image=Image.fromarray(res.astype(np.uint8))
        image.save('static/images/{}'.format("A8.png"))
        with open('static/images/{}'.format("A8.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A8.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except:
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A9/',methods=["POST"])
@captcha__is_login
def A9():   #图像压缩
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        image.save('static/images/{}'.format("A9.png"))
        image = cv2.imread('static/images/{}'.format("A9.png"), cv2.IMREAD_GRAYSCALE)
        params = [cv2.IMWRITE_PNG_COMPRESSION, 3]
        msg = cv2.imencode(".png", image, params)[1]
        msg = (np.array(msg)).tostring()
        os.remove('static/images/{}'.format("A9.png")) 
        msg = base64.b64encode(msg)
        msg=str(msg,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": msg})
    except Exception as e:
        print(e)
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A10/',methods=["POST"])
@captcha__is_login
def A10():   #图像解压
    try:
        img=request.form.get('data')
        img_data = base64.b64decode(img)
        nparr = np.frombuffer(img_data, dtype=np.uint8)
        img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite('static/images/{}'.format("A10.png"), img_decode) 
        with open('static/images/{}'.format("A10.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A10.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except Exception as e:
        print(e)
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A11/',methods=["POST"])
@captcha__is_login
def A11():   #仿射变换
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        image.save('static/images/{}'.format("A11.png"))
        src = cv2.imread('static/images/{}'.format("A11.png"))
        rows, cols = src.shape[: 2]
        post1 = np.float32([[50, 50], [200, 50], [50, 200]])
        post2 = np.float32([[10, 100], [200, 50], [100,250]])
        M = cv2.getAffineTransform(post1, post2)
        result = cv2.warpAffine(src, M, (rows, cols))
        cv2.imwrite('static/images/{}'.format("A11.png"),result) 
        with open('static/images/{}'.format("A11.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A11.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except Exception as e:
        print(e)
        return jsonify({"code":404, "message": "fail!", "datas": None})
    
@bp.route('/A12/',methods=["POST"])
@captcha__is_login
def A12():   #HOG特征提取
    try:
        img=request.form.get('data')
        head,context=img.split(",")
        img_data = base64.b64decode(context)
        image = Image.open(BytesIO(img_data))
        image.save('static/images/{}'.format("A12.png"))
        image = cv2.imread('static/images/{}'.format("A12.png"),cv2.IMREAD_GRAYSCALE)
        image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        hog = cv2.HOGDescriptor()
        features = hog.compute(image)
        hog_image = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
        for i in range(features.shape[0]):
            hog_image[int(features[i][1]), int(features[i][0])] = features[i][2]
        cv2.imwrite('static/images/{}'.format("A12.png"),hog_image) 
        with open('static/images/{}'.format("A12.png"),'rb') as f:
            image_base64 = base64.b64encode(f.read())
        os.remove('static/images/{}'.format("A12.png")) 
        image_base64=str(image_base64,'utf-8')
        return jsonify({"code":200, "message": "success!", "datas": image_base64})
    except Exception as e:
        print(e)
        return jsonify({"code":404, "message": "fail!", "datas": None})
