# 题目：给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 思路：还是层序遍历思想，用一个计数器记录while 循环的次数即为深度
# 解法一：迭代法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = [root]
        count = 0
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            count += 1
        return count

# 解法二：递归法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 1.确定入参和出参
        return self.getdepth(root)

    def getdepth(self, node):
        # 2.确定终止条件：如果为空节点的话，就返回0，表示高度为0
        if node is None:
            return 0
        # 3.单层递归逻辑：先求它的左子树的深度，再求的右子树的深度，  
        # 最后取左右深度最大的数值 再+1 （加1是因为算上当前中间节点）就是目前节点为根节点的树的深度。
        left_depth = self.getdepth(node.left)
        right_depth = self.getdepth(node.right)
        return max(left_depth, right_depth) + 1