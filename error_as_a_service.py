import flask
from flask import abort

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<error_code>')
def error_page(error_code):
    abort(int(error_code))


if __name__ == '__main__':
    app.run(debug=True)

