# 题目：给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 求找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 思路：接雨水求的是凹槽的水，这个是两边之间的水，单调栈不适用了
# 此题选用双指针。用 left 和 right 两个指针从两端向中心收缩，一边收缩一边计算矩形面积，取最大的面积值即是答案。
# 此题关键是每次收缩的是短的一边，因为因为矩形的高度是由 min(height[left], height[right]) 即较低的一边决定的：

# 解法：双指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            res = max(res, min(height[left], height[right] ) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res 
