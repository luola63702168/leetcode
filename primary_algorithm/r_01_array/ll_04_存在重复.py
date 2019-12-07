def existence_repeat(list_):
    '''测试一个数组中是否有重复选项'''
    # if len(set(list_)) < len(list_):
    #     return True
    # else:
    #     return False

    return len(set(list_)) != len(list_)

if __name__ == "__main__":
    print(existence_repeat([1,2,3,1]))
    print(existence_repeat([1,2,3,4]))
    print(existence_repeat([1,1,1,3,3,4,3,2,4,2]))

