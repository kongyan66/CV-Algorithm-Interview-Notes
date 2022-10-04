# 题目：给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

'''
1.dp[i]表示i之前包括i的以nums[i]结尾的上升子序列的长度
2. j < i
位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值，前提是nums[i] >nums[j]才行
dp[i] = max(dp[i], dp[j]+1)
3.dp[0] = 1
4.从前向后遍历
'''
# 解法
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))  # nums长度大于1
        result = 0
        
        for i in range(1,len(nums)):
            for j in range(i):
                # 寻找 nums[0..j-1] 中比 nums[i] 小的元素
                if nums[i] > nums[j]:  
                    # 把 nums[i] 接在后面，即可形成长度为 dp[j] + 1，且以 nums[i] 为结尾的递增子序列
                    dp[i] = max(dp[i], dp[j]+1)  # max()中dp[i]笔试i=0-j时的值，实时在变，我们要选取最大的。
            result = max(dp[i], result)   # 并不是最后一个是最长的，所以要一直取最大值
        return result
       