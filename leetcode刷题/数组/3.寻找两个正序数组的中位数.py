# 题目：给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。算法的时间复杂度应该为 O(log (m+n)) 。

# 解法一：暴力法
# 身而为人，只会暴力
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        mid = len(nums1) // 2
        # 分下奇偶
        if len(nums1) % 2 == 1:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid-1]) / 2

# 解法二：二分法
# 一看到 O(log (m+n)) 且排好序了，应该想到二分法，奈何题解看不懂
# TODO
