# 题目：给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# 思路：首先定义一个cur指针，指向头结点，再定义一个pre指针，初始化为null。然后让cur 指向pre，直到cur为空

# 解法：双指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem
        return pre