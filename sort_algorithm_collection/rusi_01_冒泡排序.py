#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


def bubble_sort(alist):
    '''冒泡排序'''
    n = len(alist)
    # 直接用n也可以
    for j in range(n - 1):  # 控制每一次循环都能找到一个最大的。一直到倒数第二小和倒数第一小进行比较。
        count = 0  # 改进之后最优时间复杂度由n^2变为n
        for i in range(n - 1 - j):  # 每一次循环找到一个最大的放最后
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            return


if __name__ == '__main__':
    li = [12, 53, 2, 200, 5, 101, 89, 98, 100]
    # li = [12]
    bubble_sort(li)
    print(li)

# 当相等时，不会交换位置，所以它是稳定的。


