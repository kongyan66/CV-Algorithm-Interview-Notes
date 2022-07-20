# 题目：给两个整数数组 nums1 和 nums2 ，返回两个数组中公共的、长度最长的子数组的长度。
# 思路：子数组其实是连续子序列，

'''
1. dp[i][j] 表示下标以i-1为结尾的A, 和以下标j-1结尾的B，最长重复数组长度为dp[i][j]  (不理解)
2.
if A[i-1] == B[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
3. 根据dp[i][j]的定义，dp[i][0] 和dp[0][j]其实都是没有意义的！
但需要初始化，令其都为零。
4. 内层倒序遍历(滚动数组)

'''
# 解法：二维数组
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        result = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1  # 表示nums1[:i] nums2[:j]最长重复子串加一
                result = max(result, dp[i][j])
        return result

# 滚动数组
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * (len(nums2)+1)
        result = 0
        for i in range(1, len(nums1)+1):
            for j in range(len(nums2), 0, -1):  # 使用滚动数组就得倒序，避免重复覆盖
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1  # 表示nums1[:i] nums2[:j]最长重复子串加一
                else:
                    dp[j] = 0
                result = max(result, dp[j])
        return result
        
        