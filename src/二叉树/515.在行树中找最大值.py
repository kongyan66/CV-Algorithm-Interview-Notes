# 题目：中等 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。


# 思路一：还是先套层序遍历模板，在append每一层的值的时候取最大值即可（max(list) or list.sort())
class Solution1:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        results = []
        if root is None:
            return results
        que = deque([root])
        while que:
            result = []
            for _ in range(len(que)):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            result.sort()
            results.append(result[-1])
        return results

# review-2
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        if not root:
            return results
        que = [root]
        while que:
            res = []
            for _ in range(len(que)):
                cur = que.pop(0)
                res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(max(res))
        return results