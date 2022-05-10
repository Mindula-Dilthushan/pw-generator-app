# project name   : password generate application
# project author : mindula dilthushan
# author email   : minduladilthushan1@gmail.com

from flask import Flask, render_template, request
import random
import subprocess

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    pw_len = ''
    pw = ''
    data = "qazwsxedcrfvtgbyhnujmiklop96391hnflw@&*!fplmbvgqlZAHYQLNVHGLRJWSPPIYTMV?"
    generate = ''

    if request.method == 'POST':
        if "pw_len" in request.form:
            pw_len = request.form["pw_len"]
        if "pw" in request.form:
            pw = request.form["pw"]

            generate = "".join(random.sample(data, int(pw_len)))
            pw = generate

            with open('D:\password.txt', 'w') as password:
                password.write(str(pw))
                subprocess.Popen('explorer "D:\password.txt"')

    return render_template('index.html', pw_len=pw_len, pw=pw)


if __name__ == '__main__':
    app.run(debug=True)
