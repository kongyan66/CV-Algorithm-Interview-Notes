# 题目：给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# 思路：双指针

# 解法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
  
        while cur:
            # 必须先把下一个节点保存了
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem
        return pre # 不是cur, 此时cur已为None
     