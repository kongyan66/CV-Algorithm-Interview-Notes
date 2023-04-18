# 题目：说白了就是排序

# 解法一：快速排序
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        self.sort(nums, left, right)
    
    def sort(self, nums, left, right):
        if left >= right:
            return
        p = self.partition(nums, left, right)
     
        self.sort(nums, left, p - 1)
        self.sort(nums, p + 1, right)

    def partition(self, nums, left, right):
        tem = nums[left] # 选择参考点，该调整范围的第1个值
        while left < right:
            # 从右边开始查找大于参考点的值
            while left < right and nums[right] >= tem:
                right -= 1
            nums[left] = nums[right] # 这个位置的值先挪到左边
            # 从左边开始查找小于参考点的值
            while left < right and nums[left] <= tem:
                left += 1
            nums[right] = nums[left] # 这个位置的值挪到右边
        # 写回改成的值
        nums[left] = tem
        return left
    
# 解法二：归并排序




# 解法三：冒泡排序




