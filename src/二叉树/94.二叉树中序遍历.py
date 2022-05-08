# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rightS
# 图解见 基础知识.md
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if not root:
        return []
      result = []
      stack = []
      cur = root

      while cur or stack:
        # 先迭代访问最底层的左子树结点
        if cur:          
          stack.append(cur)
          cur = cur.left
        # 到达最左结点后处理栈顶结点
        else:
          cur = stack.pop()
          result.append(cur.val)
          cur = cur.right
      return result
