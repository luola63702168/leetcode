def single_num(nums):
    only_list = list(set(nums))
    for i in only_list:
        nums.remove(i)
    for t in nums:
        if t in only_list:
            only_list.remove(t)
    return only_list[0]


if __name__ == "__main__":
    print(single_num([1, 1, 2, 2, 3]))
