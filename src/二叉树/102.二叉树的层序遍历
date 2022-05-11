# 题目：给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 考察：队列  队列先进先出，符合一层一层遍历的逻辑，而是用栈先进后出适合模拟深度优先遍历也就是递归的逻辑。

# 迭代法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        results = []
        if not root:         # 空节点就返回
            return results
        que = deque([root])  # 构建一个双端序列装每一层的节点
        while que:           # 每一轮循环就弹出该层节点的值
            size = len(que)  
            result = []
            for _ in range(size):
                node = que.popleft()
                result.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            results.append(result)
        return results

# 递归法
