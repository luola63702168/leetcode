class Solution(object):
    def removeDuplicates(self):
        nums = [0, 0, 1, 1,2, 1, 2, 2, 3, 3, 4,4,100, 100, 100,]
        # 进行n-1次即可判断所有元素了
        for i in range(len(nums) - 1):
            # print(len(nums))
            for j in nums[i + 1:]:
                # print(j)
                # print(nums[i+1:])
                if nums[i] == j:
                    # print("w%d"%nums[i])
                    # print("w%d"%nums[i])
                    nums.remove(nums[i])
                # else:
                #     break
        print(nums)


i = Solution()
i.removeDuplicates()

list0=['b','c', 'd','b','c','a','a',0, 0, 1, 1,2, 1, 100, 100, 100,2, 2, 3, 3, 2,4,4,]

# 一
# list0.index是一个函数的引用，sorted会将set(list0)中所有的元素当作参数传入这个函数中，并以返回值，也就是原列表的索引为排序标准进行排序。
# sorted()的第三个参数：reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

# list1=sorted(set(list0),key=list0.index)  # list1=sorted(list0,key=list0.index)
list1=sorted(set(list0),key=lambda x:list0.index(x))  # list1=sorted(list0,key=list0.index)

# set()方法会将重复的删除
# print(set(list0))
print( list1)

# 二（ 利用了字典的键是不可以相同的原理，keys()返回字典的key的列表）
# dict.fromkeys(seq[, value])
# seq -- 字典键值列表。
# value -- 可选参数, 设置键序列（seq）的值。
list2={}.fromkeys(list0).keys()
print(list2)

# 三
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
list3=list(set(list0))
list3.sort(key=list0.index)
print(list3)

# 四
list4=[]
for i in list0:
    if not i in list4:
        list4.append(i)
print(list4)


# 五
# 这个办法，字符串和整型不可以比较。
def sortlist(list0):
    list0.sort()
    last=list0[-1]
    for i in range(len(list0)-2,-1,-1):
        if list0[i]==last:
            list0.remove(list0[i])
        else:
            last=list0[i]
    return list0


# print(sortlist(list0))





