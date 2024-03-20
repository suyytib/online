from flask import Flask, render_template

app = Flask(__name__)

@app.route('/register'
def register():
    # return render_template('register.html')
    return render_template('temp.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=False)
