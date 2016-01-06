#!/usr/bin/env python2.7
# encoding: utf-8

import signal
import os
import time

print 'this process pid is',os.getpid()

# Define signal handler function
def myHandler(signum, frame):
    print("Now, it's the time")
    exit()

# register signal.SIGALRM's handler
signal.signal(signal.SIGALRM, myHandler)
signal.alarm(5)
while True:
    print('not yet')
    time.sleep(1)
