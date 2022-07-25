# 题目：给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 思路：这递推公式鬼也想不到啊
'''
https://leetcode.cn/problems/integer-break/solution/zheng-shu-chai-fen-by-nehzil-pg87/
当i>=2 时，假设对正整数i拆分出第一个正整数是j(1<=j<=i-1),则有以下两种方案：
- 将i拆分成j和i-j的和，且i-j不在拆分成多个正整数，此时的乘积为j*(i-j)
- 将i拆分成j和i-j的和，且i-j继续拆分，此时乘积为j*dp[i-j]
因此，当j固定时，有dp[i] = max(j*(i-j), j*dp[i-j]), 由于j的范围是1到i-1,需要遍历所有的j得到的dp[i],故：
dp[i] =max(dp[i], max((i-j)*j, dp[i-j]*j))
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        # 确定dp[i]及下标含义 dp[i]表示拆分i得到乘积最大值
        dp = [0] * (n+1)
        # 初始化 dp[0] dp[1] 无实际意义，故从2开始
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] =max(dp[i], max((i-j)*j, dp[i-j]*j)) # 每次计算dp[i](算了j次)，取最大的而已,所以还要和dp[i]比较
        return dp[-1]