# 题目：求 该数组中和为 k 的连续子数组的个数。

# 解决一：暴力法 遍历每一种连续的的组合  时间复杂度O(N^3）因为除了两层for循环，还有一层求和。  超时
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 要求的连续子数组
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i:j+1]) == k:
                    count += 1
        return count

# 解法二：前缀和
# 前缀和指一个数组的某下标之前的所有数组元素的和（包含其自身）, 可以很方便表示某段区间里的和
# 这个理解得画图，详见：https://leetcode.cn/problems/subarray-sum-equals-k/solution/python3-by-wu-qiong-sheng-gao-de-qia-non-w6jw/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = collections.defaultdict(int)
        pre_sum[0] = 1
        count = 0
        
        sum_ = 0
        for i in range(len(nums)):
            # 求当前位置前缀和
            sum_ += nums[i]
            # 求前序和为sum_ - k的数量
            count += pre_sum[sum_ - k]
            pre_sum[sum_] += 1
        return count




