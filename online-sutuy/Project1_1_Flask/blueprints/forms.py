from wtforms import Form, StringField
from wtforms.validators import Length,Email,EqualTo
# 参与注册验证的表单类
class Register_Form(Form):
    username = StringField(validators=[Length(min=4,max=20)])
    passwd = StringField(validators=[Length(min=6,max=20)])
    email=StringField(validators=[Email()])
    re_password = StringField(validators=[EqualTo("passwd",u"两次密码不一致")])

# 参与登录验证的表单类
class Login_Form(Form):
    pass