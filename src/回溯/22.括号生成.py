# 题目：数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# 思路：DFS+回溯 
# 想象有一颗树，每次选择放左括号或者右括号，当然要有限制条件，单括号数量不能超过n, 右括号数量小于左括号

# 解法
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtracking(n, 0, 0)
        return self.res
    
    def backtracking(self, n, left, right):
        # 2.确定递归停止条件 括号数量等于2xn
        if len(self.path) == 2 * n:
            self.res.append(''.join(self.path))
            return 
        # 3.确定单层递归逻辑 
        # 左括号数量小于n
        if left < n:
            self.path.append('(')
            self.backtracking(n, left+1, right)
            self.path.pop()
        # 右括号数量小于左边
        if right < left:
            self.path.append(')')
            self.backtracking(n, left, right)
            self.path.pop()






        



