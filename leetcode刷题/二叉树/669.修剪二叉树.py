# 题目：给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。

# 思路：这里涉及到选择合适节点，然后重新拼装，与450.删除节点类似
# 解法一：递归法 后续遍历
class Solution:
    # 1.确定入参与返回值
    # 返回值构建好树的根节点
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.trimBST(root.left, low, high)
        right = self.trimBST(root.right, low, high)
        
        # 后序遍历重装组装
        # 如果当前节点值小于左边界，就用右子树替换
        if root.val < low:
            root = right
        # 如果当前节点值大于右边界，就用左子树替换
        elif root.val > high:
            root = left
        # 区间内，正常连接
        else:
            root.left = left
            root.right = right

        return root