# 题目：给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。

# 思路：与前中和后中不同的是，前后构建的树并不唯一，思路基本一致

# 解法
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, postorder)

    def build(self, preorder, postorder):
        if not preorder:
            return None
        # 这里注意长度为1的情况
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # root节点为前序遍历第一个元素
        rootVal = preorder[0]
        # root.left是前序遍历的第二个元素
        leftRootVal = preorder[1]
        # leftRootVal 在后序遍历数组中的索引
        sparator_index = postorder.index(leftRootVal)
  
        preorder_left = preorder[1:sparator_index + 2]  # 这里包括切割点，所以多加一
        preorder_right = preorder[sparator_index + 2:]

        postorder_left = postorder[:sparator_index + 1]
        postorder_right = postorder[sparator_index + 1:-1]
  

        # 构建根节点
        root = TreeNode(rootVal)
        # 递归构建左右子树
        root.left = self.build(preorder_left, postorder_left)
        root.right = self.build(preorder_right, postorder_right)

        return root