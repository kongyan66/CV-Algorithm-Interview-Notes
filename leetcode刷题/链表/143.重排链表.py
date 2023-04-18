'''
考点：链表综合
思路：获取链表中点->拆两半->后半部分反转->依次合并
      先获取链表中点，然后将链表拆成两个链表（左链表包含中点），之后将右半节点反转，最后将两链表合并。
      合并顺序：先右后左
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        # 找中点
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        # 注意这里前半部分长一些（奇数下）
        right = slow.next
        slow.next = None
        # 翻转后半部分
        right = self.reverse(right)
        left = head
        # 交叉连接 一次换两即可
        # 由于左部分大于等于右半部分，所以只看右半部分就行
        while right:
            curLeft = left.next
            left.next = right
            left = curLeft

            curRight = right.next
            right.next = left
            right = curRight

    def reverse(self, head):
        pre = None
        cur = head

        while cur:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem
        return pre