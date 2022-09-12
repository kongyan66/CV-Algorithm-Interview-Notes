# 题目：给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

# 解法一：直接找
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        counter = set(nums)  # 对数组进行降重，不然会超时
        for i in range(1, n+1):
            if i not in counter:
                ans.append(i)
        return ans

# 解法二：利用set.difference(set)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(i for i in range(1, len(nums)+1)).difference(set(nums)))


# 解法三：奇技淫巧法 一般也想不到 原数组上改动
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/submissions/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
        