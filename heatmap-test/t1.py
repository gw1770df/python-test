#!/usr/bin/env python2.7
# coding:utf-8
""""""

from pyheatmap.heatmap import HeatMap

def main():
    # url = "https://raw.github.com/oldj/pyheatmap/master/examples/test_data.txt"
    ff = open('./test_data.txt', 'r')
    sdata = ff.read().split("\n")
    data = []
    for ln in sdata:
        a = ln.split(",")
        if len(a) != 2:
            continue
        a = [int(i) for i in a]
        data.append(a)

    # 开始绘制
    hm = HeatMap(data)
    hm.clickmap(save_as="hit.png")
    hm.heatmap(save_as="heat.png")

if __name__ == "__main__":
    main()

if __name__ == '__main__':
    pass
