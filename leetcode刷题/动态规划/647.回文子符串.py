# 题目：给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
# 回文字符串:是正着读和倒过来读一样的字符串。子字符串:是字符串中的由连续字符组成的一个序列。

# 思路

'''
1.确定dp数组及下标含义
dp[i][j] 表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串

2.确定递推公式
- s[i] == s[j]
1) i=j
dp[i][j] = True
2) j-i=1
dp[i][j] = True
3) dp[i+1][j-1] = True
dp[i][j] = True
- s[i] != s[j]
必然不是回文字符串，dp[i][j] = False

3.确定遍历顺序（特别说明）
由于dp[i][j] 受dp[i+1][j-1]影响，在其左下角位置，故遍历需要从左到右，从下到上。先列后行或者先行后列都可以
'''
# 解法一：动态递归 复杂度都为 O(n)
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * (len(s)) for _ in range(len(s))]
        res = 0   # 记录回文串的个数
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):      # 定义是i是左区间，j是右区间，故就有一个限制条件j>=i
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = 1
                        res += 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = 1
                        res += 1
                else:
                    dp[i][j] = 0
        return res

# 解法二：双指针 空间复杂度O(1) 时间复杂度O(n^2)
'''
首先确定回文串，就是找中心然后向两边扩散看是不是对称的就可以了。
在遍历中心点的时候，要注意中心点有两种情况。
一个元素可以作为中心点，两个元素也可以作为中心点。
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.extend(s, i, i)   # 以i为中心
            res += self.extend(s, i, i+1) # 以i和i+1为中心
        return res
    # 扩展中心
    def extend(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res