# -*- coding: utf-8 -*-

L = ['a', 'd', 'v', 's', 'g']


# 选择排序
def selectFunc(arrs, size):
    for i in range(0, size):
        minindex = i
        for j in range(i + 1, size):
            if arrs[minindex] > arrs[j]:
                arrs[minindex], arrs[j] = arrs[j], arrs[minindex]
    return arrs


print(selectFunc(L, 5))
