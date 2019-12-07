def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

    # li_nums = nums + []
    # for i in li_nums:
    #     nums.remove(i)
    #     for t in nums:
    #         if i + t == target and i !=t:
    #             return [li_nums.index(i),li_nums.index(t)]
    #         elif i + t == target and i == t:
    #             idx = li_nums.index(i)
    #             li_nums[li_nums.index(i)]=i+1
    #             return [idx,li_nums.index(t)]
    #         # else:
    #         #     nums = li_nums + []

if __name__ == '__main__':
    print(twoSum([3,3],6))