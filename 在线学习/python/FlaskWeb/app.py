from flask import Flask, render_template,request
from blueprints.login import bp as login_bp
from blueprints.root import bp as root_bp
from blueprints.table_config import db,migrate
import config
from blueprints.model import User
# flask默认去templates文件夹下面找渲染的html文件

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(root_bp)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)

# 创建了网址 /show/info 和 函数index 的对应关系
# 以后用户在浏览器上访问 /show/info, 网站自动执行
@app.route("/show/info")
def index():
    return render_template("index.html")

# 新添加如下配置
@app.route("/get/news")
def get_news():
    return render_template("get_news.html")
# 该函数放在了login文件里由登录视图函数相关蓝图对象的管理
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == "GET":
#         return render_template('register.html')
#     else:
#         username = request.form.get("username")
#         passwd = request.form.get("passwd")
#         print(username, passwd)
#         get_info = request.args
#         return get_info


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5100, debug=True)
    app.run(debug=True)
