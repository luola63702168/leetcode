class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        """
        res = ListNode(0)
        res.next = head
        l1 = res
        l2 = res
        for i in range(n):
            l1 = l1.next
        while l1.next:
            l1 = l1.next
            l2 = l2.next
        l2.next = l2.next.next
        return res.next

if __name__ == '__main__':
    s=Solution()
    s.removeNthFromEnd([1,2,3,4,5],2)