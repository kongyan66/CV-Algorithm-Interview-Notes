# 题目：给定一个二叉树，找出其最小深度。
# 说明：最小深度是从根节点到最近叶子节点的最短路径上的节点数量，叶子节点是指没有子节点的节点。

# 思路：套用层序遍历模板，遇到子叶节点就返回计数器结果

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = [root]
        count = 0
        while que:
            count += 1
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                if cur.left == None and cur.right == None:
                    return count