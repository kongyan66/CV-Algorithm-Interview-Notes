# 题目：给你一个链表数组（头结点用列表存），每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 思路1：分而治之，也可看做归并排序，链表两两合并
# 以下采用了两个递归，思路和数组排序一致，即归并排序，吧多个链表分解为两个链表，排好序后再合并，
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        return self.merge(lists, 0, len(lists) - 1)
       
    # 归并排序  这块用while循环写也是可以的
    # 1.确定返回值 两段链表数组的合并后的头结点
    def merge(self, lists, left, right):
        if left > right:
            return 
        if left == right:
            return lists[left]
        
        mid = (left + right) // 2
        list1 = self.merge(lists, left, mid)
        list2 = self.merge(lists, mid+1, right)

        return self.mergeTwoLists(list1, list2)
    # 1.确定返回值 返回两段链表合并后的节点
    def mergeTwoLists(self, list1, list2):
            # 2.确定停止条件
            if not list1:
                return list2
            if not list2:
                return list1
            # 如果list1第一个节点小，就让它去连接后面排序好得节点，相当于后续遍历
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2

# 思路2：优先级队列