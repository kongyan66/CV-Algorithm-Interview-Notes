'''
time:2021/12/18
author:kongyan
考点：二分法
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      left = 0
      right = len(nums) - 1
      # 如果target在数组中
      while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
          right = mid - 1
        elif nums[mid] < target:
          left = mid + 1
        else:
          return mid
      # 如果target不在数组中
      return right +1   # 最好自己模拟下，不然确实想不通为啥
        
   
