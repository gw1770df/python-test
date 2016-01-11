#!/usr/bin/env python2.7
# coding:utf-8
#
#
#

from tqdm import tqdm
import time

# for i in tqdm(range(20)):
#     time.sleep(0.1)

tt = tqdm(range(20))
for i in range(20):
    tt.next()
    time.sleep(0.1)
if __name__ == '__main__':
    pass
