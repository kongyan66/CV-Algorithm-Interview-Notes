# 题目：与123区别是买卖次数为k
# 思路：123买卖两次，五种状态，则k次买卖，2k+1种状态，奇买入，偶卖出，其他基本一致

# 解法
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[0]*(2*k+1) for _ in range(len(prices))]
        # dp初始化  
        for i in range(1, 2*k+1, 2):
            dp[0][i] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]  # 也可以不写，因为初始化已经为0
            # 相当于123写了一个通式，说明状态转换也是一个链条关系
            for j in range(1, 2*k+1, 2):
                dp[i][j] = max(dp[i-1][j-1] - prices[i], dp[i-1][j])
                dp[i][j+1] = max(dp[i-1][j] + prices[i], dp[i-1][j+1])
        # 最后一天卖出所有股票才能获得最大价值
        return dp[-1][2*k]