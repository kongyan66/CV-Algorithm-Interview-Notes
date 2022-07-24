# 题目：相比213.打家劫舍II 这里房屋排列由环换成了树， 其他一致
# 思路：本题是树形DP的入门题，所以需要进行遍历，必须使用后序遍历(疑惑)，框架是后序遍历，逻辑是DP

'''
1.确定dp[i]及下标含义
dp 采用一个长度为2的数组，下标0记录不偷该节点所得最大金钱，下标1表示偷改点获得最大金钱
为啥长度为2的数组就够 因为在递归的过程中，系统栈会保存每一层递归的参数
2.确定遍历顺序 (此题特殊)
后续遍历（有疑问，前序就不行吗）
如果从上往下看这棵树，是无法在遍历到某一个节点时决定【偷或不偷】这个节点的收益的。所以只能从后向前
3.确定递推公式
如果不偷当前节点, 那么左右孩子就可以偷，至于到底偷不偷一定是选一个最大的  val1 = max(left[0], left[1]) + max(right[0], right[1])
如果是偷当前节点，那么左右孩子就不能偷 val = cur.val + left[0] + right[0]
4。初始化
递归终止条件 return(0, 0)

'''
# 动规解法
# 后序遍历+DP
class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.recursion(root)
        return max(result[0], result[1])
    def recursion(self, node):
        if not node:
            return [0, 0] 
        left = self.recursion(node.left)
        right = self.recursion(node.right)
        # 不偷当前节点，获得最大价值 考虑左右节点，注意是考虑，选取最大的可能
        val1 = max(left[0], left[1]) + max(right[0], right[1])
        # 偷当前节点，获得最大价值 那么左右节点必然不可偷了
        val2 = node.val + left[0] + right[0]
        return [val1, val2]
      
# 直接递归 超时#
# 暴力解法，遍历所有可能，前序后序都可以
class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.recursion(root)
        return result
    # 1.确定入参与返回值 
    # 返回值是偷该棵树的最大的价值
    def recursion(self, node):
        # 2.确定停止条件
        if not node:
            return 0
        if not node.left and not node.right:
            return node.val
        # 3.确定单层递归逻辑
        # 偷该节点
        val1 = node.val
        if node.left: 
            val1 += self.recursion(node.left.left) + self.recursion(node.left.right)  # 跳过左节点
        if node.right:
            val1 += self.recursion(node.right.left) + self.recursion(node.right.right)  # 跳过右节点
        # 不偷该节点
        val2 = self.recursion(node.left) + self.recursion(node.right)
        return max(val1, val2)

# 记忆优化递归   加入一个map用于记录最大值
# 使用一个map把计算过的结果保存一下，这样如果计算过孙子了，那么计算孩子的时候可以复用孙子节点的结果。
class Solution:
    def __init__(self):
        self.map = {}
    def rob(self, root: TreeNode) -> int:
        result = self.recursion(root)
        return result
    # 1.确定入参与返回值 
    # 返回值是偷该棵树的最大的价值
    def recursion(self, node):
        # 2.确定停止条件
        if not node:
            return 0
        if not node.left and not node.right:
            return node.val
        if self.map.get(node) is not None:  # 如果map里已经有记录则直接返回
            return self.map[node]
        # 3.确定单层递归逻辑
        # 偷该节点
        val1 = node.val
        if node.left: 
            val1 += self.recursion(node.left.left) + self.recursion(node.left.right)  # 跳过左节点
        if node.right:
            val1 += self.recursion(node.right.left) + self.recursion(node.right.right)  # 跳过右节点
        # 不偷该节点
        val2 = self.recursion(node.left) + self.recursion(node.right)
        self.map[node] = max(val1, val2)   # map里记录一下
        return max(val1, val2)
