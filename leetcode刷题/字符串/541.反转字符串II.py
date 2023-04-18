# 题目：给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符

# 解法一：指针思想，通过指针判断满足题目要求的区间，然后进行反转
class Solution1:
    def reverseStr(self, s: str, k: int) -> str:
      def reverse_substr(start, end, strs):  # 给定整个字符串反转区间，进行反转
        left = start
        right = end
        while left < right:
          strs[left], strs[right] = strs[right], strs[left]
          left += 1
          right -= 1
        return strs
      # 虽然字符串是迭代对象，但是不可变对象(还有元组），子元素不能改变，也就无法直接反转 \
      # 故转为List 即可解决
      s = list(s)                       
      for i in range(0, len(s), 2*k):
        # 1. 每隔 2k 个字符的前 k 个字符进行反转
        # 2. 剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符
        if i + k <= len(s): 
          reverse_substr(i, i+k-1, s)
          continue
        # 3. 剩余字符少于 k 个，则将剩余字符全部反转
        reverse_substr(i, len(s)-1, s)
      s = ''.join(s)
      return s

class Solution2:
    def reverseStr(self, s: str, k: int) -> str:
      def reverse_substr(strs):  # 反转整个字符串
        left = 0
        right = len(strs) - 1
        while left < right:
          strs[left], strs[right] = strs[right], strs[left]
          left += 1
          right -= 1
        return strs 
      s = list(s)

      for i in range(0, len(s)-1, 2*k):
        # 
        s[i:i+k] = reverse_substr(s[i:i+k])  # 所以需要切片
      s= ''.join(s) 
      return s


