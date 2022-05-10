# project name   : password generate application
# project author : mindula dilthushan
# author email   : minduladilthushan1@gmail.com

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Password Generate Application !'


if __name__ == '__main__':
    app.run(debug=True)
