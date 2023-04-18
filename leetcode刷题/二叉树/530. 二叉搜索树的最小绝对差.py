# 题目：给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 
# 思路：和700.二叉树中搜索类似， 用中序遍历构建一个有序序列（单调递增），那么任意两节点的最小差值就转换为
# 相邻节点的最小差值

# 解法一： 迭代法 中序遍历

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        result = []
        res = float("inf")            # res初始值赋无穷大
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        for i in range(len(result)-1):
            res = min(res, abs(result[i+1]-result[i]))
        return res


# 解法二：递归法 思路和迭代法法一致
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre = None
        minvalue = float('INF')
        def recursion(root):
            nonlocal pre
            nonlocal minvalue
            if not root:
                return
            recursion(root.left)
            cur = root
            if pre:
                minvalue = min(minvalue, cur.val - pre.val)
            pre = cur
            recursion(root.right)
        recursion(root)
        return minvalue
