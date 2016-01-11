#!/usr/bin/env python2.7
# coding:utf-8
#
#
#

def consumer(n):
    print 'in'
    while n:
        n -= 1
        print 'before : %s' % n
        rec = yield n
        print 'after  : %s' % n
        print 'recive : %s' % rec

if __name__ == '__main__':
    pass
