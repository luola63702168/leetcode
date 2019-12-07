def fizzBuzz(n):
    # result_list = list(range(1, n + 1))
    # for i in range(len(result_list)):
    #     if result_list[i] % 3 == 0 and result_list[i] % 5 == 0:
    #         result_list[i] = "FizzBuzz"
    #     elif result_list[i] % 3 == 0:
    #         result_list[i] = "Fizz"
    #     elif result_list[i] % 5 == 0:
    #         result_list[i] = "Buzz"
    #     else:
    #         result_list[i] = str(result_list[i])
    # return result_list
    result_list = []
    for i in range(1, n + 1):
        result_list.append(
            "Fizz"[(i % 3) * len("Fizz"):] + "Buzz"[(i % 5) * len("Buzz"):len("Buzz")] or str(i))
    return result_list


if __name__ == "__main__":
    print(fizzBuzz(15))
