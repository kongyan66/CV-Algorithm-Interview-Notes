# 题目：给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

# 思路一：暴力法
# 先排序，再看相邻是否有重复
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]

# 思路二：二分查找
# https://leetcode.cn/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
# 根据mid和count关系，可知区间

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            count = sum(num <= mid for num in nums)
            # 如果 count 严格大于 mid。根据 抽屉原理，重复元素就在区间 [left..mid] 里；
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left
