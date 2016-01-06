#!/usr/bin/env python
#coding:utf-8

import redis
import time

r = redis.Redis(host='api-dev.xccxbj.com', port=10020)
a = time.time()
ii = i = 100000
while i:
    r.get('aaa')
    i -= 1
b = time.time()
use = b - a
print 'use', use
print 'qps',ii/use