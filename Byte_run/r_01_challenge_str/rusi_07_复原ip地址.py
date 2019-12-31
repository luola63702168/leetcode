import itertools

"""
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""


def restoreIpAddresses(s):
    """
    :param s: ip str
    :return: result  list : The possibility of IP address
    """
    result_list = list()
    s_len = len(s)
    if s_len > 12 or s_len < 4:
        return result_list

    def correct_num(s):
        return 0 <= int(s) <= 255 and str(int(s)) == s

    return [s[:i] + '.' + s[i:j] + '.' + s[j:k] + '.' + s[k:] for (i, j, k) in
            itertools.combinations(range(1, len(s)), 3) if
            correct_num(s[:i]) and correct_num(s[i:j]) and correct_num(s[j:k]) and correct_num(s[k:])]


# 'Python itertools' module 'combinations (iterable, r)'
# method can create an iterator to return all subsequences of length r in Iterable,
# and the items in the returned subsequences are sorted according to the order of input 'Iterable'.

if __name__ == '__main__':
    print(restoreIpAddresses("25525511135"))
