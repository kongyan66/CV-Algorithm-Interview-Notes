# 题目：简单 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 思路：交换下每个节点的左右孩子，所以要找到所有节点（即需要遍历节点），
# 这就可以用到之前的深度优先遍历（三种），广度优先遍历（1种）以及迭代法

# 解法一：层序遍历
class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        que = []      
        if root:         # 注意返回的是节点，不能写成[]
           que = [root]
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root
# 解法二：前序遍历：中左右
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return root

# 解法三：后序遍历：左右中
# 后序遍历其实就是由前序遍历来的，省略

# 解法四：中序遍历：左中右
# 因为使用递归的中序遍历，某些节点的左右孩子会翻转两次。需要注意

# 解法五：迭代法 （是自己最不熟的写法）
# 思路：递归是三步法则
# 1.确定入参与出参: root -> root
# 2.确定终止条件: deque为空时
# 3.确定单层逻辑: 交换当前节点的左右孩子，反转左子树和右子树（这步不太明白啊）
class Solution5:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
           return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root     