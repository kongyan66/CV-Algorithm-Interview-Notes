# 题目：给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案

# 思路：组合和切割字符原理类似，都是看做一颗树来处理，区别在于组合每次取一个数，切割每次取一片，至于回文判断就是一个小点了
# 解法：
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.result
    # 1.确定入参与返回值
    # 入参： 
    def backtracking(self, s, startindex):
        # 2.确定递归停止条件
        if startindex > len(s) - 1:
            self.result.append(self.path.copy())
            return 
        # 3.确定搜索逻辑
        for i in range(startindex, len(s)):
            tem = s[startindex:i+1]
            if self.isPalindrome(tem):
                self.path.append(tem)
                self.backtracking(s, i+1)
                self.path.pop()
        
    # 判断回文数组
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    # 这里也可以简化为:
    if tem == tem[::-1]:
        return True
