# 题目：给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# 思路：如果不考虑二叉搜素树特性，此题和235.二叉树最近公共祖先完全一样。
# 提到二叉搜索树（左子树的所有节点都小于当前节点，右子树的所有节点都大于当前节点，并且每棵子树都具有上述特点),我们就应该想到中序遍历和升序序列，


# 解法一：迭代法 单树遍历
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # 如果两个节点值都小于根节点，说明他们都在根节点的左子树上，我们往左子树上找
            if root.val > p.val and root.val > q.val:
                root = root.left
            # 如果两个节点值都大于根节点，说明他们都在根节点的右子树上，我们往右子树上找
            elif root.val < p.val and root.val < q.val:
                root = root.right
            # 如果一个节点值大于根节点，一个节点值小于根节点，说明他们他们一个在根节点的左子树上一个在根节点的右子树上，那么根节点就是他们的最近公共祖先节点。(想明白这个，此题就透了)
            else:
                return root
        return None 
      
# 解法二： 递归法
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2.确定停止条件（非必须，因为题中声明p、q 为不同节点且均存在于给定的二叉搜索树中）
        if root == None:
            return root
        # 3.确定单层递归逻辑
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root