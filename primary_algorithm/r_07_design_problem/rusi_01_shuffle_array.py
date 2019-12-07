import copy
import random


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
