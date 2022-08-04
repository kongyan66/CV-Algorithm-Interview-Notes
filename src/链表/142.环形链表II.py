# 题目：给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 思路：快慢指针 慢指针走一步，快指针走两步，若有环必然在环内相遇，再从头结点出发一个指针，同步走一步，会在交点处相遇


# 解法
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head 
        while fast and fast.next: # 保证fast.next不为空
            fast = fast.next.next
            slow = slow.next
            # 找环内交点
            if slow == fast:
                cur = head
                # 找相交点
                while cur != slow:
                    cur = cur.next
                    slow = slow.next
                return cur
        return None
