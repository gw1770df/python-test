#!/usr/bin/env python2.7
# coding:utf-8
""""""
@profile
def main():
    dic, i = {}, 10
    while i:
        i -= 1
        dic[i] = i
    print len(dic)

if __name__ == '__main__':
    main()
