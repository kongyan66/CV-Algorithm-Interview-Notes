# 题目：把字符串前面的若干个字符转移到字符串的尾部
# 思路：和151.反转单词类似，先局部反转再 整体反转

# python直接用切片是最简单的,s[n:len(s)-1]+s[0:n], 若不能用，且不能调用reversed(),就需要全部自己写了
# 未开开辟新空间，空间复杂度是O(n)，时间复杂度O(n)
class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
      def reverse(s):
        left = 0
        right = len(s) -1
        while left < right:
          s[left], s[right] = s[right], s[left]
          left += 1
          right -= 1
        return s
      
      s = list(s)
      s[0:n] = reverse(s[0:n])           # 反转前面一部分 切片范围很重要：左闭右开      
      s[n:len(s)] = reverse(s[n:len(s)]) # 反转后一部分
      s = reverse(s)                     # 整体反转
      s = ''.join(s)      
      return s
#方法四：考虑不能用切片的情况下，利用模+下标实现
class Solution2:
    def reverseLeftWords(self, s: str, n: int) -> str:
      new_s = ''
      for i in range(len(s)):  
        j = (i + n) % len(s)   #  比如n=2, 长度为4， 则j=2, 3, 0, 1, 这样就把位置换过来了
        new_s = new_s + s[j]
      return new_s
        