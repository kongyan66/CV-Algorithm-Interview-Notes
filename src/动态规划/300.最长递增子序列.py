# 题目：给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

'''
1.dp[i]表示i之前包括i的以nums[i]结尾的上升子序列的长度
2. j < i
位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
dp[i] = max(dp[i], dp[j]+1)
3.dp[0] = 1
4.从前向后遍历
'''
# 解法
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * (len(nums))  # nums长度大于1
        result = 0
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: 
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(dp[i], result)   # 并不是最后一个是最长的，所以要一直取最大值
        return result
       