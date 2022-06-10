# 题目：给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合（组合无序，排列有序）

# 思路：

# 解法一； 回溯法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 在这里要定义两个全局变量，一个用来存放符合条件单一结果，一个用来存放符合条件结果的集合。
        path = []
        results = []
        # 1. 确定递归的返回值和参数
        # n决定了树的宽度，k决定了树的深度
        # 每次从集合中选取元素，可选择的范围随着选择的进行而收缩，调整可选择的范围，就是要靠startIndex。
        def backtracking(n, k, startindex):
            # 2. 确定递归的终止条件
            # path这个数组的大小如果达到k，说明我们找到了一个子集大小为k的组合了，本层递归结束
            if k == len(path):
                results.append(path.copy())
                return 
            # 单层搜索过程
            # for循环用来横向遍历，递归的过程是纵向遍历。
            for i in range(startindex, n + 1):  # 为啥要加一，因为n是左闭右闭的，而range是左闭右开的
                path.append(i)  # 处理节点
                backtracking(n, k, i+1)  # 递归：控制树的纵向递归， 注意下一层搜索要从i+1开始
                path.pop() # 回溯，撤销处理的节点

        backtracking(n, k, 1)
        return results

# 疑问：为啥这么写就是不行 返回值为[]
# 解答：暂定是作用域问题，但是还没有复现出来
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        results = []
        self.backtracking(n, k, 1)
        return results

    def backtracking(self, n, k, startindex):
        if k == len(path):
            results.append(path[:])
            return 
        for i in range(startindex, n):
            path.append(i)
            self.backtracking(n, k, i+1)
            path.pop()
# 以下写法是可以的
class Solution:
    def __init__(self):
        self.path = []
        self.results = []
    def combine(self, n: int, k: int) -> List[List[int]]:

        self.backtracking(n, k, 1)
        return self.results

    def backtracking(self, n, k, startindex):
        if k == len(self.path):
            self.results.append(self.path[:])
            return 
        for i in range(startindex, n+1):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()


# 改进： 剪枝
# 接下来看一下优化过程如下：
# 已经选择的元素个数：path.size();
# 还需要的元素个数为: k - path.size();
# 在集合n中至多要从该起始位置 : n - (k - path.size()) + 1，开始遍历

for i in range(startindex,n - (k - path.size()) + 2):  # 优化的地方
    path.append(i)  # 处理节点
    backtracking(n, k, i+1)  # 递归：控制树的纵向递归， 注意下一层搜索要从i+1开始
    path.pop() # 回溯，撤销处理的节点
