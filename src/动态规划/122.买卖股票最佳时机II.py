# 题目：# 题目：给定一个prices[i]表示每天股票的价格，可以多次买卖一只股票，每次只能持有一股，问获得最大利润。
# 思路： 与121 稍有一点区别就是在dp[i][0]状态转换哪

# 解法：动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[-1][1]

