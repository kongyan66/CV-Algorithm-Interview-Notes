# 题目：给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。(所有右侧的节点值)
# 思路：层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了。

# 解法一： 迭代法
class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        results = []
        if root is None:
            return results
        que = deque([root])
        while que:
            # 最后一个就是最右的节点
            results.append(que[-1].val)
            # 执行这个遍历的目的是获取下一层所有的node
            for _ in range(len(que)):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)       
        return results
# 另一种写法
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        if not root:
            return results
        que = [root]
        while que:
            width = len(que)
            for i in range(width):
                cur = que.pop(0)
                if i == width - 1:
                    results.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return results
         

# 那我能不能只存最右的节点呢？ 试了但就是测试不通过呀  
# 答：不可以 这里有一个误区右视图就是右子树的节点，其实并不是，而是从右侧能看到的节点
# 如果该层只有一个左节点，也是对的
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