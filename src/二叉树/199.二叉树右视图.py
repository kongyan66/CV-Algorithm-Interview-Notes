# 题目：给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。(所有右侧的节点值)
# 思路：在层序遍历上改

class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        results = []
        if root is None:
            return results
        que = deque([root])

        while que:
            size = len(que)
            # 最后一个就是最右的节点
            cur = que[-1]
            results.append(cur.val)
            # 执行这个遍历的目的是获取下一层所有的node
            for _ in range(size):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)       
        return results

# 那我能不能只存最右的节点呢？ 试了但就是测试不通过呀
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        results = []
        if root is None:
            return results
        que = deque([root])
        while que:
            cur = que.popleft()
            results.append(cur.val)
            if cur.right:
                que.append(cur.right)   
        return results