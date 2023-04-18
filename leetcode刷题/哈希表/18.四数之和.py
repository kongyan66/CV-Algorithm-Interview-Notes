# 题目：由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]
# 核心思想：双指针
# 解题思路：基本解法就是在15.三数之和 (opens new window)的基础上再套一层for循环，固定两个数，用双指针找另外两个数
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]: continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum_ = nums[i] + nums[j] + nums[right] + nums[left]
                if sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
                else: 
                    ans.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
            return ans