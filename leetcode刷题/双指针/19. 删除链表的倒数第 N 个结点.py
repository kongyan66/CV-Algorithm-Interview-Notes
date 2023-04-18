# 题目：给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 解法： 快慢指针 哨兵节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 为啥需要哨兵呢？应为链表中每个节点都有可能被删除
        dumpy = ListNode()
        dumpy.next = head
        slow, fast = dumpy, dumpy
        # 先让fast 走n步，然后slow再与之同步走
        while n != 0:
            fast = fast.next
            n -= 1
        # 当fast.next 为空时，slow就到了要删除节点的前一个位置
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dumpy.next
        