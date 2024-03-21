from flask import Flask, render_template,request
from blueprints.login import bp as login_bp
import config

# flask默认去当前目录的 templates 文件夹中找html文件
app = Flask(__name__)

# 加载flask的配置,flask的数据库,邮箱等配置将从该文件中自动获取
app.config.from_object(config)

# 注册蓝图对象,使其管理的视图函数变为可用状态
app.register_blueprint(login_bp)

# 创建了网址 /show/info 和 函数index 的对应关系
# 以后用户在浏览器上访问 /show/info, 网站自动执行
@app.route("/show/info")
def index():
    return render_template("index.html")

# 新添加如下配置
@app.route("/get/news")
def get_news():
    return render_template("get_news.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        print(username, passwd)
        get_info = request.args
        return get_info


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)
