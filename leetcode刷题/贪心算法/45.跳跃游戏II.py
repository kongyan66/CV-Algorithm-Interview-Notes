# 题目：给你一个非负整数数组 nums ，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 贪心思路：局部最优：当前可移动距离尽可能多走，如果还没到终点，步数再加一。整体最优：一步尽可能多走，从而达到最小步数。
# 图解： https://leetcode.cn/problems/jump-game-ii/solution/by-nehzil-19a5/


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        curPosition = 0
        nextPosition = 0
        step = 0
        i = 0
        while i < len(nums):
            # 找下一步能能跳最远的位置
            nextPosition = max(i + nums[i], nextPosition)
            # 在到达cur位置过程中，一直在寻找next的最大位置
            if i == curPosition:
                if curPosition != len(nums) - 1:
                    step += 1
                    # 更新当前位置
                    curPosition = nextPosition
                    if nextPosition >= len(nums) - 1:
                        break
            i += 1
        return step
