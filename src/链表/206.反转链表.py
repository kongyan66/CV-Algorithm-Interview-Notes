# 题目：给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# 思路：双指针

# 解法一：双指针
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
# 解法二:递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        return self.recursion(pre, cur)
    # 1.确定入参与返回值 
    def recursion(self, pre, cur):
        # 2.确定递归停止条件
        if not cur:
            return pre
        # 3.确定单层递归逻辑
        tem = cur.next
        cur.next = pre
        # 有返回值 接收停止条件的返回值
        return self.recursion(cur, tem)