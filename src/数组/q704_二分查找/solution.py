class Solution:
    '''
    二分法核心思路：每次区间都缩小一半，难点在双指针的临界条件
    思路：本题是升序排列，所以十分符合二分法
    思考：如果非升序呢？还能用二分法吗？
    '''
    def search(self, nums: List[int], target: int) -> int:
      # 左闭右闭，若right=len(nums),则为左闭右开
      left, right = 0, len(nums) - 1
      while left <= right:
          mid = left + (right - left) // 2
          # 如果中间值大于目标值，说明目标值落在了[left,mid-1]区间内
          if nums[mid] > target:
              right = mid -1
          # 如果中间值小于目标值，说明目标值落在了[mid+1,right]区间内
          elif nums[mid] < target:
              left = left + 1
          # 以上都不符合，就找到了目标值
          else:
              return mid
      return -1
