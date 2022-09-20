# 题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 思路：关键是递推公式，
'''
设dp[i]表示爬到第i级台阶的方法数量
爬到第i阶台阶，有两种方法
第一种：从第i-1级爬一个
第二种：从第i-2级爬两个
这就将爬到第i级台阶分解为2个独立的子问题，如果还可以选着爬3个台阶，则可以继续分解为三个子问题，依次内推
所以最终完成爬到第i级台阶：dp[i] = dp[i-1] + dp[i-2]
'''
# 动态规划 方法论
'''
1. 确定dp数组及下表含义
2. 确定递归公式，即dp[i]的表达式
3. dp数组如何初始化
4. 确定遍历顺序
5. 验证：举例推导dp数组
'''

## 法一：使用list做dp数组，n有多大，数组就n+1的长度 空间复杂度O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
       # 1.确定dp数组 dp[i]表示到达第i级台阶爬法数量
       dp = [0] * (n+1)  # 为啥是n+1，因为要与题中的n对齐
       # 考虑n=1的情况
       if n <= 2:
           return n
       # 3.初始化dp
       # 至于i=0的情况，dp[0]是1还是2，可以不考虑，考虑1,2，从3开始遍历比较符合正常思维
       dp[1] = 1
       dp[2] = 2
       # 4.确定遍历顺序
       for i in range(3, n+1):
           dp[i] = dp[i-1] + dp[i-2]
       return dp[n]

## 法二：使用三个数去维护dp，因为我们每次仅需要考虑三个数 空间复杂度O（1）
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b= 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b


# 再说下递归，看暴力法能解决不
## 直接递归：超时 不可行
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
## 优化递归  通过 (这个想法很好，但不太理解，对递归理解还不够深刻)
'''
记忆化递归，自顶向下
'''
def climbStairs(self, n: int) -> int:
    def dfs(i: int, memo) -> int:
        if i == 0 or i == 1:
            return 1
        if memo[i] == -1:
            memo[i] = dfs(i - 1, memo) + dfs(i - 2, memo)
        return memo[i]

    # memo: [-1] * (n - 1)
    # -1 表示没有计算过，最大索引为 n，因此数组大小需要 n + 1
    return dfs(n, [-1] * (n + 1))


# 终极方法：转为背包问题
# 完全背包 排列问题 台阶选择nums=[1, 2]  target=n
class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [1, 2]
        dp = [0] * (n + 1)
        dp[0] = 1
        for j in range(n+1):     # 可以从0开始，不符合要求的下面 j>=nums[i] 会剔除掉
            for i in range(len(nums)):
                if j >= nums[i]:   # 保证j-nums[i] >= 0,这样dp下标才有含义
                    dp[j] += dp[j-nums[i]]
        print(dp)
        return dp[n]
