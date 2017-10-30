# -*- coding: utf-8 -*-
from sort.TestHelper import *

"""
 选择排序
:param arrs:数组

"""
def selectFunc(arrs):
    for i in range(0, len(arrs)):
        minindex = i
        for j in range(i + 1, len(arrs)):
            if arrs[minindex] > arrs[j]:
                arrs[minindex], arrs[j] = arrs[j], arrs[minindex]
    return arrs


testSort("选择", selectFunc, generateList2(0, 9999, 10000))
