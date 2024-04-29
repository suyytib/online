from flask import Flask
from blueprints.login import bp as login_bp
from blueprints.box import bp as box_bp
from blueprints.tieba import bp as tieba_bp
from blueprints.deeplearning import bp as deeplearning_bp
from blueprints.deplaning import bp as deplaning_bp
from blueprints.imageprocessing import bp as imageprocessing_bp
from table_config import db,migrate,mail
import config
from flask import session
from flask import g
from flask import render_template
from model import User
# flask默认去templates文件夹下面找渲染的html文件

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(box_bp)
app.register_blueprint(tieba_bp)
app.register_blueprint(deplaning_bp)
app.register_blueprint(deeplearning_bp)
app.register_blueprint(imageprocessing_bp)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)
mail.init_app(app)
# 这是获取登录状态函数,用于保持用户登录状态，只要session还在，用户下次进入该网站可以免登录
@app.before_request
def captcha_login():
    temp=session.get("user_id")
    if temp:
        user=User.query.get(temp)
        setattr(g,"user_id",user.id)
    else:
        setattr(g,"user_id",None)
        
@app.route('/')
def root():
    return render_template("root.html")

if __name__ == '__main__':
    app.run(debug=True)
