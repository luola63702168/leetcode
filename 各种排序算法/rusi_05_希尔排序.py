#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


alist = [17, 20, 93, 54, 77, 31, 44, 55, 226]


def shell_sort(alist):
    '''希尔排序'''
    n = len(alist)
    gap = n // 2  # gap取中间值(其实它是不固定的，需要根据数学来计算?)
    while gap > 0:  # 将gap的值不断的缩小，当gap==1的时候，实际上便是利用插入排序操作了整个序列
        # 内层循环达到的效果是：每个以gap步长为基准的“子序列”是有序的，并不能代表整个序列是有序的。
        for j in range(gap, n):  # 一个循环处理了“子序列”的以gap为步长的元素质之间的比较。
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2


shell_sort(alist)
print(alist)
# 时间复杂度： 假设gap取1，那么就是一个很普通的插入排序，最坏时间复杂度是o(n^2);最优时间复杂度需要根据gap的值来确定。
# 稳定：因为分成几部分对待，所以相同的数可能不在一个“子序列”，于是不稳定。
