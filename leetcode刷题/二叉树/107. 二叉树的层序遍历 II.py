# 题目：给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

 # 思路：参考102.二叉树层序遍历
 # 解法一：迭代法
 class Solution:
        def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
            results.append(res)
        return results[::-1]

# 解法二：递归法 
# 层序遍历用迭代法就好
class Solution:
    def __init__(self):
        self.path = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.recursion(root, 0)
        return self.path

    def recursion(self, node, depth):
        if not node:
            return 
        # 深度与列表编号一致
        if len(self.path) == depth:
            self.path.append([])
        
        self.path[depth].append(node.val)
        if node.left:
            self.recursion(node.left, depth+1)
        if node.right:
            self.recursion(node.right, depth+1)
