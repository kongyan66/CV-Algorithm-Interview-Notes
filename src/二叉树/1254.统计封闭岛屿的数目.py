# 题目：二维矩阵grid由0（土地）和1（水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
# 思路：把200.岛屿数量 中那些靠边的岛屿排除掉，剩下的不就是「封闭岛屿」了吗

# DFS

# BFS
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        # 改动就在这里，其他与200一致
        for i in range(row):       # 这里靠边岛屿指与边界接壤的岛屿，并不是都都靠边
            # 把靠左边的岛屿淹掉
            self.BFS(grid, i, 0)
            # 把靠右边的岛屿淹掉
            self.BFS(grid,i, col-1)
        for j in range(col):
            # 把靠上边的岛屿淹掉
            self.BFS(grid, 0, j)
            # 把靠下边的岛屿淹掉
            self.BFS(grid, row-1, j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0: 
                    count += 1
                    self.BFS(grid, i, j)
        return count
    # 1.确定入参与返回值 无返回值
    def BFS(self, grid, i, j):
        queue = [[i,j]]
        while queue:
            [i,j] = queue.pop(0)
            # 判断队列首部节点 (i, j) 是否未越界且为 1
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0:
                # 若是则置零（删除岛屿节点），并将此节点上下左右节点加入队列
                grid[i][j] = 1
                queue.extend([[i +1, j], [i-1, j], [i, j-1], [i, j+1]])