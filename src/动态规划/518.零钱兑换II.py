# 题目：给你一个整数数组coins表示不用面额的硬币(数量不限)， 再给一个整数amount表示金额总和，问有多少种组合的凑法。

# 思路：硬币无限可得到是一个完全背包问题，而且是一个组合问题(类似494.目标和)，不是最值问题,所以递推公式也有变化
# 背包大是amount 物品的种量和价值都是coins[i] 

'''
1.dp[j]表示金额总和为j的最大组合数
2.dp[0] = 1
3.dp[j] += dp[j-wight[i]]
4.遍历顺序：背包从小到大  外物品内背包
'''
# 完全背包，组合问题
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # dp[0]一定要为1，dp[0] = 1是 递归公式的基础，不然都是0
        # 组合问题 外物品内背包
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):  # 完全背包 背包正序; 要注意范围，背包的容量不能小于向前物品的大小
                dp[j] += dp[j-coins[i]]
        return dp[amount]


