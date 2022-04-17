class Solution:
    def isHappy(self, n: int) -> bool:
      def getSum(num):
        _sum = 0
        while num:
          _sum += (num % 10) ** 2  # 从个位开始求平方和
          num = num // 10
        return _sum

      recorde = set()
      while True:
        n = getSum(n)
        if n == 1:
          return True

        
        if n in recorde:  # 如果出现重复数，说明陷入死循环了
          return False
        else:
          recorde.add(n)  