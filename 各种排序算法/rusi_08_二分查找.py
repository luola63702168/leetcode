#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


li = [17, 20, 54, 77, 226]


def binary_search(alist, item):
    '''二分法查找'''
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            # 需要有返回值的
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False


def binary_search_02(alist, item):
    '''二分查找非递归'''
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:  # 等号也是成立的，刚好就是中间夹的那个值
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    print(binary_search(li, 17))
    print(binary_search(li, 100))
    print(binary_search(li, 226))

    print(binary_search_02(li, 17))
    print(binary_search_02(li, 100))

# 递归和非递归的区别：
# 递归需要创建一个新的列表，非递归只是改变索引的位置。

# 二分查找（折半查找）会用到索引，并且依次从中间分割，所以必须是有序的，也就只能是顺序表。
# 时间复杂度：最差时间是logn（因为一直在等分），最优时间复杂度是 1 因为第一次找的时候就可以找到便是1了。
# 遍历方法的最优时间复杂度是：o(1) 第一个就是；最坏时间复杂度是o(n)，从头到尾。
