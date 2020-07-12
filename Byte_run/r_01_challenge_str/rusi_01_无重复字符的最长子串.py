def lengthOfLongestSubstring(s):
    if not s:
        return 0
    result_str = ""
    res_set = set()
    for i in range(len(s)):
        if s[i] not in result_str:
            result_str += s[i]
            # 通过异常判断也是可以的，出现异常的时候就是该字符串不存在重复，result_list中没有数据max()函数出错
            res_set.add(len(result_str))
        else:
            res_set.add(len(result_str))
            # print(result_str.index(s[i]))
            result_str = result_str[result_str.index(s[i])+1:] + s[i]
            # print(i)
            # print(result_str)
    res_set.add(len(result_str))
    return max(res_set)

    # try:
    #     max(res_list)
    # except Exception as e:
    #     return len(s)
    # else:
    #     return max(res_list)


if __name__ == '__main__':
    # print(lengthOfLongestSubstring(" "))
    # print(lengthOfLongestSubstring(""))
    print(lengthOfLongestSubstring("au"))
    print(lengthOfLongestSubstring("aab"))
    print(lengthOfLongestSubstring("dvdf"))
    # print(lengthOfLongestSubstring("aabaab!bb"))

'''无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。'''


