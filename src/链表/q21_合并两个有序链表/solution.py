# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
核心方法：快慢指针
拉链法：用一个拉链（p）将两侧的锯齿串起来（p1,p2）,先串小数，最后补齐。
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        p1, p2 = list1, list2
        # 用p将小的数串起来
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
       # 将剩下的大数串起来（一个链表已经串完了，另一个还剩下一部分大数，直接串起来就齐活了）
        if p1:
            p.next = p1
        if p2:
            p.next = p2

        return dummy.next
