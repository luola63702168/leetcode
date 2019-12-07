def climbStairs(n):
    a = 1
    b = 2
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        for i in range(3, n + 1):
            result = a + b
            a = b
            b = result
        return result


if __name__ == '__main__':
    print(climbStairs(3))
    print(climbStairs(4))
    print(climbStairs(7))
