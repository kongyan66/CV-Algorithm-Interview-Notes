# 题目：给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# 思路：本题难点在于给定的candinadates中有重复数，但结果要求不能有重复的，所以需要去重
# 这里去重是指同一树层的重（横向遍历），而不是同一树枝下的重（纵向遍历）
# 所以这里需要bool型列表去记录是否为同一层还是同一枝
# 解法 使用标志位
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        # 本题需要使用used，用来标记区别同一树层的元素使用重复情况，注意区分递归纵向遍历遇到的重复元素，和for循环遇到的重复元素
        self.used = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.used = [False] * len(candidates)
        # 避免重复，先排序，这样如果有重复的数必然相邻，方便去降重
        candidates.sort()
        self.backtracking(candidates, target, 0)
        return self.result
    # 1.确定递归入参与返回值
    def backtracking(self, candidates, target, startindex):
        # 2.确定递归停止条件
        if sum(self.path) == target:
            self.result.append(self.path.copy())
            return 
        elif sum(self.path) > target:
            return 
        # 3.单层搜索逻辑
        for i in range(startindex, len(candidates)):
            # 检查同一树层是否出现曾经使用过的相同元素
            # 若数组中前后元素值相同，但前者却未被使用(used == False)（回溯后恢复到原来状态），说明当前元素是同一树层的相同元素情况
            if i > 0 and candidates[i] == candidates[i-1] and self.used[i-1] == False:
                continue
            self.used[i] = True
            self.path.append(candidates[i])
            self.backtracking(candidates, target, i+1)
            self.path.pop() # 回溯
            self.used[i] = False  # 回溯

# re2 使用set()标志位
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        # 因为有重复元素，本题需要使用used，用来标记区别同一树层的元素使用重复情况，注意区分递归纵向遍历遇到的重复元素，和for循环遇到的重复元素
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking(candidates, target, 0)
        return self.result

    def backtracking(self, candidates, target, startindex):
        # 2.确定递归停止条件
        if sum(self.path) == target:
            self.result.append(self.path.copy())
            return 
        if sum(self.path) > target:
            return
        # 3.确定单层递归逻辑
        use = set()
        for i in range(startindex, len(candidates)):
            # if i > 0 and candidates[i] == candidates[i-1] and self.used[i-1] == False:
            #     continue
            if candidates[i] in use:
                continue
            self.path.append(candidates[i])
            use.add(candidates[i])
            self.backtracking(candidates, target, i+1)
            self.path.pop()