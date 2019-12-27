#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


alist = [17, 20, 93, 54, 77, 31, 44, 55, 226]


def insert_sort(alist):
    '''插入排序'''
    n = len(alist)
    for j in range(n - 1):  # 操作多少个数，代表多少次
        i = j + 1  # i 代表从哪个数开始操作（索引）
        while i > 0:  # range(j,0,-1)
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            #     else 对程序本身没有影响，这是一个性能优化---o(n)2到o(n)（如果去掉else，需要把 i-=1（shift tab））
            else:
                break


insert_sort(alist)
print(alist)
# 稳定性：稳定。相同的元素的时候是不会进行交换操作的，所以稳定。
