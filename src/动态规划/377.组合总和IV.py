# 题目：给一个不同整数构成的数组，和一个目标数target，返回nums中组合和为target的个数。所有数可以重复取，且不同顺序视为不同组合

# 思路：本题其实是求排列总和，只是求排列的个数，而不是都列出来(就得回溯了)，个数可以不限使用，说明这是一个完全背包。
# 求组合数：外层遍历物品，内层遍历背包
# 求排列数：外层遍历背包，内层遍历物品
# 如果把遍历nums（物品）放在外循环，遍历target的作为内循环的话，
# 举一个例子：计算dp[4]的时候，结果集只有 {1,3} 这样的集合，不会有{3,1}这样的集合，因为nums遍历放在外层，3只能出现在1后面！


# 解
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1                     # dp[0] = 1是没有意义的，仅仅是为了推导递推公式。
        for j in range(0, target+1):
            for i in range(len(nums)):
                if j >= nums[i]:
                     dp[j] += dp[j - nums[i]]
        print(dp)
        return dp[target]