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
# 解法一：动态规划
# 只做了操作数统计 并不是列出详细步骤
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 相等 无任何操作
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                # 不等，增删改，注意增和删除是等价的，分析一种即可
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]


# 解法二：递归DFS(超时)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # 按照 dp 函数的定义，计算 s1 和 s2 的最小编辑距离
        return self.dp(word1, m - 1, word2, n - 1)
    # 定义：s1[0..i] 和 s2[0..j] 的最小编辑距离是 dp(s1, i, s2, j)
    def dp(self, word1, i, word2, j):
        # 处理base case 如果字符串为空了，就自由一种删除操作
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        
        # 进行状态转移
        if word1[i] == word2[j]:
            return self.dp(word1, i - 1, word2, j - 1)
        else:
            return min(
                self.dp(word1, i, word2, j - 1) + 1,
                self.dp(word1, i - 1, word2, j) + 1,
                self.dp(word1, i - 1, word2, j - 1) + 1
            )

# 解法三：记忆化递归
class Solution:
    def __init__(self):
        self.memo = {}

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # 按照 dp 函数的定义，计算 s1 和 s2 的最小编辑距离
        return self.dp(word1, m - 1, word2, n - 1)
    # 定义：s1[0..i] 和 s2[0..j] 的最小编辑距离是 dp(s1, i, s2, j)
    def dp(self, word1, i, word2, j):
        # 处理base case 
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        # 进行状态转移
        if word1[i] == word2[j]:
            self.memo[(i, j)] = self.dp(word1, i - 1, word2, j - 1)
            return self.memo[(i, j)]
        else:
            self.memo[(i, j)] = min(
                self.dp(word1, i, word2, j - 1) + 1,
                self.dp(word1, i - 1, word2, j) + 1,
                self.dp(word1, i - 1, word2, j - 1) + 1
            )
            return self.memo[(i, j)]