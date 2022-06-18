# 题目：给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。

# 思路：这里涉及到选择合适节点，然后重新拼装，与450.删除节点类似
# 解法一：迭代法
class Solution:
    # 1.确定入参与返回值
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 2.确定递归停止条件
        # 修建操作并不是在终止条件上进行的，所以需要空节点返回None就行
        if not root:
            return 
        # 3.确定单层递归逻辑
        # 如果root(当前节点)的元素大于high的，那么应该递归左子树，并返回左子树符合条件的头结点。
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # 如果root（当前节点）的元素小于low的数值，那么应该递归右子树，并返回右子树符合条件的头结点。
        elif root.val < low:
             return  self.trimBST(root.right, low, high)
        # 节点值符合条件，符合要求
        # 重新拼接符合条件的节点,这个写法不是很好理解，多看看吧
        elif low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root