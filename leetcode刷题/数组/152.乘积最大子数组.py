# 题目：给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组。
# 子数组 是数组的连续子序列

# 思路一：第一感觉应该是贪心算法 保证局部乘积最大 但结果不对



# 思路二：动态规划
# 对于乘法，我们需要注意，负数乘以负数，会变成正数
# https://leetcode.cn/problems/maximum-product-subarray/solution/dpfang-fa-xiang-jie-by-yang-cong-12/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDP = [0] * len(nums)
        minDP = [0] * len(nums)
        # 用两个变量维护当前最大值与最小值
        # 当前的最大值，以及最小值，最小值可能为负数，但没准下一步乘以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了。
        maxDP[0], minDP[0], ans= nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            # 最大积的可能情况有：元素i自己本身，上一个最大积与i元素累乘，上一个最小积与i元素累乘
            maxDP[i] = max(nums[i], maxDP[i-1] * nums[i], minDP[i-1] * nums[i])
            minDP[i] = min(nums[i], maxDP[i-1] * nums[i], minDP[i-1] * nums[i])
            ans = max(ans, maxDP[i])
        return ans
