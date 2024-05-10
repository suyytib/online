# 导入 Flask 类，用于创建 Flask web 应用程序实例  
from flask import Flask  
  
# 导入不同的蓝图（Blueprints），它们表示应用程序的不同部分或功能。每个蓝图都是一个可重用的小应用程序  
from blueprints.login import bp as login_bp  
from blueprints.box import bp as box_bp  
from blueprints.tieba import bp as tieba_bp  
from blueprints.deeplearning import bp as deeplearning_bp  
from blueprints.deplaning import bp as deplaning_bp  
from blueprints.imageprocessing import bp as imageprocessing_bp   
from blueprints.onlinetesting import bp as onlinetesting
  
# 导入数据库配置和其他相关配置  
from table_config import db, migrate, mail  
  
# 导入配置模块，它通常包含 Flask 应用程序的配置设置  
import config  
  
# 导入 Flask 的 session 对象，用于在多个请求之间存储用户会话数据  
from flask import session  
  
# 导入 Flask 的 g 对象，它是一个特殊的对象，可以在请求的生命周期内存储数据  
from flask import g  
  
# 导入 Flask 的 render_template 函数，用于渲染 HTML 模板  
from flask import render_template  
  
# 导入 User 模型，通常用于与数据库中的用户表进行交互  
from model import User  

# 创建一个 Flask web 应用程序实例  
app = Flask(__name__)  
  
# 注册蓝图到 Flask 应用程序，使它们成为应用程序的一部分  
app.register_blueprint(login_bp)  
app.register_blueprint(box_bp)  
app.register_blueprint(tieba_bp)  
app.register_blueprint(deplaning_bp)  
app.register_blueprint(deeplearning_bp)  
app.register_blueprint(onlinetesting) 
app.register_blueprint(imageprocessing_bp)  

# 从 config 模块加载 Flask 应用程序的配置设置  
app.config.from_object(config)  
  
# 初始化数据库连接并将其绑定到 Flask 应用程序  
db.init_app(app)  
  
# 初始化数据库迁移工具并将其绑定到 Flask 应用程序  
migrate.init_app(app, db)  
  
# 初始化邮件发送功能并将其绑定到 Flask 应用程序  
mail.init_app(app)  

# 这是一个在请求之前运行的函数，用于检查用户是否已登录  
# 如果用户已登录，它将用户的 ID 存储在 Flask 的 g 对象中，以便在请求的生命周期内使用  
@app.before_request  
def captcha_login():  
    temp = session.get("user_id")  
    if temp:  
        user = User.query.get(temp)  
        if user:  # 这里建议检查 user 是否真的存在，防止 ID 无效的情况  
            setattr(g, "user_id", user.id)  
    else:  
        setattr(g, "user_id", None)  
  
# 定义根路由（'/'），当用户访问网站的主页时，将渲染 'root.html' 模板  
@app.route('/')  
def root():  
    return render_template("root.html")  
  
if __name__ == '__main__':  
    # 运行 Flask 应用程序，如果 debug=True，则应用程序将在调试模式下运行，并自动重新加载代码更改  
    app.run(debug=True)