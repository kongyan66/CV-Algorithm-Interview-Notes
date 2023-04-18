class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rightBoader = self.getRightBoader(nums, target)
        leftBoader = self.getLeftBoader(nums, target)
        # 如果target 在数组范围的右边或者左边，只有一个边界值会变
        if leftBoader == -2 or rightBoader == -2:
            return(-1, -1)
        # 如果target在数组范围里且存在，则两者差值会大于2（分被错位一个数）
        elif rightBoader - leftBoader > 1:
            return(leftBoader + 1, rightBoader - 1)  # （错位消除）
        # 如果target 在数组范围中，且数组中不存在target
        else:
            return(-1, -1)


    # 寻找左边界（会向左超出一位）
    def getLeftBoader(self, nums, target):
        left = 0
        right = len(nums) - 1
        leftBoader = -2
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                leftBoader = right
        return leftBoader
    # 寻找右边界（会向右超出一位）
    def getRightBoader(self, nums, target):
        left = 0
        right = len(nums) - 1
        rightBoarder = -2
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid -1 
            else:
                left = mid + 1
                rightBoarder = left 
        return rightBoarder 
  
