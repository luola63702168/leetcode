def _func(s):
    if s.isdigit():
        return True
    return s.isalpha()


def isPalindrome(s):
    if not s:
        return True
    str_list = list((filter(_func, s)))
    s = ''.join(str_list)
    s = s.lower()
    return s[::] == s[::-1]


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))


# ord()
# 它是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的
# Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。

