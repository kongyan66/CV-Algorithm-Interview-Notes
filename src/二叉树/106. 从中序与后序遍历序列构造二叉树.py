# 题目：给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，
# 请你构造并返回这颗 二叉树 。

# 思想：此题需要一定技巧，所以看下面步骤（自己想肯定想不来啊），而且此题最适合递归写

# 解法一：递归
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 第一步：排除特殊情况 如果为空，说明树为空
        if len(postorder) == 0:
            return None
        # # 第二步: 后序遍历的最后一个就是当前的中间节点. 
        root_val = postorder[-1]
        root = TreeNode(root_val)
        # 第三步: 找切割点. 
        separator_index = inorder.index(root_val)
        # 第四步：切割inorder数组. 得到inorder数组的左,右半边.
        inorder_left = inorder[:separator_index]
        inorder_right = inorder[separator_index+1:]
       # 第五步：同一棵树，所以可以由inposder的左右长度，得到postorder数组的左右半边
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]
        # 第六步：递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

# 解法二：迭代法

