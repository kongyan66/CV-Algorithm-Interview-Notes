# 题目：给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 思路：可以直接复用 27. 移除元素的解法，先移除所有0，然后把最后的元素都置为0，就相当于移动0的效果。

# 解法：
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
    
        for i in range(slow, fast):
            nums[i] = 0