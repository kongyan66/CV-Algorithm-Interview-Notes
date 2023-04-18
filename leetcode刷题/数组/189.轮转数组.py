# 题目：给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

# 思路：
'''
本题是右旋转，其实就是反转的顺序改动一下，优先反转整个字符串，步骤如下：
反转整个字符串
反转区间为前k的子串
反转区间为k到末尾的子串
'''

# 解法一： 空间复杂度O()
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            tem = nums.pop()
            nums.insert(0, tem)

# 解法二：
class Solution:
    def reverse(self, nums, l, r):
        while l <= r:    # 这里等号可取可不取
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        # 需要注意的是，本题还有一个小陷阱，题目输入中，如果k大于nums.size了应该怎么办?
        # 如果k=len(nums) 则相当于没动过
        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
