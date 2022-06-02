# 题目：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先（一个节点也可以是它自己的祖先）

# 思路： 先理解定义，有两种情况：1. p,q 皆为子树节点 2.p,q其中一个为上级节点
# 利用回溯从底向上搜索，遇到一个节点的左子树里有p，右子树里有q，那么当前节点就是最近公共祖先。

# 最佳解法； 递归法 回溯
class Solution:
    # 1.确定入参出参  出参：公共祖先节点
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2.确定终止条件 如果找到了 节点p或者q，或者遇到空节点，就返回。
        if root == None or root == q or root == p :
            return root
        # 3.确定单层递归逻辑
        # 获得当前节点的左右子树查询q,p的结果
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # p,q都存在， 说明root即为公共祖先
        if left != None and right != None:
            return root
        # 
        elif left != None and right == None:
            return left 
        elif right != None and left == None:
            return right
        else:
            return None


