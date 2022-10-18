# 题目：给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。请你返回让 s 成为回文串的 最少操作次数 。

# 思路：和516回文串基本一致

# 解：动态规划
# 对字符串 s[i..j](左闭右闭)，最少需要进行 dp[i][j] 次插入才能变成回文串。
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]   # 如果左右端点相同就不需要操作
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1  # 把 s[i+1..j] 和 s[i..j-1] 变成回文串，选插入次数较少的， 然后还要再插入一个 s[i] 或 s[j]，使 s[i..j] 配成回文串
        return dp[0][-1]