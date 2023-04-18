# 题目：比较两棵树是否相等
# 思路： 和101.对称树解法基本一致，只不过这个不是对称而是完全相同

# 解法一：迭代法

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        return self.compare(p, q)

    def compare(self, p, q):
        if p == None and q != None: return False
        elif p != None and q == None: return False
        elif p == None and q == None: return True
        elif p.val != q.val: return False

        ouside = self.compare(p.left, q.left)      # 注意；这里是对应位置相等，而不是对称位置相等
        inside = self.compare(p.right, q.right)
        return ouside and inside