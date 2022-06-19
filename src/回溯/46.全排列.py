# 题目：给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 思路：与组合相比，组合需要一个指针startindex，每次向下递归都从前往后缩小集合范围，而排列只需去掉本身后的集合，就不需要startindex了

# 解法一：回溯
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        # 使用标志位
        self.used = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.backtracking(nums)
        return self.result
    # 1.确定入参与返回值
    def backtracking(self, nums):
        # 2.确定递归的终止条件
        if len(self.path) == len(nums):
            self.result.append(self.path.copy())
        # 3.确定单层搜索逻辑
        for i in range(len(nums)):
            # 若同一树枝使用过，就不能再用了
            if self.used[i]:
                continue
            self.used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums)
            self.used[i] = False # 回溯
            self.path.pop() # 回溯
