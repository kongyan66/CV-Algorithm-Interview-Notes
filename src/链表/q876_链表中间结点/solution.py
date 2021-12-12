# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
考察点：快慢指针
思想：路程一样，慢指针速度为1，快指针速度为2，则当快指针走到头时，慢指针到达中间位置
难点：因为长度有奇偶，所以需要考虑快指针在哪停合适，可以手动推倒下
'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
      slow = head
      fast = head
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      return slow
