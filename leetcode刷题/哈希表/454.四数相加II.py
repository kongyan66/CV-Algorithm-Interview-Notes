# 要求：四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
# 核心思想：哪里需要快速查值，哪里就有Hash

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
      record = dict()
      count = 0
      # 先求两数之和, 用dict{'和':出现次数}记录
      for i in nums1:
        for j in nums2:
          if i + j in record:
             record[i+j] += 1
          else:
             record[i+j] = 1
      # 这里和两数之和思想类似了， 用sum - a = b, 用b值去查询, 并用count记录次数。
      for i in nums3:
        for j in nums4:
          key = - i - j
          if key in record:
            count += record[key] # 这里需注意, 用C+D的值查次数, 第一次就写成A+B的了
      return count
