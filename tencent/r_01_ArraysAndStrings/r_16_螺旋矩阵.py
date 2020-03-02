#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author  : rusi_
# 题目链接：https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/912/


def spiralOrder(matrix):
    """
    :return:结果
    """

    def __handle_li(rl, cl, r, c, state):
        """

        :param rl:还有多少行
        :param cl:还有多少列
        :param r:哪一行开始
        :param c:哪一列开始
        :param state:“开火车”的状态 (0:左 1:下2:右3:上 )
        """
        if rl == 0 or cl == 0:
            return
        if state == 0:
            end_c = c + cl
            for i in range(c, end_c):
                res_li.append(matrix[r][i])
            rl -= 1
            r += 1
            c = end_c - 1
            state = 1
            __handle_li(rl, cl, r, c, state)
        elif state == 1:
            end_r = r + rl
            for i in range(r, end_r):
                res_li.append(matrix[i][c])
            cl -= 1
            r = end_r - 1
            c -= 1
            state = 2
            __handle_li(rl, cl, r, c, state)
        elif state == 2:
            for i in range(c, c - cl, -1):
                res_li.append(matrix[r][i])
            rl -= 1
            r -= 1
            c = c - cl + 1
            state = 3
            __handle_li(rl, cl, r, c, state)
        elif state == 3:
            for i in range(r, r - rl, -1):
                res_li.append(matrix[i][c])
            cl -= 1
            r = r - rl + 1
            c += 1
            state = 0
            __handle_li(rl, cl, r, c, state)

    if not matrix:
        return matrix

    row = len(matrix)
    col = len(matrix[0])
    res_li = []
    __handle_li(row, col, 0, 0, 0)

    return res_li


if __name__ == '__main__':
    # [1,2,3,6,9,8,7,4,5]
    print(spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
