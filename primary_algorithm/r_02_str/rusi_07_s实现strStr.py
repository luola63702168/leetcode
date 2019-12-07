def strStr(haystack,needle):
    """
    """
    import re
    if needle == "":
        return 0
    nums_re = re.compile(rf"{needle}")
    result = nums_re.search(haystack)
    if result:
        # print(result)
        return result.span()[0]
    else:
        return -1


if __name__ == '__main__':
    print(strStr("aaaaa","bba"))