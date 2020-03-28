# ://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/939/
def isPalindrome(x):
    """
    """
    tmp_s = str(x)
    return tmp_s == tmp_s[::-1]


if __name__ == "__main__":
    print(isPalindrome(121))
