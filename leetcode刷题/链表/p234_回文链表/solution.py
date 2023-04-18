# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
链表综合题
难点：链表没法像数组用双指针从两头进行比较（单向性）
思路：1.链表转数组，再进行判断
      2.将链表后一半反转过来再比较
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
      mid = self.middle(head)
      l2 = self.reverseList(mid)
      # 断开两链表连接
      mid.next = None
      l1 = head
      # 逐个比较，直到后半节点走完（避免奇偶问题）
      while l2:
        if l1.val != l2.val:
          return False
        l1 = l1.next
        l2 = l2.next
      return True
    # 获取链表中点
    def middle(self, head):
      slow = fast = head
      while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
      return slow
    # 反转链表
    def reverseList(self, head):
      pre = None
      cur = head.next
      while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
      return pre
    
    
