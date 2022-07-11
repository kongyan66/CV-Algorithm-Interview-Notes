# 题目：给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
# 思路：与300.最长递增序列 区别是：连续

'''
1.dp[i]表示以i结尾数组的连续递增子序列
2. 要连续，比较的必然是nums[i+1] 与nums[i], 也就是dp[i+1]与dp[i]
if nums[i+1] > nums[i]: dp[i+1] = dp[i] + 1
3.初始化
dp[i] = 1
'''

# 解法
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            result = max(result, dp[i])
        return result