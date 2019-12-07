import re


# coding: utf-8
def isValid(s):
    str_re = re.compile(r"\(|\)|\{|\}|\[|\]")
    temp_list = str_re.findall(s)
    if len(temp_list) % 2 != 0: return False
    elif len(temp_list) == 0: return True

    temp_map = {")": "(", "]": "[", "}": "{"}
    cont_list = [None]
    for par in temp_list:
        if par not in temp_map:
            cont_list.append(par)
        else:
            if cont_list[-1] != temp_map[par]:
                return False
            cont_list.pop()
    return len(cont_list) == 1


# 用栈来解决
if __name__ == "__main__":
    print(isValid("(){}"))
    print(isValid(""))
    print(isValid("){"))
