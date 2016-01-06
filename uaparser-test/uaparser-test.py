#!/usr/bin/env python2.7
# coding:utf-8

from ua_parser import user_agent_parser
import httpagentparser
import timeit
import time
i1 = i = 10000
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
def tt1():
    user_agent_parser.Parse(ua)
def tt2():
    httpagentparser.detect(ua)

def fun(f,n=10000):
    a = time.time()
    while n:
        n -= 1
        apply(f)
    b = time.time()
    print b - a

fun(tt1)
fun(tt2)
    
# x1 = timeit.Timer(tt1)
# x2 = timeit.Timer(tt2)
# print x1.timeit(10000)
# print x2.timeit(10000)