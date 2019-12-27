#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


def comb_sort(list_):
    lens = len(list_)
    if lens < 2:
        return list_
    else:
        i = int(lens / 1.3)
        while i >= 1:
            for j in range(lens):
                if i + j >= lens:
                    i = int(i / 1.3)
                    break
                else:
                    if list_[j] >= list_[j + i]:
                        list_[j], list_[j + i] = list_[j + i], list_[j]
        return list_


if __name__ == '__main__':
    the_list = [3, 44, 5, 21, 82, 7, 2, 3]
    print(comb_sort(the_list))

# 梳排序，类似冒泡排序，但是是按照一定的步长进行交换的，这类似希尔排序，这里取得步长是列表得长度除以1.3取整。
# 类似：8/1.3=6 6/1.3=4 ....一直到1/1.3<1结束
# 排序中心思想仍是：找到最大的，然后放最后。每一次循环都可能伴随着一次交换
