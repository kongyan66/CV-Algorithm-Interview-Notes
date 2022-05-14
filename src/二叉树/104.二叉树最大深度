# 题目：给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 思路：还是层序遍历思想，用一个计数器记录while 循环的次数即为深度

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = [root]
        count = 0
        while que:
            for i in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            count += 1
        return count