#!/usr/bin/env python2.7
# coding:utf-8

import signal
import os
print 'this pid is', os.getpid()

# Define signal handler function
def myHandler(signum, frame):
    print('I received: ', signum)

# register signal.SIGTSTP's handler
signal.signal(signal.SIGTSTP, myHandler)
signal.pause()
print('End of Signal Demo')
