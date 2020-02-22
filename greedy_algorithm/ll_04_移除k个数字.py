#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_

# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
# 注意:
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。

# 示例 1 :
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。

# 示例 2 :
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

# 示例 3 :
# 输入: num = "10", k = 2
# 输出: "0"
# 解释: 从原数字移除所有的数字，剩余为空就是0。


def removeKdigits(num, k):
    """
    移除k个数字
    思想：高位大于次高位，那么就把高位剔除掉(利用了栈这个数据结构)
    :param num:
    :param k:
    :return:
    """
    if k >= len(num):
        return "0"
    num_list = []
    for ns in num:
        while k > 0 and num_list and num_list[-1] > ns:
            num_list.pop(-1)
            k -= 1
        num_list.append(ns)
    # print(num_list)
    num = ''.join(num_list)
    num = num[:-k] if k > 0 else num
    return str(int(num))


def removeKdigits2(num, k):
    """
    移除k个数字
    思想：高位大于次高位，那么就把高位剔除掉
    :param num:
    :param k:
    :return:
    """
    i = 0  # 游标
    if k >= len(num):
        return "0"
    while k > 0 and i < len(num) - 1:
        if int(num[i]) > int(num[i + 1]):  # 高位大于次高位
            num = num[0:i] + num[i + 1:]  # 那么就把高位剔除掉
            if i > 0:
                # 删除一个字符，游标不得回去?（这也是为什么用for不好使的原因）
                i -= 1
            k -= 1
        else:
            i += 1
    num = num[:len(num) - k]  # 循环结束，说明现在是递增的，没有进入k-1的那环，则去掉最后k个数
    return str(int(num))  # int去掉前导0


if __name__ == '__main__':
    print(removeKdigits(num="1432219", k=3))
    print(removeKdigits(num="112", k=1))
    print(removeKdigits(num="10200", k=1))
    print(removeKdigits(num="0", k=0))
    print(removeKdigits(num="1173", k=2))
    print(removeKdigits(num="5337", k=2))
    print(removeKdigits(num="10", k=1))
    print(removeKdigits("1234567890", 9))

