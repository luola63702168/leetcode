def hammingWeight(n):
    return n.count(b"1")


if __name__ == '__main__':
    print(hammingWeight(b"00000000000000000000000000001011"))
