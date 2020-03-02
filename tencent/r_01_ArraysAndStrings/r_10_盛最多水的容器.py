#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_

# 题目链接：https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/903/


def maxArea(height):
    """
    双指针求解
    :param height: 高度们
    :return: 最大面积
    """
    left = 0
    right = len(height) - 1
    res_sum = min(height[0], height[1]) * 1
    while left < right:
        res_sum = max((right - left) * min(height[left], height[right]), res_sum)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return res_sum


def maxArea1(height):
    """
    换个别的方法试试(超时了)
    :return: 最大面积
    """
    leh = len(height)
    cur_sum = min(height[0], height[1]) * 1
    for i in range(leh):
        for k in range(i + 1, leh):
            cur_sum = max(cur_sum, min(height[i], height[k]) * (k - i))

    return cur_sum


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
