# 题目：给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）

# 思路：参考560.和为k的数组，采用前缀和找路径，这里把数组换成了树，所以需要统计每个节点的前缀和，采用前序遍历，
# 同时需要维护不同路径的和，所以需要用到回溯。

# 解法：前缀和+递归+回溯
# 因为涉及向左走、向右走两条不同的路径，且两者互不影响，故应采用回溯算法
class Solution:
    def __init__(self):
        self.count = 0
        self.path_sum = collections.defaultdict(int)
        self.sum_ = 0
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path_sum[0] = 1
        self.recursion(root, targetSum)
        print(self.path_sum)
        return self.count

    def recursion(self, root, targetSum):
        if not root:
            return
        # 这块和560.和为k的子数组完全一致
        self.sum_ += root.val
        self.count += self.path_sum[self.sum_ - targetSum]
        self.path_sum[self.sum_] += 1
        
        self.recursion(root.left, targetSum)
        self.recursion(root.right, targetSum)
        # 回溯算法需要在递归后回溯，避免影响不同路径的递归
        self.path_sum[self.sum_] -= 1        # 回溯
        self.sum_ -= root.val                # 回溯