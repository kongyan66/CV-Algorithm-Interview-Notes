# 题目：给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

# 思路：归并排序，利用DFS—postorder
# 分割（找中点）：利用快慢指针，快指针到头了，慢指针就到中点了，奇数个节点找到中点，偶数个节点找到中心左边的节点。
# 合并：对两段链表重新排序，参考88.合并两个有序数组

# 解法：归并排序
class Solution:
    # 1.确定返回值 排好序的子链表的头结点
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2.确定递归停止条件
        # 如果就剩一个节点或者空节点就停止
        if not head or not head.next:
            return head
        # 前序分割
        slow, fast = head, head.next  # 奇数个节点找到中点，偶数个节点找到中心左边的节点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        # 后续合并
        dumppy = p = ListNode()
        # 对子链表进行排序
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right 
                right = right.next
            p = p.next
        # left 或者 right 可能有一个一点都没动
        p.next = left if left else right
        return dumppy.next