# 题目：给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 要求时间复杂度O(N）

# 解法一：调包 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# 解法二：二叉堆-大顶堆
# 维护一个长度为k的小顶堆
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            # 如果堆长度没到k，无脑塞
            if len(heap) < k:
                heapq.heappush(heap, num)
            # 如果长度到k了，且当前元素比堆顶要大，我们才加进去，当然要先把最小的pop出来再加
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        print(heap)
        return heapq.heappop(heap)
  