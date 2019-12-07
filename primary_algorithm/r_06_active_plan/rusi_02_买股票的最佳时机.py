def maxProfit(prices):
    if not prices:
        return 0
    min_num = prices[0]
    # result = None
    result = 0
    for i in prices:
        min_num = min(i, min_num)
        result = max(i - min_num, result)
    return result


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 6, 4, 3, 1]))
