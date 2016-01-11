#!/usr/bin/env python2.7
# coding:utf-8
import random

def generate(num):
    while num:
        yield random.randrange(10)
        num -= 1
