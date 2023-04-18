# 题目：给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 装水的多少，当然根据木桶效应，我们只需要看左边最高的墙和右边最高的墙中较矮的一个就够了。
# 遍历每一列，然后分别求出这一列两边最高的墙。找出较矮的一端，和当前列的高度比较，结果就是上边的三种情况。

# 解法一 双指针
# 提交时间超限  找左右侧最大高度可以优化 时间复杂度O(n^2）
class Solution:
    def trap(self, height: List[int]) -> int:
        sum_ = 0
        # 遍历每一列，头和尾不可能存水，故直接跳过
        for i in range(1, len(height)-1):
            cur = height[i]
            left = 0
            right = 0
            # 找左侧最大高度 
            for j in range(0, i):
                left = max(left, height[j])
            # 找右侧最大值
            for j in range(i+1, len(height)):
                right = max(right, height[j])
            # 计算雨水
            if cur < min(left, right):    
                sum_ += min(left, right) - cur
          
        return sum_

# 解法二：动态递归 时间复杂度O(n) 通过
class Solution:
    def trap(self, height: List[int]) -> int:
        sum_ = 0
        left_max = [0] * len(height)   # left_max[i]表示height[:i+1]以内的最大值
        right_max = [0] * len(height)  # right_max[i]表示height[i:]以内的最大值
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        
        # 找左侧最大值
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])   # 递推公式
        # 找右侧最大值
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        # 收集雨水 
        for i in range(1, len(height)-1):
            cur = height[i]
            min_ = min(left_max[i-1], right_max[i+1])
            if cur < min_:
                sum_ += min_ - cur
        return sum_

# 解法三：单调栈 终于找到好懂的方法  时间复杂度O(n), 入栈和出栈只有一次
# 当遍历墙的高度的时候，如果当前高度小于栈顶的墙高度，说明这里会有积水，我们将墙的高度的下标入栈。
# 如果当前高度大于栈顶的墙的高度，说明之前的积水到这里停下，我们可以计算下有多少积水了。计算完，就把当前的墙继续入栈，作为新的积水的墙。
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        res = 0
        for i in range(1, len(height)):
            # 遇到高的大于栈顶的
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()
                # 如果栈顶元素一直相等，那么全都pop出去，只留第一个
                while stack and height[cur] == height[stack[-1]]:
                    stack.pop()
                # 计算雨水
                if stack:
                    # 指向的是此次接住的雨水的左边界的位置
                    left = stack[-1]
                    h = min(height[i], height[left]) - height[cur]
                    w = i - left - 1
                    res += w * h                 
            stack.append(i)
        return res
# re-2
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        res = 0
        for i in range(1, len(height)):
            while stack and height[stack[-1]] < height[i]:
                cur = stack.pop()
                # 只有当栈中还有左部分，才计算面积
                # m每弹出一次，算一次面积
                if stack:
                    w = i - stack[-1] - 1
                    h = min(height[stack[-1]], height[i]) - height[cur]
                    res += w * h
            stack.append(i)
        return res