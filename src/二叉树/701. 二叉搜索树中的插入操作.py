# 题目：给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树
# 思路：根据二叉搜索树的有序性，只要找到他的父节点（值大于它）接入即可

# 解法一：迭代法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        parent = None
        cur = root
        # 定位要插入位置父节点的位置
        while cur: 
            if cur.val > val:
                parent = cur
                cur = cur.left
            elif cur.val < val:
                parent = cur
                cur = cur.right
            
        if parent.val > val:
           parent.left = TreeNode(val)
        else:
           parent.right = TreeNode(val)
        return root

# 解法二： 递归法
class Solution:
    # 1.确定入参与出参(yao)
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 2.确定终止条件 
        # 找到遍历节点为None的时候，就是要插入节点的位置，返回要插入的节点
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root 