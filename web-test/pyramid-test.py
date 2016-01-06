#!/usr/bin/env python2.7
# coding:utf-8

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
