#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_
# 题目链接：https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/907/
from functools import reduce


def productExceptSelf(nums):
    """
    核心思想为：用其左边所有数的乘积，乘以右边所有数的乘积
    :param nums:
    :return:
    """
    tmp = 1  # 占位值(1乘以任何一个数还为他自己)
    leh = len(nums)
    res_li = [1] * leh
    for i in range(0, leh):
        res_li[i] = tmp
        tmp *= nums[i]  # 求左边数的积

    # res_li [占位值，第一个数 * 1，前两个数的乘积，前三个数的乘积]

    tmp = 1
    for i in range(leh)[::-1]:  # 倒着遍历
        res_li[i] *= tmp
        tmp *= nums[i]  # 求右边数的积
    return res_li


def productExceptSelf1(nums):
    """
    使用reduce库（超时）
    :return:
    """
    return [reduce(lambda x, y: x * y, nums[:i] + nums[i + 1:]) for i in range(len(nums))]


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
