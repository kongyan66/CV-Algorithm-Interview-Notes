# 题目：给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
# 思路：局部最优：当前累加rest[j]的和curSum一旦小于0，起始位置至少要是j+1，因为从j开始一定不行。全局最优：找到可以跑一圈的起始位置。

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0 
        cursum = 0
        totalsum = 0
        for i in range(len(gas)):
            # 不仅下一个地方有够用，也要保证后面油也都够用
            cursum += gas[i] - cost[i]
            # 如果能回到起点，油量一定是大于等于零的
            totalsum += gas[i] - cost[i]
            # 后面又不够start就换一个地
            if cursum < 0:
                 cursum = 0
                 start = i + 1
        if totalsum < 0:
            return -1
        return start
