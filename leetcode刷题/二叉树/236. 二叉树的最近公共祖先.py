# 题目：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先（一个节点也可以是它自己的祖先）
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
# 思路： 先理解定义，有两种情况：1. p,q 皆为子树节点 2.p,q其中一个为上级节点
# 利用回溯从底向上搜索，遇到一个节点的左子树里有p，右子树里有q，那么当前节点就是最近公共祖先。

# 最佳解法； 递归法 回溯
class Solution:
    # 1.确定函数返回值与入参
    # 需要递归函数返回值，来告诉我们是否找到节点q或者p,如果找到就返回根节点，没找到就返回None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2.确定递归停止条件
        if not root:
            return root
        # 如果找到了p,q 其中一个是根节点，就返回该节点
        if root == q or root == p:
            return root
        
        # 3.确定单层递归逻辑
        # 在左子树找,由于p,q值不同，所以不会找重复的
        left = self.lowestCommonAncestor(root.left, p, q)
        # 在右子树找
        right = self.lowestCommonAncestor(root.right, p, q)
        # 分情况讨论
        # p,q分别在左右子树上:left,right 均有值,那么公共祖先就是当前节点了
        if left and right:
            return root
        # q,p 在同一子树上：这里也分两种情况，谁在前后
        elif left and not right:
            return left
        elif not left and right:
            return right
        # 最后一种情况就是未找到(当然本题给的条件时必然存在)
        else:
            return None
            


