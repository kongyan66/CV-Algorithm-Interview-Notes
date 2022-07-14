# 题目：给一个整数n, 返回和为完全平方数的最小数量，如1， 4， 9等整数的平方

# 思路：背包容量为n, 物品就是完全平方数组，且可以无限用，故是一个完全背包问题
# 求的是完全平方数的最小个数，是一个最小值问题
'''
1.dp[j] 表示所用完全平方数的最小个数
2.dp[0] = 0
3. dp[j] = min(dp[j], dp[j-nums[i]] + 1)
4. 外物品，内背包， 正序比遍历

'''
# 解：完全背包 最小值问题
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i**2 for i in range(1, n+1) if i**2 <= n]  # 加个if避免放太多无用的
        dp = [n + 1] * (n+1)  # 最小值问题，放最大值
        dp[0] = 0  # 根据dp[i]定义，0的平方和个数为0
        for i in range(len(nums)):
            for j in range(nums[i], n+1):
                dp[j] = min(dp[j], dp[j - nums[i]] + 1)
        return dp[n]