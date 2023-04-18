# 题目：给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 解法一：排序
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]

# 解法二:异或运算
# 任何数和0做异或运算，结果仍然是原来的数，任何数和其自身做异或运算，结果是 0
# https://leetcode.cn/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            a ^= nums[i]
        return a