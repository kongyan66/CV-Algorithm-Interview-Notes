# 求一共有多少下法


class Solution:
    def __init__(self):
        self.result = 0

    def totalNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        self.backtracking(board, n, 0)
        return self.result
    # 1.确定入参与返回值
    # board记录棋盘信息， row记录行，等于n说明就找到了一种下法
    # 无返回值，结果都在board中
    def backtracking(self, board, n, row):
        if row == n:
            self.result += 1
            return 

        for col in range(n):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtracking(board, n, row + 1)
            board[row][col] = '.'

    
    def is_valid(self, board, row, col):
        # 是否有同列
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # 是否正对角线
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 是否副对角线
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
        