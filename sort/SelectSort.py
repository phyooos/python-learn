# -*- coding: utf-8 -*-
from sort.TestHelper import *

L = ['a', 'd', 'v', 's', 'g']
L2 = [1,2,3,12,4,111,31,22,12,5435,21,53,222,3432]

# 选择排序
def selectFunc(arrs):
    for i in range(0, len(arrs)):
        minindex = i
        for j in range(i + 1, len(arrs)):
            if arrs[minindex] > arrs[j]:
                arrs[minindex], arrs[j] = arrs[j], arrs[minindex]
    return arrs


testSort("选择",selectFunc,generateList(0,9999999,10000))
