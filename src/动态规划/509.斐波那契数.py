# 题目：（通常用 F(n) 表示）形成的序列称为 斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和

# 解法一：动态规划 dp数组
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n+1)   # 为啥n+1，因为我们要求dp[n]呀，必须补一个空子
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
# 解法二:动态规划 滚动数组
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * 3
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(2, n):
            dp[1], dp[0] = dp[2], dp[1]
            dp[2] = dp[1] + dp[0]
        return dp[2]
        return r

# 解法三：递归
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
