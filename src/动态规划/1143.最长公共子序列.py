# 题目：给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
# 与718区别是：此题是子序列，可以不连续，但要求顺序，这样遇到不相等的也到记录原理值而不是清零

'''
1.确定dp数组及下标含义
dp[i][j]：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
2.确定递推公式
主要就是两大情况： text1[i - 1] 与 text2[j - 1]相同，text1[i - 1] 与 text2[j - 1]不相同
如果text1[i - 1] 与 text2[j - 1]相同，那么找到了一个公共元素，所以dp[i][j] = dp[i - 1][j - 1] + 1;
如果text1[i - 1] 与 text2[j - 1]不相同，那就看看text1[0, i - 2]与text2[0, j - 1]的最长公共子序列 和 text1[0, i - 1]与text2[0, j - 2]的最长公共子序列，取最大的。
即：dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
'''

# 解法
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        results = 0
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1   # 与1049j基本一致
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])  # 可以不连续，所以要保存原来的值，如果必须连续，这里就是0了
                results = max(results, dp[i][j])  
        return results