# 题目：给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

# 解法一：双指针 时间复杂度o(nlogn) 空间复杂度o(n)
# 先复制一个数组，再排序，然后用左右指针去比较，不相同的区间即为要排序的
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = nums.copy()
        arr.sort()

        left, right = 0, len(nums) - 1
        while left <= right and nums[left] == arr[left]:
                left += 1
        while left <= right and nums[right] == arr[right]:
                right -= 1
        return right - left + 1