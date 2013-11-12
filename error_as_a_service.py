import flask
from flask import abort, render_template, url_for
import sys

sys.path.insert(0, "/var/www/flask/error_as_a_service")
app = flask.Flask(__name__)
from error_as_a_service import app as application


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<error_code>')
def error_page(error_code):
    abort(int(error_code))


if __name__ == '__main__':
    app.run(debug=False)

