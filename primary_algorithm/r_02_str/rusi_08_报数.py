def countAndSay(n):
    """
    算法核心是：依次按照规则往后数，相同的数字怎么处理，不同的又该怎样处理：相同的计数后添加到字符串，不同的直接添加到字符串。
    :param n:
    :return:
    """
    if n == 1:
        return "1"
    # 递归，从1开始。
    s = countAndSay(n - 1)  # 312211
    count = 0  # 数字的重复次数
    now_num_str = s[0]
    result_str = ""  # 得存下结果
    for i in s:
        if i == now_num_str:
            count += 1
        else:
            # now_num_str = str(count) + now_num_str
            result_str = result_str + str(count) + now_num_str
            now_num_str = i  # 此时now_num_str = i，而且i已经被遍历了，所以count必定会为1，这样后面与之相同的数出现了，直接加1就是2了
            count = 1
    # result_str只在不同的时候产生，
    # 如果最后一个数字就是出现不同的数字，那么只需要加上“1个i即可（此时count和i已经被重置了）”
    # 如果最后一个数字仍然相同，那么只需要加上“count个i即可”
    return result_str + str(count) + now_num_str


if __name__ == '__main__':
    print(countAndSay(1))