#!/usr/bin/env python3
""" a simple flask application to demonstrate different languages support"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    """return the root of this application"""
    return(render_template('0-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
