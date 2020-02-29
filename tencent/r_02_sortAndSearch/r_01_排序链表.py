# 排序链表
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 示例 1:
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    归并排序
    """

    def sortList(self, head):
        """
        快慢指针分割链表
        :param head:
        :return:
        """
        # 空的，或者只有一个
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        # print(id(slow),id(fast),id(head))

        # 快慢指针找到中间节点（slow走一步，fast走两步）
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next

        slow.next = None  # 由于链表种存的都是地址，所以此时改变的其实是该链表中的链接关系，从而断开链表
        return self.merge(*map(self.sortList, [head, mid]))

    def merge(self, l1, l2):
        """
        依次合并子链表
        :param l1: 子链表1
        :param l2: 子链表2
        :return: 排序后的结果
        """
        dummy = tmp_l = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                tmp_l.next, tmp_l, l1 = l1, l1, l1.next
            else:
                tmp_l.next, tmp_l, l2 = l2, l2, l2.next

        tmp_l.next = l1 or l2  # 把剩下的还有的也拼接一下
        return dummy.next


def sortList1(head):
    """
    第二种方法：利用列表替换数据。。。
    :param head:
    :return:
    """
    if not head or not head.next:
        return head

    res_link = head
    tmp_list = []
    while head:
        tmp_list.append(head.val)
        head = head.next

    tmp_list.sort()
    head = res_link
    i = 0
    while head:
        head.val = tmp_list[i]
        head = head.next
        i += 1

    return res_link


if __name__ == "__main__":
    s = Solution()
    l_tmp = head = ListNode(None)
    # print(id(l),id(head))
    for val in [0, 4, 1, 6, 7]:
        l_tmp.next = ListNode(val)
        l_tmp = l_tmp.next
    # print(id(l), id(head))
    li = s.sortList(head.next)
    while li:
        print(li.val)
        li = li.next
