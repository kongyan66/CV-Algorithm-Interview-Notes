# 题目：给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

# 思路：相比去找两个等和的子集，可转换为找一个和为sum/2子集，剩下子集必然也是sum/2，这样就变成找一个子集问题
# 首先我们想到的是回溯法了，但会超时（这个咋知道啥时候能用呢?这能靠试吗?)
# 另一个就01背包来解决了，把数组每一个数看做一个物品，下标是序号，重量和价值都为其值，背包容量是sum/2

# 解法一：回溯法
# TODO

# 解法二：01背包 最大值问题
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        # 1.dp[i]表示容量为i的背包装入nums所获的最大总和
        dp = [0] * (target + 1)  # target就是背包的容量，也就是dp数组的长度
        dp[0] = 0
        for i in range(len(nums)):
            # 倒序遍历是为了保证物品i只被放入一次
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[-1] == target  # 说明找到一个和为sum // 2的子数组，所以成立