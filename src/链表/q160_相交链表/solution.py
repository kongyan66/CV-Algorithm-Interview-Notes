# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
难点在于如果两条链表长度不同，就无法用双指针逐一比较
如果把两条链表拼在一起，那么结尾部分必然是重复节点部分，否则为空
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      p1 = headA
      p2 = headB 
      # 目的是找p1=p2,所以循环条件可以设置为p1!=p2
      while p1 != p2:
        # 如果链表一遍历完了，就去链表二继续遍历,直到二者相等
        if p1 == None:
          p1 = headB
        else:
          p1 = p1.next
        if p2 == None:
          p2 = headA
        else:
          p2 = p2.next
      return p1
