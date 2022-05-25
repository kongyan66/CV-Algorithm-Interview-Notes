# 题目：合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
# 否则，不为 null 的节点将直接作为新二叉树的节点。
# 思路：遍历一个树逻辑是一样的，只不过传入两个树的节点，同时操作

# 解法一：递归法
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        # 2.确定终止条件
        if not root1:
            return root2
        if not root2:
            return root1

        # 3.确定单层递归逻辑
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right =  self.mergeTrees(root1.right, root2.right)

        return root1