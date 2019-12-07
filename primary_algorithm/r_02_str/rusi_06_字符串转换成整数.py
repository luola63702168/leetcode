def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    import re
    nums_re = re.compile(r"[\s]*([+-]?[\d]+)")
    result = nums_re.match(str)
    if result:
        res = int(result.group(0))
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        if res < - 2 ** 31:
            res = - 2 ** 31
    else:
        res = 0
    return res

# match(r"[\s]*[+-]?[\d]+",str)只要开头对了就可以了可以不匹配整个除非加$,它默认的是有^的
if __name__ == '__main__':
    print(myAtoi("  4193 with words"))