# 题目：给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null

# 思路：通过计算路径关系，我们得到一个结论：当fast与slow相遇后，出发一个指针与从头节点出发一个指针，两者会在交点处相遇
# 解法一： 双指针  快慢指针
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:  # 结束位置在节点倒数第二个位置，刚好fast.next.next=None
            slow = slow.next
            fast = fast.next.next  # fast速度是slow的二倍
            # 当快慢指针相遇，此时从相遇处、头结点处分被出发一个新指针，再次相遇就是环交点处了
            if slow == fast:
                q = head
                p = slow
                while q != p:
                    q = q.next
                    p = p.next
                return q
        return None