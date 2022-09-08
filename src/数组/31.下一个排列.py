# 题目：整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
# 说人话就是，给定若干个数字，将其组合为一个整数。如何将这些数字重新排列，以得到下一个更大的整数。如 123 下一个更大的数为 132。如果没有更大的整数，则输出最小的整数。


# 思路：自己还是想简单了，以为相邻的找就行，其实需要考虑许多
# https://leetcode.cn/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/

# 题解：
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j, k = n - 2, n - 1, n - 1

        # 找一个峰值
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        
        # 那么[j:end]区间必然是降序，看是否有大于nums[i]
        if i >= 0:
            while k >= j:
                if nums[k] > nums[i]:
                    nums[k], nums[i] = nums[i], nums[k]
                    break
                k -= 1
     
        # 反转[j:end]区间
        left = j
        right = n - 1
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1
        