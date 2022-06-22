# 题目：n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。给你一个整数 n ，
# 返回所有不同的 n 皇后问题 的解决方案。

# 思路：用一个二维数组先画好棋盘，然后横向遍历选择第一个Q放在某一列，然后用递归搜索每一行的Q位置，当到达子叶位置就回收结果
# 这里还有个难点是判断N皇后的合法性，采用放旗子前先看看其前方位置去判断

class Solution:
    def __init__(self):
        self.result = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        row = 0
        self.backtracking(board, n, row)
        return self.result
    # 1.确定递归入参与返回值
    def backtracking(self,board, n, row):
        # 2.确定递归的停止条件
        if row == n:
            # 转换下输出格式
            tem_result = []
            for tem in board:
                tem_result.append("".join(tem))
            self.result.append(tem_result)
            
        # 3.确定单层递归逻辑
        for col in range(n):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtracking(board, n, row+1)
            board[row][col] = '.'
    def is_valid(self, board, row, col):
        # 判断是否同一列
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        # 判断是否同一行
        # 因为我们递归每次每行只放放一个Q, 所以不存在多个Q同行的情况，也就不需要再判断

        # 判断是否在同一正对角线上
        # 在board[row, col]放置‘Q’前,我们需要看(row,col)之前的对角线上是否有‘Q’，有的话就不能放了
        # 方向：右下->左上
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 判断反对角线
        # 原理同上，方向：左下->右上
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True
           