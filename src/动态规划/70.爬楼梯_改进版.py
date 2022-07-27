# 爬楼梯，一次爬1、2、3,但是多了如果当前爬2、3下次只能爬1的限制 --2023 虹软笔试题

# 暴力解法 DFS 
class Solution1:
    def climbStairs(self, n: int, step) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        if step > 1:
            

        return self.climbStairs(n-1, 1) + self.climbStairs(n-2, 2) + self.climbStairs(n-3, 3)

# 优化一 动态规划
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        dp = [0] * (n+1)  # dp[0]无实际意义，但要走到n阶梯，所以+1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
        return dp[-1]

if __name__ == '__main__':
    import sys
    line = sys.stdin.readline()
    n = int(line)
    solution = Solution1()
    res = solution.climbStairs(n)
    print(res)
    