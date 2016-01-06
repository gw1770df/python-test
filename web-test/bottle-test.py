#!/usr/bin/env python2.7
# coding:utf-8

from bottle import route, run, request, response
import time
import redis

r = redis.Redis(host='api-dev.xccxbj.com', port=10020)
@route('/')
def hello():
    if request.get_cookie('visited'):
        return 'see you again'
    else:
        response.set_cookie('visited', 'True')
        return 'hello'

@route('/get')
def get():
    return r.get('aaa')


run(erver='paste', host='localhost', port=10082, debug=True)
