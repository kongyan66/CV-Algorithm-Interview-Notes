# 题目：给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

# 解法一：排序+去重 时间复杂度o(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 0
        count = 0
        nums = list(set(nums))
        nums.sort()
      
        for i in range(len(nums)- 1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans + 1

# 解法二：哈希表 时间复杂度o(n)
# 枚举数组中的每个数 x，考虑以其为起点，不断尝试匹配 x+1, x+2, \cdotsx+1,x+2,⋯ 是否存在
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0 
        nums = set(nums)  # 降重
        # 遍历每一个数的最长序列
        for num in nums:
            # 从最小的数开始
            if num - 1 not in nums:
                cur_num = num
                cur_length = 1
                # 如果连续就继续找
                while cur_num + 1 in nums:
                    cur_num += 1
                    cur_length += 1
                ans = max(ans, cur_length)
        return ans