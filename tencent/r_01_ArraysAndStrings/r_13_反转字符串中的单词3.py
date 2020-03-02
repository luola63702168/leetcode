#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_

# 参考链接：https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/906/


def reverseWords(s):
    """

    :return:
    """
    return ' '.join(cr[::-1] for cr in s.split())




if __name__ == '__main__':
    print(reverseWords("Let's take LeetCode contest"))
