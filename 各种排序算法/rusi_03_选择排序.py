#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


def select_sort(alist):
    '''选择排序'''
    n=len(alist)
    for j in range(n-1):  # 默认第一个是最小的索引
        min_num = j
        for i in range(1+j, n):  # 取出真正的最小的索引
            if alist[min_num] > alist[i]:
                min_num = i
        alist[j], alist[min_num] = alist[min_num], alist[j]  # 交换位置

# 当两数相等时，排序之后不会影响其原本所在的位置，即为稳定。
# 当以寻找最大数放置-1索引位置时，该函数是不稳定的。


alist = [17,20,93,54,77,31,44,55,226]

select_sort(alist)

print(alist)
