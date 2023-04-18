# 题目：有一个长度为n的数组，初始化都为0， 给你k组操作，每组用一个三元组表示（startindex, endindex, inc), 表示对该闭区间增加inc

# 思路：显然是一道差分区间的题

# 解
class Difference:
    def __init__(self, nums) -> None:
        self.diff = [0] * len(nums)
        self.diff_arr(self.diff, nums)
        
    # 初始化差分矩阵
    def diff_arr(self, diff, nums):
        diff[0] = nums[0]
        for i in range(1, len(nums)):
            diff[i] = nums[i] - nums[i - 1]
    # 给闭区间[i, j]增加val
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val
    # 返回最终结果
    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res

if __name__ == "__main__":
    nums = [0] * 5
    updates = [(1, 3, 2), (2, 4, 3), (0, 2, -2)]

    diff = Difference(nums)
    for up in updates:
        i, j, val = up
        diff.increment(i, j, val)
    ans = diff.result()
    print(ans)
# 返回[-2, 0, 3, 5, 3]