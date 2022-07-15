# 题目：给你两个单词word1和word2，请返回将word1转换成word2所使用的最少操作数。
# 可执行操作：1.插入一个字符 2.删除一个字符 3.替换一个字符

# 思路：和583类似

'''
1. 确定dp数组及下标含义
dp[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]。
2. 确定递推公式
- word1[i - 1] == word2[j - 1])
不做任何操作
dp[i][j] = dp[i-1][j-1]
增、删、换
- (word1[i - 1] != word2[j - 1])
1) word1删除一个元素
dp[i][j] = dp[i-1][j] + 1
2) word2删除一个元素(word2添加一个元素，相当于word1删除一个元素)
dp[i][j] = dp[i][j - 1] + 1;
3) 替换元素，word1替换word1[i - 1]
dp[i][j] = dp[i - 1][j - 1] + 1;
综上 dp[i][j] = min({dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]}) + 1;

3. dp数组初始化
dp[i][0] 和 dp[0][j]
'''
# 解法
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        return dp[-1][-1]

