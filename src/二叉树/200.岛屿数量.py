# 题目：给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 思路：DFS/BFS

# 解法一：DFS
# 遍历网格，遇到陆地(1),数量就加一， 然后就对该位置进进DFS，淹没相邻的陆地（遇1置零），好处是避免用visited保存访问路径。
# 设目前指针指向一个岛屿中的某一点 (i, j)，寻找包括此点的岛屿边界，然后向此点的上下左走做深度搜索
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    self.DFS(grid, i, j)
        return count
    # 1.确定入参与返回值 无返回值
    def DFS(self, grid, m, n):
        # 2.确定递归停止条件
        # 越界或者遇到水(0)
        if not 0 <= m < len(grid) or not 0 <= n < len(grid[0]) or grid[m][n] == '0':
            return
        # 3.确定单层递归逻辑
        # 将陆地淹没（1置0）
        grid[m][n] = '0'
        self.DFS(grid, m+1, n)  # 向上
        self.DFS(grid, m-1, n)  # 向下
        self.DFS(grid, m, n+1)  # 向右
        self.DFS(grid, m, n-1)  # 向左
 
 # 解法二：BFS 
 # 唯一区别是与DFS搜索岛屿边界方法不同 写法和二叉树的层序遍历类似
     # 1.确定入参与返回值 无返回值
    def BFS(self, grid, i, j):
        queue = [[i,j]]
        while queue:
            [i,j] = queue.pop(0)
            # 判断队列首部节点 (i, j) 是否未越界且为 1
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                # 若是则置零（删除岛屿节点），并将此节点上下左右节点加入队列
                grid[i][j] = '0'
                queue.extend([[i +1, j], [i-1, j], [i, j-1], [i, j+1]])

    # 或者按照原版写
        while que:
            for _ in range(len(que)):
                i, j = que.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    que.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
