# 题目：求两数之和 时间复杂度小于O(n^2)

# 思路：用map去避免重复计算
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      redcord = dict()              # 用字典来保存值和索引，保证可以回头查，若是用list或set是达不到这个需求的
      for i, val in enumerate(nums):
        if (target - val)  not in redcord:
          redcord[val] = i
        else:
          return[redcord[target - val], i]