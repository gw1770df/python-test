#! /usr/bin/python
# -*- coding: utf-8 -*-
# pythontab提醒您注意中文编码问题，指定编码为utf-8
# import struct
# import IPython
# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少则2字符，长则8字符


FILE_TYPE_MAP = {"FFD8FF": "JPEG",
                 "89504E47": "PNG"}

# 获取文件类型


def filetype(filename):
    binfile = open(filename, 'rb')  # 必需二制字读取
    ftype = 'unknown'
    for hcode in FILE_TYPE_MAP:
        numOfBytes = len(hcode) / 2  # 需要读多少字节
        binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
        code = binfile.read(numOfBytes)
        # IPython.embed()
        if code.encode('hex') == hcode.lower():
            ftype = FILE_TYPE_MAP[hcode]
            break
    binfile.close()
    return ftype

if __name__ == '__main__':
    print filetype('./logo.png')
