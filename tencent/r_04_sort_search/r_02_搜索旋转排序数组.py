#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_

# https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/927/


def search1(nums, target):
    """用python自带的内置函数"""
    try:
        inx = nums.index(target)
    except Exception:
        inx = -1
    return inx


def binary_search(left, right, nums, target):
    """search的辅助函数"""
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def search(nums, target):
    """二分法"""
    right = len(nums) - 1
    mid = right - 1
    while nums[mid] < nums[right]:
        mid -= 1
    idx = binary_search(0, mid, nums[:mid+1], target)
    if idx == -1:
        idx = binary_search(0, right-mid, nums[mid+1:], target)
        if idx != -1:
            idx = mid + idx + 1
    return idx


if __name__ == '__main__':
    # print(search([4, 5, 6, 7, 0, 1, 2], 2))
    print(search([4, 5, 6, 7, 0, 1, 2], 3))
