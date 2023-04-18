# 题目：给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列
# 思路：与组合一样，此题多了重复数字，所以需要同层去重，方法和组合完全一样，同时还有一个使用去重(46.全排列)
# 此题完全体现了used在同一树枝和同一树层怎么进进剪枝（去重）的

# 解法一：回溯
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.used = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        nums.sort()
        self.backtracking(nums)
        return self.result
    # 1.确定入参与返回值
    def backtracking(self, nums):
        # 2.确定递归的终止条件
        if len(self.path) == len(nums):
            self.result.append(self.path.copy())
        # 3.确定单层搜索逻辑
        for i in range(len(nums)):
            # 如果同一层取的数有重复，则停止该层递归
            # 如果同一树枝下，再次取了本身，则停止递归 
            # 两种去重是独立的，所以是or连接呀
            if (i > 0 and nums[i] == nums[i-1] and not self.used[i-1]) or self.used[i]:
                continue
            self.used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums)
            self.used[i] = False # 回溯
            self.path.pop() # 回溯
