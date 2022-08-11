# 题目：用两条链表倒序存另个数，求两个数的和，依然用连班保存。
# 思路：对应位求和，先算进位符，再算当前位值

# 解法一：迭代法
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dumpy = ListNode()
        p = dumpy
        carry = 0  # 进位符
        while l1 or l2 or carry > 0:
            val = 0
            # 先处理第一条链表
            if l1:
                val += l1.val
                l1 = l1.next
            # 处理另一条节点
            if l2:
                val += l2.val
                l2 = l2.next
            # 处理当前值与进位值
            
            val += carry
            carry = val // 10 # 一定先算carry，后面val就变了
            val = val % 10
            p.next = ListNode(val)
            p = p.next
    
        return dumpy.next

# 解法二：递归
# 递归写法简化了迭代的很多操作
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        # 确定返回值
        def recursion(l1, l2, carry):
            # 当两条节点为空且无进位，加法结束
            if not l1 and not l2 and carry == 0:
                return None
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            node = ListNode(val % 10)
            node.next = recursion(l1.next if l1 else None, l2.next if l2 else None, val // 10)
            return node
        return recursion(l1, l2, 0)