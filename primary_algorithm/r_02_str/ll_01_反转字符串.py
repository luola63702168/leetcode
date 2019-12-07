def reverseString(s):
    str_list = s.copy()
    str_list.reverse()
    s[:] = str_list
    return s



if __name__ == '__main__':
    print(reverseString(["h","e","l","l","o"]))