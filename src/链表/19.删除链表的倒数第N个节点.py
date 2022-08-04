# 思路： 快慢指针 快指针先去定位
# 定位倒数第N个位置，因为链表都是正序的，所以首先需要知道节点总数，才能算出N节点的正序位置

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 为啥需要哨兵呢？应为链表中每个节点都有可能被删除
        dummpy =  ListNode()
        dummpy.next = head
        fast = slow = dummpy
        # fast先走（n+1)步
        for _ in range(n+1):
            fast = fast.next
        # 然后fast slow同步走，当fast为空时，slow到达要删除节点的前一个位置
        while fast:
            fast = fast.next
            slow = slow.next
        # 删除节点，重新连接
        slow.next = slow.next.next
        return dummpy.next