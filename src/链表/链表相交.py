# 思路 追击原理
'''
根据快慢法则，走的快的一定会追上走得慢的。
在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。
那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个位置相遇
'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a, cur_b = headA, headB
        # 若有交点，则再某节点出，cur_a与cur_b相等
        # 若无交点，在a+b步后均会同时指向null，退出循环（这点不好理解）
        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB # a走完了切换到b
            cur_b = cur_b.next if cur_b else headA # 同理
        return cur_a
        