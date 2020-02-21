import copy
import random


# 打乱一个没有重复元素的数组。
#
# 示例:
#
# // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();

# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();

# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();

class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.reset_nums = copy.deepcopy(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.reset_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        length = len(self.nums)
        for i in range(length):
            index = random.randint(0, length - 1)
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)

# reversed() 反转函数
