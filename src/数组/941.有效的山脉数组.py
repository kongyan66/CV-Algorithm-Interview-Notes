# 题目：给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。

# 思路：主要看左区间与右区间是否单调递增

# 解法一：双指针
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left, right = 0, len(arr) - 1
        # 移动左区间,且防止越界
        while left + 1 <= right and arr[left] < arr[left+1]:  # 先判断是否越界，再判断是否递增
            left += 1
        # 移动右区间
        while  right - 1 >= 0 and arr[right-1] > arr[right]:
            right -= 1
        # 如果left与right相遇，且不在原位置，说明是山峰
        if left == right and left != 0 and right != len(arr) - 1:
            return True
        else:
            return False