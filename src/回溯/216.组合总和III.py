# 题目：找出（1-9）中所有相加之和为 n 的 k 个数的组合，返回 所有可能的有效组合的列表 

# 思路：对77.组合改造在

# 写法一：回溯 函数不分开
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        # 1.确定递归函数的返回值
        def backtracking(k, n, startindex):
            # 2.确定递归停止条件
            # 无论是否有满足条件的，到底了就要停止
            if k == len(path):
                # 满足条件的存入result中
                if sum(path) == n:
                    result.append(path.copy())
                return 
            # 3.单层搜索过程
            # for循环用来横向遍历
            for i in range(startindex, 10):
                path.append(i)
                backtracking(k, n, i+1) # 递归
                path.pop() # 回溯
       
        backtracking(k, n, 1)
        return result
# 写法二：函数独立
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, 1)
        return self.result
    # 1.确定递归函数的返回值
    def backtracking(self, k, n, startindex):
        # 2.确定递归停止条件
        # 无论是否有满足条件的，到底了就要停止
        if k == len(self.path):
            # 满足条件的存入result中
            if sum(self.path) == n:
                self.result.append(self.path.copy())
            return 
        # 3.单层搜索过程
        # for循环用来横向遍历
        for i in range(startindex, 10):
            self.path.append(i)
            self.backtracking(k, n, i+1) # 递归
            self.path.pop() # 回溯
# 改进： 剪枝
# 如果当期path sum值已经大于n,那么后面就没意义了，所以在递归停止条件出剪枝

'''
if sum(path) > n:
    return 
'''
