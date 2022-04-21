# 题目：判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 核心思想：双指针

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      ans = []
      n = len(nums)
      nums.sort() # 时间复杂度O(nlogn) 排序后用双指针才不会重复
      # 去除nums为空或长度小于3的badcase
      if  n < 3:
        return ans
      # 固定一位数去遍历，就变成了两数之和问题，然后用双指针找符合要求的位置
      for i in range(n):  
        target = -nums[i]   # 左指针
        left = i+1
        right = n -1
        # 去除nums中的重复元素，比如[-1,-1,0,1,2],我们需要从第二个位置开始找，以免结果重复
        if i > 0 and nums[i-1] == nums[i]:
          continue
        # 双指针移动条件
        while left < right:
         sum = nums[left] + nums[right]
         if sum < target: # 值小了，往右移
           left += 1
         elif sum > target: # 值大了，往左移
            right -=1
         else: # 相等找到目标值
            ans.append([nums[i], nums[left], nums[right]])
            # 去重,排序后重复值都相邻
            while left < right and nums[left] == nums[left+1]:
              left += 1
            while left < right and nums[right] == nums[right-1]:
              right -= 1
            # 去重后移动双指针，为啥移动两个呢？因为只动一个，再也不会找到和等于目标值的数字了
            left += 1
            right -=1
      return ans

        