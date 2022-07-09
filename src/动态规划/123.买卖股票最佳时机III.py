# 题目：与212区别是 允许两次买卖，每次最多持有一股

# 思路：至多买卖两次，这意味着可以买卖一次，可以买卖两次，也可以不买卖。状态比较多
'''
1.确定dp及下标含义
一天结束后一共五个状态：
0.没有操作
1.第一次买入
2.第一次卖出
3.第二次买入
4.第三次卖出
dp[i][j]表示 第i天状态j所剩最大现金
2.确定递推公式
1) dp[i][0] = dp[i-1][0]
2) dp[i][1] 表示的是第i天，买入股票的状态，并不是说一定要第i天买入股票
- 第i天买入股票 dp[i][1] = dp[i-1][0] - prices[i]
- 第i天没有操作,而是沿用前一天买入的状态 dp[i][1]= dp[i-1][1]
dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
3) dp[i][2]
- 第i天卖出股票,前一天买入股票 dp[i][2] = dp[i-1][1] + prices[i]
- 第i天没有操作，沿用i-1天的卖出状态 dp[i][2] = dp[i-1][2]
dp[i][2] = max(dp[i-1][1]+prices[i], dp[i-1][2])
4) dp[i][3]
dp[i][3] = max(dp[i-1][2] - prices[i], dp[i-1][3])
5) dp[i][4]
dp[i][4] = max(dp[i-1][3]+prices[i], dp[i-1][4])

3.dp初始化
dp[0][0] = 0
dp[0][1] = -prices[0]
dp[0][2] = 0          卖出的操作一定是收获利润
dp[0][3] = -prices[0] 不好理解
dp[0][4] = 0

4.从前往后遍历
5.验证
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])  # 依赖0状态
            dp[i][2] = max(dp[i-1][1]+prices[i], dp[i-1][2])  # 依赖于1状态
            dp[i][3] = max(dp[i-1][2]-prices[i], dp[i-1][3])  # 依赖于2状态
            dp[i][4] = max(dp[i-1][3]+prices[i], dp[i-1][4])  # 依赖于3状态

        # 肯定所有股票都卖出收益最大
        return dp[-1][4]
