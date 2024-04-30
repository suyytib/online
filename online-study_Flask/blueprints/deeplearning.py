# from torchvision.transforms import transforms
from flask import Blueprint, request
from flask import render_template
import numpy as np
import tensorflow as tf
from keras.models import load_model
import skimage.io as io  
from functool import captcha__is_login
from model import Comment
# import tensorflow as tf
bp=Blueprint("deeplearning",__name__,url_prefix="/deeplearning")
@bp.route('/A1')
@captcha__is_login
def A1():
    comment = Comment.query.filter(Comment.tieba_id == 1)
    return render_template(f'/deeplearning/A1.html', comment=comment)

@bp.route('/A2',methods=["GET","POST"])
@captcha__is_login
def A2():
    if request.method == "GET":
        comment = Comment.query.filter(Comment.tieba_id == 2)
        return render_template(f'/deeplearning/A2.html', comment=comment)
    else:
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
        return render_template('/deeplearning/A2.html')

@bp.route('/A3',methods=["GET","POST"])
@captcha__is_login
def A3():
    if request.method == "GET":
        comment = Comment.query.filter(Comment.tieba_id == 3)
        return render_template(f'/deeplearning/A3.html', comment=comment)
    else:
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
        return render_template('/deeplearning/A3.html',**context)


@bp.route('/A4')
@captcha__is_login
def A4():
    comment = Comment.query.filter(Comment.tieba_id == 4)
    return render_template(f'/deeplearning/A4.html', comment=comment)

@bp.route('/A5')
@captcha__is_login
def A5():
    comment = Comment.query.filter(Comment.tieba_id == 5)
    return render_template(f'/deeplearning/A5.html', comment=comment)