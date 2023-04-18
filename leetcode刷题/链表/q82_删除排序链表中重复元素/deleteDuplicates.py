# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
如果有重复元素，就让cur指向最后一个重复元素位置，然后pre指向cur的下一个节点，即可断开重复
部分元素（删除重复元素）
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 创建加节点，用于构建per（师傅）、cur（二师兄）、nex（大师兄）
        dummpy = ListNode(0)
        dummpy.next = head
        pre = dummpy
        cur = head
        # 如果给的链表为空或者只有两个元素，返回该链表
        if not head or not head.next:
            return head
        # cur遍历所有节点（师徒三人西天取经）
        while cur:
            # 遍历所有重复的数，并将指针cur 定位到最后一个重复数字位置（如果遇到妖怪，徒弟二人前去探路，师傅留在原地）
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 如果没有重复数，就让pre跟在cur后面（pre和cur相邻）（一路平安，师徒三人同步前进）
            if pre.next == cur:
               pre = pre.next
            # 如果有重复的数，就跳过所有数，让pre指向第一个不重复的数 （化险为夷，师傅直接跳过危险区，走到安全区）
            else: 
               pre.next = cur.next
            # 继续往后平移（一路平安，师徒三人同步前进）
            cur = cur.next

        return dummpy.next
