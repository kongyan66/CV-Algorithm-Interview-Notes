# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
考点：链表综合
思路：获取链表中点->拆两半->后半部分反转->依次合并
      先获取链表中点，然后将链表拆成两个链表（左链表包含中点），之后将右半节点反转，最后将两链表合并。
      合并顺序：先右后左
'''
class Solution:
    # 总函数
    def reorderList(self, head: ListNode) -> None:
      # 若为空，返空
      if not head:
         return
      # 获得中间节点
      mid = self.middle(head)
      head1 = head
      head2 = mid.next
      # 断开链表
      mid.next = None
      # 右半链表反转
      head2 = self.reverseList(head2)
      self.mergeList(head1,head2)
      
    # 获得链表的中间节点（偶数为左中）
    def middle(self, head):
      slow = fast = head
      while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
      return slow
    # 反转链表
    def reverseList(self, head):
      pre = None
      cur = head
      while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
      return pre
   # 将两个节点交叉融合
    def mergeList(self, head1, head2):
      dummy = head1
      l1 = head1
      l2 = head2
      while l1 and l2:
        nex1 = l1.next
        nex2 = l2.next
        # 依次连接
        l1.next = l2
        l1 = nex1
        l2.next = l1
        l2 = nex2
      return dummy
