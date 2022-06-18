# 题目：给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
# 思路：与216.组合相比，本题增加了两项：1）不是直接把所有节点路径保存下来，还得是递增子序列 2）去重不能直接对原数组进行排序了，
# 不然都是递增序列了，所以我们要每一层设置一个set记录使用情况

# 解法：
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.res
    # 1.确定递归入参与返回值
    def backtracking(self, nums, startindex):
        # 递增序列必须两个以上
        if len(self.path) >= 2:
            self.res.append(self.path.copy())
        # 2.确定递归终止条件
        if startindex >= len(nums):
            return
        # 3.确定单层搜索逻辑
        # 这里每一层都用有一个全新的usage_list用于记录本层元素是否重复使用
        use_list = set()   # 用set比list更节省空间
        for i in range(startindex, len(nums)):
            # 如果存在递减序列或已经使用过的数，则停止递归
            if (self.path and nums[i] < self.path[-1]) or nums[i] in use_list:
                continue 
            use_list.add(nums[i])  # 实时记录该层元素情况
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()     # 回溯
            