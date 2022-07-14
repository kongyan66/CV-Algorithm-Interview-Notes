# 题目：给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# https://leetcode.cn/problems/distinct-subsequences/comments/ 解释为啥dp这么设计

# 思路没整明白
'''
1.确定dp数组及下标含义
dp[i][j] 表示以i-1结尾的字符串出现以j-1结尾的字符串t的个数
2.确定递推公式
1) s[i - 1] 与 t[j - 1]相等
dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];   没整明白
2) s[i - 1] 与 t[j - 1] 不相等
dp[i][j] = dp[i-1][j]

'''
# 解答
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s)):
            dp[i][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t) +1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]