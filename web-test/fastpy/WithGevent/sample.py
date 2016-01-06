#-*- coding:utf-8 -*-
import os
import imp
import sys
import time
#from Cheetah.Template import Template
import json
#import redis
import logging
import traceback
import urllib
import urllib2
import httplib
#from common import base

reload(sys)
sys.setdefaultencoding('utf8')
FastpyAutoUpdate = True

#rlog = base.FeimatLog("logs/sample.log")

def fetch(pid, url, request):
    print('Process %s: %s start work' % (pid, url))
    flag = None
    status = None
    error_msg = None

    conn = httplib.HTTPConnection("127.0.0.1:8998")
    headers = {
    }

    body_str = ""
    conn.request("POST", "/sample.test_alive", body_str, headers)

    res = conn.getresponse()
    conn.close()

    data = res.read()

    print('Process %s: %s %s' % (pid, url, res.status))
    return "suc"

class sample():
    def __init__(self):
        # init here
        #self.up_t = Template(file="templates/upload.html")
        self.content = 1
        self.id = 1
        pass

    def test_alive(self, request, response_head):
        res = ""
        for i in range(1, 10):
            res += str(self.content)
        self.content += 1
        return res

    def web(self, request, response_head):
        print "a"
        url = 'http://127.0.0.1:8998/sample.test_alive'
        self.id += 1
        return fetch(self.id, url, request)

