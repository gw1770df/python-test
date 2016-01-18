#!/usr/bin/env python2.7
# coding:utf-8
import multiprocessing
import time
import os
import sys
import signal

def daemon(wt=2):
    name = multiprocessing.current_process().name
    print name, 'Starting'
    print name, 'pid', os.getpid()
    time.sleep(wt)
    sys.stdout.write('%s Exit\n' % name)
    # print name, 'Exiting'

def onsignal_term(a,b):
    print '收到SIGTERM信号 signal pid', os.getpid()
    #这里是绑定信号处理函数，将SIGTERM绑定在函数onsignal_term上面


signal.signal(signal.SIGTERM,onsignal_term)



def non_daemon(wt):
    name = multiprocessing.current_process().name
    print 'Starting:', name
    time.sleep(wt)
    print 'Exiting :', name

if __name__ == '__main__':
    print 'father pid', os.getpid()
    d = multiprocessing.Process(name='daemon',
                                target=daemon,
                                args=(20,))
    # d.daemon = True

    n = multiprocessing.Process(name='non-daemon',
                                target=daemon,
                                args=(3,))
    n.daemon = False

    d.start()
    n.start()

    # d.join(1)
    print 'd.is_alive()', d.is_alive()
    # n.join()
    print 'all done'
