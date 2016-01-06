#!/usr/bin/env python2.7
# coding:utf-8

import tornado.ioloop
import tornado.web
import time
import redis

r = redis.Redis(host='api-dev.xccxbj.com', port=10020)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #ts = str(time.time())
        ts = r.get('aaa')
        self.write(ts)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(10081)
    tornado.ioloop.IOLoop.instance().start()
