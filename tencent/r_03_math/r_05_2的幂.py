#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_


def isPowerOfTwo(n: int) -> bool:
    """
    幂解法
    :param n:
    :return:
    """
    if n == 0:
        return False
    return n & (n - 1) == 0


def isPowerOfTwo1(n):
    """
    普通解法
    """
    if n == 0:
        return False
    while n % 2 == 0:
        n = n / 2
    return n == 1


if __name__ == '__main__':
    print(isPowerOfTwo1(1))
