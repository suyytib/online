from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route("/do/register", methods=['GET'])
def do_register():
    get_info = request.args
    return get_info
@app.route("/post/register", methods=['POST'])
def post_register():
    get_info = request.form

    username = request.form.get("username")
    passwd = request.form.get("passwd")
    sex = request.form.get("sex")
    hobby_list = request.form.getlist("hobby")
    city = request.form.get("city")
    more = request.form.getlist("textarea")

    print(username, passwd, sex, hobby_list, city, more)

    return get_info


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)
