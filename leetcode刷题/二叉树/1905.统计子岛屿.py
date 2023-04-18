# 题目：给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含0（表示水域）和1（表示陆地）。
# 如果grid2的一个岛屿，被grid1 的一个岛屿完全包含，称grid2中的这个岛屿为子岛屿，问grid2中子岛屿的数量。 

# 思路：如果岛屿 B 中存在一片陆地，在岛屿 A 的对应位置是海水，那么岛屿 B 就不是岛屿 A 的子岛，这种就要先淹没
# 与1254思路类似，先处理，再统计

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid1)
        col = len(grid1[0])
        # 1.先淹没不可能成为子岛屿的岛
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and grid1[i][j] == 0:  # grid2为陆地而grid为岛屿，则该陆地不可能为子岛屿
                    self.DFS(grid2, i, j)
        # 2.再对grid2中岛屿计数 和200.完全一致
        count = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1:
                    count += 1
                    self.DFS(grid2, i, j)
        return count
    # 1.确定入参与返回值 无返回值
    def DFS(self, grid, m, n):
        # 2.确定递归停止条件
        # 越界或者遇到水(0)
        if not 0 <= m < len(grid) or not 0 <= n < len(grid[0]) or grid[m][n] == 0:
            return
        # 3.确定单层递归逻辑
        # 将陆地淹没（1置0）
        grid[m][n] = 0
        self.DFS(grid, m+1, n)  # 向上
        self.DFS(grid, m-1, n)  # 向下
        self.DFS(grid, m, n+1)  # 向右
        self.DFS(grid, m, n-1)  # 向左
 