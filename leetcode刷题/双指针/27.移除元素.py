# 题目：给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度
# 要求不能使用额外空间

# 思路：双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        while fast < len(nums):
            # 当nums[fast] == val 时，slow就停止，slow的值就是去掉val后数组长度
            # 当nums[fast] != val 时，slow前进一步，后面值补上val的值
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
           
            fast += 1    
        return slow