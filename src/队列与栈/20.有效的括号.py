# 题目：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 思路：栈结构的特殊性，非常适合做对称匹配类的题目
# 解题：该题重要是分析匹配不上的情况
# 1. 左边括号多了 2.右边括号多了  3.中间没有匹配上

class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      # 遍历字符串，用栈存另一半，如果能匹配上，则下一位置必然是该括号的另一半
      for item in s:
        if item == '(':
          stack.append(')')
        elif item == '{':
          stack.append('}')
        elif item == '[':
          stack.append(']')
        # 这里有两种不配情况：1.如果stack为空说明右半多了  2.如果stack的尾数不和下一位置相等，未匹配上
        elif not stack or stack[-1] != item:  
          return False
        else:
          stack.pop()  # 下一位置匹配上就弹出，最后都能匹配上的话，stack就为空
      return True if not stack else False