# 题目：给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 考察：栈(优选)、双指针
# 思路：遍历所有字符串，依次存入栈，若当前值与前一个相等，则弹出前一个值，最后身剩下的就是不重复字母

class Solution:
    def removeDuplicates(self, s: str) -> str:
      stack = []
       
      for item in s:
        if stack and item == stack[-1]:
          stack.pop()
        else:
          stack.append(item)
      res = ''.join(stack)
      return res


