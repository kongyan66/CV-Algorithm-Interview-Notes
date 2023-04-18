# 题目：定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 思路：和岛屿问题挺像,先找到数组中符合word第一个字符的位置，再进行深度优先搜索，朝一个方向搜索到底，
# 如果遇到数组当前位置储存字符不等于当前word字符或数组越界的情况，立即返回

# 解法
class Solution:  
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.backtracking(board, word, i, j, 0):
                    return True
        return False
                    
    def backtracking(self, board, word, i, j, curlen):
        # 找到一条路径就返回
        if curlen == len(word):
            return True
        # 越界或者不等于word的值
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[curlen]:
            return False
        tem = board[i][j]
        board[i][j] = '1'
        t = self.backtracking(board, word, i+1, j, curlen+1)
        b = self.backtracking(board, word, i-1, j, curlen+1)
        l = self.backtracking(board, word, i, j-1, curlen+1)
        r = self.backtracking(board, word, i, j+1, curlen+1)
        board[i][j] = tem
        
        return t or b or l or r
        

