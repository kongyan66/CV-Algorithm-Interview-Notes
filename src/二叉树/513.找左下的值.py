# 题目：给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

# 思路:层序遍历
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root != None:
            que = [root]
        result = 0
        while que:
            for i in range(len(que)):
                if i == 0:                 # 这地方我始终没看明白
                    result = que[i].val
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return result