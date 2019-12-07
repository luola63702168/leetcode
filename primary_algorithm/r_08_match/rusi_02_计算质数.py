def countPrimes(n):
    # result_list = []
    # for i in range(1, n):
    #     tem_list = [i for t in range(1, i + 1) if i % t == 0]
    #     if len(tem_list) == 2:
    #         result_list.append(i)
    # return len(result_list)

    # 厄拉多塞筛法
    # 西元前250年，希腊数学家厄拉多塞(Eeatosthese)想到了一个非常美妙的质数筛法，
    # 减少了逐一检查每个数的的步骤，可以比较简单的从一大堆数字之中，筛选出质数来，
    # 这方法被称作厄拉多塞筛法(Sieveof Eeatosthese)。
    # 具体操作：先将2~n的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；
    # 第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；现在既未画圈又没有被划去的第一个数是5，
    # 将它画圈，并划去5的其他倍数……依次类推，一直到所有小于或等于n的各数都画了圈或划去为止。
    # 这时，表中画了圈的以及未划去的那些数正好就是小于n的素数。

    if n <= 2:
        return 0
    temp_list = [0, 0] + list(range(2, n))
    for i in range(2, n):
        if i != 0:
            temp_list[i * 2:n:i] = [0] * len(temp_list[i * 2:n:i])
    # result_set = sorted(set(temp_list),key=temp_list.index,reverse=False)
    result_set = set(temp_list)
    result_set.remove(0)
    return len(result_set)


if __name__ == '__main__':
    print(countPrimes(10))
    print(countPrimes(10000))
