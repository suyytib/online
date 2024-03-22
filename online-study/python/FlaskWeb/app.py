from flask import Flask, render_template,request
from blueprints.login import bp as login_bp
from blueprints.root import bp as root_bp
from blueprints.table_config import db,migrate
import config
from blueprints.model import User
from flask_mail import Mail
from flask_mail import Message
# flask默认去templates文件夹下面找渲染的html文件

app = Flask(__name__)
mail = Mail(app)
app.register_blueprint(login_bp)
app.register_blueprint(root_bp)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)


if __name__ == '__main__':
    app.run(debug=True)
