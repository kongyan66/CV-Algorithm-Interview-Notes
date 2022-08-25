# https://zhajiman.github.io/post/connected_component_labelling/#seed-filling-%E7%AE%97%E6%B3%95
# 

class Solution:
    def __init__(self):
        self.list_mark = []
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        mark_id = 2
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.DFS(grid, i, j, mark_id)
                    self.list_mark.append(mark_id)
                    mark_id += 1
        print(grid)
    def DFS(self, grid, i, j, mark_id):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0 or grid[i][j] in self.list_mark:
            return 
        # 走过了就不能再走了（这个不太还理解）
        if grid[i][j] == mark_id:
            return 
        grid[i][j] = mark_id

        self.DFS(grid, i+1, j, mark_id)
        self.DFS(grid, i-1, j, mark_id)
        self.DFS(grid, i, j+1, mark_id)
        self.DFS(grid, i, j-1, mark_id)                            
                    
