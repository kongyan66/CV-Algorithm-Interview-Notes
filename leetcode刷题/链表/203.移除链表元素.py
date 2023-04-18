# 题目：给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 思路：遇到等于val的节点就跳过，还有就是哨兵节点很重要

# 解法
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 这里哨兵很重要，假若删除是第一个节点，那么就不好找头结点了，所以从哨兵开始遍历
        dummpy = ListNode(next=head)
        cur = dummpy
        while cur.next:
            # 遇到下一个值为val就跳过，这里哨兵的值不参与比较，所以是下一个节点的值
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummpy.next