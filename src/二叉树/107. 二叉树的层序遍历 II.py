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
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.recursion(root, 0, res)
        return res[::-1]
     
    def recursion(self, node, depth, res):
        if not node:
            return 
        
        if len(res) == depth:
            res.append([])
        res[depth].append(node.val)
        if node.left:
            self.recursion(node.left, depth+1, res)
        if node.right:
            self.recursion(node.right, depth+1, res)
