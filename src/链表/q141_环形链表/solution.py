# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
考点：快慢指针
思想：若有环，一个快，一个慢，必相遇
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
      fast = slow = head
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
          return True
      return False
