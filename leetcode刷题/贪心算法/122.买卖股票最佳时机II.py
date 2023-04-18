# 题目：给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。设计一个算法来计算你所能获取的最大利润（每次只能持有一股），无限次买卖

# 思路：贪心算法核心思想：局部最优解推出全局最优解
# 如果把利润分解为以天为单位的利润(等价于每天都买卖），那么就变成贪心算法问题了，我们保证每一天利润最大就能得到全局最大利润

# 贪心算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 从第二天就开始卖
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i-1], 0)
        return result

# 动态递归
'''
1.确定dp及下标含义
dp[i][0] 第i天持有股票得最大价值
dp[i][1] 第i天不持有股票得最大价值
2.确定递推公式
1) dp[i][0]
- 第i-1天持有股票，保持现状，最大价值为dp[i-1][0]
- 第i天买入股票，则总价值减少，花钱了嘛，则最大价值为dp[i-1][1]-price[i] 
2) dp[i][1]
- 第i-1天不持有股票. 最大价值为dp[i-1][1]
- 第i天卖出股票，则最大价值为dp[i-1][0] + price[i]
3.dp初始化
4.遍历顺序
5.验证 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[-1][1]

