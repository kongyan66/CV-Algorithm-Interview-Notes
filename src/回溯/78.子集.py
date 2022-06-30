# 题目：给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）
# 思路：如果把 子集问题、组合问题、分割问题都抽象为一棵树的话，那么组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点！
# 所以我们要保留所有路径

# 解法：
class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.res
    # 1.确定递归入参与返回值
    def backtracking(self, nums, startindex):
        # 就这块和之前的组合问题不一样
        self.res.append(self.path.copy())
        # 2.确定递归停止条件
        # 剩下子集为空时，停止递归
        if len(nums[startindex:]) == 0:
            return 
        # 另一种写法
        # if startindex >= len(nums):
        #     return 
        # 3.单层搜索逻辑
        for i in range(startindex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
           
           