'''
考点：快慢指针
思想：若有环，一个快，一个慢，必相遇
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
      fast = slow = head  # 注意需要同起点，和找中点写法一致
      while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
          return True
      return False