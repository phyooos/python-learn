# -*- coding: utf-8 -*-
from sort.TestHelper import *

"""
插入排序

"""
def insertSortFunc(list):
    n = len(list)
    for i in range(1, n):
        # 这里是拿到第 i 个数字
        for j in range(i, 0, -1):
            # 这里倒序,从i开始,向前一个元素比较
            if list[j] < list[j-1]:
                list[j],list[j-1] = list[j-1],list[j]
            else:
                break



def insertSortPro(list):
    n = len(list)
    for i in range(1,n):
        #现在应该记住当前的位置
        item = list[i]
        index = i
        for j in range(i, 0, -1):
            index = j
            # 这里倒序,从i开始,向前一个元素比较
            if list[j-1] > item:
                list[j] = list[j-1]
            else:
                break

        list[index] = item




testSort("插入", insertSortPro, generateList2(0, 9999, 1000))
