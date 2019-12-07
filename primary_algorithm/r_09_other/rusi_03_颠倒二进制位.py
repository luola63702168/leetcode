def reverseBits(n):
    # bits = "{:0>32b}".format(n)  # 2进制，左边填充0，宽度32
    # return int(bits[::-1], 2)

    x = bin(n)[2:]
    x = x.zfill(32)  # 字符串宽度32，不够补左边0
    return int(x[::-1],2)

if __name__ == '__main__':
    print(reverseBits(4294967293))