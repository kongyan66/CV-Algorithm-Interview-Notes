# 题目：二叉树后续遍历 左右中

# 解法一： 迭代法 将前序遍历稍微改造下
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack: 
            cur = stack.pop()
            res.append(cur.val)
            # 这里顺序对调下，不然输出顺序是右左中
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]  # 逆序输出

# 解法二：递归法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recursion(root, res)
        return res

    def recursion(self, node, res):
        if node is None:
            return 
        self.recursion(node.left, res)
        self.recursion(node.right, res)
        res.append(node.val)  # 相当于回溯
        