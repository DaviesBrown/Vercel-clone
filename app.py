#!/usr/bin/python3
""" Starts Vercel Web Application """
from os import environ
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """


@app.route('/', strict_slashes=False)
def index():
    """ index page """
    return render_template('index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
