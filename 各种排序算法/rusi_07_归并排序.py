#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


def merge_sort(alist):
    '''归并排序'''
    n = len(alist)
    if n <= 1:  # 递归退出条件
        return alist  # 这个返回值是由最后一次调用递归的那个函数接受的（拆分到不能拆分了就返回了），也就是被left_li或者right_li接受了。这时并不会终止程序，只会终止此次递归,而后这次递归返回的数据也就是（left_li和right__li）都会进行下面的循环代码,之后返回值result_list便是可进行下面循环代码的递归函数来接受的，还是用（left_li或者right_li来接受），然后反复进行下面的循环，直到第一次调用这个函数得到了属于自己的返回值，代码运行结束。
    mid = n // 2
    # 接受归并排序后左边的有序列表
    left_li = merge_sort(alist[:mid])
    # 接受归并排序后右边的有序列表
    right_li = merge_sort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    result_list = []
    # 循环条件满足时，说明左右两边的游标都没有走到列表的末尾
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:  # =号 是使排序稳定的作用
            result_list.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_li[right_pointer])
            right_pointer += 1

    # 退出循环后，让result_list需要和最后剩下的那个列表中的所有的元素都需要合并
    result_list += left_li[left_pointer:]
    result_list += right_li[right_pointer:]
    return result_list


if __name__ == '__main__':
    li = [17, 20, 93, 54, 77, 31, 44, 55, 226]

    print(merge_sort(li))

# 时间复杂度：nlogn n每次合并的最大次数，logn为拆分的总次数。由于必须从中间拆分（没有特殊情况）：所以最优最差时间复杂度都是nlogn
# 稳定：因为合并的时候并没有改变相同元素的排列位置。
# 拓展： 时间最短，但是它要新建一个列表，所以在空间上是有额外的开销的。

# 归并排序和快速排序的区别:
# 后者是在列表本身上操作，前者需要新建列表来接受“确定值”。
# 后者理念是：将大的放“某一个数”右边，小的放左边，然后再以“某一个数”为分界点拆开，拆开后还按照“大的在右，小的在左”的思想去操作。前者的理念是：全都拆开，然后一点点的比较，然后放置新的列表中并返回。
