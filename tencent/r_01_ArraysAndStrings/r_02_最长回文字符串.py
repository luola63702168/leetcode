#   最长回文子串
#   给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

#   示例 1：
#   输入: "babad"
#   输出: "bab"
#   注意: "aba" 也是一个有效答案。

#   示例 2：
#   输入: "cbbd"
#   输出: "bb"


def longestPalindrome(s):
    """
    基本思路：
    1、是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。
    2、如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。
    :param s:
    :return:
    """
    s_leh = len(s)
    max_l = 0  # 指的是这个回文字符串的长度
    curr = 0  # 这个指的是，每次回文字符串索引对应的位置。
    for i in range(s_leh):
        # i - max_l >= 1：看看：看看添加两个字母能不能达到回文字符串的效果。
        # s[i - max_l - 1: i + 1]：以i索引所在的位置往前数max_l的长度在加上头和尾，看看是否为回文字符串。
        if i - max_l >= 1 and s[i - max_l - 1: i + 1] == s[i - max_l - 1: i + 1][::-1]:
            print(s[i - max_l - 1: i + 1])
            curr = i - max_l - 1
            max_l += 2  # 此时加上头和尾的长度
            continue
        # i - max_l >= 0 代表：看看添加一个字母能不能达到回文字符串的效果。
        # s[i - max_l - 1: i + 1]：以i索引所在的位置往前数max_l的长度在加上尾，看看是否为回文字符串。
        if i - max_l >= 0 and s[i - max_l: i + 1] == s[i - max_l: i + 1][::-1]:
            # print(s[i - max_l: i + 1])
            curr = i - max_l
            max_l += 1  # 此时加上尾的长度
    # print(curr, max_l)
    return s[curr: curr + max_l]

# 为什么 i - max_l >= 1 要放在前面？：因为当满足：i - max_l >= 1 条件的时候，max_l是要 += 2 的 ，比 max_l += 1 “划算”。
# 为什么要有 continue， 当满足上面条件的时候不会再满足下面条件了（下面的条件其实只是为 单个字母回文字符串和添加相同字母后的回文字符串 服务的。）。
# 所以其实可以把两个if条件换个位置都能解决该问题，这样写代码的目的是为了配合 continue 达到性能最优。

# i - max_l >= 0 和 i-max_l >=1 的区别是：前者是不能在 头尾 各加一个字母的，但是后者可以在尾部加一个字母（这也是为什么>=的缘故，因为>=1必定满足>=0，头尾加字母不行，就只在尾加字母试试）。
# 比如i = max_l 时 i-max_l - 1 是等于 -1 的 --->s[i - max_l - 1: i + 1] 是会出错的。


if __name__ == '__main__':
    # print(longestPalindrome("abcdedcba"))
    # print(longestPalindrome("abcda"))
    # print(longestPalindrome(""))
    # print(longestPalindrome("bacab"))
    # print(longestPalindrome("abacab"))
    print(longestPalindrome("babad"))
    # print(longestPalindrome("aaabaaaaaa"))
