# 题目：给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。

# 思路：贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点。

# 解
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        i = 0
        # 如果长度为1，就已经满足要求了
        if len(nums) == 1:
            return True
        # 这里不能用for i in range(len(nums)), 因为我们不一定能调到最后一步
        while i <= cover:
            # 每次更新最大范围，注意这里是数组相对长度，从零开始算的
            cover = max(i+nums[i], cover)
            if cover >= len(nums)-1:   # 所以这里需要减一
                return True
            i += 1
        return False
  