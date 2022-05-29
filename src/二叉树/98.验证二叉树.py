# 题目：给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
'''
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''
# 思路：中序遍历下，输出的二叉搜索树节点的数值是升序序列，这点很重要啊

# 解法一：迭代法 中序遍历
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        pre_val = float('-inf')    # 表示负无穷，记录前一个节点值
        # 中序遍历
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 判断是否为升序
            if root.val <= pre_val:
                return False
            pre_val = root.val
            root = root.right
        return True

# 解法二: 递归法
