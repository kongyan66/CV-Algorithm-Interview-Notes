# 题目：给定一个prices[i]表示每天股票的价格，你只能莫某一天迈入这只股票，然后在未来某一天卖出，问能获得最大利润
# 思路：只能买卖一次，就是求数组的最大差值

# 贪心算法 最小值最小 最大值最大
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        result = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            result = max(result, prices[i] - low)
        return result
# 动态规划 
'''
1.确定dp[i]及下标含义
dp[i][0] 表示第i天持有股票所得最多现金
dp[i][1] 表示第i天不持有股票所得最多现金
2.确定递推公式
1) dp[i][0] 可由两个状态得到
- 第i-1天就持有股票，那么保持，所得最大现金就是dp[i][0]
- 第i天买入股票，钱花出去了，那么所得最大现金就是负的:-price[i]
则 dp[i][0] = max(dp[i-1][0], -price[i])
2) dp[i][1] 
- 第i-1天不持有股票，那么最大现金为dp[i-1][1]
- 第i天卖出股票，则最大现金为 dp[i-1][0] + price[i]
则 dp[i][1] = max(dp[i-1][1], dp[i-1][0]+price[i])
3. dp 初始化
dp[0][0] = -price[0]
dp[0][1] = 0
4. 遍历顺序
天数正序遍历
5.打印验证
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       dp = [[0] * 2 for _ in range(len(prices))]
       dp[0][0] = -prices[0]
       dp[0][1] = 0

       for i in range(1, len(prices)):
           dp[i][0] = max(dp[i-1][0], -prices[i])
           dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
       # 当然卖出最后卖出所以股票才有最大值，即不持有的
       return dp[len(prices)-1][1]

