# 题目：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先（一个节点也可以是它自己的祖先）

# 思路： 先理解定义，有两种情况：1. p,q 皆为子树节点 2.p,q其中一个为上级节点

# 最佳解法； 递归法 回溯
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2.确定终止条件
        if root == None or root == q or root == p :
            return root
        # 3.确定单层递归逻辑
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None:
            return root
        elif left != None and right == None:
            return left 
        elif right != None and left == None:
            return right
        else:
            return None


