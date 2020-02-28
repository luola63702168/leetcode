#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


# 三数之和:
# 给定一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c ，使得a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

# 示例：
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

def threeSum(nums):
    """
    定义两个游标左右开找，直到游标相遇停止
    去重：1、之前找过的数就别找了，2、找的left和right相同还要它干什么？
    :return:list
    """
    nums.sort()
    tmp_li = []
    leh = len(nums)

    for i in range(leh):
        # 游标
        left = i + 1
        right = leh - 1
        # 之前已经找到的就别找了
        if i > 0 and nums[i] == nums[i - 1]:
            left += 1
            continue
        while left < right:
            num_sum = nums[i] + nums[left] + nums[right]
            if num_sum == 0:
                tmp_li.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # 一样的就不要了，无论多少个。
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
            elif num_sum < 0:
                left += 1
            elif num_sum > 0:
                right -= 1

    return tmp_li


def threeSum2(nums):
    """

    :return:list
    """
    nums.sort()
    tmp_li = []
    leh = len(nums)

    for i in range(leh):
        # 游标
        left = i + 1
        right = leh - 1
        while left < right:
            num_sum = nums[i] + nums[left] + nums[right]
            if num_sum == 0:
                tmp_li.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif num_sum < 0:
                left += 1
            elif num_sum > 0:
                right -= 1

    # 去重（下面这种方法超时）
    res_li = []
    for li in tmp_li:
        if li not in res_li:
            res_li.append(li)
    return res_li


if __name__ == '__main__':
    # print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([-2, 0, 0, 2, 2]))
