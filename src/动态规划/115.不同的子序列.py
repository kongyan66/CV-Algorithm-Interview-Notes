# 题目：给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# 翻译：在 s 串身上 “挑选” 字符，去匹配 t 串的字符，求挑选的方式数
# https://leetcode.cn/problems/distinct-subsequences/comments/ 解释为啥dp这么设计
# https://leetcode.cn/problems/distinct-subsequences/solution/shou-hua-tu-jie-xiang-jie-liang-chong-ji-4r2y/ 解释递归公式
# 递推式不理解
'''
1.确定dp数组及下标含义
dp[i][j] 表示以i-1结尾的字符串出现以j-1结尾的字符串t的个数
2.确定递推公式
1) s[i - 1] 与 t[j - 1]相等
举例，s 为babgbag，t 为bag，末尾字符相同，于是 s 有两种选择：
用s[s.length-1]去匹配掉t[t.length-1]，问题规模缩小：继续考察babgba和ba
不这么做，但t[t.length-1]仍需被匹配，于是在babgba中继续挑，考察babgba和bag

dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];  
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
