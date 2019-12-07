def reverse(x):
    str_ = str(x)
    if x == 0:
        return 0
    elif x > 0:
        x = int(str_[::-1])
    else:
        x = int('-' + str_[::-1].rstrip("-").rstrip("0"))
    if -2 ** 31 < x < 2 ** 31 - 1:
        return x
    return 0
    
    # str_= str(x)
    # if x == 0 or x <= -2 ** 31 or x >= 2 ** 31-1 :
    #     return 0
    # elif x > 0:
    #     if not str_.endswith("0"):
    #         return int(str_[::-1])
    #     else:
    #         return int(str_[::-1])
    # else:
    #     return int('-' + str_[::-1].rstrip("-").rstrip("0"))


if __name__ == '__main__':
    print(reverse(-123))
    print(reverse(123))
    print(reverse(120))
    print(reverse(0))
    print(reverse(-10))

