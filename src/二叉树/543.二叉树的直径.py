# 题目：给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

# 思路：直径即为就是左右子树的最大深度之和

# 思路一：求左右子树的最高度之和，用层序遍历,时间复杂度O(N)  AC了100/104 
# 以下下发均未考虑这条路径可能穿过也可能不穿过根结点，故不全AC
class Solution:
    def __init__(self):
        self.depth = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left = self.travelse(root.left)
        right = self.travelse(root.right)
        return left + right 

    def travelse(self, root):
        que = [root]
        res = 0
        if not root:
            return res
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res += 1
        return res

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        return left + right
    
    def recursion(self, root):
        if not root:
            return 0
      
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        return max(left, right) + 1

# 思路二： 实时找合适的根节点 与124.二叉树最大路径和 思路完全一致
# https://leetcode.cn/problems/diameter-of-binary-tree/solution/hot-100-9er-cha-shu-de-zhi-jing-python3-di-gui-ye-/
class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recursion(root)
        return self.res - 1
    
    def recursion(self, root):
        if not root:
            return 0
      
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        # 每个结点都要当做根节点一样去判断  左子树最大深度+右子树最大深度+1
        self.res = max(self.res, left + right + 1)
        # 求子树最大深度
        return max(left, right) + 1