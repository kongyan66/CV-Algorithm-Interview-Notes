# 题目：给你一个整数数组nums ，请计算数组的中心下标。数组中心下标是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。


# 思路一：把每个数都当做中心去遍历，算出左半边的和，存在就返回中心值下标 
# 时间复杂度O(N^2) 太费时间了
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums)):
            mid = nums[i]
            # 如果左半边值没有，就不存在，继续找
            if (total - nums[i]) % 2 == 1:
                continue
            left = (total - nums[i]) // 2
            if sum(nums[:i]) == left:
                return i
        return -1

# 思路二：区间求和 应该立马想到前缀和
class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        preSum = 0
        for i in range(len(nums)):
            if preSum == total - preSum - nums[i]:   # 左半边等于右半边
                return i
            preSum += nums[i]
        return -1
