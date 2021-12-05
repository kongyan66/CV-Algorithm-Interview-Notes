# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
在头节点前加一个空值，依次将后面节点指向前面节点（还是pre、cur、nex三者同步滑动）
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre =cur
            cur =nex
        return pre
