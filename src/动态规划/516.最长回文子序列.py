# 题目：给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

# 思路：与647.回文子串区别是子串是连续的，子序列可以不连续
'''
1.确定dp数组及下标含义
dp[i][j] 表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串

2.确定递推公式
- s[i] == s[j]
- s[i] != s[j]

3.初始化
单个字符的最长回文序列是 1
首先要考虑当i 和j 相同的情况，从递推公式：dp[i][j] = dp[i + 1][j - 1] + 2; 可以看出 递推公式是计算不到 i 和j相同时候的情况。

3. 确定遍历顺序
画个状态转移图就知道了
必须从下到上，从左到右

'''

# 解
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        # 单个字符的最长回文序列是 1
        for i in range(len(s)):   # 不太好想
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
       
        return dp[0][-1]  # 整个字符串的才最大嘛