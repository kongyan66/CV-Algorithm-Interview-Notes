# 题目：有一堆石头，重量为stone[i], 每次任意取两块，如果重量相等，则粉碎了，如果重量不等，剩下一块石头重量为二者差值，
# 求问剩下的石头最小可能的值

# 思路：此题能想到是01背包问题不太容易，从题意得我们想得到的是剩下石头的最小值(最值问题)，怎么会有最小值呢？
# 极限情况就是每次拿的石头重量一样，在放大一点就是把石头分两堆，重量为sum/2, 每次从两堆各取一块石头，肯定有一种取法得到剩下值为0，类似两两抵消
# 当然并不是sum/2一定能整除，但我们保证两堆石头最接近sum//2，就能获得最小的剩下值，说到这就和416挺像了
# 所以对齐背包问题：有一个容量为sum//2的背包，去装重量stone[i]，价值stone[i]的, 求dp[j]的最大值

# 解法：动态规划-01背包
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # dp[j] 表示容量为j的背包能装的物品的最大价值
        # stone最大值是100，最大长度为30，那么最大和为100*30 ，则sum/2 最大值为1500
        dp = [0] * 1501   # 加一是因为数组是从下标0开始的，所以长度需加一
        target = sum(stones) // 2  
        # 初始化
        dp[0] = 0
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):  # 减一才能到stones[i]
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        res = dp[target]
        # 两堆加起来就是最多能粉碎的，总数一减就是剩下的
        return sum(stones) - (2 * res)