#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


def quick_sort(alist, first, last):
    '''快速排序'''

    # 递归终止条件
    if first >= last:  # 为什么是>号，而不是==号？ 因为递归传参的时候可能存在传递的first和low-1中的low已经相等了，这个时候first是>low-1的，而这时候first和low-1作为索引对应的值在列表中还是可以找到的，所以仍会递归，于是出现递归错误。（这里判断条件有无=都可以）
        return
    # 规定第一个值为中间值
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        # 条件成立，height左移，循环不成立将小于中间值的放置左边
        while low < high and alist[high] >= mid_value:  # 等号存在的意义是将相等的数值放置右边（这是快速排序的思想决定的）。
            # 另外条件low<height是不可以去掉的，假设alist[high] >= mid_value一直满足，high就会一直变小，直到已经等于low，甚至小于low的时候还没有退出循环，就会超出索引的情况了。（在第一层循环满足的情况下，第二层循环在没退出的情况下是不受第一层循环限制的）。
            high -= 1
        alist[low] = alist[high]

        # 当退出上层循环的时候alist[height]的位置空着，所以我们判断左边的
        # 条件成立，low右移，循环不成立将大于中间值的放置右边
        while low < high and alist[
            low] < mid_value:  # 由于上一个同级别循环的限制，形成了即使low无限的+1，也一定会存在alist[low] == mid_value,即退出循环，所以这一个循环的判断条件，有无low < high都可以。
            low += 1
        alist[high] = alist[low]

    # 循环退出时 low==height
    alist[low] = mid_value

    # 递归
    # 对low左边列表执行快速排序（low是中间值，当然这个low也可以是high，因为中间值的时候就是alist[low]==alist[high]的时候）
    quick_sort(alist, first, low - 1)
    # 对low右边列表执行快速排序
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    alist = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
# 最优时间复杂度是Nlogn.(logn是因为把n等分多少次而得的)n是每次拆分需要进行n次比较。
# 最坏时间复杂度是n2  第一个n是因为需要对每个元素操作  第二个n是因为每次对其中的一个元素操作的时候还要对n-1个元素操作。所以n*（n-1）约等于n^2
# 不稳定（参考二层循环中的第一个循环）
