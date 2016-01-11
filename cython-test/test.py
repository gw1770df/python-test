#!/usr/bin/env python2.7
# coding:utf-8
#
#
#

import timeit
print(timeit.timeit("sum(generator.generate(999))", setup="import generator", number=1000))
print(timeit.timeit("sum(generator_py.generate(999))", setup="import generator_py", number=1000))
