# 题目：给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# 思路一：用list保存链表值，然后再判断是否为回文列表

# 思路二：找到中间位置阶段，反转后半部分链表，然后再逐一比较
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = pre =   head
        # 找中点
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        # 翻转后半部分
        head1 = self.reverse(slow)
        # 逐一比较
        while head:
            if head.val != head1.val:
                return False
            head = head.next
            head1 = head1.next
        return True

    def reverse(self, head):
        pre = None
        cur = head

        while cur:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem
        return pre