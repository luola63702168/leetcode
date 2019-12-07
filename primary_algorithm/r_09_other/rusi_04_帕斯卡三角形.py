def generate(numRows):
    result_list = []
    if numRows <= 0:
        return result_list
    for i in range(0, numRows):
        result_list.insert(i, [1])
    length = len(result_list)
    for k in range(length):
        if k < 1:
            continue
        temp_list = []
        for j in range(len(result_list[k - 1]) - 1):
            temp_list.append(result_list[k - 1][j] + result_list[k - 1][j + 1])
        result_list[k].extend(temp_list + [1])
    return result_list


if __name__ == "__main__":
    print(generate(0))
    print(generate(1))
    print(generate(2))
    print(generate(5))
