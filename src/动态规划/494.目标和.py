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
# 01背包(决定遍历顺序) 组合问题（决定状态转移式）
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (target + total) % 2 == 1 or abs(target) > total:   # 后面一个例外条件提交的时候才知道
            return 0
        bagsize = (target + total) // 2  
        dp = [0] * (bagsize + 1)   
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagsize, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagsize]

# 解法二：回溯（超时，无法AC）
# 枚举出所有情况，即加+和-的所有情况，然后看符合和为target的路径的数量
class Solution:
    def __init__(self):
        self.path = []
        self.map = [-1, 1]
        self.count = 0
        self.target = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int：
        self.target = target
        self.dfs(nums, 0)
        return self.count

    def dfs(self, nums, index):
        if len(self.path) == len(nums):
            if sum(self.path) == self.target:
                self.count += 1
            return
        
        for i in range(len(self.map)):
            self.path.append(nums[index] * self.map[i])
            self.dfs(nums, index + 1)
            self.path.pop()

# 解法三：回溯+记忆化优化（不太好懂啊）
# 参考：https://leetcode.cn/problems/target-sum/solution/by-flix-rkb5/
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # 记忆化单元
        # @functools.cache  # python functions 自带记忆化单元，启用后可以省去自定义cache单元
        def dfs(i, summ, target):
            if (i, summ) in cache:       # 记忆化：已存在，直接返回
                return cache[(i, summ)] 
            
            if i == len(nums):           # 遍历完了全部的元素，递归中止
                if summ == target:       # 找到了一个满足要求的组合
                    cache[(i, summ)] = 1
                else:
                    cache[(i, summ)] = 0
                return cache[(i, summ)]

            pos = dfs(i + 1, summ + nums[i], target)   # nums[i]前面添加'+'号
            neg = dfs(i + 1, summ - nums[i], target)
            cache[(i, summ)] = neg + pos               # 以上两种情况的组合数之和

        return dfs(0, 0, target)



 