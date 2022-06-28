# 题目：（通常用 F(n) 表示）形成的序列称为 斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和

# 思路1:动态规划 此题有DP的思想，没有DP的模子
class Solution:
    def fib(self, n: int) -> int:
        # 特殊情况
        if n <= 1:
            return n
        # 初始化
        p, q, r = 0, 0, 1
        for i in range(2, n+1):
            # 实时更新相邻数字
            p, q = q, r
            # 确定推导公式
            r = p + q
        return r

# 思路2：递归
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
