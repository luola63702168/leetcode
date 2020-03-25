# hello
# 扑克牌,顺子 [1 2 3 4 5] [3 4 5 6 7] [3 5 4 2 1]
# 王牌 2张 -1
# [1 2 3 -1 5]
# input: a[]
# output: True/False


def sort_card(nums):
    nums.sort()
    tmp = nums.count(-1)
    if tmp > 2:
        return False
    tmp_nums = nums[tmp:]
    while tmp >= 0:
        for p in range(1, len(tmp_nums)):
            if tmp_nums[p] - tmp_nums[p - 1] != 1:
                tmp_nums.insert(p, tmp_nums[p - 1] + 1)
                tmp -= 1
            if tmp == -1:
                break
        tmp -= 1
    print(tmp_nums)
    return


if __name__ == '__main__':
    sort_card([-1, -1, 3, 8, 5])
# [3,4,5]
# [1,4,7]
