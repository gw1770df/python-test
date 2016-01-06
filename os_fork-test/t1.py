#!/usr/bin/env python2.7
# coding:utf-8
#
#
#

import os

def child():
    print 'A new child:', os.getpid()
    print 'Parent id is:', os.getppid()
    os._exit(0)

def parent():
    while True:
        newpid=os.fork()
        print newpid
        if newpid==0:
            child()
        else:
            pids=(os.getpid(),newpid)
            print "parent:%d,child:%d"%pids
            print "parent parent:",os.getppid()
        if raw_input()=='q':
            break

if __name__ == '__main__':
    parent()
