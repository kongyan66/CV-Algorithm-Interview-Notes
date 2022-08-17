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
    # 1.确定入参与返回值
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2.递归停止条件
        if not root:
            return None
        # 3.单层递归逻辑
        # 与二叉树相比，二叉树搜索树有序特性可以帮我们缩小搜索区域，但公共节点情况还是一样的
        # 1) 都在左子树
        if root.val > p.val and root.val > q.val:
            left = self.lowestCommonAncestor(root.left, p, q)
            return left
        # 2)都在右子树
        elif root.val < p.val and root.val < q.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            return right 
        # 3)左右子树都有  就是root的值介于p,q之间
        else:
            return root

            
        