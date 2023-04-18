# 题目：给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 思路：42.接雨水是找每个柱子左右两边第一个大于该柱子高度的柱子，形成凹槽，算积水面积
# 而本题是找每个柱子左右两边第一个小于该柱子的柱子，形成凸槽，算矩形面积


# 解法一：单调栈
# 使用单调栈好处是左边第一个小于该元素的与之相邻，如果不重复，就是左边元素
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [0]
        # 与雨水区别是，我们要遍历头尾，为了保证左中右结构，我们需要补在头尾补0
        heights.insert(0, 0)
        heights.append(0)

        for i in range(1, len(heights)):
            # 保证栈内的单调性 由底到头单调增
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()       # 循环最后一次得到的就是凸槽左边元素
                # 先弹出所有相等的栈顶元素，再计算面积
                # 去掉该行，就是弹出一个，计算一次面积，反正最后取最大
                # while stack and heights[cur] == heights[stack[-1]]:
                #     stack.pop()
                if stack: # 栈内还有元素才能算面积
                    w = i - stack[-1] - 1
                    h = heights[cur]   # height[cur] 一定大于>= height[i] 与接雨水的区别
                    res = max(res, w * h)
            stack.append(i)
        return res

# 解法二：动态规划