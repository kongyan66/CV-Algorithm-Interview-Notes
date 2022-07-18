# 题目：给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 思路：42.接雨水是找每个柱子左右两边第一个大于该柱子高度的柱子，形成凹槽，算积水面积
# 而本题是找每个柱子左右两边第一个小于该柱子的柱子，形成凸槽，算矩形面积


# 解法一：单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [0]
        heights.insert(0, 0)
        heights.append(0)

        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                while stack and heights[cur] == heights[stack[-1]]:
                    stack.pop()
                if stack:
                    w = i - stack[-1] - 1
                    h = heights[cur]
                    res = max(res, w * h)
            stack.append(i)
        return res

# 解法二：动态规划