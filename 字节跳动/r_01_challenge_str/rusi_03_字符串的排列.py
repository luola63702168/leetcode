def checkInclusion(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if s1 == s2:
        return True
    if l2 < l1:
        return False
    s = "abcdefghijklmnopqrstuvwxyz"
    dict1, dict2 = {}, {}

    for i in range(len(s)):
        dict1[s[i]] = 0
        dict2[s[i]] = 0

    for j in range(l1):
        dict1[s1[j]] += 1
        dict2[s2[j]] += 1

    if dict1 == dict2:  # 此时说明按照s1的长度而言，s2最初的几个元素是和s1相符的
        return True

    for k in range(l2 - l1):
        # 这里可以理解从字符串的左边依次移除元素，每移除一个在右边添加一个，而且每次都会进行一次比较，当所有的都比较完了就退出循环了，也就说明不存在了
        dict2[s2[k]] -= 1
        dict2[s2[k + l1]] += 1
        if dict1 == dict2:
            return True
    return False

    # # todo 暴力测试（超时）
    # length_s1 = len(s1)
    # length_s2 = len(s2)
    # for i in range(length_s2):
    #     temp_str = s2[i:length_s1 + i]
    #     # print(temp_str)
    #     l1, l2 = [], []
    #     l1.extend(s1)
    #     l1.sort()
    #     l2.extend(temp_str)
    #     l2.sort()
    #     if l1 == l2:
    #         return True
    #     else:
    #         continue
    # return False


if __name__ == '__main__':
    print(checkInclusion(s1="ab", s2="eiadbaooo"))
    print(checkInclusion(s1="adc", s2="dcda"))
    print(checkInclusion("hello", "ooolleoooleh"))

"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False

注意：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
"""

# result_list = list()
# for i in range(len(s1)):
#     if s1[i] not in s2:
#         return False
#     else:
#         for k, s in enumerate(s2):
#             # print(k, s)
#             if s == s1[i]:
#                 result_list.append(k)
# print(result_list)  # 此时获得了s2中所有s1元素的索引，如果进行排序的话，必定存在一截连续的索引数据等于s1的length，或者必定满足索引相减不会大于len(s1)-1。
# result_list.sort()
# print(result_list)
# finally_list = result_list.copy()
# for j in range(1, len(result_list)):
#     if result_list[j] != result_list[j - 1] + 1:
#         finally_list.remove(result_list[j - 1])
# if len(s2) == len(finally_list):
#     return True
# return len(s1) == len(finally_list)

