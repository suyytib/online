from flask import Flask, render_template,request

app = Flask(__name__)

# 创建了网址 /show/info 和 函数index 的对应关系
# 以后用户在浏览器上访问 /show/info, 网站自动执行
@app.route("/show/info")
def index():
    # 默认去当前目录的 templates 文件夹中找
    return render_template("index.html")

# 新添加如下配置
@app.route("/get/news")
def get_news():
    # 默认去当前目录的 templates 文件夹中找
    return render_template("get_news.html")
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/post/register", methods=['post'])
def post_register():
    get_info = request.form
    return get_info


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)
