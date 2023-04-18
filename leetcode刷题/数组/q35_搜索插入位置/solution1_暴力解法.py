class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      for i in range(len(nums)):
        # 分别处理如下三种情况
        # 目标值在数组所有元素之前
        # 目标值等于数组中某一个元素
        # 目标值插入数组中的位置
        if nums[i] >= target:  # 一旦发现大于或者等于target的num[i]，那么i就是我们要的结果
          return i
        i += 1
      # 目标值在数组所有元素之后的情况
      return len(nums)  # 如果target是最大的，或者 nums为空，则返回nums的长度
