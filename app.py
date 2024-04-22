from flask import Flask
# flask默认去templates文件夹下面找渲染的html文件

app = Flask(__name__)

@app.route('/')
def root():
    return "flask部署"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
