# 题目：给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 
# 思路：和700.二叉树中搜索类似， 用中序遍历构建一个有序序列就很容易了

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


# 解法二：递归法