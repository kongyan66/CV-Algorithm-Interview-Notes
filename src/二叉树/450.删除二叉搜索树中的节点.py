# 题目：给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变

# 思路：先找到要删除节点的位置，再根据其左右子树的情况进行删除
# https://leetcode.cn/problems/delete-node-in-a-bst/solution/miao-dong-jiu-wan-shi-liao-by-terry2020-tc0o/
# 疑问： 对递归的返回参数不是很理解
# 解法1： 递归
class Solution:
    # 1.确定入参与出参
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 2.确定终止条件
        if root is None:
            return None
        # 3.确定单层递归逻辑
        # 搜寻欲删除节点的位置
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # 情况一：欲删除的节点无左节点, 其右子顶替其位置, 如果左右均无，则返回空
            if root.left is None:
                return root.right
            # 情况二：欲删除的节点无右节点, 其左子顶替其位置
            if root.right is None:
                return root.left
            # 情况三：欲删除的节点左右节点均有,其左子树转移到其右子树的最左节点的左子树上，然后右子树顶替其位置
            node = root.right
            while node.left:         # 找右子树最左节点
                node = node.left
            node.left = root.left    # 只能放左左子树（有序性）
            root = root.right        # 右子树覆删除节点位置
        return root
