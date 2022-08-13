# 题目：给你一个整数数组 nums，请你将该数组升序排列。

# 解法一：归并排序  先拆分，后合并（合并两个有序数组）
# https://leetcode.cn/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/
# 时间 O(nlog n)  空间复杂度：O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        i, j = len(left) - 1, len(right) - 1
        p = i + j + 1
        tem = [0] * (p+1)
        while i >= 0 and j >= 0:
            if left[i] > right[j]:
                tem[p] = left[i]
                i -= 1
            else:
                tem[p] = right[j]
                j -= 1
            p -= 1
        while i >= 0:
            tem[p] = left[i]
            i -= 1
            p -= 1
        while j >= 0:
            tem[p] = right[j] 
            j -= 1
            p -= 1

        return tem