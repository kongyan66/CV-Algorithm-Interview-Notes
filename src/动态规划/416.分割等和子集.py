# 题目：给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

# 思路：相比去找两个等和的子集，可转换为找一个和为sum/2子集，剩下子集必然也是sum/2，这样就变成找一个子集问题
# 首先我们想到的是回溯法了，但会超时（这个咋知道啥时候能用呢?这能靠试吗?)
# 另一个就01背包来解决了，把数组每一个数看做一个物品，下标是序号，重量和价值都为其值，背包容量是sum/2

# 解法一：回溯法
# TODO

# 解法二：01背包
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        # 如果不可分一定就没有这样的子集
        if target % 2 == 1:
            return False
        target //= 2
        # 题目中说：每个数组中的元素不会超过 100，数组的大小不会超过 200
        # 总和不会大于20000，背包最大只需要其中一半，所以10001大小就可以了
        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
                # 因为背包容量最大为sum?2（也是价值最大值）,故dp[j]<=target
                if dp[j] == target:
                    return True
        # 所以这块也能这么写
        # return dp[target] == target
        return False