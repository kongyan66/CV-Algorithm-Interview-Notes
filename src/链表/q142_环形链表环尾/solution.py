# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
考点：快慢指针
难点：推导相交节点数学规律
思路：第一步：查看是否有环（q141）
      第二步：若有环，分别从头结点和相遇节点出发，再次相遇时既是相交节点，否则返回空
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
      fast = slow = head
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
          # 分别从头结点和相遇节点出发，再次相遇时既是相交节点（需要通过公式推导规律）
          while head != slow:
            head = head.next
            slow = slow.next
          return slow

      return None
         
         
         

       

        
      
