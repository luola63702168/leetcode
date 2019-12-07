import math


def isPowerOfThree(n):
    # has_three = True
    # if n <= 0:
    #     return False
    # t = math.log(n, 3)
    # print(t, int(t))  # 因为精度问题，当n取243的时候，这种方法错误
    # if t > int(t):
    #     has_three = False
    # return has_three

    if n <= 0:
        return False
    return 3 ** round(math.log(n, 3)) == n


if __name__ == '__main__':
    # print(isPowerOfThree(27))
    # print(isPowerOfThree(0))
    print(isPowerOfThree(243))
