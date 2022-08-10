# 题目:给定二叉树的根节点 root ，返回所有左叶子之和。
# 思路：首先要知道左叶子的定义:有父节点，其左右节点为空则为一个左子叶（三层确定）

# 解法一：迭代法  还是遍历好写好理解呀
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = [root]
        sum = 0
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                    # 判断是否为左子叶
                    if not cur.left.left and not cur.left.right:
                        sum += cur.left.val
                if cur.right:
                    que.append(cur.right) 
        return sum

# 解法二：递归法 整体写法比较简单，但递归逻辑哪有点迷惑
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root)
    # 1.确定返回值与参数
    # 返回值就是数左子叶之和
    def recursion(self, node):
        # 2.确定停止条件
        # 遇到空节点停止
        if not node:
            return 0
        # 3.确定递归逻辑
        # 这块逻辑和迭代法相似
        midvalue = 0
        if node.left and not node.left.right and not node.left.left:
            midvalue = node.left.val
        left_value = self.recursion(node.left)
        right_value = self.recursion(node.right)
        return midvalue + left_value + right_value
# 写法二
class Solution:
    def __init__(self):
        self.sum_ = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.recursion(root)
        return self.sum_

    def recursion(self, node):
        if not node:
            return 0
        # 碰到左子叶就求和
        if node.left and not node.left.left and not node.left.right:
            self.sum_ += node.left.val
        self.recursion(node.left)
        self.recursion(node.right)
        
# 添加一个flag作为判断当前是左节点还是右节点 flag==1 为左节点 0为右节点，加入递归
    def recursion(self, node, flag):
        if not node:
            return 0
        # 碰到左子叶就求和
        if flag == 1 and not node.left and not node.right:
            self.sum_ += node.val
        self.recursion(node.left, 1)
        self.recursion(node.right, 0)