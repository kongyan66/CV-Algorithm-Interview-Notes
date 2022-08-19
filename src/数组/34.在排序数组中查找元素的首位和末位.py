# 题目：给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

# 思路一：先找到第一个位置，再根据排序关系找最后一位 但比较慢

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        try: 
            start = nums.index(target)
        except:
            start = -1
        p = start
        end = -1 
        while p < len(nums) and nums[p] == target:
            end = p
            p += 1
        return [start, end]
            