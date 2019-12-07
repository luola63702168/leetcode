
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in nums:
        if i == 0:
            nums.append(nums.pop(nums.index(i)))
    print(nums)

if __name__ == '__main__':
	moveZeroes([1,0,2])