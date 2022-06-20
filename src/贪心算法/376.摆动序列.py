# 题目：如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列。
# 给一个nums，求其摆动序列的最长子序列长度

# 解法
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cur, pre, count = 0, 0, 1
        for i in range(len(nums)-1):
            cur = nums[i+1] - nums[i]
            # 发生摆动，计数加一，且跳过不摆动的pre
            if pre * cur <= 0 and cur != 0:  
                count += 1
                pre = cur
        return count