# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dummpy = ListNode(0)
        dummpy.next = head
        pre = dummpy
        cur = head
        if not head or not head.next:
            return head

        while cur:
            # 遍历所有重复的数，并将指针cur 定位到最后一个重复数字位置
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 如果没有重复数，就让pre跟在cur后面（pre和cur相邻）
            if pre.next == cur:
               pre = pre.next
            # 如果有重复的数，就跳过所有数，让pre指向第一个不重复的数
            else:
               pre.next = cur.next
            # 继续往后平移
            cur = cur.next

        return dummpy.next
