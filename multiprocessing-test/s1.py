#!/usr/bin/env python2.7
# coding:utf-8

import multiprocessing

def worker(num):
    """thread worker"""
    print 'worker :',num

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i, ))
        jobs.append(p)
        p.start()
