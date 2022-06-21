# 题目：给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。设计一个算法来计算你所能获取的最大利润（每次只能持有一股）

# 思路：贪心算法核心思想：局部最优解推出全局最优解
# 如果把利润分解为以天为单位的利润，那么就变成贪心算法问题了，我们保证每一天利润最大就能得到全局最大利润

# 解
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i-1], 0)
        return result