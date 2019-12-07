def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    cur_num = nums[0]
    max_num = nums[0]
    for num in nums[1:len(nums)]:
        cur_num = max((cur_num + num, num))
        max_num = max(max_num, cur_num)
    return max_num


if __name__ == '__main__':
    # print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    # print(maxSubArray([1]))
    # print(maxSubArray([-2,1]))
    print(maxSubArray([1, 2, -1, -2, 2, 1, -2, 1]))
    print(maxSubArray([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]))
    # print(maxSubArray([2,1]))
