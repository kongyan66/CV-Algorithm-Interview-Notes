# 题目：给定一个非负整数数组A， A中一半整数是奇数，一半整数是偶数。对数组进行排序，以便当A[i]为奇数时，i也是奇数；当A[i]为偶数时， i也是偶数。

# 思路一：两个for循环 超时
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        used = [0] * len(nums)
        for i in range(len(res)):
            for j in range(len(nums)):
                if i % 2 == 0:
                    if not used[j] and nums[j] % 2 == 0:
                        res[i] = nums[j]
                        used[j] = 1
                        break
                else:
                    if not used[j] and nums[j] % 2 == 1:
                        res[i] = nums[j]
                        used[j] = 1
                        break
        return res

# 思路二：遍历偶数位，遇到偶数就去奇数位找偶数  time:O(N) space:O(1)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        oddindex = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1:
                while nums[oddindex] % 2:
                    oddindex += 2
                nums[i], nums[oddindex] = nums[oddindex], nums[i]
        return nums
