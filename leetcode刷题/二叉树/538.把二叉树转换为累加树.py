# 题目：给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
# 思路：先搞清楚什么是累加树，其实就是左中右的累加顺序

# 解法一： 递归 反序中序遍历 对中序遍历稍作改变
class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.DFS(root)
        return root
    
    def DFS(self, root):
        if not root:
            return 
        # 本题其实就是中序遍历的路径
        self.DFS(root.right)
        self.sum += root.val
        root.val = self.sum
        self.DFS(root.left)