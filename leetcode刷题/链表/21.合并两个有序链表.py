# 题目：将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 思路：

# 解法一：递归法
# 一定想好返回值是啥，功能抽象化
class Solution:
    # 1.确定返回值 合并好链表的头结点
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

# 解法二：迭代法
# 与排序链表、排序数组思路一致

class Solution:
    # 1.确定返回值 合并好链表的头结点
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # p 相当于拉链， dummpy还是哨兵节点用于定位
        dummpy = p = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        # 如果其中一个节点还剩下一部分，p继续补完
        while list1:
            p.next = list1
            list1 = list1.next
            p = p.next
        
        while list2:
            p.next = list2
            list2 = list2.next
            p = p.next
        
        return dummpy.next
