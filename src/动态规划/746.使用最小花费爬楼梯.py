# 题目：给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用（过路费）。
# 一旦你支付此费用，即可选择向上爬一个或者两个台阶。

# 这里的每一级楼梯都是有价格的，想要跨过它，就要交保护费，而我们每次可以从前一个楼梯或者前两个楼梯爬上来，难在在于写状态转移动方程
'''
状态定义：dp[i] 表示到达第 i 级楼梯所需要的最小代价（注意：是到达，还没有跨过）。
转移方程：dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])，要想到达 i，要么交 i-2 的保护费走两步上来，要么交 i-1 的保护费走一步上来。
初始值：dp[0] = dp[1] = 0，可以直接从 0 或 1 号楼梯开始，前面没有台阶，所以它们不需要花费代价。
返回值：dp[n]，表示到达第 n 级楼梯的最小代价，也就是跨过第 n-1 的最小代价。
优化：可以看到转移方程中只与前两项有关，所以，可以声明两个变量轮动减小空间。
'''
# time:O(n) space:O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1.dp[i]指针到达第i个阶梯时需要花费的最小代价
        dp = [0] * (len(cost)+1)
        # 2.dp[i]初始化
        dp[0] = dp[1] = 0
        
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])  # 比较好理解的一种状态转移方程
        return dp[len(cost)]

# time:O(n) space:O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p, q = 0, 0
        for i in range(2, len(cost)+1):
            p, q = q, min(p + cost[i-2], q + cost[i-1])
        return q
