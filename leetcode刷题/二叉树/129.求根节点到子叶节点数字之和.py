# 题目：给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字， 计算从根节点到叶节点生成的 所有数字之和.

# 思路：遍历问题 前序遍历记路径，到子叶求和

# 解法：递归法
class Solution:
    def __init__(self):
        self.res = 0
        self.path = []

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.res

    def DFS(self, root):
        self.path.append(root.val)
        if not root.left and not root.right:
            self.res += int(''.join(map(str, self.path)))
            return
        if root.left:
            self.DFS(root.left)
            self.path.pop()
        if root.right:
            self.DFS(root.right)
            self.path.pop()

    