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

# 思路二：两次二分查找，分别找左边界后右边界, 与二分查找区别是前者找到target就返回了，而此题还要缩小范围，找到边界的位置

# 情况一：target在数组的左侧或者右侧
# 情况二：arget在数组中，但却不存在
# 情况三：target在数组中，且存在

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftBoarder = self.getLeftBoarder(nums, target)
        rightBoarder = self.getRightBoarder(nums, target)

        return [leftBoarder, rightBoarder]
            
    # 找左边界，
    def getLeftBoarder(self, nums, target):
        left, right = 0, len(nums) - 1
  
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1   # 唯一区别，缩小右侧边界
        # 检查出界情况
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    # 找右边界
    def getRightBoarder(self, nums, target):
        left, right = 0, len(nums) - 1
  
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid + 1   # 唯一区别，缩小左侧边界
        if right < 0 or nums[right] != target:
            return -1
        return right
        
            