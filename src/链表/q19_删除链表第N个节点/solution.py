# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
定位倒数第N个位置，因为链表都是正序的，所以首先需要知道节点总数，才能算出N节点的正序位置
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        cur = head
        dummy.next = cur
        pre = dummy
        node_nums = 0
        while cur:
            node_nums += 1
            cur = cur.next
        N = node_nums - n
        while N:
            pre = pre.next
            N -= 1
        pre.next = pre.next.next
        return dummy.next
