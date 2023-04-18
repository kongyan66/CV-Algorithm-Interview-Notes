# 题目：给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

# 解法一：暴力法 o(n^2)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m = len(nums)
        res = []
        for i in range(m):
            count = 0
            for j in range(m):
                if nums[i] > nums[j]:
                    count += 1
            res.append(count)
        return res

# 改进一 排序之后加哈希，时间复杂度为O(n\log n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        res.sort() # 从小到大排序之后，元素下标就是小于当前数字的数字
        hash = dict()

        for i, num in enumerate(res):
            #  遇到了相同的数字，那么不需要更新该 number 的情况
            if num not in hash:
                hash[num] = i   
        for i, num in enumerate(nums):
            res[i] = hash[num]
        return res

        