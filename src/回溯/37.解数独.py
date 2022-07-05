# 题目：填满一个9x9的棋盘来解决数独问题。
# 数独的解法需 遵循如下规则：
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

# 思路：之前都是一维递归，即for遍历行，递归遍历列，而二维递归是，行和列都由递归遍历

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)
        return board
    # 1.确定递归入参与返回值 
    # 返回值为bool
    def backtracking(self, board):
        # 2.确定递归停止条件
        # 解数独是要遍历整个树形结构寻找可能的叶子节点就立刻返回(就找一个解,找到就返回True,递归结束),棋盘填满了自然就停了
        # 3.确定单层搜索逻辑
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    continue
                for k in range(1, 10):
                    if self.is_valid(board, row, col, k):
                        board[row][col] = str(k)
                        if self.backtracking(board):
                            return True
                        board[row][col] = '.'  # 回溯
                # 数字1-9都不能填入空格，说明无解，搜索失败
                return False
        # 遍历完棋盘所有位置，完没有返回false，说明找到了一个成功的下法，搜索成功
        return True
    
    def is_valid(self, board, row, col, k):
        # 判断同一行还否有冲突  行不同，列动
        for i in range(9):
            if board[row][i] == str(k):
                return False
        # 判断同一列是否有冲突， 列不同，行动
        for i in range(9):
            if board[i][col] == str(k):
                return False
        # 判断3x3网格内是否有冲突 行动，列动
        # 首先判断在哪个网格内
        start_row = row // 3 * 3
        start_col = col // 3 * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(k):
                    return False
        return True
