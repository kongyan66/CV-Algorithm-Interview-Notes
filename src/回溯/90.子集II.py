# 题目：给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）
# 思路：与78.子集区别是nums中有重复数字了，所以需要去重了，去重方法参考40.组合总和II
# 这么看去重和剪枝有异曲同工之妙了，前者是避免不必要的递归，后者是去掉重复的递归，本质一样

# 解法一： 有使用标志位
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.used = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        # 必须先排序，方便后面去重，重复必然重复
        nums.sort()
        self.backtracking(nums, 0)
        return self.result
    # 1.确定递归的入参与返回值
    def backtracking(self, nums, startindex):
        self.result.append(self.path.copy())
        # 2.确定递归停止条件
        if startindex >= len(nums):
            return
        # 3.确定单层搜索逻辑
        for i in range(startindex, len(nums)):
            # 去掉同一层之间的重复数字
            # 若数组中前后元素值相同，但前者却未被使用(used == False)，说明是for loop中的同一树层的相同元素情况
            if i > 0 and nums[i] == nums[i-1] and self.used[i-1] == False:
                continue
            self.used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.used[i] = False  # 回溯
            self.path.pop()  # 回溯
            
