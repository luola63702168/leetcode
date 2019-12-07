# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = head
        temp = None
        while res:
            case = res.next
            res.next = temp
            temp = res
            res = case
        return temp

