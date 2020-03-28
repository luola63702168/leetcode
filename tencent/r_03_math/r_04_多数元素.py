# ://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/941/ass

def majorityElement1(nums):
    """
    找出最大的元素（常规解法）
    return：max int
    """
    tmp_set = set(nums)
    res_num = 0
    cou_num = 0
    for p in tmp_set:
        if nums.count(p) > cou_num:
            cou_num = nums.count(p)
            res_num = p
    return res_num


def majorityElement(nums):
    """
    找出最大的元素（简单解法-->题目中的提示：多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素）
    return：max int
    """
    nums.sort()
    return nums[int(len(nums) / 2)]


if __name__ == "__main__":
    print(majorityElement([3, 2, 3]))
