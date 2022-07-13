# 题目：给定不同面额的硬币coins和一个总金额amount，求凑成总金额的最小硬币个数，凑不成就返回-1 (硬币数量不限)

# 思路：硬币数量不限说明是完全背包， 最小数量说明是最小值问题

'''
1. dp[j]表示总额为j所需硬币的最小个数
2. dp[0] = 0  
3. 遍历顺序：背包正序
4. dp[j] = min(dp[j], dp[j-nums[i]] + nums[i])
'''
# 解法  完全背包 最小值问题
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 我们要取最小值，所以初始化必须放最大的，观察得知最小数量小于等于amount(比如硬币面额都为1时为相等条件)
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]] + 1)   # 注意这里加1不是coins[i],这取决于dp的含义
        return dp[amount] if dp[amount] < amount+1 else -1  # 如果找不到，那么初始值就不会替换掉，也是个小细节呀
