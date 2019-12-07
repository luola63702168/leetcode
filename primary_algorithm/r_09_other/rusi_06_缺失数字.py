def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    else:
        return len(nums)


if __name__ == '__main__':
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([0]))
