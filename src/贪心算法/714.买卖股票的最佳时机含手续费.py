# 题目：给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。求最大利润

#思路：122 无需关系什么时候买个卖，只需要最后利润和最大即可(可以多次买卖)，但此题有手续费，我们就需要考虑买卖的时间了
# 使用贪心策略，就是最低值买，最高值（如果算上手续费还盈利）就卖。分情况讨论

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        minvalue = prices[0]
        for i in range(1, len(prices)):
            # 情况一： 找最低价格，即入手时间
            if prices[i] < minvalue:
                minvalue = prices[i]
                continue
            # 情况二： 没有利润，不买不卖
            elif prices[i] >= minvalue and prices[i] <= minvalue + fee:
                continue
            # 情况三：有利润，计算利润，可能有多次计算利润，最后一次计算利润才是真正意义的卖出
            # 这块也可以看做每天都有利润的买卖，不是最后一次就没手续费
            elif prices[i] > minvalue + fee:
                result += prices[i] - minvalue - fee
                # 更新下minvalue，至于为啥减去一个fee,是补补中间的值，保证了该段区间fee只被减一次
                # 这块还是比较灵活的，自己想肯定是想办法标记最后一次
                minvalue = prices[i] - fee 
        return result

# 动态递归
# 思路：与122 基本一致，只需在卖出时减去手续费
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]                 # 还是喜欢dp[i][1]表示持有的最大价值

        for i in range(1, len(prices)):
            # 不持有股票最大的价值
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)  # 唯一区别在这
            # 持有股票最大的价值
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]
       

