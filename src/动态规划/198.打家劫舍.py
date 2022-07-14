# 题目：你是一个小偷，计划偷沿途的房屋，价值用list表示，但你不能偷相邻家的，否则会触发警报，问一晚上能偷到的最大价值。
# 思路：动规经典问题，经典方法分析
'''
1. 确定dp[i]及下标含义
dp[i]表示下标i以内房屋，最多可以偷窃的金额为dp[i]
2.确定递推公式
决定dp[i]的就是第个房间偷还是不偷
如果第i房间偷 dp[i] = dp[i-2] + nums[i]
如果第i个房间不偷 dp[i] = dp[i-1] 注意这里是考虑，并不是一定要偷i-1房
然后dp[i]取最大值 dp[i] = max(dp[i-2]+nums[i], bdp[i-1])
3.dp数组初始化
从递推公式可以看出，初始值是dp[0]和dp[1]
dp[0] = nums[0] dp[1] = max(nums[0], nums[1])
4. 确定遍历顺序
dp[i]是由dp[i-1] 和dp[i-2] 推到来的，故必须从前向后遍历
5.举例推导dp
输入[2, 7, 9, 3, 1]
则dp = [2, 7, 11, 11, 12]
''' 

# 解 
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0] * (size)  # 等长，因为j与i一样长
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[size-1]

# 如果按照背包思想，但增加了时间复杂度
        for i in range(2, size):
            for j in range(i, size):
                dp[j] = max(dp[j-1], dp[j-2]+nums[i])