#!/usr/bin/env python2.7
# encoding: utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print aaa
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)
