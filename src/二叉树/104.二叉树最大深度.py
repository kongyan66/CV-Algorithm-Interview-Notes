# 题目：给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 思路：还是层序遍历思想，用一个计数器记录while 循环的次数即为深度
# 解法一：迭代法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return count
        que = [root]
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            count +=1 
        return count


# 解法二：递归法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root)
    # 1.确定入参与返回值
    # 返回值就是当前节点的深度depth
    def recursion(self, node):
        # 2.确定终止条件
        # 此题有返回值，故终止的时候也要有返回值（空节点深度为0）
        if not node:
            return 0
        # 3.确定单层递归逻辑
        # 分别求左右子树的深度，至于为啥不需要判断节点是否存在了，不存在深度就为0呗
        left_depth = self.recursion(node.left)
        right_depth = self.recursion(node.right)
        # 这里需要注意下，是从当前节点往下看，所以最终深度需要+1
        return max(left_depth, right_depth)+1
