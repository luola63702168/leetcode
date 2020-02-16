# 堆是什么？
# 1、是一棵完全二叉树；2、所有父节点的值大于子节点的值--大顶堆（小顶堆相反）
# 如果用一个数组表示一个完全二叉树（下标顺序为从上到下，从左往右）的话，那么对于下标i而言，就会满足下面两个公式：parent=(i-1)//2  c1=2i+1 c2=2i+2。
# heapify：指的是使完全二叉树满足堆定义的操作。


def heapify(list_, n, i):
    max_ = i
    c_left = 2 * i + 1
    c_right = 2 * i + 2
    # n 是用来防止越界的
    if c_left < n and list_[i] < list_[c_left]:
        max_ = c_left

    if c_right < n and list_[max_] < list_[c_right]:
        max_ = c_right

    if max_ != i:
        list_[i], list_[max_] = list_[max_], list_[i]  # 交换
        # 递归，继续对该节点的下面层做heapify(避免修改节点值之后，下面层不满足堆定义)。
        heapify(list_, n, max_)
    # 递归出口为 max_ = i 的时候
    # return


def heap_sort(list_):
    n = len(list_)

    # 创建一个大顶堆
    last_node = n - 1
    parent = (last_node - 1) // 2
    # 倒着从最后一个父节点开始，使每个节点都能做heapify
    for i in range(parent, -1, -1):
        heapify(list_, n, i)
    print(list_)

    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        list_[i], list_[0] = list_[0], list_[i]  # 交换
        heapify(list_, i, 0)  # 恢复剩下数据的堆结构(i:刚好代表了剩下节点的数目；0代表：每次交换后都从第0个节点开始做heapify)
        # print("***", list_)


list_ = [12, 1, 14, 5, 20, 31, 6, 7]
heap_sort(list_)
print(list_)
