#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_
#   子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
def subsets(nums):
    import itertools
    def t_to_l(t):
        return list(t)

    res_li = []
    for i in range(1, len(nums) + 1):
        res_li += list(itertools.combinations(nums, i))
    res_li = list(map(t_to_l, res_li))
    res_li.append([])
    return res_li


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
