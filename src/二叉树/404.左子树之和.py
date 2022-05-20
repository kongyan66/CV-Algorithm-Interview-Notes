# 题目:给定二叉树的根节点 root ，返回所有左叶子之和。
# 思路：首先要知道左叶子的定义， 然后可以考虑用层序遍历遍历所有节点并判断是否为左叶子，是就求和。

# 解法一：迭代法  还是遍历好写好理解呀
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = [root]
        sum = 0
        while que:
            cur = que.pop(0)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
            if cur.left != None and cur.left.left == None and cur.left.right == None:
                sum += cur.left.val
        return sum

# 解法二：迭代法 整体写法比较简单，但递归逻辑哪有点迷惑
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 1.确定入参出参
        return self.left_sum(root)
    def left_sum(self, node):
        # 2.确定停止条件
        if not node:
            return 0
        # 3.确定单层递归逻辑
        leftvalue = self.left_sum(node.left)
        rightvalue = self.left_sum(node.right)
        midvalue = 0
        # 该句判断是否为左子叶
        if node.left != None and node.left.left == None and node.left.right == None:
            midvalue = node.left.val
        return leftvalue + rightvalue + midvalue   # 这个写法着实看不太懂