# 题目：打家劫舍扩展一 假设所有房屋围成一个圈，问盗窃的最大价值

# 思路：本题特别是是一个环形数组，环形数组特点是首位相同，如果我们只考虑其中一个，此问题就变成打家劫舍的初级版了
#为两个单排排列房间子问题
# 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是P1
# 在不偷窃最后一个房子的情况下（即 nums[:n−1]），最大金额是P2
# 最后输出max(p1, p2)

# 写法一：不利用python特性(切片)， C风格 
# 缺点是对数组指针操作比较繁琐，一不小心就出错
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums[0], nums[1])
        res1 = self.robRange(nums, 1, size-1)
        res2 = self.robRange(nums, 0, size-2)
        return max(res1, res2)
    # 对198 进行了改造 
    def robRange(self, nums, start, end):
        # dp和Nums同长度，后面才好写
        dp = [0] * (len(nums)) 
        dp[start] = nums[start]
        dp[start+1] = max(nums[start], nums[start+1])
        for i in range(start+2, end+1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[end]

# 写法二：python风格 看起来就舒服
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res1 = self.robRange(nums[:len(nums)-1])
        res2 = self.robRange(nums[1:])
        return max(res1, res2)
    # 198 一点未改动
    def robRange(self, nums):
        size = len(nums)
        # 当然这块去掉最好，和上面重复了
        if size == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]



