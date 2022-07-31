# 爬楼梯，一次爬1、2、3,但是多了如果当前爬2、3下次只能爬1的限制 --2023 虹软笔试题

# 暴力解法 DFS 还不对
class Solution1:
    def climbStairs(self, n: int, step=1) -> int:
        if n == 1:
            return 1
        # 楼梯数为大于1时便需要开始判断步长
        elif n == 2:
            # 如果上一次走了一步，则还有二种走法
            if step == 1:
                return 2
            # 超过一步，则只有一种走法
            else:
                return 1
        elif n == 3:
            # 如果上一次走了一步,
            if step == 1:
                return 4
            else:
                return 2

        if step > 1:
            return self.climbStairs(n-1, 1)
        else:
            return self.climbStairs(n-1, 1) + self.climbStairs(n-2, 2) + self.climbStairs(n-3, 3)

# 优化一 动态规划
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        dp = [0] * (n+1)  # dp[0]无实际意义，但要走到n阶梯，所以+1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

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
    