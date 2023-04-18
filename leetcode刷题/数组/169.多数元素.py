# 题目：给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 思路一：哈希表计数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        map = collections.defaultdict(int)
        for i in range(n):
            map[nums[i]] += 1
        
        for k, v in map.items():
            if v > n / 2:
                return k
# 思路二：排序思路
# 既然数组中有出现次数> ⌊ n/2 ⌋的元素，那排好序之后，众数必然在中间
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]