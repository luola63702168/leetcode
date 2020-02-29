#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
# 找出 nums 中的三个整数，使得它们的和与 target 最接近。
# 返回这三个数的和。假定每组输入只存在唯一答案。

# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


def threeSumClosest(nums, target):
    """
    利用两个游标测试所有和
    :return: int 结果
    """
    nums.sort()
    leh = len(nums)
    res_sum = nums[0] + nums[1] + nums[2]
    for i in range(leh):
        left = i + 1  # i 为什么要加1？  因为left从头轮询可能出现 i=lef的情况
        right = leh - 1
        while left < right:
            tmp_sum = nums[left] + nums[i] + nums[right]
            if tmp_sum == target:
                return tmp_sum
            res_sum = tmp_sum if abs(res_sum - target) > abs(tmp_sum - target) else res_sum
            if tmp_sum < target:
                left += 1
            else:
                right -= 1
    return res_sum


if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1, -4], 1))
