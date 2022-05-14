# 题目：简单 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 思路：交换下每个节点的左右孩子

# 解法一：层序遍历
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        que = []      
        if root:         # 注意返回的是节点，不能写成[]
           que = [root]
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root