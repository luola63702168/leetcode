def _add(digits):
    res_list = list()
    res_list.extend(str(int("".join(str(i) for i in digits))+1))
    return res_list


if __name__ == "__main__":
    print(_add([1, 2, 3]))
    print(_add([4, 3, 2, 1]))
    print(_add([9]))


# num_list = list()
#     res_list = list()
#     for i in digits:
#         num_list.append(str(i))
#     res_list.extend(str(int("".join(num_list))+1))
#     return res_list