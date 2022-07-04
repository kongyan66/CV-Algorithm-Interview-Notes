# 题目：给一个帧数数组Nums和整数target，向整数中每个整数前添加一个'+'或"-",然后和为target，问多多少中方法。

# 思路
# 咋一看也与01背包没啥关系，关键还是在于如何转换，拆分出一个背包的概念出来
# 假设我们拆分出一个正子集P和一个负子集N，则有sum(P) + sum(N) = target
# 两边同时加上一个sum(nums),得到2*sum(P) = target + sum(P) 
# 最终得到：sum(p) = (target + sum(nums)) / 2 
# 这里的sum(p) 就是背包容量了， 当然必须为整数，否则return 0 ,物品重量和价值都还是nums[i]
# 这里最大区别就此题是一个组合问题，而不是最值问题，所以转换公式也有变换，当然到这里也可以用回溯法39.组合总和,注意不需要去重

# 五步走
'''
1. dp[j] 表示背包容量为j能有多少种装法
2. dp[0] = 1，装满容量为0的背包，有1种方法，就是装0件物品。
3. 假设背包容量j=4
i= 1 , 则还有dp[3]种装法
i=2，还有dp[2]种装法
i=3，还有dp[1]z中装法
i=4，还有dp[0]种装法
则有dp[j] += dp[j-nums[i]]
4. 背包反向遍历
5.打印dp检查
'''

# 解法一： 动态规范
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (target + total) % 2 == 1 or abs(target) > total:   # 后面一个例外条件提交的时候才知道
            return 0
        bagsize = (target + total) // 2  
        dp = [0] * (bagsize + 1)   # 为啥这里不用计算了
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagsize, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagsize]

