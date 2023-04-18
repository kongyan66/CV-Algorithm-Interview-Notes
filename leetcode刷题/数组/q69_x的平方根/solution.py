'''
前提：零的平方根为零，其他的都介与（1，本身）之间
思路：平方根处于中点附近，本质还是平方根落在的区间，
'''
class Solution:
    def mySqrt(self, x: int) -> int:
      left = 1
      right = x
      while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x:
          if (mid + 1) * (mid + 1) > x:  # 两个均满足，说明改点即为平方根
            return mid
          else:
            left = mid + 1               # 向右缩小区间
        else:
          right = mid - 1                # 向左缩小区间
      return 0                           # 输入为零，平方根为零
