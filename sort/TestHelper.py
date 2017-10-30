# -*- coding: utf-8 -*-
import random
import time
import numpy as np
from datetime import datetime

"""
:param start:开始值
:param end:最大值
:param size:生成个数

:return List
"""


def generateList(start, end, size):
    return random.sample(range(start, end), size)

def generateList2(start, end, size):
    return np.random.randint(start,end,size=size)


def printSortList(list):
    for item in list:
        print(item)
    print('\n')


"""
:param name:排序名字
:param func:排序的方法
:param lists:测试用例

:return
"""


def isSorted(lists):
    for index in range(0, len(lists) - 1):
        if lists[index] > lists[index + 1]:
            return False
    return True


def testSort(name, func, lists):
    print("开始时间 :")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    starttime = time.time()
    func(lists)
    print("完成时间 :")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    endtime = time.time()
    if isSorted(lists):
        print("使用%s排序共耗时 : %d 秒" % (name, (endtime - starttime)))
    else:
        print("使用%s排序失败!" % (name))
