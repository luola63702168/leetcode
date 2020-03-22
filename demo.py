# hello
# 扑克牌,顺子 [1 2 3 4 5] [3 4 5 6 7] [3 5 4 2 1]
# 王牌 2张 -1
# [1 2 3 -1 5]
# input: a[]
# output: True/False


def sort_card(nums):
    nums.sort()

    # leg = len(nums)
    # tmp = 0
    # for i in range(leg):
    #     if nums[i] != -1:
    #         tmp = i
    #         break

    tmp = nums.count(-1)
    tmp_nums = nums[tmp:]
    while tmp >= 0:
        for p in range(1, len(tmp_nums)):
            if tmp_nums[p] - tmp_nums[p-1] != 1:
                tmp_nums.insert(p-1, tmp_nums[p-1] + 1)
                tmp -= 1
                break
        tmp_nums.sort()
        tmp -= 1
    print(tmp_nums)

    return


if __name__ == '__main__':
    sort_card([-1, -1, 3, 8, 5])
