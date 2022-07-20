# 题目：给两个数组nums1和nums2，若nums1[i]==nums2[j], 记为一条交线，但交线之间不能相交，问最多有几条交线
# 思路：其实就是求连个字符串的最长公共子串，与1143.完全一致

'''
1. 确定dp数组及下标含义
dp[i][j] 表示nums1[:i]与nums2[:j]最长公共子串 非连续
2. 确定递推公式
if nums1[i-1] == nums2[j-1]:
    dp[i][j] = dp[i][j] + 1
else:
    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
3.初始化
dp[0][j] = dp[i][0] = 0
'''

# j解法
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        res = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:             # 疑问：为啥不会取重复呢
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                res = max(res, dp[i][j])
        return res