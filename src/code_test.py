class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.used = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, 0)
        return self.result
   
    def backtracking(self, nums, startindex):
        self.result.append(self.path.copy())

        if startindex >= len(nums):
            return

        for i in range(startindex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
        
        
