def romanToInt(s):
    # rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # result_num = 0
    # for i in range(len(s) - 1):
    #     if rom_dict[s[i]] >= rom_dict[s[i + 1]]:
    #         result_num += rom_dict[s[i]]
    #     else:
    #         result_num -= rom_dict[s[i]]
    # return result_num + rom_dict[s[-1]]  # roman_str[i + 1]
    d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
         'CM': 800, 'M': 1000}
    print(list(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s)))
    return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))

if __name__ == '__main__':
    print(romanToInt("CMCMIV"))
    # print(romanToInt("III"))