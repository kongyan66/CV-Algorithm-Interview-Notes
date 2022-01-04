'''
方法：二分法
思路： 只要找到mid*mid = num就返回True，其他情况就缩小区间范围
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
      left = 1
      right = num
      while left <= right:
        mid = left + (right - left)//2
        if mid * mid < num:
          left = mid + 1
        elif mid * mid > num:
          right = mid -1
        else:
          return True
      return False
