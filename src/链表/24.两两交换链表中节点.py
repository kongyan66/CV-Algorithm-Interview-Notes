# 题目：给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。

# 思路：三个为一个单位进行交换，注意要提前保存连接点位置

# 迭代法
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dumpy = ListNode(next=head)
        pre = dumpy
        # 必须有pre的下一个和下下个才能交换，
        while pre.next and pre.next.next:   # 顺序有讲究的额，否则会报空指针错误
            # 提前保存下需要连接的节点
            cur = pre.next
            post = pre.next.next.next

            # 交换相邻节点
            pre.next = cur.next
            pre.next.next = cur
            cur.next = post
            # cur 更新位置 向前走两步
            pre = pre.next.next
        return dumpy.next

# 递归法
# https://leetcode.cn/problems/swap-nodes-in-pairs/solution/hua-jie-suan-fa-24-liang-liang-jiao-huan-lian-biao/
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.recursion(head)
    # 1.确定入参与返回值
    # 返回值 交换完成的子链表头节点
    def recursion(self, head):
        # 2.确定停止条件
        # head 为空指针或者 next 为空指针，也就是当前无节点或者只有一个节点，无法进行交换
        if not head or not head.next:
            return head
        # 3.单层递归逻辑
        # 设需要交换的两个点为 head 和 next，head 连接后面交换完成的子链表，next 连接 head，完成交换
        post = head.next
        head.next = self.recursion(post.next)
        post.next = head
        return post
        