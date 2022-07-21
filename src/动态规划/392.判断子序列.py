# 题目：给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。

'''
1.确定dp数组及下标含义
dp[i][j] 表示下标i-1结尾的字符串s,和以j-1结尾的字符串t, 相同子序列长度为dp[i][j] (为了初始化方便)
在设计dp时，len(dp) >= len(nums),这样才能遍历完所有数嘛，此题需要初始化dp[0][0], 多留一个位置，从1正式开始，映射到数组就是i-1和j-1
2.确定递推公式
if s[i-1] == t[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
if (s[i - 1] != t[j - 1])，此时相当于t要删除元素，t如果把当前元素t[j - 1]删除，
那么dp[i][j] 的数值就是 看s[i - 1]与 t[j - 2]的比较结果了，即：dp[i][j] = dp[i][j - 1]
'''
# 解法一：动态递归
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                elif s[i-1] != t[j-1]:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1] == len(s)

# 情况一：这里说下为啥dp[i][j] 表示为s[:i] t[:j] 中相等子串好些 即dp长度+1
# 情况二：我们表示为s[:i+1] s[:j+1]即dp长度与s,t对齐, 看下以下代码
'''
最大的问题是dp[0][0]的初始化
根据状态方程：dp[0][0] 需要进行初始化
对于情况一：dp[0][0]是没有实际意义的，且i,j从1开始遍历，覆盖到了s[:1] t[:1]的情况
对于情况二：dp[0][0]是有实际意义的，它表示s[0]与t[0]共同的子序列长度，这就有很多情况，没法赋给一个固定值，而且一旦赋值错误，
        后面状态转移动就都错了
所以说情况一大大简化了dp[0][0]初始化的难度
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s) or not len(t):
            return True
        dp = [[0] * (len(t)) for _ in range(len(s))]
        dp[0][0] = 1  # 此处就不对了， 假若s[0] != t[0] dp[0][0] = 0
        for i in range(0, len(s)):
            for j in range(0, len(t)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1] == len(s)
