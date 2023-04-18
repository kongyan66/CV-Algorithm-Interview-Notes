# 题目：给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 思路 还是组合问题 分析递归的深度和宽度 每一个数字对应的字符串作为一层 画好树就明白了

# 解法： 回溯
class Solution:
    def __init__(self):
        self.path = ''
        self.results = []
        self.map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        else:
            self.backtracking(digits, 0)
        return self.results

    # 1.确定入参与返回值 
    def backtracking(self, digits, index):
        # 2.确定递归停止条件 控制递归的深度
        if index == len(digits):
            self.results.append(self.path)
            return
        # 3.单层搜索逻辑 
        # 递归深度= 输入数字个数 宽度=3
        letters = self.map[digits[index]]
        for letter in letters:  # 控制递归的宽度
            self.path += letter
            self.backtracking(digits, index+1)
            self.path = self.path[:-1]  # 回溯
