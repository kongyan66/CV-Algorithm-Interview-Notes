# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# 遍历问题：递归或迭代

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      result = []

      def traversal(root):
        if root is None:        # 该层递归停止条件
          return
        result.append(root.val)
        traversal(root.left)     # root.left 获取下一个节点的值
        traversal(root.right)
      
      traversal(root)  
      return result

# 小结
# 前序遍历：中左右  后序遍历：左右中 中序遍历：左中右