# 题目：给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

# 思路：由n可知循环的次数为n//2, 根据循环不变量原则，我们每次循环都是左开有闭原则，控制好起始点和终点，其中终点利用循环次数，即偏置来控制

# 解法
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        start_x, start_y = 0, 0       # 起始点
        loop, mid = n // 2, n // 2    # 迭代次数、n为奇数时，矩阵的中心点
        count = 1                     # 计数器

        # 每循环一层偏移量加1，偏移量从1开始
        for offset in range(1, loop+1):
            # 从左到右，左闭右开
            for j in range(start_x, n - offset):
                grid[start_x][j] = count
                count += 1
            # 从上到下，左闭右开
            for i in range(start_y, n - offset):
                grid[i][n -offset] = count
                count += 1
            # 从右往左，左闭右开
            for j in range(n - offset, start_y, -1):
                grid[n-offset][j] = count
                count += 1
            # 从下到上，左闭右开
            for i in range(n -offset, start_x, -1):
                grid[i][start_y] = count
                count += 1
            
            start_x += 1
            start_y += 1
        
        # n为奇数时，填补中间元素
        if n % 2 == 1:
            grid[mid][mid] = count
        return grid