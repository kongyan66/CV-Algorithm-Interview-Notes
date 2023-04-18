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

# re-2 
class Solution:
    def __init__(self):
        self.list_num = set()
    def isHappy(self, n: int) -> bool:
        return self.recursion(n)

    # 1.确定入参与返回值
    # 返回值： bool
    def recursion(self, n):
        # 2.确定递归停止条件
        n_str = str(n)
        sum = 0
        for i in range(len(n_str)):
            sum += int(n_str[i])**2
        if sum in self.list_num:
            return False
        if sum == 1:
            return True
        # 单层递归逻辑
        self.list_num.add(sum)
        return self.recursion(sum)