# 题目：给你一个无重复元素的整数数组candidates和一个目标整数target ，找出candidates中可以使数字和为目标数target的所有不同组合，并以列表形式返回。

# 思路：本次递归宽度还是数组长度， 但深度无限，知道sum >= target才停止，77.组合等都是固定深度的
# 所以区别在递归停止条件哪

# 第一版版本：结果是排列结果 原因是拿出又放回，组合问题：拿出不放回
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(candidates, target)
        return self.result
    # 1.确定递归的入参与返回值
    # 入参：
    def backtracking(self, candidates, target):
        
        if sum(self.path) == target:
            self.result.append(self.path.copy())
            return
        elif sum(self.path) > target:
            return 
        for i in range(len(candidates)):
            self.path.append(candidates[i])
            self.backtracking(candidates, target)
            self.path.pop()
# 改正版本
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(candidates, target, 0)
        return self.result
    # 1.确定递归的入参与返回值
    # 入参：这里startindex必须有
    # 出参：就是result了
    def backtracking(self, candidates, target, startindex):
        # 2.确定递归停止条件
        # 这就两种情况停止递归
        if sum(self.path) == target:
            self.result.append(self.path.copy())
            return
        elif sum(self.path) > target: 
            return 
        # 3.单层搜索逻辑
        for i in range(startindex, len(candidates)):
            self.path.append(candidates[i])   # 组合问题还是拿出不放回，这里特别之处是同一个数字可以无限制重复被选取,所以startindex为i
            self.backtracking(candidates, target, i) # 递归
            self.path.pop() # 回溯
# 剪枝
# 前面也分析过了，如果sum会大于target，就没有必要进入下一层递归了。
# 在单层搜素逻辑哪修改
        # 3.单层搜索逻辑
        for i in range(startindex, len(candidates)):
            if sum(self.path) == target:
                return 
            self.path.append(candidates[i])   
            self.backtracking(candidates, target, i) # 递归
            self.path.pop() # 回溯


