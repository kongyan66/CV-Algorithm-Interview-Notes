# 题目：给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， 
# inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

# 思路：和106基本一样，关键是前序遍历（or后续遍历）数组用于找切割点，首位就是中节点；
# 中序遍历数组用于拆分数组，分出左右子树，以切割点为界。
# 以上思路确实就是根据深度遍历的自身性质来的，迷惑了自己画一画就好了

# 解法一：递归法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 1.排除为空的情况
        if not preorder:
            return None
        # 2.获取节点值（前序遍历第一个就是首节点）
        node_val = preorder[0]
        root = TreeNode(node_val)
        # 3.获取中序遍历的当前节点的索引，用于分割
        sparator_index = inorder.index(node_val)
        # 4.拆分中序遍历数组
        inorder_left = inorder[:sparator_index]
        inorder_right = inorder[sparator_index+1:]
        # 5.根据中序遍历数组左右长度，裁分前序遍历数组. 注意去掉数组的第一位后再去拆分
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        # 6.递归
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
       