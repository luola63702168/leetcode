def firstUniqChar(s):
    return min([s.find(i) for i in "abcdefghijklmnopqrstuvwxyz" if s.count(i) == 1] or [-1])


if __name__ == '__main__':
    print(firstUniqChar("leetcode"))
    print(firstUniqChar("loveleetcode"))