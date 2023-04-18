# 题目：一个机器人在一个m*n的网格左上角，每次只能向下或向右走一步，问到达右下角有多少种走法？

# 思路：到达一个位置，前一个状态只有两种走法：向下或向右 状态方程就有了，此题的初始化不好想，到达边缘位置只有一种走法

# 动规 time：O(m*n) 用了一个m*n的数组  space:(m*n) 两次嵌套的for循环
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1.dp[i][j] 表示到达（i，j）位置的路径数量
        dp = [[0] * n for _ in range(m)]         # 注意dp长度也为m,n 看状态转移式子，不需要多个（0,0）位置
        # 2.初始化 
        # 从(0, 0)的位置到(i, 0)的路径只有一条，那么dp[0][j]也同理。
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]     # 到达(i, j）有两条路径，后面不需加2，自己画个图就知道了
        return dp[m-1][n-1]

# DFS 超时
# 递归深度 m+n-1, 节点个数就是2^(m + n - 1) - 1 Time:O(2^(m + n - 1) - 1) 这是指数级别的时间复杂度，是非常大的。
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1.确定入参与返回值
        def dfs(i, j, m, n):
            # 2.确定终止条件
            if i > m or j > n:  # 出界
                return 0
            if i == m and j == n:  # 找到一个子叶，即到找到一条路径到达终点
                return 1
            # 3.确定单层递归逻辑
            return dfs(i+1, j, m, n) + dfs(i, j+1, m, n)  # 汇总两个方向的路径总和
        return dfs(1, 1, m, n)  # 起点(1, 1) 终点(m,n)
