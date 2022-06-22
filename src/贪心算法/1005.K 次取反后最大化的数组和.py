# 题目：给你一个整数数组nums和一个整数k，按以下方法修改该数组：选择某个下标i并将nums[i]替换为 -nums[i]，重复K次,求返回数组的最大和

# 思路：局部最优：让绝对值大的负数变为正数(绝对值小的变负)，当前数值达到最大，整体最优：整个数组和达到最大。
# sort用法：https://www.runoob.com/python/python-func-sorted.html

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
        nums = sorted(nums, key=lambda x:abs(x), reverse=True)
        # 第二步：从前向后遍历，遇到负数将其变为正数，同时K--
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        # 第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
        if k > 0:
            nums[-1] *= (-1)**k
        # 第四步:求和  
        return sum(nums)