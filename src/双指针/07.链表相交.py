# 题目：给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

# 思想: 根据快慢法则，走的快的一定会追上走得慢的。

# 解法：快慢指针
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
         """
        根据快慢法则，走的快的一定会追上走得慢的。
        在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

        那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
        位置相遇
        """
        cur_a, cur_b = headA, headB
        while cur_a != cur_b:
            if cur_a:
                cur_a = cur_a.next
            else:
                cur_a = headB
            if cur_b:
                cur_b = cur_b.next
            else:
                cur_b = headA
        return cur_a
